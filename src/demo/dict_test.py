#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2021/6/30 1:50 下午
# @Author  : 玄凌
# @File    : dict_test.py
# @Description : 功能描述
# @Software: PyCharm
"""


# init
def init() -> dict:
	# 1
	name_age_dict_1 = {'hao': 30, 'ye': 20}
	print(name_age_dict_1)
	# # 2
	# name_age_dict_2 = dict({'hao': 30, 'ye': 20})
	# print(name_age_dict_2)
	# # 3
	# name_age_dict_3 = dict([('hao', 30), ('ye', 20)])
	# print(name_age_dict_3)
	# # 4
	# name_age_dict_4 = dict(hao=30, ye=20)
	# print(name_age_dict_4)
	return name_age_dict_1


# 类型判断
def type_judge(name_age_dict: dict) -> bool:
	print(type(name_age_dict))
	flag = isinstance(name_age_dict, dict)
	print(flag)
	empty_dist = {}
	print('name_age_dict is null ? %s' % (empty_dist is None))
	print('name_age_dict is empty ? %s' % (empty_dist.__len__() == 0))
	return flag


# 查询
def search(name_age_dict: dict) -> None:
	print(name_age_dict['ye'])
	if 'ye' in name_age_dict:
		print(name_age_dict.__getitem__('ye'))
	print(len(name_age_dict))
	print(name_age_dict.__len__())
	print(name_age_dict.keys())
	print(name_age_dict.values())
	print(name_age_dict.__contains__('ye'))
	print(name_age_dict.items())


# 添加
def add(name_age_dict: dict) -> None:
	name_age_dict.setdefault('zhong', 50)
	print(name_age_dict)
	name_age_dict.__setitem__('fang', 40)
	print(name_age_dict)
	pass


# 删除
def delete(name_age_dict: dict) -> None:
	name_age_dict_copy = name_age_dict.copy()
	# if name_age_dict_copy.__contains__('hao'):
	# 	name_age_dict_copy.pop('hao')
	# if 'hao' in name_age_dict_copy:
	# 	name_age_dict_copy.pop('hao')
	name_age_dict_copy.clear()
	print(name_age_dict_copy)


# 遍历
def iter_dict(name_age_dict: dict) -> None:
	# for key in name_age_dict:
	# 	print(key)
	# for key, value in enumerate(name_age_dict):
	# 	print('key={},value={}'.format(key, value))
	# for key, value in name_age_dict.items():
	# 	print('key={},value={}'.format(key, value))
	for key in name_age_dict.keys():
		print('key={},value={}'.format(key, name_age_dict.__getitem__(key)))


if __name__ == '__main__':
	name_age_dict_11 = init()
	# type_judge(name_age_dict_11)
	# search(name_age_dict_11)
	# add(name_age_dict_11)
	# delete(name_age_dict_11)
	iter_dict(name_age_dict_11)
	pass
