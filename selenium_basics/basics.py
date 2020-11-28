from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from shutil import which

chrome_path = which("chromedriver")

'''
chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(executable_path = chrome_path, options=chrome_options)
driver.get("https://www.duckduckgo.com")

search_input =  driver.find_element_by_id("search_form_input_homepage")
# search_input =  driver.find_element_by_xpath("(//input[contains(@class,'js-search-input')])[1]")
search_input.send_keys("My User Agent")

# search_btn = driver.find_element_by_id("search_button_homepage")
# search_btn.click()

search_input.send_keys(Keys.ENTER)

print(driver.page_source)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''
driver = webdriver.Chrome(executable_path = chrome_path)
driver.get("https://curiositystream.com/categories")
categories =  driver.find_elements_by_xpath("(//span[contains(@class,'styles__title___1Vsjl')])[1]")

# for cat in categories:

print(categories)




# driver.close()