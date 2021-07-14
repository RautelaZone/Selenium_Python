from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
driver.find_element_by_name("proceed").click()

alert = driver.switch_to.alert #handling alert
print("Alert text is: " +alert.text)
time.sleep(3)
alert.accept() #for submission/accept
driver.switch_to.default_content()  #back to main page
driver.find_element_by_id("login1").send_keys("anyusername")
time.sleep(3)
# alert.dismiss() #for dismiss
alert.send_keys("") #for entering value

driver.quit()