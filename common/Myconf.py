#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: zhaochencheng
@contact: 907779487@qq.com
@file: Myconf.py
@time: 2020/5/24 14:09
@IDE:PyCharm
'''
import configparser
import os
import sys

# config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"config\conf.ini")
class Myconfig():
    def __init__(self, config_path):
        if config_path:
            # 如果路径存在 则使用配置路径
            self.Config_path = config_path
        else:
            # 不存在，这在上一层文件中找 config.ini

            config_path_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            self.Config_path = os.path.join(config_path_dir, "config.ini")
        self.cf = configparser.ConfigParser()
        self.cf.read(self.Config_path)

    def get_sections(self):
        '''
        # 获取配置文件中所有 section []
        :return: list
        '''
        return self.cf.sections()
    def get_options(self, section):
        '''
        # 获取该section下的所对应的键
        :param section:
        :return: list
        '''
        return self.cf.options(section=section)
    def get_items(self,section):
        '''
        # 获取该section下的所有键值对
        :param section:
        :return: list
        '''
        return self.cf.items(section=section)
    def get_value(self, section, option):
        '''
         获取section下制定option的值
        :param section:
        :param option:
        :return: str
        '''
        return self.cf.get(section=section, option=option)
    def check_section_ishas(self, section):
        '''
        判断 section 是否已存在
        :param section:
        :return: bool
        '''
        return self.cf.has_section(section=section)
    def check_option_ishas(self, section, option):
        '''
        判断 section下 option 是否已存在
        :param section:
        :param option:
        :return: bool
        '''
        return self.cf.has_option(section=section, option=option)
    def add_section(self, section):
        '''
        向配置中写入 section
        :param section:
        :return:
        '''
        if not self.check_section_ishas(section=section):
            self.cf.add_section(section=section)
            self.cf.write(open(self.Config_path, "w"))
            return True
        return False
    def update_option_value(self, section, option, value=""):
        '''
        修改或添加做制定节点下的option 或 option的值
        :param section:
        :param option:
        :return:
        '''
        if not self.check_section_ishas(section=section):
            self.add_section(section=section)
        self.cf.set(section=section, option=option, value=value)
        self.cf.write(open(self.Config_path, "w"))
    # def del_section(self, section):
    #     return self.cf.remove_section(section=section)




# if __name__ == '__main__':
#     # 初始化 配置文件路径
#     config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"config\conf.ini")
#     myconfig = Myconfig(config_path=config_path)
#     sections = myconfig.get_sections()
#     print(sections)
#     options = myconfig.get_options("mongo")
#     print(options)
#     items = myconfig.get_items("mongo")
#     print(items,type(items[0]))
#     value = myconfig.get_value("mongo","url")
#     print(value)
#     check = myconfig.check_section_ishas("mmm")
#     print(check)
#     check_option = myconfig.check_option_ishas("mongo", "url2")
#     print(check_option)
#     add_section = myconfig.add_section("mongo7")
#     print(add_section)
#     update = myconfig.update_option_value("mongo7", "url", "2123")
#     print(update)
#     # del_section = myconfig.del_section("mongo7")
#     # print(del_section)
