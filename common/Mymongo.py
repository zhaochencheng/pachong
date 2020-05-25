#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: zhaochencheng
@contact: 907779487@qq.com
@file: Mymongo.py
@time: 2020/5/24 13:56
@IDE:PyCharm
'''
import pymongo

class MyMongo():
    def __init__(self, host, port, database):
        self.host = host
        self.port = int(port)
        self.database = database
        self.mongo = pymongo.MongoClient(host=self.host, port=self.port)
        self.db = self.mongo[self.database]
    def col(self,col):
        return self.db[col]

    def Insert_one(self, col, data):
        '''
        插入一条数据
        :param col:
        :param data: 字典{}
        :return: id
        '''
        self.col = self.db[col]
        return self.col.insert_one(document=data).inserted_id
    def Insert_many(self, col, data):
        '''
        插入多条数据
        :param col:
        :param data: 字典列表[{}, {}, {}]
        :return: list[id1,id2,id3]
        '''
        self.col = self.db[col]
        return self.col.insert_many(documents=data).inserted_ids
    def Delete_one(self, col, data):
        '''
        删除符合条件的一条数据
        :param col:
        :param data:
        :return: deleted_count
        '''
        self.col = self.db[col]
        return self.col.delete_one(filter=data).deleted_count
    def Delete_many(self, col, data):
        '''
        删除多条符合条件的数据
        :param col:
        :param data:
        :return: deleted_count
        '''
        self.col = self.db[col]
        return self.col.delete_many(filter=data).deleted_count
    def Find_one(self, col, data):
        '''
         查找符合条件的一条数据
        :param col:
        :param data:
        :return: dict
        '''
        self.col = self.db[col]
        return self.col.find_one(filter=data)
    def Find(self, col, data):
        '''
        查找符合条件的所有数据
         result.sort()排序---sort('alexa') 升序 sort('alexa' -1) 降序
         result.limit(3) 输出3条
        :param col:
        :param data:
        :return: <pymongo.cursor.Cursor object at 0x03A595B0> [i for i in result]
        '''
        self.col = self.db[col]
        return self.col.find(filter=data)
    # def Update_one(self, col, data):
    #     self.col = self.db[col]
    #     return self.col.update_one(data)
#
# if __name__ == '__main__':
#     host = "172.31.114.5"
#     port = 27017
#     database = "test"
#     col = "test"
# # #     one = {"name": "jon", "age": 123}
# # #     findone = {"age": 123}
# # #     many = [{'x': i, "age": 12} for i in range(3)]
# # #     many_delete = {}
# # #     update = {"age": 123},{'$set':{"age":"123456"}}
# #     import time
# #     start = time.time()
#     code_file = r"E:\python_speace\pachun\tonghuashun\tonghuashun\股票信息2.txt"
#     with open(code_file, "r") as f:
#         code_list = f.readlines()
#     import time
#     start = time.time()
#     # url_forecast = "http://basic.10jqka.com.cn/605001/worth.html"
#     url_forecast = "http://basic.10jqka.com.cn/605001/worth.html"
#     header ={
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36"
#     }
#     import requests
#     mymongo = MyMongo(host=host, port=port, database=database)
#     for code in code_list:
#         url_forecast = "http://basic.10jqka.com.cn/605001/worth.html"
#         r = requests.get(url_forecast, headers=header)
#     print(str(r.content, encoding="GBK"), type(str(r.content, encoding="GBK")))
# #     list = []
# #     for i in range(4000):
# #         print(i)
#     one = {'code': "605001\n", 'text': str(r.content, encoding="GBK")}
# #         list.append(one)
#     insert_one = mymongo.Insert_one(col=col, data=one)
#     print(insert_one)
#     end = time.time()
#     print('Queue多线程爬虫总时间为：',end-start)
#
#     mymongo = MyMongo(host=host, port=port, database=database)
#     insert_one = mymongo.Insert_one(col=col, data=one)
#     print(insert_one)
    # insert_many = mymongo.Insert_many(col=col, data=many)
    # print()
    # delete_one = mymongo.Delete_one(col=col, data=one)
    # print(delete_one)
    # delet_many = mymongo.Delete_many(col=col, data=many_delete)
    # print(delet_many)
    # find_one = mymongo.Find_one(col, data=findone)
    # print(find_one, type(find_one))
    # find = mymongo.Find(col,data=findone)
    # print(find)
    # update_one = mymongo.Update_one(col, data=update)
    # print(update_one)

