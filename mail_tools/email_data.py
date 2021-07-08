#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2021/6/29 5:20 下午
# @Author  : 玄凌
# @File    : email_data.py
# @Description : 功能描述
# @Software: PyCharm
"""
from common.attr_display import AttrDisplay


class EmailData(AttrDisplay):
	__slots__ = ('_receiver', '_mail_title', '_mail_body')

	def __init__(self, receiver: str, mail_title: str, mail_body: str):
		self._mail_body = mail_body
		self._mail_title = mail_title
		self._receiver = receiver

	# 收件人
	@property
	def receiver(self):
		return self._receiver

	# 标题
	@property
	def mail_title(self):
		return self._mail_title

	# 正文
	@property
	def mail_body(self):
		return self._mail_body


if __name__ == '__main__':
	pass
