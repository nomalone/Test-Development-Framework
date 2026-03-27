import time
import seldom
from seldom.utils import cache

from config.config import Config
from public.api_client_v1 import APIClient
from public.login import Login
from public.strengthen.content_security import ContentSecurity


class TestKeywordRespClose(seldom.TestCase):
    """增强管理-内容安全-关键词监测:回答-关闭"""

    @classmethod
    def start_class(cls):
        # 初始化配置
        cls.cookie = Login().login()

        config = {}
        ContentSecurity(cls.cookie, Config.route_content_security_id).ks_keyword_guard_set(config)
        time.sleep(Config.time_random)  # 等待配置生效

        cls.api = APIClient(Config.route_content_security_name)

    @seldom.file_data("keyword_resp_data.json", key="5-2-1-keyword-resp-close")
    def test_keyword_resp_close(self, scene, req, resp):
        """调用大模型，发起请求"""
        # 1. 发送API请求
        content_type, full_response, uu_id = self.api.stream_chat_completion(
            content=req["content"]
        )
        cache.set(({f"{scene}_uu_id": uu_id}))

        # 2. 执行断言,判断调用大模型是否成功
        self.assertStatusCode(resp["code"], msg=f"场景 [{scene}] 状态码不匹配")
        self.assertIn(resp["content_type"], content_type, msg=f"场景 [{scene}] 响应类型错误，正确类型为'流式'")
        self.assertNotIn(resp["resp_content"], full_response, msg=f"场景 [{scene}] 响应内容不匹配")

