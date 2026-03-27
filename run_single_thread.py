import time, seldom, urllib3
from seldom import logging
from seldom.utils import cache
from urllib3.exceptions import InsecureRequestWarning

# 禁用 InsecureRequestWarning 警告
urllib3.disable_warnings(InsecureRequestWarning)

# 设置日志级别为WARNING，只打印警告及以上级别日志
logging.log_cfg.set_level(
level='WARNING'
)

if __name__ == "__main__":
    # 清理缓存
    cache.clear()
    # report_name = "test_result.xml"  # xml用于ALLURE生成统一报告
    report_name = "test_result.html"   # html

    # 执行测试用例目录
    seldom.main(
        path="testcase/05_strengthen",
        title="****",
        tester="****",
        rerun=0,
        report=report_name,
        # debug=True,
        description="windows 10",
        timeout=120
    )
    # 清理缓存
    cache.clear()



