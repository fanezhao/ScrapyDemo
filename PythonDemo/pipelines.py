# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
import pymysql
import json
from PythonDemo.settings import mongo_host, mongo_port, mongo_db_name, mongo_db_collection
from PythonDemo.settings import mysql_host, mysql_port, mysql_username, mysql_password, mysql_db_name


class PythondemoPipeline(object):

    # def __init__(self):
    # host = mongo_host
    # port = mongo_port
    # dbname = mongo_db_name
    # sheetname = mongo_db_collection
    # client = pymongo.MongoClient(host=host, port=port)
    # mymongo = client[dbname]
    # self.post = mymongo[sheetname]

    def process_item(self, item, spider):
        data = dict(item)
        # self.post.insert(data)
        db = pymysql.Connect(mysql_host, mysql_username, mysql_password, mysql_db_name)
        cursor = db.cursor()
        sql = "insert into movies (serial_number, movie_name, introduce, evaluate, star, movie_describe) " \
              "values ('%s', '%s', '%s', '%s', '%s', '%s')" \
              % (data['serial_number'], data['movie_name'], data['introduce'], data['evaluate'], data['star'],
                 data['describe'])
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
        db.close()
        return item