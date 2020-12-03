import scrapy


class QuotesLoginSpider(scrapy.Spider):
    name = 'quotes-login'
    allowed_domains = ['quotes.toscrape.com/login']
    start_urls = ['http://quotes.toscrape.com/login/']

    def parse(self, response):
        pass
