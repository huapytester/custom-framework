# -*- coding:utf-8 -*-

import os
import sys
import smtplib
from config import settings
from email.mime.text import MIMEText
from email.header import Header

Base_path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))


# 获取最新的测试报告
def get_latest_report():
    report_path = os.path.join(Base_path, 'report')
    listdir = os.listdir(report_path)
    # 按照case的修改时间进行排序
    sorted(listdir, key=lambda rule: os.path.getmtime(os.path.join(report_path, rule)))
    report_file = os.path.join(report_path, listdir[-1])
    print report_file
    # 返回最近的报告绝对路径
    return report_file


# 发送测试结果邮件
def send_email(*args):
    # 打开测试html报告
    with open(get_latest_report(), 'rb') as fp:
        report_html = fp.read()
    sender = '15558015183@163.com'
    subject = args[0]
    smtpserver = 'smtp.163.com'
    receivers = args[1]
    # 中文需参数‘utf-8'，单字节字符不需要
    msg = MIMEText(report_html, 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = '自动化测试<lizhenhua@163.com>'
    msg['To'] = ','.join(receivers)
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(sender, "Happy2151")
    smtp.sendmail(sender, receivers, msg.as_string())
    smtp.quit()

