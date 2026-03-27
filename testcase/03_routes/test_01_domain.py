
import time, seldom
from seldom.utils import cache
from config.config import Config
from public.login import Login
from public.route.domain import Domain


class TestDomain(seldom.TestCase):
    """域名管理"""

    @classmethod
    def start_class(cls):
        cls.cookie = Login().login()
        cls.headers = {'Cookie': cls.cookie}
        cls.url = Config().URL
        cls.model_host = Config().HOST

    @seldom.file_data("***", key="***")
    def test_00_add_domain(self, scene, req, resp):
        """新增域名"""
        # 删除即将创建的域名
        name = req["name"]
        Domain(self.cookie).del_domain(name)

        url = f"***"
        self.post(url, headers=self.headers, json=req, verify=False)
        self.assertStatusCode(resp["code"], msg=f"场景 [{scene}] 状态码不匹配")

    @seldom.file_data("***", key="***")
    def test_01_edit_domain(self, scene, req, resp):
        """编辑域名"""
        url = f"****"
        self.put(url, headers=self.headers, json=req, verify=False)
        self.assertStatusCode(resp["code"], msg=f"场景 [{scene}] 状态码不匹配")

    @seldom.file_data("***", key="***")
    def test_02_del_domain(self, scene, req, resp):
        """珊瑚域名"""
        url = f"****"
        self.delete(url, headers=self.headers, verify=False)
        self.assertStatusCode(resp["code"], msg=f"场景 [{scene}] 状态码不匹配")

