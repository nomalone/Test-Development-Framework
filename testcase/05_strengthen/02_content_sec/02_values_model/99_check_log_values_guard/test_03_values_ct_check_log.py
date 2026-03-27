"""
author: cheny68
data: 2025/09/19
"""
import time, seldom
from seldom.utils import cache
from config.config import Config
from public.log_management.search_log_v1 import SearchLog
from public.login import Login


class TestValuesCTCheckLog(seldom.TestCase):
    """增强管理-内容安全-价值观模型监测:监测上下文-日志校验"""

    @classmethod
    def start_class(cls):
        # 初始化配置
        cls.log_searcher = SearchLog(Login().login())
        ## 等待日志生成后开始运行日志检测
       #  time.sleep(Config().wait_time)

    @seldom.file_data("../03_values_ct/values_ct_data.json", key="5-2-2-values-ct-001")
    def test_values_ct_check_log_01(self, scene, _, resp):
        """查询日志"""
        uu_id = cache.get(f"{scene}_uu_id")
        print("uu_id:", uu_id)

        log_data = self.log_searcher.search_content_log(uu_id)
        self.assertStatusCode(resp["code"], msg=f"场景 [{scene}] 状态码不匹配")
        self.assertEqual(resp["log_total"], log_data,
                              msg=f"场景 [{scene}] 日志记录条数不正确")

    @seldom.file_data("../03_values_ct/values_ct_data.json", key="5-2-2-values-ct-002")
    @seldom.skip("跳过用例：宽松模型下，监测上下文时而匹配到，时而匹配不到")
    def test_values_ct_check_log_02(self, scene, _, resp):
        """查询日志"""
        uu_id = cache.get(f"{scene}_uu_id")
        print("uu_id:", uu_id)

        log_data = self.log_searcher.search_content_log(uu_id)
        self.assertStatusCode(resp["code"], msg=f"场景 [{scene}] 状态码不匹配")
        self.assertEqual(resp["log_total"], log_data,
                              msg=f"场景 [{scene}] 日志记录条数不正确")

    @seldom.file_data("../03_values_ct/values_ct_data.json", key="5-2-2-values-ct-003")
    def test_values_ct_check_log_03(self, scene, _, resp):
        """查询日志"""
        uu_id = cache.get(f"{scene}_uu_id")
        print("uu_id:", uu_id)

        log_data = self.log_searcher.search_content_log(uu_id)
        self.assertStatusCode(resp["code"], msg=f"场景 [{scene}] 状态码不匹配")
        self.assertEqual(resp["log_total"], log_data,
                              msg=f"场景 [{scene}] 日志记录条数不正确")

    @seldom.file_data("../03_values_ct/values_ct_data.json", key="5-2-2-values-ct-004")
    @seldom.skip("跳过用例：宽松模型下，监测上下文时而匹配到，时而匹配不到")
    def test_values_ct_check_log_04(self, scene, _, resp):
        """查询日志"""
        uu_id = cache.get(f"{scene}_uu_id")
        print("uu_id:", uu_id)

        log_data = self.log_searcher.search_content_log(uu_id)
        self.assertStatusCode(resp["code"], msg=f"场景 [{scene}] 状态码不匹配")
        self.assertEqual(resp["log_total"], log_data,
                              msg=f"场景 [{scene}] 日志记录条数不正确")

    @seldom.file_data("../03_values_ct/values_ct_data.json", key="5-2-2-values-ct-005")
    def test_values_ct_check_log_05(self, scene, _, resp):
        """查询日志"""
        uu_id = cache.get(f"{scene}_uu_id")
        print("uu_id:", uu_id)

        log_data = self.log_searcher.search_content_log(uu_id)
        self.assertStatusCode(resp["code"], msg=f"场景 [{scene}] 状态码不匹配")
        self.assertEqual(resp["log_total"], log_data,
                              msg=f"场景 [{scene}] 日志记录条数不正确")

    @seldom.file_data("../03_values_ct/values_ct_data.json", key="5-2-2-values-ct-006")
    def test_values_ct_check_log_06(self, scene, _, resp):
        """查询日志"""
        uu_id = cache.get(f"{scene}_uu_id")
        print("uu_id:", uu_id)

        log_data = self.log_searcher.search_content_log(uu_id)
        self.assertStatusCode(resp["code"], msg=f"场景 [{scene}] 状态码不匹配")
        self.assertEqual(resp["log_total"], log_data,
                              msg=f"场景 [{scene}] 日志记录条数不正确")

