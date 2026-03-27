
from seldom.request import HttpRequest
from config.config import Config
from config.mylogger import my_log


class Provider(HttpRequest):

    def __init__(self, cookie):
        self.cookie = cookie
        self.headers = {'Cookie': self.cookie}
        self.url = Config().URL

    def create_provider(self, req=None):

        if not req:
            req = {}
        url = f"******"
        try:
            r = self.post(url, headers=self.headers, json=req, verify=False)
            r.raise_for_status()
            provider_id = r.json()["rawConfigs"]["id"]
            return provider_id
        except Exception as e:
            print(f"创建模型发生错误: {e}")
            my_log.error(f"创建模型发生错误: {e}")


    def del_provider(self, provider_id="******"):
        """删除模型"""
        url = f"*********"
        try:
            r = self.delete(url, headers=self.headers, verify=False)
            r.raise_for_status()
        except Exception as e:
            my_log.error(f"创建模型发生错误: {e}")


