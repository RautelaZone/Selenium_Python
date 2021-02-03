from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.maximize_window()

# IMPORTANT: It will only work if (type="file") for upload/open button
# If in DOM, type is 'file' for upload/open button then we can use direct send_keys method

driver.get("https://cgi-lib.berkeley.edu/ex/fup.html")
driver.find_element_by_name("upfile").send_keys('C:/Users/anilr/Desktop/UK_Ticket_11Dec2020.pdf')
#driver.find_element_by_xpath("//input[@type='submit']").click()