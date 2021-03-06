import scrapy
import logging


class CountiesSpider(scrapy.Spider):
    name = 'counties'
    allowed_domains = ['www.worldometers.info']
    # start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    country_name = ''

    def parse(self, response):
        # countries = response.xpath("//td/a")
        # for country in countries:
        #     name = country.xpath(".//text()").get()
        #     link = country.xpath(".//@href").get()
        #     self.country_name = name
            # absolute_url = f"https://www.worldometers.info{link}"
            # absolute_url = response.urljoin(link)

            # yield scrapy.Request(url=absolute_url)
            # Relative url
            # yield response.follow(link, callback=self.parse_countries, meta={'country_name':name})
        yield response.follow(url='https://www.worldometers.info/world-population/population-by-country/', callback=self.parse_countries, meta={'country_name':'china'})

    def parse_countries(self, response):
        name = response.request.meta['country_name']
        rows = response.xpath("(//table[@class='table table-striped table-bordered table-hover table-condensed table-list'])[1]/tbody/tr")
        for row in rows:
            year = row.xpath(".//td[1]/text()").get()
            population = row.xpath(".//td[2]/strong/text()").get()

            yield {
                'country_name' : name,
                'year': year,
                'population': population
            }
