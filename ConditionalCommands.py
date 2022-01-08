""""
Conditional commands return boolean values always either True or False
Below are the Conditional Commands:
1) is_enabled())
2) is_displayed())
3) is_selected()
"""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

url = "http://demo.guru99.com/test/newtours/"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get(url)

username = driver.find_element_by_name("userName")
print("is Enabled:", username.is_enabled())
print("is Displayed:", username.is_displayed())

pwd = driver.find_element_by_name("password")
print("is Enabled:", pwd.is_enabled())
print("is Displayed:",pwd.is_displayed())

username.send_keys("mercury")
pwd.send_keys("mercury")
submit = driver.find_element_by_name("submit")
submit.click()

flight = driver.find_element_by_link_text("Flights")
flight.click()

radioButton = driver.find_element_by_name("tripType")
print("is Selected:", radioButton.is_selected())

driver.quit()
