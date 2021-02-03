import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

'''
This program will verify that total hours are equal or not at TimeSheet Page
'''
class LoginReact():

    print("*" * 50)
    hotelId = input("Enter Hotel Name: ")
    hotelId = hotelId.upper()

    date = input("Enter complete date like 4 January 2020 or 16 june 2020: ")
    print("*" * 50)

    day = date.split(" ")[0]
    month = date.split(" ")[1]
    if month == "may":
        month = month.capitalize()
    else:
        while len(month) <= 3:
            month = input("Enter complete month: ")
            print("*" * 50)
        month = month.capitalize()

    year = date.split(" ")[2]
    intYear = int(year)
    while intYear > 2021:
        year = input("Enter current or previous month and year: ")
        print("*" * 50)
        intYear = int(year)

    stringYear = str(intYear)
    completeDate = day + " " + month + " " + stringYear

    print("Launching Chrome Browser.....")
    print("*" * 50)

    print("Selected Date is: " + completeDate)
    print("*" * 50)

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    baseUrl = "https://inn-flow-v2-dev.azurewebsites.net/login"
    driver.get(baseUrl)
    driver.implicitly_wait(5)

    driver.find_element_by_id("formBasicEmail").send_keys("admin.163")          #Give Tenant Name
    driver.find_element_by_id("formBasicPassword").send_keys("test.123")
    driver.find_element_by_xpath("//button[starts-with(@class,'lg-btn')]").click()

    time.sleep(2)
    #driver.find_element_by_xpath("//div[contains(text(),'Labor')]").click()
    driver.find_element_by_link_text("Labor").click()
    driver.find_element_by_link_text("Timesheets").click()
    driver.find_element_by_id("dropdown-hid").click()

    driver.find_element_by_xpath("//span[contains(text(), '"+hotelId+"')]").click() #Give hotel name
    print("*" * 50)
    print("Hotel '" + hotelId + "' is selected.")
    driver.find_element_by_class_name("chevron-down").click()
    date = completeDate.split(" ")[0]
    monthYear = completeDate.split(" ")[1] + " " + completeDate.split(" ")[2]

    selectedMonYear = driver.find_element_by_xpath(
        "//span[@class='react-calendar__navigation__label__labelText react-calendar__navigation__label__labelText--from']").text
    while monthYear != selectedMonYear:
        driver.find_element_by_xpath("//button[contains(text(),'‹')]").click()
        selectedMonYear = driver.find_element_by_xpath(
            "//span[@class='react-calendar__navigation__label__labelText react-calendar__navigation__label__labelText--from']").text

    driver.find_element_by_xpath("//abbr[contains(text(), '" + date + "' )]").click()
    date1 = date + " " + monthYear
    print("Date '" + date1 + "' has been clicked.")
    print("*" * 50)

    time.sleep(10)

    # Calculating Total Hours at Left Side
    th = driver.find_element_by_xpath("//div[contains(text(),'Total Hours')]//preceding::div[@class='ttl'][1]").text
    strth = str(th)
    thrs = strth.split(":")
    intthhrs = int(thrs[0]) * 60
    intthmins = int(thrs[1])
    totalhours = intthhrs + intthmins

    # Calculating Hours of Regular Hours
    rh = driver.find_element_by_xpath("//div[contains(text(),'Regular')]//preceding::div[@class='ttl'][1]").text
    strrh = str(rh)
    rhrs = strrh.split(":")
    intrhhrs = int(rhrs[0]) * 60
    intrhmins = int(rhrs[1])
    regularhours = intrhhrs + intrhmins

    # Calculating Overtime Hours
    ot = driver.find_element_by_xpath("//div[contains(text(),'Overtime')]//preceding::div[@class='ttl'][1]").text
    strot = str(ot)
    othrs = strot.split(":")
    intothrs = int(othrs[0]) * 60
    intotmins = int(othrs[1])
    overtime = intothrs + intotmins
    Hr = int(intothrs / 60)
    Min = intotmins % 60
    print("OT hours are:", Hr, "Hours and", Min, "Minutes")
    print("*" * 50)

    # Calculating Double Overtime Hours
    try:
        doubleovertime = 0
        dot = driver.find_element_by_xpath(
            "//div[contains(text(),'Double Overtime')]//preceding::div[@class='ttl'][1]").text
        print("DOT is present")
        strdot = str(dot)
        dothrs = strdot.split(":")
        intdothrs = int(dothrs[0]) * 60
        intdotmins = int(dothrs[1])
        doubleovertime = intdothrs + intdotmins
        Hr = int(intdothrs / 60)
        Min = intdotmins % 60
        print("DOT hours are:", Hr, "Hours and", Min, "Minutes")
        print("*" * 50)

    except:
        print("DOT is not present")
        print("*" * 50)

    # Calculating PTO Hours
    pto = driver.find_element_by_xpath("//div[contains(text(),'PTO')]//preceding::div[@class='ttl'][1]").text
    strto = str(pto)
    tohrs = strto.split(":")
    inttohrs = int(tohrs[0]) * 60
    inttomins = int(tohrs[1])
    ptotimeoff = inttohrs + inttomins
    Hr = int(inttohrs / 60)
    Min = inttomins % 60
    print("PTO hours are:", Hr, "Hours and", Min, "Minutes")
    print("*" * 50)

    # Calculating Holiday Hours
    try:
        holiday = 0
        hol = driver.find_element_by_xpath(
            "//div[contains(text(),'Holiday')]//preceding::div[@class='ttl'][1]").text
        print("Holiday is present")
        strhol = str(hol)
        holhrs = strhol.split(":")
        intholhrs = int(holhrs[0]) * 60
        intholmins = int(holhrs[1])
        holiday = intholhrs + intholmins
        Hr = int(intholhrs / 60)
        Min = intholmins % 60
        print("Holiday hours are:", Hr, "Hours and", Min, "Minutes")
        print("*" * 50)

    except:
        print("Holiday is not present")
        print("*" * 50)

    # Calculating UTO Hours
    try:
        unpaidTO = 0
        UTO = driver.find_element_by_xpath(
            "//div[contains(text(),'UTO')]//preceding::div[@class='ttl'][1]").text
        print("UTO is present")
        strUTO = str(UTO)
        UTOhrs = strUTO.split(":")
        intUTOhrs = int(UTOhrs[0]) * 60
        intUTOmins = int(UTOhrs[1])
        unpaidTO = intUTOhrs + intUTOmins
        Hr = int(intUTOhrs / 60)
        Min = intUTOmins % 60
        print("UTO hours are:", Hr, "Hours and", Min, "Minutes")
        print("*" * 50)

    except:
        print("UTO is not present")
        print("*" * 50)

    driver.quit()

    totalRight = regularhours + overtime + doubleovertime + ptotimeoff + holiday    #UTO hours does not include as per story
    #print("Total of Regular Hrs,Over Time,Double Over Time,Holiday and PTO is : " + str(totalRight) + " minutes")
    Hr1 = int(totalhours/60)
    Min1 = totalhours%60

    Hr2 = int(totalhours/60)
    Min2 = totalRight % 60

    print("Total LHS is:",Hr1,"Hours and" ,Min1,"Minutes")
    print("Total RHS is:",Hr2,"Hours and",Min2,"Minutes")
    print("*" * 50)

    # print("Total time at LHS is : " + str(totalhours) + " minutes")
    # print("Total time of RHS is : " + str(totalRight) + " minutes")

    if totalRight == totalhours:
        print("Total Hours are verified and correct.")
        print("*" * 50)
    else:
        print("Total Hours are not correct.")
        print("*" * 50)


