# -*- coding: utf-8 -*-
import scrapy
from PythonDemo.items import BusinessInformationItem


class IndustryAndCommerceRecordSpiderSpider(scrapy.Spider):
    name = 'business_information_spider'
    allowed_domains = ['www.wdzj.com']
    start_urls = ['https://www.wdzj.com/dangan/hxd5/gongshang/']

    def parse(self, response):
        msg = response.xpath("//div[@class='lcen']")
        item = BusinessInformationItem()
        item['corporate_title'] = msg.xpath("//div[@class='title']//h1/text()").extract_first()

        item['corporate_name'] = msg.xpath(".//tr[1]/td[2]/text()").extract_first()
        item['unified_social_credit_code'] = msg.xpath(".//tr[1]/td[4]/text()").extract_first()

        item['legal_representative'] = msg.xpath(".//tr[2]/td[2]/text()").extract_first()
        item['registered_capital'] = msg.xpath(".//tr[2]/td[4]/text()").extract_first()

        item['type_of_company'] = msg.xpath(".//tr[3]/td[2]/text()").extract_first() + \
                                  msg.xpath(".//tr[3]/td[2]/font/text()").extract_first() + "）"
        item['paid_capital'] = msg.xpath(".//tr[3]/td[4]/text()").extract_first()

        item['registered_address'] = msg.xpath(".//tr[4]/td[2]/text()").extract_first()
        item['opening_date'] = msg.xpath(".//tr[4]/td[4]/text()").extract_first()

        item['registration_status'] = msg.xpath(".//tr[5]/td[2]/text()").extract_first()
        item['operating_period'] = msg.xpath(".//tr[5]/td[4]/text()").extract_first()

        item['registration_authority'] = msg.xpath(".//tr[6]/td[2]/text()").extract_first()
        item['approval_date'] = msg.xpath(".//tr[6]/td[4]/text()").extract_first()

        item['domain_name'] = msg.xpath(".//tr[7]/td[2]/text()").extract_first().strip()
        item['filing_time'] = msg.xpath(".//tr[7]/td[4]/text()").extract_first()

        item['name_of_record_unit'] = msg.xpath(".//tr[8]/td[2]/text()").extract_first()
        item['nature_of_record_unit'] = msg.xpath(".//tr[8]/td[4]/text()").extract_first().strip()

        item['icp_record_number'] = msg.xpath(".//tr[9]/td[2]/text()").extract_first()
        item['icp_business_license'] = msg.xpath(".//tr[9]/td[4]/text()").extract_first()

        item['platform_used_name'] = msg.xpath(".//tr[10]/td[2]/text()").extract_first()
        item['scope_of_operation'] = msg.xpath(".//tr[11]/td[2]/p/text()").extract_first()

        yield item
