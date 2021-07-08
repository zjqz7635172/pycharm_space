#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2021/6/29 4:55 下午
# @Author  : 玄凌
# @File    : student.py
# @Description : 功能描述
# @Software: PyCharm
"""
from common.attr_display import AttrDisplay


class Student(AttrDisplay):
	__slots__ = ('_name',)

	def __init__(self):
		self._name = None

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, value):
		self._name = value


if __name__ == '__main__':
	student = Student()
	student.name = 'ZH'
	print(student.name)
	print(dir(Student))
