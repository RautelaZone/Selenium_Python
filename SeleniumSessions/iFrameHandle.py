from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("http://www.londonfreelance.org/courses/frames/")

driver.switch_to.frame(2)   #switch by Index
headerValue = driver.find_element_by_css_selector("body > h2").text
print("Switching frame by Index: ", headerValue)
driver.switch_to.default_content()  #back to main page

driver.switch_to.frame('main')  #switch by Name/Id
headerValue = driver.find_element_by_css_selector("body > h2").text
print("Switching frame by Name: ",headerValue)
driver.switch_to.parent_frame() #back to main page

frame_element = driver.find_element_by_name("main")
driver.switch_to.frame(frame_element)
headerValue = driver.find_element_by_css_selector("body > h2").text
print("Switching frame by Frame Element: ",headerValue)
driver.switch_to.parent_frame() #back to main page

driver.quit()