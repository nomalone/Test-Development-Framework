import time, seldom

from seldom.utils import cache
from config.config import Config
from public.strengthen.net_security import NetSecurity
from public.api_client_v1 import APIClient
from public.login import Login


class TestWafDetect(seldom.TestCase):

    @classmethod
    def start_class(cls):
        # 初始化配置
        cls.cookie = Login().login()

        config = {
            "enableObserve": True,
            "enable": True,
            "enableScanner": True,
        }
        NetSecurity(cls.cookie, Config.route_net_security_id).ks_waf_set(config)
        time.sleep(Config.time_random)  # 等待配置生效

        # 初始化工具和客户端
        cls.api = APIClient(Config.route_net_security_name)

    @seldom.file_data("waf_data.json", key="5-1-1-waf-002")
    def test_waf_detect(self, scene, req, resp):
        """调用大模型，发起请求"""
        # 1. 发送API请求
        if req.get("ua"):
            content_type, full_response, uu_id = self.api.stream_chat_completion(
                content=req["content"],
                agent=req.get("ua")
            )
        elif req.get("fileI"):
            content_type, full_response, uu_id = self.api.stream_chat_completion(
                content=req["content"],
                uri=req.get("fileI")
            )
        else:
            content_type, full_response, uu_id = self.api.stream_chat_completion(
                content=req["content"]
            )
        cache.set(({f"{scene}_uu_id": uu_id}))

        # 2. 执行断言,判断调用大模型是否成功
        self.assertStatusCode(resp["code"], msg=f"场景 [{scene}] 状态码不匹配")
        self.assertIn(resp["content_type"], content_type, msg=f"场景 [{scene}] 响应类型错误，正确类型为'流式'")
        self.assertNotIn(resp["resp_content"], full_response, msg=f"场景 [{scene}] 响应内容不匹配")

