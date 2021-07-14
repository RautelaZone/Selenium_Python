""""
1) Implicit Wait :
--Implicit Wait directs the Selenium WebDriver to wait for a certain measure of time before throwing an exception.
Once this time is set, WebDriver will wait for the element before the exception occurs.
--This can be useful when certain elements on the webpage are not available immediately and need some time to load.
--applicable for all the elements which are present in the page.
--we need to specify only one time at the beginning of the code.

driver.implicitly_wait(time_to_wait)
driver.implicitly_wait(10)

2) Explicit Wait:
--Wait for a certain condition to occur before proceeding further in the code.
--Need to import WebDriverWait and expected_conditions

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, 'someid')))

3) Fluent Wait:
-- used to define maximum time for the web driver to wait for a condition,
as well as the frequency with which we want to check the condition before throwing an "ElementNotVisibleException"
--checks for the web element at regular intervals until the object is found or timeout happens.

wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[Exception1, Exception2])
element = wait.until(EC.element_to_be_clickable((By.ID, 'someid')))
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

url = "http://demo.guru99.com/test/newtours/"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get(url)

# Implicit Wait
driver.implicitly_wait(10)

username = driver.find_element_by_name("userName")
pwd = driver.find_element_by_name("password")

username.send_keys("mercury")
pwd.send_keys("mercury")

# Explicit Wait
wait = WebDriverWait(driver,10)
submit = wait.until(EC.presence_of_element_located((By.NAME,"submit")))
submit.click()
print(driver.title)

# Fluent Wait
wait = WebDriverWait(driver,10,2)
flight = wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Flights")))
flight.click()

driver.quit()
