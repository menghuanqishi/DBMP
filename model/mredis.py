# ！/usr/bin/env python
# -*- coding:utf-8 -*-
"""
 author : 梦幻骑士
 email  : wp_226@163.com
 @Project : DBMP
 @File  : m_redis.PY
 @Time  : 2023/3/16 10:15
 @Desc  :
"""
import redis


class Mredis:
    def __init__(self, redis_info):
        self.rdb = redis.Redis(
            host=redis_info['host'],
            port=redis_info['port'],
            db=int(redis_info['db_num']),
            username=None,
            password=None)

    # 按key查询，结果返回Bytes
    def find_key(self,key):
        return self.rdb.get(key)

    # 获取匹配的key,返回列表
    def find_keys(self,pattern='*'):
        return self.rdb.keys(pattern)

    # 设置key值 失败返回False，成功返回True
    def set_value(self,key,value):
        return self.rdb.set(key,value)

    #  删除指定的key
    def delete_key(self,key):
        self.rdb.delete(key)

    # 删除匹配的key,默认为全部
    def delete_keys(self,pattern='*'):
        keys = self.find_keys(pattern)
        for key in keys:
            self.delete_key(key)

    def close_db(self):
        self.rdb.close()

