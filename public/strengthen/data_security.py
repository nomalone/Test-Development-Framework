import json
from seldom.request import HttpRequest
from seldom.utils import cache

from config.config import Config
from config.mylogger import my_log
from public.login import Login


class DataSecurity(HttpRequest):
    """
    数据安全配置
    """
    def __init__(self, cookie, route_id):
        self.cookie = cookie
        self.route_id = route_id
        self.url = Config().URL

    def sensitive_data_rules_set(self, configurations):
        """
        敏感数据规则设置:通过内置规则对身份证、手机号、银行账号、邮箱、股票账号、交易明细等敏感数据进行监测、拦截，保障模型数据安全
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
                r.raise_for_status()  # 检查请求是否成功
        except Exception as e:
            print("请求发生错误:", e)

    def sensitive_data_model_set(self, configurations):
        """
        敏感数据模型设置:通过小模型对敏感数据进行检测、拦截，保障模型数据安全
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
            my_log.error(f"请求发生错误: {e}")

