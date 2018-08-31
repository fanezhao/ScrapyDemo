from scrapy import cmdline
cmdline.execute(['scrapy', 'crawl', 'overview_spider'])

# # 多爬虫同时执行脚本
# import os
# # 必须先加载项目settings配置
# # project需要改为你的工程名字（即settings.py所在的目录名字）
# os.environ.setdefault('SCRAPY_SETTINGS_MODULE', 'PythonDemo.settings')
# from scrapy.crawler import CrawlerProcess
# from scrapy.utils.project import get_project_settings
# process = CrawlerProcess(get_project_settings())
# # 执行所有 spider
# for spider_name in process.spider_loader.list():
#     # print spider_name
#     process.crawl(spider_name)
# process.start()