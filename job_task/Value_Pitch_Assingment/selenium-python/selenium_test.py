from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from shutil import which


# chrome_options = Options()
# chrome_options.add_argument('--headless')

chrome_path = which("chromedriver")

# driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)
driver = webdriver.Chrome(executable_path=chrome_path)

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

driver.implicitly_wait(0.5)

elem = driver.find_element_by_xpath("//*")
source_code = elem.get_attribute("innerHTML")
with open('html_source_code_inner.html', 'w') as f:
    f.write(str(source_code.encode('utf-8')))


print("--------------Success---------------")

# driver.close()