"""
author: cheny68
data: 2025/09/25
"""
import time, seldom

from seldom.utils import cache

from config.config import Config
from public.strengthen.content_security import ContentSecurity
from public.api_client_v1 import APIClient
from public.login import Login


class TestValuesRespInterceptHitLenientNoStream(seldom.TestCase):
    """增强管理-内容安全-价值观模型监测:回答-开启-拦截-命中-宽松-非流式"""

    @classmethod
    def start_class(cls):
        # 初始化配置
        cls.cookie = Login().login()
        # cls.wait_time = Config().wait_time
        # cls.max_workers = Config().max_workers

        config = {
            "checkRequest": False,
            "checkResponse": True,
            "checkContext": False,
            "modelFilter": [
                {
                    "label": "政治敏感",
                    "action": "intercept",
                    "mode": "lenient"
                },
                {
                    "label": "暴力恐怖",
                    "action": "intercept",
                    "mode": "lenient"
                },
                {
                    "label": "色情低俗",
                    "action": "intercept",
                    "mode": "lenient"
                },
                {
                    "label": "歧视谩骂",
                    "action": "intercept",
                    "mode": "lenient"
                },
                {
                    "label": "不良价值观",
                    "action": "intercept",
                    "mode": "lenient"
                }
            ]
        }
        ContentSecurity(cls.cookie, Config.route_content_security_id).ks_model_guard_set(config)
        time.sleep(Config.time_random)  # 等待配置生效

        # 初始化工具和客户端
        cls.api = APIClient(Config.route_content_security_name)
        # self.log_searcher = SearchLog(conf.cookie)
        # self.runner = DataParallelRunner(max_workers=self.max_workers)  # 使用现有并发执行器

    @seldom.file_data("values_resp_data.json", key="5-2-2-values-resp-005")
    def test_values_resp_intercept_hit_lenient_no_stream(self, scene, req, resp):
        """调用大模型，发起请求"""
        if  "暴力恐怖" in scene or "其他类型" in scene:
            self.skipTest(f"跳过场景：{scene}, 暂无宽松模式下的 {scene} 测试数据")

        # 1. 发送API请求
        content_type, full_response, uu_id = self.api.no_stream_chat_completion(
            content=req["content"]
        )
        cache.set(({f"{scene}_uu_id": uu_id}))

        # 2. 执行断言,判断调用大模型是否成功
        self.assertStatusCode(resp["code"], msg=f"场景 [{scene}] 状态码不匹配")
        self.assertIn(resp["content_type"], content_type, msg=f"场景 [{scene}] 响应类型错误，正确类型为'流式'")
        self.assertIn(resp["resp_content"], full_response, msg=f"场景 [{scene}] 响应内容不匹配")


