import json
from seldom.request import HttpRequest
from seldom.utils import cache

from config.config import Config
from config.mylogger import my_log
from public.login import Login


class OtherSecurity(HttpRequest):
    """
    其他管控配置
    """
    def __init__(self, cookie, route_id):
        self.cookie = cookie
        self.route_id = route_id
        self.url = Config().URL

    def ks_ai_prompt_enhance_set(self, configurations):
        """
        提示词加固设置:
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

    def ks_redline_guard_set(self, configurations):
        """
        安全代答:
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

    def ks_file_extract_set(self, configurations):
        """
        文件监测设置:
        """
        data = {}

        headers = {'Cookie': self.cookie}
        url = f"**"
        try:
            r = self.put(url, headers=headers, json=data, verify=False)
            if r.status_code == 401:
                cache.clear("cookie")
                new_cookie = Login().login()
                r = self.put(url, headers={'Cookie': new_cookie}, json=data, verify=False)
                r.raise_for_status()  # 检查请求是否成功
        except Exception as e:
            print("请求发生错误:", e)

    def ks_log_request_response_set(self, configurations):
        """
        请求响应日志设置:
        """
        data = {}

        headers = {'Cookie': self.cookie}
        url = f"**"
        try:
            r = self.put(url, headers=headers, json=data, verify=False)
            if r.status_code == 401:
                cache.clear("cookie")
                new_cookie = Login().login()
                r = self.put(url, headers={'Cookie': new_cookie}, json=data, verify=False)
                r.raise_for_status()  # 检查请求是否成功
        except Exception as e:
            print("请求发生错误:", e)
