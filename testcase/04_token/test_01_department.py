
import time, seldom
from seldom.utils import cache
from config.config import Config
from public.login import Login
from public.token.department import Department


class TestDepartment(seldom.TestCase):
    """组织架构"""

    @classmethod
    def start_class(cls):
        cls.cookie = Login().login()
        cls.headers = {'Cookie': cls.cookie}
        cls.url = Config().URL
        cls.model_host = Config().HOST

    @seldom.file_data("***", key="***")
    def test_00_add_department(self, scene, req, resp):
        """新增组织架构"""
        # 删除即将创建的组织架构
        name = "默认/" + req["name"]
        Department(self.cookie).del_department(name)

        url = f"***"
        r = self.post(url, headers=self.headers, json=req, verify=False)
        self.assertStatusCode(200)
        self.assertEqual(resp["code"], r.json()["code"], msg=f"场景 [{scene}] code码不匹配")

    @seldom.file_data("****", key="****")
    def test_01_edit_department(self, scene, req, resp):
        """编辑组织架构"""
        url = f"****"
        r = self.put(url, headers=self.headers, json=req, verify=False)
        self.assertStatusCode(200)
        self.assertEqual(resp["code"], r.json()["code"], msg=f"场景 [{scene}] code码不匹配")

    @seldom.file_data("****", key="***")
    def test_02_del_department(self, scene, req, resp):
        """删除组织架构"""
        url = f"*"
        r = self.post(url, headers=self.headers, json=req, verify=False)
        self.assertStatusCode(200)
        self.assertEqual(resp["code"], r.json()["code"], msg=f"场景 [{scene}] code码不匹配")
