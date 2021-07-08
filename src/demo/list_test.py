#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2021/6/30 10:22 上午
# @Author  : 玄凌
# @File    : list_test.py
# @Description : 功能描述
# @Software: PyCharm
"""


# 初始化
def init() -> list:
	# 1
	name_list_1 = ['1', '2', '3', '11', '2', '3']
	print(name_list_1)
	# # 2
	# name_tuple = ('1', '2', '3', '11', '2', '3')
	# print(list(name_tuple))
	# # 3
	# name_dist = {'1': 'a', '2': 'b', '3': 'c', '11': 'k', '2': 'b', '3': 'c'}
	# print(list(name_dist.keys()))
	# # 4
	# name_set = {'1', '2', '3', '11', '2', '3'}
	# print(list(name_set))
	# 5
	# name_list_2 = name_list_1.copy()
	# print(name_list_2)
	return name_list_1


# 类型判断
def type_judge(name_list: list) -> bool:
	print(type(name_list))
	flag = isinstance(name_list, list)
	print(flag)
	age_list = []
	print('age_list is null ? %s' % (age_list is None))
	print('age_list is empty ? %s' % (age_list.__len__() == 0))
	return flag


# 查询
def search(name_list: list) -> None:
	# print(name_list[0])
	print(name_list.__getitem__(0))
	# print(name_list[-1])
	print(name_list.__getitem__(-1))
	# print(len(name_list))
	print(name_list.__len__())
	print(name_list.count('2'))
	print(name_list.index('2'))
	print(sorted(name_list))
	print(list(reversed(name_list)))


# 添加
def add(name_list: list) -> None:
	name_list.append('ccc')
	print(name_list)
	name_list.insert(1, 'ddd')
	print(name_list)


# 删除
def delete(name_list: list) -> None:
	name_list_copy = name_list.copy()
	if 'hao' in name_list_copy:
		name_list_copy.remove('hao')
		print(name_list_copy)
	if '1' in name_list_copy:
		name_list_copy.remove('1')
		print(name_list_copy)
	name_list_copy.pop(0)
	print(name_list_copy)
	name_list_copy.clear()
	print(name_list_copy)


# 切片
def sub_list(name_list: list) -> None:
	print(name_list[0:1])
	print(name_list[:2])
	print(name_list[2:])


# 遍历
def iter_list(name_list: list) -> None:
	for name in name_list:
		print(name)
	for index, name in enumerate(name_list):
		print('index=%s,name=%s' % (index, name))
	for index in range(0, len(name_list)):
		print('index=%s,name=%s' % (index, name_list.__getitem__(index)))
	# for index in range(0, len(name_list)):
	# 	print('index=%s,name=%s' % (index, name_list[index]))
	print(list(map(lambda item: item[0], name_list)))
	print(list(filter(lambda item: str.startswith(item, 'z'), name_list)))


# 去重
def dup_list(name_list: list) -> None:
	print(set(name_list))


if __name__ == '__main__':
	name_list_11 = init()
	# type_judge(name_list_1)
	# search(name_list_11)
	# add(name_list_11)
	# delete(name_list_11)
	# sub_list(name_list_11)
	# iter_list(name_list_11)
	dup_list(name_list_11)
	pass

