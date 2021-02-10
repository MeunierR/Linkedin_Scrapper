from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from parsel import selector
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import os
os.chdir("/Users/romainmeunier/Desktop/Projet Informatique/Projet_Dorian_Tapie")
import openpyxl

driver = webdriver.Chrome("/Applications/chromedriver")
driver.get('https://www.linkedin.com')

username = driver.find_element_by_id('session_key')
username.send_keys('meunier.romn@gmail.com')

password = driver.find_element_by_id('session_password')
password.send_keys('Moulikadid38')

log_in_button = driver.find_element_by_class_name("sign-in-form__submit-button")
log_in_button.click()

time.sleep(15)
#################################### INSERT URL ####################################

driver.get('https://www.linkedin.com/sales/search/people?companySize=D&doFetchHeroCard=false&functionIncluded=10&geoIncluded=105015875&logHistory=true&page=1&rsLogId=655578044&searchSessionId=lhbxt6FsT8mK8wumbTjGfQ%3D%3D&seniorityIncluded=10%2C8')

####################################################################################
time.sleep(3)
links =[]
tab = []
number_page = 1
number_candidate = 1
path = "/Users/romainmeunier/Desktop/Projet Informatique/Projet_Dorian_Tapie"
while number_page < 83:
    time.sleep(5)
    height = 0
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    while height < driver.execute_script("return document.body.scrollHeight"):
        driver.execute_script("window.scrollTo(0, {});".format(height))
        height += 20
    names = driver.find_elements_by_tag_name("a")
    for name in names:
        link = name.get_attribute('href')
        if 'https://www.linkedin.com/sales/people/' in link:
            if link not in links:
                links.append([len(links),link])


    number_page += 1
    next_button = driver.find_element_by_class_name("search-results__pagination-next-button")
    next_button.click()
    print(len(links)/2)

    df = pd.DataFrame(np.array(links))
    df.to_excel(r'{}/Linkedin_URL.xlsx'.format(path), index=False, header=True)