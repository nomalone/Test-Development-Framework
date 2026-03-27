
from seldom.request import HttpRequest
from config.config import Config
from config.mylogger import my_log


class Department(HttpRequest):

    def __init__(self, cookie):
        self.cookie = cookie
        self.headers = {'Cookie': self.cookie}
        self.url = Config().URL

    def create_department(self, req=None):

        if not req:
            req = {
                "name": "===",
                "parent": "==="
            }
        url = f"==="
        try:
            r = self.post(url, headers=self.headers, json=req, verify=False)
            r.raise_for_status()
            department_id = r.json()["data"]["_id"]
            return department_id

        except Exception as e:
            print(f"创建组织架构发生错误: {e}")
            my_log.error(f"创建组织架构发生错误: {e}")

    def del_department(self, name="默认/功能测试部-dev"):

        req = {
            "fullnameList": [name]
        }

        url = f"***"

        try:
            r = self.post(url, headers=self.headers, json=req, verify=False)
            r.raise_for_status()
        except Exception as e:
            my_log.error(f"创建组织架构发生错误: {e}")


