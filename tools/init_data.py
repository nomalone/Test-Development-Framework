
class InitConfig(object):
    """存储项目的配置相关"""

    # 项目的URL
    HOST = "****"
    PORT = '****'
    URL = "https://" + HOST + ":" + PORT

    # 登录请求body
    LOGIN_REQ = {
        "username": "***",
        "password": "***",
        "captcha": "***",
        "uuid": "***",
        "type": "***"
    }

    # 模型：请求body
    PROVIDER_MOCK_REQ = [
        {}
    ]
    PROVIDER_NORMAL_REQ = [
        {}
    ]

    # 路由域名列表
    ROUTE_MOCK_INFO = []
    ROUTE_NORMAL_INFO = []
    ROUTE_API_CHECK_INFO = []

    # 消费者：
    CONSUMER = []



