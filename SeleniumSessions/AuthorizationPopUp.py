from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.maximize_window()

# below url will display a authorization pop-up
driver.get("http://the-internet.herokuapp.com/basic_auth")

# to overcome this, use username:password@ before the url-- in this site, username/pwd is admin
driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")

