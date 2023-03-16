# ！/usr/bin/env python
# -*- coding:utf-8 -*-
"""
 author : 梦幻骑士
 email  : wp_226@163.com
 @Project : DBMP
 @File  : tredis.PY
 @Time  : 2023/3/16 10:45
 @Desc  :
"""

from model.mredis import Mredis
from libs.profile import INI
from config.setting import CONFIG_FILE
import time


if __name__ == '__main__':
    cnf = INI(CONFIG_FILE)
    # redis_info = cnf.get_options('REDIS',['host','port','db_num','user','password'])
    redis_info = cnf.get_options('REDIS',['host','port','db_num'])
    print(redis_info)
    rdb = Mredis(redis_info)
    # rdb.delete_keys('*')
    index = 1
    while True:
        rdb.set_value(index,time.strftime("%Y-%m-%d %h:%M:%S", time.localtime()))
        index = index + 1
        time.sleep(1)