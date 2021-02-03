# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# import datetime
# import time
# from selenium.webdriver.support.ui import Select
import os
#
# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.implicitly_wait(5)
# driver.maximize_window()
#
# driver.get("http://form-cube.com")
# driver.find_element_by_id("txt_Uname").send_keys("C161020202052")
# driver.find_element_by_id("txt_pass").send_keys("2VPYA")
# driver.find_element_by_id("btnsubmit").click()
#
# x = 1061
# select = Select(driver.find_element_by_name("ctl00$ContentPlaceHolder1$drp_pagejump"))
# select.select_by_index(x)
#
# while x <= 1200:
#     driver.execute_script("window.scrollBy(0,4000);")
#     timestamp = datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')
#     fileName = timestamp+'.png'
#     driver.get_screenshot_as_file(fileName)
#     driver.find_element_by_id("ctl00_ContentPlaceHolder1_btnsubmit").click()
#     x = x+1
#
# driver.find_element_by_id("ctl00_lnklogout").click()
# driver.quit()

os.system("shutdown /s /t/ 1")








