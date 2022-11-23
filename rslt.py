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
    
    # mywrk = tasks[0]
    aa = 0
    index = len(tasks)
    
    print(tasks[aa])
    
    script_dir = sys.path[0]
    while (index >= 0):
        opts = webdriver.ChromeOptions()
        opts.add_argument('--ignore-certificate-errors')
        opts.add_argument("--test-type")
        opts.add_experimental_option("detach", False)
        driver = Chrome(chrome_options=opts)
        driver.maximize_window()
        driver.get(tasks[aa]['url'])
        time.sleep(2)
        
        img_path = os.path.join(script_dir, 'assets/ocp/htpasswd.jpg')
        print(img_path)
        x, y = pyautogui.locateCenterOnScreen(img_path, confidence = 0.6)
        pyautogui.moveTo(x, y, duration=0.4)
        pyautogui.leftClick()
        time.sleep(5)
        username = driver.find_element("name", "username")
        username.send_keys(tasks[aa]['user'])
        password = driver.find_element("name","password")
        password.send_keys(tasks[aa]['pwd'])
        password.submit()
        time.sleep(5)
        driver.execute_script("document.body.style.zoom='80%'")
        time.sleep(5)           
        
        img_path = os.path.join(script_dir, 'assets/ocp/administrator/operators.jpg')
        x, y = pyautogui.locateCenterOnScreen(img_path, confidence = 0.8)            
        print(x, y)
        pyautogui.moveTo(x, y, duration=0.4)
        pyautogui.leftClick()
        time.sleep(5)
        img_path2 = os.path.join(script_dir, 'assets/ocp/administrator/operators/operatorhub.jpg')
        x, y = pyautogui.locateCenterOnScreen(img_path2 , confidence = 0.8)            
        print(x, y)
        pyautogui.moveTo(x, y, duration=0.4)
        pyautogui.leftClick()
        print("wait 40 sec")
        time.sleep(40)
        print("after 40 sec")
        aa +=1
        index -=1

    
    # try:
    # for k, v in tasks.items():
        # print(k)
        # print(f"{k=}: {v=}")
        # if(k==tasks):
        #     print(k=="tasks")
        # if v['url'] == LOOKING_FOR_THIS_USER:
        #     print(f"Found it! {k} is the user we looked for.")
    # except yaml.YAMLError as exc:
    #     print(exc)
    # print(mywrk)
    
    # print("already 10")
    
    # script_dir = sys.path[0]
    
    # opts = webdriver.ChromeOptions()
    # opts.add_argument('--ignore-certificate-errors')
    # opts.add_argument("--test-type")
    # opts.add_experimental_option("detach", True)
    # driver = Chrome(chrome_options=opts)
    # driver.maximize_window()
    # driver.get(mywrk['url'])
    # time.sleep(2)
    
    # img_path = os.path.join(script_dir, 'assets/ocp/htpasswd.jpg')
    # print(img_path)
    # x, y = pyautogui.locateCenterOnScreen(img_path, confidence = 0.6)
    # pyautogui.moveTo(x, y, duration=0.4)
    # pyautogui.leftClick()
    # time.sleep(5)
    # username = driver.find_element("name", "username")
    # username.send_keys(mywrk['user'])
    # password = driver.find_element("name","password")
    # password.send_keys(mywrk['pwd'])
    # password.submit()
    # time.sleep(5)
    # driver.execute_script("document.body.style.zoom='80%'")
    # time.sleep(5)           
    
    # img_path = os.path.join(script_dir, 'assets/ocp/administrator/operators.jpg')
    # x, y = pyautogui.locateCenterOnScreen(img_path, confidence = 0.8)            
    # print(x, y)
    # pyautogui.moveTo(x, y, duration=0.4)
    # pyautogui.leftClick()
    # time.sleep(5)
    # img_path2 = os.path.join(script_dir, 'assets/ocp/administrator/operators/operatorhub.jpg')
    # x, y = pyautogui.locateCenterOnScreen(img_path2 , confidence = 0.8)            
    # print(x, y)
    # pyautogui.moveTo(x, y, duration=0.4)
    # pyautogui.leftClick()
    # time.sleep(5)
    
    # save_path = os.path.join(script_dir,"ss/"+str(mywrk['label'])+".png")
    # driver.save_screenshot(str(save_path))