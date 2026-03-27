
import time, seldom
from seldom.utils import cache
from config.config import Config
from public.login import Login
from public.provider.provider import Provider
from public.route.domain import Domain
from public.route.route import Route
from public.token.consumer import Consumer
from public.token.department import Department


class TestConsumer(seldom.TestCase):
    """消费者"""

    @classmethod
    def start_class(cls):
        cls.cookie = Login().login()
        cls.headers = {'Cookie': cls.cookie}
        cls.url = Config().URL
        cls.model_host = Config().HOST

        Route(cls.cookie).create_route()
        cls.department_id = Department(cls.cookie).create_department()


    @classmethod
    def end_class(cls):
        Department(cls.cookie).del_department()
        Route(cls.cookie).del_route()
        Domain(cls.cookie).del_domain()
        Provider(cls.cookie).del_provider()
        time.sleep(20)

    @seldom.file_data("***", key="***")
    def test_00_add_consumer(self, scene, req, resp):
        """新增消费者"""
        # 删除即将创建的消费者
        name = req["name"]
        Consumer(self.cookie).del_consumer(name)
        req["department"] = self.department_id

        url = f"****"
        r = self.post(url, headers=self.headers, json=req, verify=False)
        self.assertStatusCode(200)
        self.assertEqual(resp["code"], r.json()["code"], msg=f"场景 [{scene}] code码不匹配")

    @seldom.file_data("****", key="****")
    def test_01_edit_consumer(self, scene, req, resp):
        """编辑消费者"""
        req["department"] = self.department_id
        url = f"****"
        r = self.put(url, headers=self.headers, json=req, verify=False)
        self.assertStatusCode(200)
        self.assertEqual(resp["code"], r.json()["code"], msg=f"场景 [{scene}] code码不匹配")

    @seldom.file_data("***", key="***")
    def test_02_del_consumer(self, scene, req, resp):
        """删除消费者"""
        url = f"***"
        r = self.post(url, headers=self.headers, json=req, verify=False)
        self.assertStatusCode(200)
        self.assertEqual(resp["code"], r.json()["code"], msg=f"场景 [{scene}] code码不匹配")
