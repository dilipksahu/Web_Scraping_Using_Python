# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from shutil import which


class CoinSpiderSelenium(scrapy.Spider):
    name = 'case_status'
    allowed_domains = ['www.main.sci.gov.in']
    start_urls = [
        'http://main.sci.gov.in/case-status'
    ]

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')

        chrome_path = which("chromedriver")

        driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)
        driver.set_window_size(1920, 1080)
        driver.implicitly_wait(0.5)
        driver.get("https://main.sci.gov.in/case-status")

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

        self.html = driver.page_source
        driver.close()

    
    def parse(self, response):
        resp = Selector(text=self.html)
        print(resp)

        case_details = resp.xpath("(//table)[3]/tbody/tr")
        for case_detail in case_details:

            print(case_detail)
            yield {
                    'Diary No.': case_detail.xpath(".//td[2]/div/font/text()").get(),
                    'Case No.': case_detail.xpath(".//td[2]/div/text()").get(),
                    'Present/Last Listed On': case_detail.xpath(".//td[2]/b/font/text()").get(),
                    'Status/Stage': case_detail.xpath(".//td[2]/font/text()").get(),
                    'Category': case_detail.xpath(".//td[2]/text()").get(),
                    'Act': case_detail.xpath(".//td[2]/text()").get(),
                    'Petitioner(s)': case_detail.xpath(".//td[2]/p/text()").get(),
                    'Respondent(s)': case_detail.xpath(".//td[2]/p/text()").get(),
                    'Pet. Advocate(s)': case_detail.xpath(".//td[2]/p/text()").get(),
                    
                }