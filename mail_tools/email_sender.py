#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2021/6/29 7:26 下午
# @Author  : 玄凌
# @File    : email_sender.py
# @Description : 功能描述
# @Software: PyCharm
"""
from common.attr_display import AttrDisplay


class EmailSenderData(AttrDisplay):
    __slots__ = ('_sender', '_smtp_server', '_user_name', '_pass_word')

    def __init__(self, sender: str, user_name: str, pass_word: str):
        self._pass_word = pass_word
        self._user_name = user_name
        self._smtp_server = 'smtp.qq.com'
        self._sender = sender

    # 发件人
    @property
    def sender(self):
        return self._sender

    @property
    def smtp_server(self):
        return self._smtp_server

    @smtp_server.setter
    def smtp_server(self, value):
        self._smtp_server = value

    @property
    def user_name(self):
        return self._user_name

    @property
    def pass_word(self):
        return self._pass_word


if __name__ == '__main__':
    pass

