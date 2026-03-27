from seldom.request import HttpRequest
from config.config import Config
from config.mylogger import my_log


class Route(HttpRequest):

    def __init__(self, cookie):
        self.cookie = cookie
        self.headers = {'Cookie': self.cookie}
        self.url = Config().URL

    def create_route(self, req=None):

        if not req:
            req = {}
        url = f"*****"
        try:
            r = self.post(url, headers=self.headers, json=req, verify=False)
            r.raise_for_status()

        except Exception as e:
            print(f"创建路由发生错误: {e}")
            my_log.error(f"创建路由发生错误: {e}")

    def del_route(self, route_id="***"):
        """删除路由"""
        url = f"****"
        try:
            r = self.delete(url, headers=self.headers, verify=False)
            r.raise_for_status()
        except Exception as e:
            my_log.error(f"创建路由发生错误: {e}")


