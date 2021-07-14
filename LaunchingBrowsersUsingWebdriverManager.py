from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.microsoft import IEDriverManager

url = "http://demo.guru99.com/test/newtours/"
driver = webdriver.Chrome(ChromeDriverManager().install()) #Using Chrome
# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install()) --Using FF
# driver = webdriver.Edge(EdgeChromiumDriverManager().install()) --Using Edge
# driver = webdriver.Ie(IEDriverManager().install()) --Using IE
driver.maximize_window()
driver.get(url)
title = driver.title
current_url = driver.current_url
print("Title is:", title)
print("Current URL is:", current_url)
driver.close()