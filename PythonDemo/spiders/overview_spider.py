# -*- coding: utf-8 -*-
import scrapy
from PythonDemo.items import OverViewItem


class OverviewSpider(scrapy.Spider):
    name = 'overview_spider'
    allowed_domains = ['www.wdzj.com']
    start_urls = ['https://www.wdzj.com/dangan/hxd5/']

    def parse(self, response):
        msg = response.xpath("//div[@class='bgbox-bt zzfwbox']//dl[1]")
        ov_item = OverViewItem()
        ov_item['platform_name'] = msg.xpath("//div[@class='title']//h1/text()").extract_first()
        ov_item['register_money'] = msg.xpath(".//dd[1]/div[2]/text()").extract_first().replace('\n', '').replace(' ', '')
        ov_item['public_equity'] = msg.xpath(".//dd[2]/div[2]/text()").extract_first().strip().replace(' ', '')
        ov_item['bank_depository'] = msg.xpath(".//dd[3]/div[2]/text()").extract_first().strip().replace(' ', '')
        financing_one = msg.xpath(".//dd[4]/div[2]/p[1]/text()").extract()
        for one in financing_one:
            part_of_one = ''.join(one.split())
        financing_two = msg.xpath(".//dd[4]/div[2]/p[2]/text()").extract()
        for two in financing_two:
            part_of_two = ''.join(two.split())
        ov_item['financing'] = part_of_one + '|' + part_of_two
        association = msg.xpath(".//dd[5]/div[2]/p/text()").extract()
        for ass in association:
            ov_item['association'] = ''.join(ass.split())
        ov_item['icp'] = msg.xpath(".//dd[6]/div[2]/text()").extract_first().strip()
        yield ov_item