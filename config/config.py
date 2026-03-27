
class Config(object):
    """存储项目的配置相关"""
    # 项目的HOST
    # HOST = "****"
    HOST = ""
    # HOST = ""
    # HOST = ""
    PORT = ''

    # 项目的URL
    URL = "https://" + HOST + ":" + PORT

    # 项目的用户信息
    USER = "***"
    PW = "***"
    UUID = "***"

    # 大模型请求信息
    # LLM_URL = ""
    LLM_URL = "***"
    # LLM_URL = "***"
    # LLM_URL = "***"
    LLM_CHECK_URL = "http://" + HOST
    LLM_Authorization = "***"
    LLM_CHECK_Authorization = "***"
    LLM_HOST = "***"
    LLM_MODEL = "***"
    LLM_MODEL_AUTO = '**'

    wait_time = 40

    time_random = (5,10)

    # 路由名称
    route_net_security_name = "*"
    route_content_security_name = "**"
    route_content_security_name1 = "***"
    route_content_security_name2 = "***"

    # 路由id
    route_net_security_id = "111"
    route_content_security_id = "111"
    route_content_security_id1 = "111"
    route_content_security_id2 = "a111"

    # 实例名称
    api_check_name = "111"
    api_check_domain = "111"

    # 最大线程数
    max_workers = 10

    # log日志的相关信息
    LOG_LEVEL = "DEBUG"
    SH_LEVEL = "INFO"
    FH_LEVEL = "DEBUG"
    LOG_NAME = "my_log"



conf = Config()

