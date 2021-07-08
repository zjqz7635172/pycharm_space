#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2021/6/29 6:05 下午
# @Author  : 玄凌
# @File    : email_helper.py
# @Description : 功能描述
# @Software: PyCharm
"""
import smtplib
from email.mime.text import MIMEText
from email.header import Header

from mail_tools.email_data import EmailData
from mail_tools.email_sender import EmailSenderData


def get_smtp(email_sender_data: EmailSenderData) -> smtplib.SMTP:
	smtp = smtplib.SMTP_SSL(email_sender_data.smtp_server, 465)  # 创建一个连接
	smtp.login(email_sender_data.user_name, email_sender_data.pass_word)  # 登录服务器
	return smtp


def send_mail(email_sender_data: EmailSenderData, email_data: EmailData, smtp: smtplib.SMTP) -> None:
	# 创建一个实例
	message = MIMEText(email_data.mail_body, 'plain', 'utf-8')  # 邮件正文
	# (plain表示mail_body的内容直接显示，也可以用text，则mail_body的内容在正文中以文本的形式显示，需要下载）
	message['From'] = email_sender_data.sender  # 邮件上显示的发件人
	message['To'] = email_data.receiver  # 邮件上显示的收件人
	message['Subject'] = Header(email_data.mail_title, 'utf-8')  # 邮件主题
	smtp.sendmail(email_sender_data.sender, email_data.receiver, message.as_string())  # 填入邮件的相关信息并发送


def smtp_quit(smtp: smtplib.SMTP) -> None:
	smtp.quit()


class EmailHelper:
	pass


if __name__ == '__main__':
	pass
