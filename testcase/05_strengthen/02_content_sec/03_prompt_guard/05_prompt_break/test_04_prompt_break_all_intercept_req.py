import json
import seldom
import time

from config.config import Config
from public.api_client_v1 import APIClient
from public.login import Login
from public.strengthen.content_security import ContentSecurity
from public.thread_utils import DataParallelRunner


class TestPromptBreakAllInterceptReqHit(seldom.TestCase):
    """增强管理-内容安全-模型越狱防护:所有规则-开启-拦截-提问命中"""

    @classmethod
    def start_class(cls):
        # 初始化配置
        cls.cookie = Login().login()
        cls.max_workers = Config().max_workers

        config = {}
        ContentSecurity(cls.cookie, Config.route_content_security_id).ks_prompt_guard(config)
        time.sleep(Config.time_random)  # 等待配置生效

        cls.api = APIClient(Config.route_content_security_name)
        cls.runner = DataParallelRunner(max_workers=cls.max_workers)  # 使用现有并发执行器

        # 加载测试数据
        with open("testcase/05_strengthen/02_content_sec/03_prompt_guard/05_prompt_break/prompt_break_all_data.json", "r",
                  encoding="utf-8") as f:
            json_data = json.load(f)
        cls.test_data = json_data.get("5-2-3-prompt-break-all-004", [])

    @classmethod
    def end_class(cls):
        config = {}
        ContentSecurity(cls.cookie, Config.route_content_security_id).ks_prompt_guard(config)

    def test_prompt_break_all_intercept_req(self):
        """调用大模型，发起请求"""
        # 确保有测试数据
        if not self.test_data:
            self.fail("未收集到任何测试数据")

        print(f"开始并发执行 {len(self.test_data)} 组测试数据")

        # 使用线程池并发执行所有测试数据
        self.runner.run(
            test_instance=self,
            data_list=self.test_data
        )

