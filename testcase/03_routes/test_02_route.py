
import time, seldom
from seldom.utils import cache
from config.config import Config
from public.login import Login
from public.provider.provider import Provider
from public.route.domain import Domain
from public.route.route import Route


class TestRoute(seldom.TestCase):
    """路由管理"""
    @classmethod
    def start_class(cls):
        cls.cookie = Login().login()
        cls.headers = {'Cookie': cls.cookie}
        cls.url = Config().URL
        cls.model_host = Config().HOST
        Provider(cls.cookie).create_provider()
        Domain(cls.cookie).create_domain()

    @seldom.file_data("route_data.json", key="3-1-1-route-000")
    def test_00_add_route(self, scene, req, resp):
        """新增路由"""
        # 删除即将创建的路由
        route_name = req["name"]
        Route(self.cookie).del_route(route_name)

        url = f"***"
        self.post(url, headers=self.headers, json=req, verify=False)
        self.assertStatusCode(resp["code"], msg=f"场景 [{scene}] 状态码不匹配")

    @seldom.file_data("***", key="***")
    def test_01_edit_route(self, scene, req, resp):
        """编辑路由"""
        url = f"***"
        self.put(url, headers=self.headers, json=req, verify=False)
        self.assertStatusCode(resp["code"], msg=f"场景 [{scene}] 状态码不匹配")

    @seldom.file_data("***", key="***")
    def test_02_del_route(self, scene, req, resp):
        """删除路由"""
        url = f"***"
        self.delete(url, headers=self.headers, verify=False)
        self.assertStatusCode(resp["code"], msg=f"场景 [{scene}] 状态码不匹配")

