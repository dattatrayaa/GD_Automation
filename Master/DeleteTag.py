'''
Created on 14-Jun-2018

@author: Sheethu C
'''

import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xlrd

from BaseTestClass import BaseTestClass
from BaseTestClass import driver


class DeleteTag:
    
    def tagDeletion(self,Tagname):
        
        wait=WebDriverWait(driver, 60)
        driver.refresh()
        wait.until(EC.visibility_of_element_located((By.XPATH,("(//a[@href='/admin/users'])[1]"))))
        driver.find_element_by_xpath("(//a[@href='/admin/users'])[1]").click()
        print "Clicked on admin icon"
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[1]/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/div/ul/li[5]/a")))
        driver.find_element_by_xpath("html/body/div[1]/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/div/ul/li[5]/a").click()
        wait.until(EC.visibility_of_element_located((By.ID,"tag-index-search")))
        tag= driver.find_element_by_id("tag-index-search")
        tag.send_keys(Tagname)
        tag.send_keys(Keys.ENTER)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[1]/div/div[3]/div[2]/div/div/section[2]/div/ul/li[1]/a")))
        driver.find_element_by_xpath("html/body/div[1]/div/div[3]/div[2]/div/div/section[2]/div/ul/li[1]/a").click()
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[1]/div/div[3]/div[2]/div/header/div/button")))
        wait.until(EC.element_to_be_clickable((By.XPATH,"html/body/div[1]/div/div[3]/div[2]/div/header/div/button")))
        driver.find_element_by_xpath("html/body/div[1]/div/div[3]/div[2]/div/header/div/button").click()
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[4]/div/div/div[2]/div/button[1]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,"html/body/div[4]/div/div/div[2]/div/button[1]")))
        driver.find_element_by_xpath("html/body/div[4]/div/div/div[2]/div/button[1]").click()
        time.sleep(4)
        
        
        
        
        
        
        