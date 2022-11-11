import yaml
import pprint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver import ChromeOptions, Chrome

with open('config.yaml') as f:
    
    
    data = yaml.load(f, Loader=yaml.FullLoader)
    
    #split data param
    headless = data['headless']
    screenshoot_dir = data['screenshot_dir']
    tasks = data['tasks']
    
    pprint.pprint(tasks[0]['user'])
    pprint.pprint(tasks[0]['pwd'])
    

    opts = webdriver.ChromeOptions()
    opts.add_argument('--ignore-certificate-errors')
    opts.add_argument("--test-type")
    opts.add_experimental_option("detach", True)
        
    driver = Chrome(chrome_options=opts)
    driver.maximize_window()
    driver.get(tasks[0]['url'])

# sleep(.5)
    
username = driver.find_element("name", "username")
username.send_keys(tasks[0]['user'])

# sleep(.5)
# username.submit()

password = driver.find_element("name","password")
password.send_keys(tasks[0]['pwd'])
# sleep(.5)

# password.submit()
# btn = driver.find_element_by_css_selector('.button.pf-c-button pf-m-primary pf-m-block')
# btn.submit()
# driver.find_element_by_xpath("//button[id ='value']").click()

driver.save_screenshot("percobaan1.png");    

# username.send_keys(tasks[0]['user'])
# search_box.submit()


    