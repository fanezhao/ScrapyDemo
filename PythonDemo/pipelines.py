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
from PythonDemo.items import PythondemoItem
from PythonDemo.items import TestItem
from PythonDemo.items import BusinessInformationItem


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
        if isinstance(item, PythondemoItem):
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
        elif isinstance(item, TestItem):
            print("this is TestItem")
        elif isinstance(item, BusinessInformationItem):
            data = dict(item)
            db = pymysql.Connect(mysql_host, mysql_username, mysql_password, mysql_db_name)
            cursor = db.cursor()
            sql = "insert into wdzj_company_business_information " \
                  "(corporate_title, corporate_name, unified_social_credit_code, legal_representative, " \
                  "registered_capital, type_of_company, paid_capital, registered_address, opening_date, " \
                  "registration_status, operating_period, registration_authority, approval_date, domain_name, " \
                  "filing_time, name_of_record_unit, nature_of_record_unit, icp_record_number, icp_business_license, " \
                  "platform_used_name, scope_of_operation)" \
                  "values " \
                  "('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', " \
                  "'%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" \
                  % (data['corporate_title'], data['corporate_name'], data['unified_social_credit_code'],
                     data['legal_representative'], data['registered_capital'], data['type_of_company'],
                     data['paid_capital'], data['registered_address'], data['opening_date'],
                     data['registration_status'], data['operating_period'], data['registration_authority'],
                     data['approval_date'], data['domain_name'], data['filing_time'], data['name_of_record_unit'],
                     data['nature_of_record_unit'], data['icp_record_number'], data['icp_business_license'],
                     data['platform_used_name'], data['scope_of_operation']
                     )
            try:
                cursor.execute(sql)
                db.commit()
            except ConnectionError:
                db.rollback()
            db.close()
            return item
        else:
            pass