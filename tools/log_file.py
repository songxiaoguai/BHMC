import logging.handlers
import os

from tools.path_file import path_absolute

class GetLogin:
    __logger = None
    @classmethod
    def get_logger(cls):
        if cls.__logger is None:
            # 创建日志器
            cls.__logger = logging.getLogger()
            cls.__logger.setLevel(logging.INFO)
            # 创建日志输出
            trh = logging.handlers.TimedRotatingFileHandler(filename=path_absolute() + os.sep+"log"+os.sep+"log_data.log",
                                                            when="midnight",
                                                            interval=1,
                                                            backupCount=0,
                                                            encoding="utf-8")
            # 创建日志格式
            fm = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
            fmt = logging.Formatter(fm)
            # 日志输出添加格式
            trh.setFormatter(fmt)
            # 日志器添加日志输出
            cls.__logger.addHandler(trh)
        return cls.__logger