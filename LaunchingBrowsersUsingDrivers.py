from selenium import webdriver

url = "http://demo.guru99.com/test/newtours/"
driver = webdriver.Chrome(executable_path="E://Drivers//chromedriver//chromedriver.exe")  # Using Chrome
# driver = webdriver.Firefox(executable_path="E://Drivers//geckodriver//geckodriver.exe") --Using FF
# driver = webdriver.Edge(executable_path="E://Drivers//edgedriver//msedgedriver.exe") -- Using Edge
# driver = webdriver.Ie(executable_path="E://Drivers//iedriver//IEDriverServer.exe") -- Using IE

driver.maximize_window()
driver.get(url)
title = driver.title
current_url = driver.current_url
print("Title is:", title)
print("Current URL is:", current_url)
driver.close()
