#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2021/6/29 3:36 下午
# @Author  : 玄凌
# @File    : attr_display.py
# @Description : 功能描述
# @Software: PyCharm
"""


class AttrDisplay(object):

    def _gather_attrs(self):
        return ",".join("{}={}"
                        .format(k, getattr(self, k))
                        for k in self.__dict__.keys())

    def __str__(self):
        return "[{}:{}]".format(self.__class__.__name__, self._gather_attrs())


if __name__ == '__main__':
    pass
