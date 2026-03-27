import threading
import uuid
from concurrent.futures import ThreadPoolExecutor, as_completed
from seldom.utils import cache
from unittest import SkipTest
from config.config import Config


class DataParallelRunner:
    """测试数据并发执行器（带报告处理）"""

    def __init__(self, max_workers=5):
        self.max_workers = max_workers
        self.lock = threading.Lock()

    def run(self, test_instance, data_list, test_func=None):
        """
        执行测试数据（单条直接运行，多条并发）
       """
        # 存储所有执行结果
        results = []

        # 确定测试执行函数（优先使用自定义函数，否则使用默认实现）
        exec_func = test_func if test_func is not None else self.execute_test

        # 单条数据直接执行，不启用线程池
        if len(data_list) == 1:
            results = [self._safe_execute(exec_func, test_instance, data_list[0])]
        else:
            results = self._run_parallel(exec_func, test_instance, data_list)

        self._generate_reports(test_instance, results)

    def _safe_execute(self, exec_func, test_instance, data):
        """安全执行单条测试，统一异常处理"""
        try:
            return exec_func(test_instance, data)
        except Exception as e:
            return {
                "scene": data.get("scene", "未知场景"),
                "req": data.get("req"),
                "status": "failed",
                "error": str(e)
            }

    def _run_parallel(self, exec_func, test_instance, data_list):
        """并发执行多条测试数据"""
        results = []
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            future_to_data = {
                executor.submit(exec_func, test_instance, data): data
                for data in data_list
            }

            for future in as_completed(future_to_data):
                data = future_to_data[future]
                try:
                    result = future.result()
                except Exception as e:
                    result = {
                        "scene": data.get("scene", "未知场景"),
                        "req": data.get("req"),
                        "status": "failed",
                        "error": str(e)
                    }
                with self.lock:
                    results.append(result)
        return results

    @staticmethod
    def execute_test(test_instance, data):
        """默认测试执行逻辑（包含断言）"""
        scene = data["scene"]
        req = data["req"]
        resp = data["resp"]

        try:
            # 判断数据安全正则的是严格模式，会匹配未通过强校验的数据,匹配范围更大,不执行 '未命中-宽松' 的场景, 严格模型下该数据会被拦截
            # 在宽松模式下，才会使用强校验，不通过强校验的数据，不是敏感数据
            if Config().run_mode == "strict" and "宽松" in scene:
                uu_id = str(uuid.uuid4())
                cache.set({f"{scene}_uu_id": uu_id})
                test_instance.skipTest("跳过 '未命中-宽松' 的数据")

            # 1. 发送API请求
            if "非流式" in scene:
                content_type, full_response, uu_id = test_instance.api.no_stream_chat_completion(
                    content=req["content"]
                )
                expected_type_label = "非流式"
            else:
                content_type, full_response, uu_id = test_instance.api.stream_chat_completion(
                    content=req["content"]
                )
                expected_type_label = "流式"

            # 2. 基础断言
            test_instance.assertStatusCode(resp["code"], msg=f"场景 [{scene}] 状态码不匹配")
            test_instance.assertIn(resp["content_type"], content_type,
                                   msg=f"场景 [{scene}] 响应类型错误，正确类型为'{expected_type_label}'")
            cache.set({f"{scene}_uu_id": uu_id})

            # 3. 内容断言
            if "敏感数据替换" in scene:
                expect_present = "未命中" not in scene
                if expect_present:
                    test_instance.assertIn(resp["resp_content"], full_response, msg=f"场景 [{scene}] 响应内容不匹配")
                else:
                    test_instance.assertNotIn(resp["resp_content"], full_response, msg=f"场景 [{scene}] 响应内容不匹配")
                count = full_response.count(resp["resp_content"])
                print(full_response)
                test_instance.assertEqual(resp["replace_total"], count, msg=f"场景 [{scene}] 实际替换的数量与预期不相等")
            elif any(keyword in scene for keyword in ["未命中", "-监测-", "白名单"]):
                test_instance.assertNotIn(resp["resp_content"], full_response, msg=f"场景 [{scene}] 响应内容不匹配")
            else:
                test_instance.assertIn(resp["resp_content"], full_response, msg=f"场景 [{scene}] 响应内容不匹配")

            return {
                "scene": scene,
                "status": "passed"
            }
        except SkipTest:
            return {
                "scene": scene,
                "status": "skipped",
                "error": f"跳过场景：{scene}, 严格模式下,会匹配未通过强校验的数据,匹配范围更大,不执行 '未命中-宽松' 的场景"
            }
        except Exception as e:
            return {
                "scene": scene,
                "req": req,
                "status": "failed",
                "error": str(e)
            }

    def _generate_reports(self, test_instance, results):
        """生成测试报告，为每组数据创建独立子测试"""
        for res in results:
            with test_instance.subTest(scene=res["scene"]):
                if res["status"] == "failed":
                    test_instance.fail(f"\n场景执行失败: {res['error']};\n失败场景的请求数据为： {res.get('req')}")
                elif res["status"] == "skipped":  # 跳过的用例执行skipTest，标记为跳过
                    test_instance.skipTest(res["error"])