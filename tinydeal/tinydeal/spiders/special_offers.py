import scrapy


class SpecialOffersSpider(scrapy.Spider):
    name = 'special_offers'
    allowed_domains = ['www.cigabuy.com']
    start_urls = ['https://www.cigabuy.com/consumer-electronics-c-56_75-pg-1.html']

    # def parse(self, response):
    #     for product in response.xpath("//div[@class='r_b_c']"):
    #         yield {
    #             'title' : product.xpath(".//div[@class='p_box_wrapper']/div/a[2]/text()").get(),
    #             'url' : product.xpath(".//div[@class='p_box_wrapper']/div/a[2]/@href").get(),
    #             'discounted_price' : product.xpath(".//div[@class='p_box_price cf']/span[1]/text()").get(),
    #             'original_price' : product.xpath(".//div[@class='p_box_price cf']/span[2]/text()").get()
    #         }

    def parse(self, response):
        for product in response.xpath("//div[@class='p_box_wrapper']"):
            yield {
                'title': product.xpath(".//a[@class='p_box_title']/text()").get(),
                'url': response.urljoin(product.xpath(".//a[@class='p_box_title']/@href").get()),
                'discoutned_price': product.xpath(".//div[@class='p_box_price']/span[1]/text()").get(),
                'original_price': product.xpath(".//div[@class='p_box_price']/span[2]/text()").get(),
            }
