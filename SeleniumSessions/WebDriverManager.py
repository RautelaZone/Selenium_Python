from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager        #importing respective browser driver manager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time

'''
ABOUT WEBDRIVER MANAGER:
1) To user Webdriver Manager, first need to install it using 'pip install webdriver_manager'
2) WebDriverManager automates the browser setup in the Selenium code.
3) By default,  it downloads the latest version of the browser driver.
4) It supports various browsers like  Google Chrome, Firefox, IE, Edge, Opera, etc.
'''
browserName = 'chrome'

if browserName =='chrome' or 'Chrome' or 'CHROME':
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browserName == 'firefox' or 'Firefox' or 'FIREFOX' or 'ff' or 'FF':
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif browserName == 'safari' or 'Safari' or 'SAFARI':
    driver = webdriver.Safari()
else:
    print("Please pass the correct browser name...", browserName)

driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.google.com/")
driver.quit()