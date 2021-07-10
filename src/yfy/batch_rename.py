#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2021/7/8 10:26 上午
# @Author  : 玄凌
# @File    : batch_rename.py
# @Description : 批量重命名
# @Software: PyCharm
"""
import os
import shutil
from os.path import isfile, isdir

from common.attr_display import AttrDisplay
from excel_tools.excel_helper import ExcelHelper


class RenameData(AttrDisplay):
	a: str = None  # 源文件名称
	b: str = None  # 目标文件名称


def source_has_repeat(_tables: list[list: RenameData]):
	source_file_set = []
	for _table in _tables:
		for _data in _table:
			_source_data: RenameData = _data
			if source_file_set.__contains__(_source_data.a):
				raise Exception("excel源文件列有数据重复,str={0}".format(_source_data.a))
			else:
				source_file_set.append(_source_data.a)


def dest_has_repeat(_tables: list[list: RenameData]):
	dest_file_set = []
	for _table in _tables:
		for _data in _table:
			_source_data: RenameData = _data
			if dest_file_set.__contains__(_source_data.b):
				raise Exception("excel目标文件列有数据重复,str={0}".format(_source_data.b))
			else:
				dest_file_set.append(_source_data.b)


def copy_and_rename(_source_file_dir: str, _dest_file_dir: str, _tables: list[list: RenameData]):
	source_dest_map = {}
	for _table in _tables:
		for _data in _table:
			_source_data: RenameData = _data
			source_dest_map.__setitem__(_source_data.a, _source_data.b)
	source_path = os.path.abspath(_source_file_dir)
	target_path = os.path.abspath(_dest_file_dir)

	if not os.path.exists(target_path):
		# 如果目标路径不存在原文件夹的话就创建
		os.makedirs(target_path)

	if os.path.exists(source_path):
		# 如果目标路径存在原文件夹的话就先删除，然后创建
		shutil.rmtree(target_path)
		os.makedirs(target_path)

	# root 所指的是当前正在遍历的这个文件夹的本身的地址
	# dirs 是一个 list，内容是该文件夹中所有的目录的名字(不包括子目录)
	# files 同样是 list, 内容是该文件夹中所有的文件(不包括子目录)
	for root, dirs, files in os.walk(source_path):
		for file in files:
			src_file_name = file.split('.')[0]
			if not source_dest_map.__contains__(src_file_name):
				print("文件重命名失败,源文件名称={0}".format(file))
			else:
				dest_file_name = source_dest_map.get(src_file_name)
				src_file = os.path.join(root, file)
				dest_file = target_path + "/" + file.replace(src_file_name, dest_file_name)
				shutil.copyfile(src_file, dest_file)
	print('copy files finished!')


if __name__ == '__main__':
	# 使用时只需要修改这里
	# excel文件路径
	# excel格式，第一列为源文件名称，第二列为目标文件名称
	# 例子（不需要带扩展名）
	# |源文件名称|目标文件名称|
	# |111     |222|
	excel_file_name = "/Users/pro/Desktop/rename/杭州易才凯捷科技有限公司纸质合同导入模板 (2).xlsx"
	# 文件夹路劲
	source_file_dir = "/Users/pro/Desktop/rename/2 - 副本"
	# 使用时只需要修改这里
	dest_file_dir = source_file_dir + "_copy"
	if not isfile(excel_file_name):
		raise FileNotFoundError("文件路径 {0} 不存在".format(excel_file_name))
	if not isdir(source_file_dir):
		raise NotADirectoryError("文件目录 {0} 不存在".format(source_file_dir))
	tables = ExcelHelper.convert_2_class(excel_file_name, RenameData, True)
	source_has_repeat(tables)
	dest_has_repeat(tables)
	copy_and_rename(source_file_dir, dest_file_dir, tables)
	print("文件重命名已成功!")
