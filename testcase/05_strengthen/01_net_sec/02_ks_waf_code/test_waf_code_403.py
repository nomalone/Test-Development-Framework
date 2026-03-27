import time, seldom

from seldom.utils import cache
from config.config import Config
from public.strengthen.net_security import NetSecurity
from public.api_client_v1 import APIClient
from public.login import Login


class TestWafCode403(seldom.TestCase):
    """增强管理-网络安全-高级扫描防护: 403"""

    @classmethod
    def start_class(cls):
        # 初始化配置
        cls.cookie = Login().login()

        config = {
            "status_code_policy": [
                {
                    "status": "403",
                    "duration": 60,
                    "requests": 10,
                    "rato": 1,
                    "blocktime": 1,
                    "enable": True
                }
            ]
        }
        NetSecurity(cls.cookie, Config.route_net_security_id).ks_waf_code_set(config)
        time.sleep(Config.time_random)  # 等待配置生效

        # 初始化工具和客户端
        cls.api = APIClient(Config.route_net_security_name)

    @classmethod
    def end_class(cls):
        config = {"status_code_policy": []}
        NetSecurity(cls.cookie, Config.route_net_security_id).ks_waf_code_set(config)


    @seldom.file_data("waf_code_data.json", key="5-1-1-waf-code-403")
    def test_waf_code_403(self, scene, req, resp):
        """调用大模型，发起请求"""
        # 1. 发送API请求
        for i in range(11):
            results = self.api.chat_code(
                content=req["content"],
                uri="/aa"
            )

        content_type, full_response, uu_id = results
        cache.set(({f"{scene}_uu_id": uu_id}))

        # 2. 执行断言,判断调用大模型是否成功
        self.assertStatusCode(resp["code"], msg=f"场景 [{scene}] 状态码不匹配")
        self.assertIn(resp["content_type"], content_type, msg=f"场景 [{scene}] 响应类型错误，正确类型为'非流式'")
        self.assertIn(resp["resp_content"], full_response, msg=f"场景 [{scene}] 响应内容不匹配")



