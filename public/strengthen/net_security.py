import json
from seldom.request import HttpRequest
from seldom.utils import cache

from config.config import Config
from config.mylogger import my_log
from public.login import Login


class NetSecurity(HttpRequest):
    """
    网络安全配置
    """
    def __init__(self, cookie, route_id):
        self.cookie = cookie
        self.route_id = route_id
        self.url = Config().URL

    def ks_waf_set(self, configurations, enable = True):
        data = {}
        headers = {'Cookie': self.cookie}
        url = f"***"
        try:
            r = self.put(url, headers=headers, json=data, verify=False)
            if r.status_code == 401:
                cache.clear("cookie")
                new_cookie = Login().login()
                r = self.put(url, headers={'Cookie': new_cookie}, json=data, verify=False)
                r.raise_for_status()  # 检查请求是否成功
        except Exception as e:
            print("请求发生错误:", e)

    def ks_waf_code_set(self, configurations):
        """
        网络安全-高级扫描防护:
        """
        data = {}
        headers = {'Cookie': self.cookie}
        url = f"***"
        try:
            r = self.put(url, headers=headers, json=data, verify=False)
            if r.status_code == 401:
                cache.clear("cookie")
                new_cookie = Login().login()
                r = self.put(url, headers={'Cookie': new_cookie}, json=data, verify=False)
                r.raise_for_status()
        except Exception as e:
            print("请求发生错误:", e)

    def ks_waf_policy_set(self, configurations):
        """
        网络安全-防火墙-屏蔽时间:
        """
        data = {}
        headers = {'Cookie': self.cookie}
        url = f""
        try:
            r = self.put(url, headers=headers, json=data, verify=False)
            if r.status_code == 401:
                cache.clear("cookie")
                new_cookie = Login().login()
                r = self.put(url, headers={'Cookie': new_cookie}, json=data, verify=False)
                r.raise_for_status()  # 检查请求是否成功
        except Exception as e:
            print("请求发生错误:", e)

    def ks_request_block_set(self, configurations):
        """
        网络安全-CC策略控制:
        """
        data = {}
        headers = {'Cookie': self.cookie}
        url = f""
        try:
            r = self.put(url, headers=headers, json=data, verify=False)
            if r.status_code == 401:
                cache.clear("cookie")
                new_cookie = Login().login()
                r = self.put(url, headers={'Cookie': new_cookie}, json=data, verify=False)
                r.raise_for_status()  # 检查请求是否成功
        except Exception as e:
            print("请求发生错误:", e)

    def ks_ip_restriction_set(self, configurations):
        """
        网络安全-CC策略控制:
        """
        data = {}
        headers = {'Cookie': self.cookie}
        url = f""
        try:
            r = self.put(url, headers=headers, json=data, verify=False)
            if r.status_code == 401:
                cache.clear("cookie")
                new_cookie = Login().login()
                r = self.put(url, headers={'Cookie': new_cookie}, json=data, verify=False)
                r.raise_for_status()  # 检查请求是否成功
        except Exception as e:
            print("请求发生错误:", e)
