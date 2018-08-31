# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PythondemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 序号
    serial_number = scrapy.Field()
    # 电影名称
    movie_name = scrapy.Field()
    # 介绍
    introduce = scrapy.Field()
    # 星级
    star = scrapy.Field()
    # 电影的评论数
    evaluate = scrapy.Field()
    # 电影描述
    describe = scrapy.Field()


class TestItem(scrapy.Item):
    name = scrapy.Field()
    age = scrapy.Field()


# 工商备案
class BusinessInformationItem(scrapy.Item):
    # 平台名称
    platform_name = scrapy.Field()
    # 公司名称
    corporate_name = scrapy.Field()
    # 统一社会信用代码
    unified_social_credit_code = scrapy.Field()
    # 法人代表
    legal_representative = scrapy.Field()
    # 注册资本
    registered_capital = scrapy.Field()
    # 公司类型
    type_of_company = scrapy.Field()
    # 实缴资本
    paid_capital = scrapy.Field()
    # 注册地址
    registered_address = scrapy.Field()
    # 开业日期
    opening_date = scrapy.Field()
    # 登记状态
    registration_status = scrapy.Field()
    # 营业期限
    operating_period = scrapy.Field()
    # 登记机关
    registration_authority = scrapy.Field()
    # 核准日期
    approval_date = scrapy.Field()
    # 备案域名
    domain_name = scrapy.Field()
    # 备案时间
    filing_time = scrapy.Field()
    # 备案单位名称
    name_of_record_unit = scrapy.Field()
    # 备案单位性质
    nature_of_record_unit = scrapy.Field()
    # ICP备案号
    icp_record_number = scrapy.Field()
    # ICP经营许可证
    icp_business_license = scrapy.Field()
    # 平台曾用名
    platform_used_name = scrapy.Field()
    # 经营范围
    scope_of_operation = scrapy.Field()


# 概览
class OverViewItem(scrapy.Item):
    # 平台名称
    platform_name = scrapy.Field()
    # 注册资金
    register_money = scrapy.Field()
    # 股权上市
    public_equity = scrapy.Field()
    # 银行存管
    bank_depository = scrapy.Field()
    # 融资记录
    financing = scrapy.Field()
    # 监管协会
    association = scrapy.Field()
    # ICP号
    icp = scrapy.Field()