
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# Headless browser will execute without opening any browser
options = webdriver.ChromeOptions()
options.headless = True #True means, it will run in headless mode means without launching Chrome Browser
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.implicitly_wait(5)
driver.maximize_window()
print("Just checking new pycharm")

driver.get("https://www.google.com/")
print("From Chrome Headless--Without launching Chrome, Title is: "+driver.title)

options = webdriver.FirefoxOptions()
options.headless = True
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),options=options)
driver.get("https://www.google.com/")
print("From Firefox Headless--Without launching Firefox, Title is: "+driver.title)

options = webdriver.ChromeOptions()
options.headless = False    #now it will launch the Chrome
options.add_argument('--incognito') #launch in Incognito
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.google.com/")
driver.quit()
print("From Chrome--Launching Incognito Chrome, Title is: "+driver.title)