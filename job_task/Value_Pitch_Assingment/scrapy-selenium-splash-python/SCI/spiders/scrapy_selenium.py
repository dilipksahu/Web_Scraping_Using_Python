import scrapy
from scrapy_selenium import SeleniumRequest
from scrapy.selector import Selector
import time


class CaseInfoSpider(scrapy.Spider):
    name = 'case_info'
    
    diary_number = 1
    year = 2001

    def start_requests(self):
        yield SeleniumRequest(
            url='http://main.sci.gov.in/case-status',
            wait_time=60,
            screenshot=True,
            callback=self.parse
        )

    def parse(self, response):

        driver = response.meta['driver']

        captcha_text = driver.find_element_by_xpath("(//font)[4]").text
        print("Captcha===========>",captcha_text)
        captcha_input = driver.find_element_by_id("ansCaptcha")
        captcha_input.send_keys(captcha_text)

        diary_input = driver.find_element_by_xpath("//input[@id='CaseDiaryNumber']") 
        diary_input.send_keys("1")

        year_input = driver.find_element_by_xpath("//select[@id='CaseDiaryYear']")
        year_input.send_keys(f"2020")

        submit_btn = driver.find_element_by_xpath("//input[@id='getCaseDiary']")
        submit_btn.click()

        
        # img = response.meta['screenshot']

        # with open('screenshot.png', 'wb') as f:
        #     f.write(img)

        # print(driver.page_source)
        html = driver.page_source
        response_obj = Selector(text=html)

        case_details = response_obj.xpath("(//table)[3]/tbody/tr/td[2]")
        for case_detail in case_details:
            yield {
                    'Diary No.': case_detail.xpath(".//div/font/text()").get(),
                    'Case No.': case_detail.xpath(".//div/text()").get(),
                    'Present/Last Listed On': case_detail.xpath(".//b/font/text()").get(),
                    'Status/Stage': case_detail.xpath(".//font/text()").get(),
                    'Category': case_detail.xpath(".//text()").get(),
                    'Act': case_detail.xpath(".//text()").get(),
                    'Petitioner(s)': case_detail.xpath(".//p/text()").get(),
                    'Respondent(s)': case_detail.xpath(".//p/text()").get(),
                    'Pet. Advocate(s)': case_detail.xpath(".//p/text()").get(),
                    
                }   

        driver.close()
