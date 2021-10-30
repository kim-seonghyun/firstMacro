from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import openpyxl

wb = openpyxl.load_workbook('names.xlsx')
sheet = wb['Sheet1']
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
for i in range(1,53):
    for j in range(0,13):
        driver1 = webdriver.Chrome('/Users/gimseonghyeon/Downloads/chromedriver' , chrome_options=chrome_options)
        driver1.implicitly_wait(3)
        driver1.get('')


        cityFinder = driver1.find_element_by_name('')
        selector =  Select(cityFinder)
        selector.select_by_visible_text('')

        cityFinder2 = driver1.find_element_by_name('')
        selector2 =  Select(cityFinder2)
        selector2.select_by_visible_text('')

        driver1.find_element_by_name("agree").click()
        driver1.find_element_by_name("ra1").click()

        
        bidNm = driver1.find_element_by_id('name') 
        bidNm.clear()  
        bidNm.send_keys(sheet[i][j].value)

        search_button = driver1.find_element_by_xpath("""//*[@id="Form"]/div/div[5]/div/div[3]/button""")
        search_button.click()
        driver1.refresh()
        print(sheet[i][j].value)
        time.sleep(1)
