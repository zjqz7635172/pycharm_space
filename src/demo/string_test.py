#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2021/6/30 6:02 下午
# @Author  : 玄凌
# @File    : string_test.py
# @Description : 功能描述
# @Software: PyCharm
"""


def print_a(name: str) -> None:
	pass


if __name__ == '__main__':
	message = 'I\'m a student'
	print(message)
	print(message[0])
	print(message[0:5])
	for s in message:
		print(s)
	print('hello {}'.format('zhonghao'))
	print('hello %s' % 'zhonghao')
	print(message.__add__(',what'))
	print(message + ',what')
	message.__add__()
	pass
