from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


url1 = "http://demo.guru99.com/test/newtours/"
url2 = "https://www.pavantestingtools.com/"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

driver.get(url1)
print(driver.title)

driver.get(url2)
print(driver.title)

driver.back()
print(driver.title)

driver.forward()
print(driver.title)

driver.quit()