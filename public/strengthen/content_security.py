
import json
from seldom.request import HttpRequest
from seldom.utils import cache

from config.config import Config
from config.mylogger import my_log
from public.login import Login


class ContentSecurity(HttpRequest):
    """
    内容安全配置
    """

    def __init__(self, cookie, route_id):
        self.cookie = cookie
        self.route_id = route_id
        self.url = Config().URL

    def ks_keyword_guard_set(self, configurations):
        """
        内容安全-关键词监测:对模型输入输出的非法内容进行监测、拦截，保障模型内容安全
        """
        data = {
            "****"
        }
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

    def ks_model_guard_set(self, configurations):
        """
        内容安全-价值观模型监测:对模型政治敏感、暴力恐怖、黄赌毒及其他不良价值观内容进行监测、拦截，保障模型内容安全
        """
        data = {
           "**"
        }
        headers = {'Cookie': self.cookie}
        url = f"****"
        try:
            r = self.put(url, headers=headers, json=data, verify=False)
            if r.status_code == 401:
                cache.clear("cookie")
                new_cookie = Login().login()
                r = self.put(url, headers={'Cookie': new_cookie}, json=data, verify=False)
                r.raise_for_status()  # 检查请求是否成功
        except Exception as e:
            print("请求发生错误:", e)

    def ks_prompt_guard(self, configurations):
        """
        内容安全-提示词注入防护/模型越狱防护:
        """
        data = {
            "***"
        }
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

