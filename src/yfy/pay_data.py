#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Time    : 2021/6/29 10:27 上午
# @Author  : 玄凌
# @File    : pay_data.py
# @Description : 功能描述
# @Software: PyCharm
"""
import smtplib

from common.attr_display import AttrDisplay
from common.utils import print_iterable
from excel_tools.excel_helper import ExcelHelper
from mail_tools.email_data import EmailData
from mail_tools.email_helper import get_smtp, send_mail, smtp_quit
from mail_tools.email_sender import EmailSenderData


class PayData(AttrDisplay):
    b = None  # 员工姓名
    c = None  # 邮箱
    d = None  # 基本工资
    e = None  # 孝工资
    f = None  # 绩效奖金
    g = None  # 提成
    h = None  # 补贴（生日金等）
    i = None  # 考勤扣款
    j = None  # 其他
    k = None  # 应发工资合计
    l = None  # 扣养老保险
    m = None  # 扣医保费
    n = None  # 扣失业险
    o = None  # 扣住房公积金
    p = None  # 社保扣款合计
    q = None  # 子女教育
    r = None  # 赡养老人
    s = None  # 住房贷款利息
    t = None  # 住房租金
    u = None  # 继续教育
    v = None  # 大病医疗
    w = None  # 本次应扣税额
    x = None  # 净工资
    y = None  # 其他税后调整
    z = None  # 实发工资


def build_html(payData: PayData) -> str:
    html = ""
    html += "<table border=\"1\">"
    html += "<tr>"
    html += "<th>员工姓名</th>"
    html += "<th>邮箱</th>"
    html += "<th>基本工资</th>"
    html += "<th>孝工资</th>"
    html += "<th>绩效奖金</th>"
    html += "<th>提成</th>"
    html += "<th>补贴（生日金等）</th>"
    html += "<th>考勤扣款</th>"
    html += "<th>其他</th>"
    html += "<th>应发工资合计</th>"
    html += "<th>扣养老保险</th>"
    html += "<th>扣医保费</th>"
    html += "<th>扣失业险</th>"
    html += "<th>扣住房公积金</th>"
    html += "<th>社保扣款合计</th>"
    html += "<th>子女教育</th>"
    html += "<th>赡养老人</th>"
    html += "<th>住房贷款利息</th>"
    html += "<th>住房租金</th>"
    html += "<th>继续教育</th>"
    html += "<th>大病医疗</th>"
    html += "<th>本次应扣税额</th>"
    html += "<th>净工资</th>"
    html += "<th>其他税后调整</th>"
    html += "<th>实发工资</th>"
    html += "</tr>"
    html += "<tr>"
    html += "<td>" + payData.b + "</td>"
    html += "<td>" + payData.c + "</td>"
    html += "<td>" + payData.d + "</td>"
    html += "<td>" + payData.e + "</td>"
    html += "<td>" + payData.f + "</td>"
    html += "<td>" + payData.g + "</td>"
    html += "<td>" + payData.h + "</td>"
    html += "<td>" + payData.i + "</td>"
    html += "<td>" + payData.j + "</td>"
    html += "<td>" + payData.k + "</td>"
    html += "<td>" + payData.l + "</td>"
    html += "<td>" + payData.m + "</td>"
    html += "<td>" + payData.n + "</td>"
    html += "<td>" + payData.o + "</td>"
    html += "<td>" + payData.p + "</td>"
    html += "<td>" + payData.q + "</td>"
    html += "<td>" + payData.r + "</td>"
    html += "<td>" + payData.s + "</td>"
    html += "<td>" + payData.t + "</td>"
    html += "<td>" + payData.u + "</td>"
    html += "<td>" + payData.v + "</td>"
    html += "<td>" + payData.w + "</td>"
    html += "<td>" + payData.x + "</td>"
    html += "<td>" + payData.y + "</td>"
    html += "<td>" + payData.z + "</td>"
    html += "</tr>"
    html += "</table>"
    return html


def build_email_send_data() -> EmailSenderData:
    return EmailSenderData('895664407@qq.com', '895664407@qq.com', 'Zh20150609')


def build_email_data(payData: PayData) -> EmailData:
    return EmailData(payData.c, '工资条', build_html(payData))


if __name__ == '__main__':
    email_send_data = build_email_send_data()
    smtp = get_smtp(email_send_data)
    tables = ExcelHelper.convert_2_class("/Users/pro/Desktop/excel/pay.xlsx", PayData)
    for table in tables:
        for data in table:
            email_data = build_email_data(data)
            send_mail(email_send_data, email_data, smtp)
    smtp_quit(smtp)
    # print_iterable(tables)
