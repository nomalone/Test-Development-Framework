
import requests
from seldom.request import HttpRequest
from seldom.utils import cache
from config.config import Config
from config.mylogger import my_log


class Login(HttpRequest):

    def __init__(self):
        self.url = Config().URL
        self.user = Config().USER
        self.pw = Config().PW
        self.uuid = Config().UUID
        self.session = requests.session()

    def login(self):

        cookie = cache.get("cookie")
        if cookie:
            return cookie
        data = {
            "username": self.user,
            "password": self.pw,
            "captcha": "***",
            "uuid": self.uuid,
            "type": "****"
        }
        url = f"******"
        try:
            r = self.post(url, json=data, verify=False)
            r.raise_for_status()
            cookies = r.headers.get("set-cookie").split("path=/;")
            cookie = ""
            for i in cookies[:4]:
                if 'secure; httponly,' in i:
                    x = i.split('secure; httponly,')[1]
                    cookie += x
                else:
                    cookie += i
            cache.set({"cookie": cookie})
            return cookie
        except Exception as e:
            my_log.error("请求发生错误:", e)

# Login().login()