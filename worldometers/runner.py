import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from worldometers.spiders.counties import CountiesSpider

process = CrawlerProcess(settings=get_project_settings())
process.crawl(CountiesSpider)
process.start()