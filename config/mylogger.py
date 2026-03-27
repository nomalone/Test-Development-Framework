
import os
import logging
from config.config import conf
from config.paths import p_path
from logging.handlers import TimedRotatingFileHandler


class MyLogging(object):
    log_name = conf.LOG_NAME
    log_level = conf.LOG_LEVEL
    sh_level = conf.SH_LEVEL
    fh_level = conf.FH_LEVEL
    # 拼接日志文件路径
    file_path = os.path.join(p_path.LOG_PATH, log_name + ".log")

    def __new__(cls, *args, **kwargs):
        """创建对象"""
        # 第一步：创建日志收集器对象，并设置等级
        my_log = logging.getLogger(cls.log_name)
        my_log.setLevel(cls.log_level)

        # 第二步：创建日志输出渠道，并设置等级
        # 1、输出到控制台
        sh = logging.StreamHandler()
        sh.setLevel(cls.sh_level)
        # 2、输出到日志文件
        # 按照时间间隔进行日志轮转，每天存放一个文件，最多轮转7个文件，即一周
        fh = TimedRotatingFileHandler(filename=cls.file_path, when="D", backupCount=7, interval=1, encoding="utf8")
        fh.setLevel(cls.fh_level)

        # 第三步：添加日志输出渠道到日志收集器中
        my_log.addHandler(sh)
        my_log.addHandler(fh)

        # 第四步：指定日志输出格式
        fot = logging.Formatter("[%(asctime)s][%(filename)s-->line:%(lineno)d][%(levelname)s] %(message)s")
        # 将日志输出格式对象绑定到日志输出渠道中
        sh.setFormatter(fot)
        fh.setFormatter(fot)

        return my_log


# 创建一个日志收集器对象
my_log = MyLogging()
