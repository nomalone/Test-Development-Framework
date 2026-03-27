
import seldom
from config.config import Config
from public.login import Login
from public.provider.provider import Provider


class TestProvider(seldom.TestCase):
    """模型管理"""
    @classmethod
    def start_class(cls):
        cls.cookie = Login().login()
        cls.headers = {'Cookie': cls.cookie}
        cls.url = Config().URL
        cls.model_host = Config().HOST

    @seldom.file_data("provider_data.json", key="***")
    def test_00_add_provider(self, scene, req, resp):
        """新增模型"""
        # 尝试删除即将创建的模型
        provider_id = req["name"]
        Provider(self.cookie).del_provider(provider_id)

        url = f"***"
        self.post(url, headers=self.headers, json=req, verify=False)
        self.assertStatusCode(resp["code"], msg=f"场景 [{scene}] 状态码不匹配")

    @seldom.file_data("provider_data.json", key="***")
    def test_01_edit_provider(self, scene, req, resp):
        """编辑模型"""
        url = f"***"
        self.put(url, headers=self.headers, json=req, verify=False)
        self.assertStatusCode(resp["code"], msg=f"场景 [{scene}] 状态码不匹配")

    @seldom.file_data("provider_data.json", key="***")
    def test_02_del_provider(self, scene, req, resp):
        """删除模型"""
        url = f"***"
        self.delete(url, headers=self.headers, verify=False)
        self.assertStatusCode(resp["code"], msg=f"场景 [{scene}] 状态码不匹配")

