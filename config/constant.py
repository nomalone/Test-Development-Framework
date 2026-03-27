
from datetime import datetime, timedelta


class Constants(object):
    """存储所有的常量"""
    # 日期相关
    TODAY = datetime.now().strftime("%Y-%m-%d")
    A_WEEK = (datetime.now() + timedelta(days=-7)).strftime("%Y-%m-%d")
    A_MONTH = (datetime.now() + timedelta(weeks=-4)).strftime("%Y-%m-%d")
    # 时间相关
    NOW_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    A_DAY_TIME = (datetime.now() + timedelta(days=-1)).strftime("%Y-%m-%d %H:%M:%S")
    A_WEEK_TIME = (datetime.now() + timedelta(days=-6)).strftime("%Y-%m-%d %H:%M:%S")
    SEVEN_DAY_TIME = (datetime.now() + timedelta(days=-7)).strftime("%Y-%m-%d %H:%M:%S")
    NOW_NUM = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    NOW_TIME_NUM = datetime.now().strftime("%Y%m%d%H%M%S")
    # 特殊时间点
    TODAY_00_TIME = datetime.now().strftime("%Y-%m-%d 00:00:00")
    TODAY_59_TIME = datetime.now().strftime("%Y-%m-%d 23:59:59")
    TODAY_LAST_TIME = (datetime.now() + timedelta(days=-1)).strftime("%Y-%m-%d 23:59:59")
    A_MONTH_FIRST_TIME = (datetime.now() + timedelta(weeks=-4)).strftime("%Y-%m-01 00:00:00")
    A_MONTH_START_TIME = (datetime.now() + timedelta(weeks=-4)).strftime("%Y-%m-%d 00:00:00")


cons = Constants()
