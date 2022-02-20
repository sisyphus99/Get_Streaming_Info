# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 16:15:51 2022

@author: Arijit
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver as webdriver
import requests
print("Enter movie name:\n")
title=input()
requestUrl='http://www.omdbapi.com/?apikey=8e51f38a&t='+title
response=requests.get(requestUrl).json()
id=None
try:
    id=response['imdbID']
except:
    print("Invalid movie name")
if(id!=None):
    url = "https://www.imdb.com/title/"+id+"/"
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver =  webdriver.Chrome(executable_path=r'C:\Users\Arijit\Downloads\chromedriver_win32\chromedriver.exe')
    driver.get(url)
    try:
        print(WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[2]/div/a/div/div[1]"))).text)
    except:
        print('Not Available in India')