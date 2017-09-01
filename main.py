#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/31 22:21
# @Author  : 李振华

import unittest
import os
from common.HTMLTestrunner import HTMLTestRunner
from config import settings
import sys
from common.send_email import send_email
import time

# 项目根目录
Base_path = os.path.abspath(os.path.dirname(__file__))


# 添加用例到测试套件
def add_test(test_name='cases', rules='test*.py'):
    # 加载测试模块的所有用例
    cases_path = os.path.join(Base_path, test_name)
    # 模块路径若不存在，则创建该模块
    if not os.path.exists(cases_path):
        os.mkdir(cases_path)
        with open('cases/__init__.py', 'wb') as fp:
            fp.write('# -*- coding: utf-8 -*-')
    # 定义discover实例
    discover = unittest.defaultTestLoader.discover(cases_path, pattern=rules, top_level_dir=None)
    return discover


# 执行测试套件中的case
def run_test():
    test_time = time.strftime("%Y_%m_%d_%H%M%S")
    # 定义测试报告存储的位置
    test_report = os.path.join(Base_path, 'report')
    if not os.path.exists(test_report):
        os.mkdir(test_report)
    with open('report/%s.html' % test_time, 'w') as fp:
        runner = HTMLTestRunner(stream=fp, title='自动化测试报告：', description='测试执行情况：')
        runner.run(add_test())


if __name__ == '__main__':
    run_test()
    time.sleep(3)
    send_email(settings.EMAIL_SUBJECT, settings.EMAIL_RECEIVERS)










