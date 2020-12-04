import scrapy
from scrapy_splash import SplashRequest, SplashFormRequest
 
 
class QuotesLoginSpider(scrapy.Spider):
    name = 'sci'
    allowed_domains = ['main.sci.gov.in']
    
    script = '''
        function main(splash, args)
          assert(splash:go(args.url))
          assert(splash:wait(0.5))
          return splash:html()
        end
    '''
    
    def start_requests(self):
        yield SplashRequest(
            url='https://main.sci.gov.in/php/case_status/case_status_process.php',
            endpoint='execute',
            args = {
                'lua_source': self.script
            },
            callback=self.parse
        )
 
    def parse(self, response):
        captcha_text = response.xpath('(//font)[4]/text()').get()
        yield SplashFormRequest.from_response(
            response,
            formid="ansCaptcha",
            formdata={
                'd_no': '1',
                'd_yr': '2020',
                'ansCaptcha': captcha_text
            },
            callback=self.after_login
        )
    
    def after_login(self, response):
        if response.xpath("//table)[3]/tbody/tr[1]/td[2]/div/text()").get():
            print('Success')
