import time, seldom
from seldom.utils import cache
from config.config import Config
from public.strengthen.content_security import ContentSecurity
from public.api_client_v1 import APIClient
from public.login import Login


class TestPromptInjectAllClose(seldom.TestCase):
    """增强管理-内容安全-提示词注入防护:所有规则-关闭"""

    @classmethod
    def start_class(cls):
        # 初始化配置
        cls.cookie = Login().login()

        config = {}
        ContentSecurity(cls.cookie, Config.route_content_security_id).ks_prompt_guard(config)
        time.sleep(Config.time_random)  # 等待配置生效
        cls.api = APIClient(Config.route_content_security_name)

    # 第一个方法：收集所有测试数据
    @seldom.file_data("prompt_inject_all_data.json", key="5-2-3-prompt-inject-all-001")
    def test_prompt_inject_all_close(self, scene, req, resp):
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


if __name__ == "__main__":
    seldom.main()
