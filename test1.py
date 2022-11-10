from selenium import webdriver  
import time  
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver import ChromeOptions, Chrome
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = Chrome(chrome_options=opts)
driver.maximize_window()
driver.get("http://www.google.com")
search_box = driver.find_element("name", "q")
search_box.send_keys('kentang bulat')
search_box.submit()
print("sample test case successfully completed")  