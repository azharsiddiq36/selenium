import yaml
import pprint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver import ChromeOptions, Chrome
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import sys, os
import time

import pyautogui

with open('config.yaml') as f:
    
    
    data = yaml.load(f, Loader=yaml.FullLoader)
    
    #split data param
    headless = data['headless']
    screenshoot_dir = data['screenshot_dir']
    tasks = data['tasks']

    # for x in tasks:
    #     print(x['url'])
    def execTask(task):
        opts = webdriver.ChromeOptions()
        opts.add_argument('--ignore-certificate-errors')
        opts.add_argument("--test-type")
        opts.add_experimental_option("detach", True)
            
        driver = Chrome(chrome_options=opts)
        driver.maximize_window()
        driver.get(task['url'])

        try:
            pyautogui.moveTo(504, 550, duration=0.4)
            pyautogui.leftClick()
            username = driver.find_element("name", "username")
            username.send_keys(task['user'])
            password = driver.find_element("name","password")
            password.send_keys(task['pwd'])
            password.submit()
            def countdown(t):
                while t:
                    time.sleep(1)
                    t -= 1
                driver.execute_script("document.body.style.zoom='80%'")
                
                script_dir = sys.path[0]
                img_path = os.path.join(script_dir, 'assets/ocp/administrator/operators.jpg')
                x, y = pyautogui.locateCenterOnScreen(img_path, confidence = 0.8)
                pyautogui.moveTo(x, y, duration=0.4)
                pyautogui.leftClick()
                print(x, y)
                driver.save_screenshot("wadaw1.png");
            t = 10
            
            countdown(int(t))
        
        except TimeoutException:
            print("Loading took too much time!")


    execTask(tasks[0])
    
    # num = 0
    # while num <= len(tasks)-1:
    #     # print(tasks[num])
    #     execTask(tasks[0])
    #     num += 1            




# time.sleep(.10)




  

# username.send_keys(tasks[0]['user'])
# search_box.submit()


    # def 