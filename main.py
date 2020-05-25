#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: zhaochencheng
@contact: 907779487@qq.com
@file: main.py
@time: 2020/5/24 13:57
@IDE:PyCharm
'''
import os
import time


if __name__ == '__main__':

    down_excel = "test3.xls"
    save_excel = "股票信息抓取1.xlsx"
    code_file = "股票信息.txt"
    if os.path.exists(save_excel):
        os.remove(save_excel)
    if os.path.exists(down_excel):
        os.remove(down_excel)
    if os.path.exists(code_file):
        with open(code_file, "r") as f:
            code_list = f.readlines()
        num = 0
        for code in code_list:
            print(num)
            # try:
            print("开始获取股票：", code)
            main(code=code.strip(), down_excel=down_excel, save_excel=save_excel)
            time.sleep(1)
            print("---获取完成---")
            num += 1
            # except Exception as E:
            #     print(E)
            # print(code.strip())
    else:
        print("股票信息.txt-不存在")

    if os.path.exists(down_excel):
        os.remove(down_excel)