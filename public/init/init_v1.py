import time

import seldom
from seldom.request import HttpRequest
from seldom.utils import cache
from config.config import Config
from public.login import Login


class Init(HttpRequest):

    def __init__(self, cookie):
        self.cookie = cookie
        self.headers = {'Cookie': self.cookie}
        self.url = Config().URL
        self.model_host = Config().HOST


    def create_mock_model(self):
        """
        创建mock服务模型：
        """
        provider_id = cache.get("provider_mock_id")
        if provider_id:
            return provider_id
        req = {

        }

        url = f"*****"
        try:
            r = self.post(url, headers=self.headers, json=req, verify=False)
            provider_id = r.json()["rawConfigs"]["id"]
            cache.set({"provider_mock_id": provider_id})
            return provider_id
        except Exception as e:
            print(f"创建模型发生错误: {e}")

    def create_private_model(self):
        """
        创建私有模型：
        """
        provider_id = cache.get("provider_auto_id")
        if provider_id:
            return provider_id
        req = {

        }

        url = f"******"
        try:
            r = self.post(url, headers=self.headers, json=req, verify=False)
            provider_id = r.json()["rawConfigs"]["id"]
            cache.set({"provider_auto_id": provider_id})
            return provider_id
        except Exception as e:
            print(f"创建模型发生错误: {e}")

    def create_domain(self, domain_name):
        """
        创建域名：返回域名：domain_name
        """
        req = {

        }
        url = f"****"
        r = self.post(url, headers=self.headers, json=req, verify=False)
        try:
            r.raise_for_status()
        except Exception as e:
            print(f"创建域名发生错误: {e}")

    def create_route(self, provider_id, route_name, route_id):
        """
        创建域名和路由，返回路由id：route_id
        """
        self.create_domain(route_name)
        req2 = {
          }
        url = f"***"
        r = self.post(url, headers=self.headers, json=req2, verify=False)
        try:
            r.raise_for_status()
        except Exception as e:
            print(f"创建路由发生错误: {e}")

    def create_department(self):
        """
        创建组织架构，返回组织架构id：department_id
        """
        req = {
        }
        url = f"***"
        r = self.post(url, headers=self.headers, json=req, verify=False)
        try:
            r.raise_for_status()
            department_id = r.json()["data"]["_id"]
            return department_id
        except Exception as e:
            print(f"创建部门发生错误: {e}")

    def create_consumer(self):
        """
        创建消费者，返回消费者id：consumer_id
        """
        # 查看缓存是否有消费者，有就直接返回
        consumer_id = cache.get("**")
        if consumer_id:
            return

        # 查看系统中是否有对应的消费者，有就直接返回
        uid = self.search_consumer("**")
        if uid:
            return

        # 都没有就创建对应的消费者
        req = {
        }
        provider_mock_id = self.create_mock_model()
        provider_auto_id = self.create_private_model()
        for index, i in enumerate(self.route_info):
            if index < 4:
                self.create_route(provider_id=provider_mock_id, route_id=i[0], route_name=i[1])
        # j = self.route_info[-1]
            else:
                self.create_route(provider_id=provider_auto_id, route_id=i[0], route_name=i[1])
        req["department"] = self.create_department()
        url = f"{self.url}/api/consumer/user"
        r = self.post(url, headers=self.headers, json=req, verify=False)
        consumer_id = req["uid"]
        cache.set({"consumer_id": consumer_id})
        time.sleep(30)

    def search_consumer(self, consumer_id):
        """
        查询消费者
        """
        # 查询系统是否存在该消费者
        url = f"***"
        r = self.get(url, headers=self.headers, params={"uid": consumer_id}, verify=False)
        uids = [item['uid'] for item in r.json()['data']['list']]
        if consumer_id in uids:
            cache.set({"consumer_id": consumer_id})
            return consumer_id


if __name__ == '__main__':

    cache.clear()
    seldom.main(timeout=120)
    init = Init(Login().login())
    init.create_consumer()
