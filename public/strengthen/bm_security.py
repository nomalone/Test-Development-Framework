
from seldom.request import HttpRequest
from seldom.utils import cache

from config.config import Config
from config.mylogger import my_log
from public.login import Login


class BMSecurity(HttpRequest):
    """
    保密安全配置
    """

    def __init__(self, cookie, route_id):
        self.cookie = cookie
        self.route_id = route_id
        self.url = Config().URL

    def bm_rule_set(self, action="block"):
        """
        保密自定义规则设置:
        """
        data = [
            {
           "****"
            }
        ]
        headers = {'Cookie': self.cookie}
        url = f"{"***"}"
        try:
            for i in data:
                r = self.post(url, headers=headers, json=i, verify=False)
                r.raise_for_status()  # 检查请求是否成功
                cache.set({f"{i['name']}-id": r.json()['data']["_id"]})
        except Exception as e:
            print("请求发生错误:", e)

    def bm_rule_del(self):
        """
        保密自定义规则删除:
        """
        ids = [cache.get("bm-rule-id")]
        headers = {'Cookie': self.cookie}
        try:
            for i in ids:
                url = f"***"
                r = self.delete(url, headers=headers, verify=False)
                r.raise_for_status()  # 检查请求是否成功
        except Exception as e:
            print("请求发生错误:", e)

    def apply(self):
        """
        保密自定义规则生效:
        """
        data = {"success": True}
        headers = {'Cookie': self.cookie}
        url = f"***"
        self.post(url, headers=headers, json=data, verify=False)

    def ks_bm_guard_set(self, configurations):
        """
        保密安全:
        """
        data = {
            "****"
        }
        headers = {'Cookie': self.cookie}
        url = f"*****"
        try:
            r = self.put(url, headers=headers, json=data, verify=False)
            if r.status_code == 401:
                cache.clear("cookie")
                new_cookie = Login().login()
                r = self.put(url, headers={'Cookie': new_cookie}, json=data, verify=False)
                r.raise_for_status()  # 检查请求是否成功
        except Exception as e:
            print("请求发生错误:", e)
