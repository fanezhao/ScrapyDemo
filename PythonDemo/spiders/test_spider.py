# -*- coding: utf-8 -*-
import scrapy
from PythonDemo.items import TestItem

class TestSpiderSpider(scrapy.Spider):
    name = 'test_spider'
    # 允许域名
    allowed_domains = ['movie.douban.com']
    # 入口URL
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        test_item = TestItem()
        test_item['name'] = 'fanezhao'
        test_item['age'] = 18
        yield test_item
