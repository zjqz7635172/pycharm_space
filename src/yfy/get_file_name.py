#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2021/7/8 1:03 下午
# @Author  : 玄凌
# @File    : get_file_name.py
# @Description : 提取文件名并保持excel
# @Software: PyCharm
"""
import os
from os.path import isdir

from common.attr_display import AttrDisplay
from excel_tools.excel_helper import ExcelHelper


class FileName(AttrDisplay):
    fileName: str = None


def get_src_file_name(_source_file_dir: str) -> list:
    _file_name_list = []
    if not isdir(_source_file_dir):
        raise NotADirectoryError("文件目录 {0} 不存在".format(_source_file_dir))
    source_path = os.path.abspath(_source_file_dir)
    for root, dirs, files in os.walk(source_path):
        for file in files:
            _file_name = file.split('.')[0]
            if _file_name.__len__() == 0:
                continue
            _file_name_list.append(_file_name)
    return _file_name_list


if __name__ == '__main__':
    # 使用时只需要修改这里
    # 源文件路径
    source_file_dir = "/Users/pro/Desktop/rename/2"
    # 需要保存的excel路径
    save_excel_file = "/Users/pro/Desktop/rename/2.xlsx"
    # 使用时只需要修改这里
    file_name_list = get_src_file_name(source_file_dir)
    if file_name_list.__len__() == 0:
        print("文件夹：{0},没有文件".format(source_file_dir))
    else:
        table = []
        for file_name in file_name_list:
            fileName = FileName()
            fileName.__setattr__("fileName", file_name)
            table.append(fileName)
        tables = [table]
        ExcelHelper.save(save_excel_file, tables, FileName)
        print("导出文件名已保存至excel,路径={0}".format(save_excel_file))
