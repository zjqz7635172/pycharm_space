#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2021/7/8 12:20 下午
# @Author  : 玄凌
# @File    : file_copy.py
# @Description : 功能描述
# @Software: PyCharm
"""
import os
import shutil


def copy_1(_source_file_dir: str, _dest_file_dir: str):
	source_path = os.path.abspath(_source_file_dir)
	target_path = os.path.abspath(_dest_file_dir)
	if not os.path.exists(target_path):
		# 如果目标路径不存在原文件夹的话就创建
		os.makedirs(target_path)
	if os.path.exists(source_path):
		# 如果目标路径存在原文件夹的话就先删除
		shutil.rmtree(target_path)
	shutil.copytree(source_path, target_path)
	print('copy dir finished!')


def copy_2(_source_file_dir: str, _dest_file_dir: str):
	source_path = os.path.abspath(_source_file_dir)
	target_path = os.path.abspath(_dest_file_dir)
	if not os.path.exists(target_path):
		os.makedirs(target_path)
	if os.path.exists(source_path):
		# root 所指的是当前正在遍历的这个文件夹的本身的地址
		# dirs 是一个 list，内容是该文件夹中所有的目录的名字(不包括子目录)
		# files 同样是 list, 内容是该文件夹中所有的文件(不包括子目录)
		for root, dirs, files in os.walk(source_path):
			for file in files:
				src_file = os.path.join(root, file)
				shutil.copy(src_file, target_path)
				print(src_file)
	print('copy files finished!')


if __name__ == '__main__':
	pass
