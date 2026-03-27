import os


def mkdir_file(path_name):
    """创建文件目录，没有则自动创建"""
    os.makedirs(path_name, exist_ok=True)


class Paths(object):
    """存储所有的路径相关"""

    # 项目路径
    BASE_PATH = os.path.dirname(os.path.dirname(__file__))
    # 测试用例所在目录
    TESTS_PATH = os.path.join(BASE_PATH, 'testcase')
    # 测试工具所在目录
    TOOL_PATH = os.path.join(BASE_PATH, 'tool')
    # 输出文件所在目录
    OUTPUT_PATH = os.path.join(BASE_PATH, 'reports')
    mkdir_file(OUTPUT_PATH)
    # 日志文件所在目录
    LOG_PATH = os.path.join(OUTPUT_PATH, 'log')
    mkdir_file(LOG_PATH)



p_path = Paths()
print(p_path.BASE_PATH)
