from seldom.request import HttpRequest
from config.config import Config
from config.mylogger import my_log

class Consumer(HttpRequest):

    def __init__(self, cookie):
        self.cookie = cookie
        self.headers = {'Cookie': self.cookie}
        self.url = Config().URL

    def create_consumer(self, req=None):

        if not req:
            req = {}
        url = f"***"
        try:
            r = self.post(url, headers=self.headers, json=req, verify=False)
            r.raise_for_status()

        except Exception as e:
            print(f"创建消费者发生错误: {e}")
            my_log.error(f"创建消费者发生错误: {e}")

    def del_consumer(self, consumer_id="***"):
        """删除消费者"""
        url = f"****l"
        req = {
            "uidList": [consumer_id]
        }
        r = self.post(url, headers=self.headers, json=req, verify=False)
        try:
            r.raise_for_status()
        except Exception as e:
            raise Exception("删除消费者发生错误: %s" % e)


