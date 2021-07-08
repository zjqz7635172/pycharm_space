#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2021/6/28 3:43 下午
# @Author  : 玄凌
# @File    : utils.py
# @Description : 功能描述
# @Software: PyCharm
"""


def build_get_str(name):
    print('    @property')
    print('    def %s(self):' % name[1:len(name)])
    print('        return self.%s' % name)
    print()


def build_set_str(name):
    print('    @%s.setter' % name[1:len(name)])
    print('    def %s(self, value):' % name[1:len(name)])
    print('        self.%s = value' % name)
    print()


def print_iterable(iterable_data):
    for data in iterable_data:
        print(data)


if __name__ == '__main__':
    attributeList = ['_sender', '_smtp_server', '_user_name', '_pass_word', '_receiver', '_mail_title', '_mail_body']
    for attribute in attributeList:
        build_get_str(attribute)
        build_set_str(attribute)
