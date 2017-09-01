# coding:utf-8

import logging
import time
import os

# log_path是存放日志的路径
cur_path = os.path.dirname(os.path.abspath(__file__))
test_time = time.strftime("%Y_%m_%d_%H%M%S")
log_path = os.path.join(os.path.dirname(cur_path), 'log')
# 如果不存在这个logs文件夹，就自动创建一个
if not os.path.exists(log_path):
    os.mkdir(log_path)


# 配置日志写入log目录
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='%s/%s.log' % (log_path, test_time),
                    filemode='w')


# 打印消息
def loginfo(mes):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    # 定义屏幕控制器把日志输出屏幕
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)  # 输出屏幕的日志级别
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)  # 给输出屏幕的日志设置日志格式
    logger.addHandler(ch)  # 将设定好的控制器添加到日志器中
    return logger.info(mes)


