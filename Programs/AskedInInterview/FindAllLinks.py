import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class example:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("https://www.google.com/")
    allURLs = driver.find_elements_by_tag_name("a")
    print("Total links are:", len(allURLs)) # No of links
    print("*"*50)
    word = "Business"
    for elem in allURLs:
        allURLTexts=elem.get_attribute("href") #fetch all URLs
        d = elem.text   # Fetch all link text
        if word in d:
            print("Given word is:",d)
            break
    else:
        print("word :",word,"not found in the page")

    print("*" * 50)
    driver.quit()
