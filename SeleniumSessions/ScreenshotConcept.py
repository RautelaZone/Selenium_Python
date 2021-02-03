from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.maximize_window()

driver.get('https://reddit.com/')

# normal screenshot
driver.get_screenshot_as_file("screenshot.png")
driver.quit()

''' Full Screenshot'''
# Make sure full screenshot can be captured only in headless mode

options = webdriver.ChromeOptions()
options.headless = True #True means, it will run in headless means without launching Chrome Browser
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('https://reddit.com/')

S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'), S('Height'))
driver.find_element_by_tag_name("body").screenshot("fullscreenshot.png")

''' Screenshot with a file name and when an error occurs'''
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://letskodeit.teachable.com/")
driver.find_element_by_link_text("Login").click()
wait =  WebDriverWait(driver,10,poll_frequency=1,
                          ignored_exceptions=[NoSuchElementException,
                                              ElementNotVisibleException,
                                              ElementNotSelectableException])
element = wait.until(EC.element_to_be_clickable((By.ID,"user_email")))
element.send_keys("abc@gmail.com")
driver.find_element_by_id("user_password").send_keys("testest")
driver.find_element_by_name("commit").click()
destinationFileName = "C:\\Automation\\PyCharmWorkSpace\\SeleniumWithPython\\SeleniumSessions\\Screenshots\\error.png"

try:
    driver.save_screenshot(destinationFileName)
    print("screenshot saved successfully to path:" +destinationFileName)
except NotADirectoryError:
    print("Not a directory.")

driver.quit()