from seldom import logging
import time, seldom, urllib3
from seldom.utils import cache
from multiprocessing import Pool
from urllib3.exceptions import InsecureRequestWarning



# 禁用 InsecureRequestWarning 警告
urllib3.disable_warnings(InsecureRequestWarning)

# 设置日志级别为WARNING，只打印警告及以上级别日志
logging.log_cfg.set_level(
level='WARNING',
)

def run_test_suite(relative_path):
    """
    单个测试任务：独立进程中执行指定目录的测试用例
    """
    report_type = "xml"
    if type(relative_path) == list:
        report_name = f"****"
        print("开始执行：", report_name)
    else:
        report_suffix = relative_path.split("/")[-1]
        print("开始执行：", report_suffix)
        report_name = f"{report_suffix}_result.{report_type}"

    seldom.main(
        path=relative_path,
        title="****",
        tester="***",
        rerun=0,
        description="****",
        timeout=120,
        report=report_name
    )


if __name__ == "__main__":
    cache.clear()
    
    test_paths = [
        "testcase"
           ]
    with Pool(processes=1) as pool:
        results = pool.map_async(run_test_suite, test_paths)
        try:
            results.get(timeout=7200)
            print("所有测试任务执行完毕！")
        except Exception as e:
            print(f"测试执行失败: {str(e)}")
            pool.terminate()  # 异常时强制终止所有进程

    cache.clear()
