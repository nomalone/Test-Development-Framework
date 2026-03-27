import os
import seldom
from seldom.utils import cache
from config.config import Config
from public.login import Login
from public.token.consumer import Consumer
from public.token.department import Department

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_FILE_PATH = os.path.join(CURRENT_DIR, "***")


class Testtoken(seldom.TestCase):
    @classmethod
    def start_class(cls):
        cache.clear()
        Login().login()



    """创建部门"""
    @seldom.file_data(JSON_FILE_PATH, key="***")
    def test_00_add_department(self, scene, req, resp):
        cookie = cache.get("cookie")
        headers = {"Cookie": cookie.strip()}
        url = Config().URL

        name = "默认/" + req["name"]
        Department(cookie).del_department(name)

        response = self.post(
            url=f"***",
            headers=headers,
            json=req,
            verify=False
        )
        self.assertStatusCode(200)
        self.assertEqual(resp["code"], response.json()["code"], msg=f"场景 [{scene}] code不匹配")


    """创建消费者"""
    @seldom.file_data(JSON_FILE_PATH, key="***")
    def test_01_add_comsumer(self, scene, req, resp):
        cookie = cache.get("cookie")
        headers = {'Cookie': cookie.strip()}
        url = Config().URL

        uid = req["uid"]
        Consumer(cookie).del_consumer(uid)

        response = self.post(
            url=f"***r",
            headers=headers,
            json=req,
            verify=False
            )

        self.assertStatusCode(200)
        self.assertEqual(resp["code"], response.json()["code"])


    #设置token额度
    @seldom.file_data(JSON_FILE_PATH, key="***n")
    def test_02_set_token(self,scene, req, resp):
        cookie = cache.get("cookie")
        headers = {"Cookie": cookie.strip()}
        url = Config().URL

        response = self.post(
            url=f"*",
            headers=headers,
            json=req,
            verify=False
        )

        self.assertStatusCode(200)
        self.assertEqual(resp["code"], response.json()["code"])


    #设置token限速
    @seldom.file_data(JSON_FILE_PATH, key="***")
    def test_03_set_detoken(self, scene, req):
        cookie = cache.get("cookie").strip()
        headers = {"Cookie": cookie}
        url = Config().URL

        uid = "***"
        Consumer(cookie).del_consumer(uid)
        req1 = {}
        response0 = self.post(
            url=f"***",
            headers=headers,
            json=req1,
            verify=False
        )

        r = self.put(
            url=f"****",
            headers=headers,
            json=req,
            verify=False
        )

        print("限速接口响应：", r.json())
        self.assertStatusCode(200)


    #设置请求限速
    @seldom.file_data(JSON_FILE_PATH, key="****")
    def test_04_set_reqspeed(self,scene, req, resp):
        cookie = cache.get("cookie")
        headers = {"Cookie": cookie.strip()}
        url = Config().URL

        response = self.put(
            url=f"****",
            headers=headers,
            json=req,
            verify=False
        )
        print("请求限速接口响应：", response.json())
        self.assertStatusCode(200)


    # 为消费者绑定路由
    @seldom.file_data(JSON_FILE_PATH, key="****")
    def test_05_set_routes(self, scene, req, resp):
        cookie = cache.get("cookie")
        headers = {"Cookie": cookie.strip()}
        url = Config().URL

        response = self.put(
            url=f"****",
            headers=headers,
            json=req,
            verify=False
        )
        self.assertStatusCode(200)
        self.assertEqual(resp["code"], response.json()["code"], msg=f"场景 [{scene}] code不匹配")


    #调整消费者部门
    @seldom.file_data(JSON_FILE_PATH, key="****")
    def test_06_put_department(self, scene, req, resp):
        cookie = cache.get("cookie")
        headers = {"Cookie": cookie.strip()}
        url = Config().URL

        response = self.post(
            url=f"****",
            headers=headers,
            json=req,
            verify=False
        )
        self.assertStatusCode(200)
        self.assertEqual(resp["code"], response.json()["code"], msg=f"场景 [{scene}] code不匹配")


    #吊销消费者令牌
    @seldom.file_data(JSON_FILE_PATH, key="***")
    def test_07_set_status(self,scene, req, resp):
        cookie = cache.get("cookie")
        headers = {"Cookie": cookie.strip()}
        url = Config().URL

        response = self.post(
            url=f"*",
            headers=headers,
            json=req,
            verify=False
        )
        self.assertStatusCode(200)
        self.assertEqual(resp["code"], response.json()["code"], msg=f"场景 [{scene}] code不匹配")



if __name__ == '__main__':
    seldom.main()