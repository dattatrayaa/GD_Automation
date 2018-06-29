'''
Created on 13-Mar-2018
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
from BaseTestClass import WebDriverWait
from BaseTestClass import driver
from BaseTestClass import projectPath

class APIUserDeactivate:
    def deactivateuserAPI(self):
        for i in range(15):
            print "Reading data from excel "
            book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
            sheet1=book.sheet_by_name('API testing')
            #Read from Excel to search
            cell1 = sheet1.cell(i+1,1)
            searchlastName = cell1.value
            #Clicking on Admin Menu from Grovo Application
            wait=WebDriverWait(driver,80)
            wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/a")))
            driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/a").click()
            
            wait.until(EC.visibility_of_element_located((By.ID,"search-users")))
            driver.find_element_by_id("search-users").send_keys(searchlastName)
            wait=WebDriverWait(driver,80)
            #To click on FirstName link
            wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/div/div[3]/table/tbody/tr[1]")))
            driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[2]/div/div/div[3]/table/tbody/tr/td[1]/a").click()
            driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[2]/div/header/div/button").click()
            wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div/div/div[2]/div[2]/button[1]")))
            driver.find_element_by_xpath("html/body/div[2]/div/div/div[2]/div[2]/button[1]").click()  
            print"Clicked on Deactivate button"
            wait.until(EC.visibility_of_element_located((By.ID,"search-users")))
            driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[1]/div/nav/div/div[4]").click()
            print "Deactivated User with Last Name : " +searchlastName
     
    def mainDeleteAPIUser(self):
        try:     
            d=APIUserDeactivate()
            d.deactivateuser()
        finally:
            book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
            second_sheet = book.sheet_by_name('Login_Credentials')
            cell = second_sheet.cell(1,1)
            url = cell.value
            driver.get(url)
            
if __name__ == '__main__':
    ob= BaseTestClass()
    ob.UserLogin()
    obj1= APIUserDeactivate()
    obj1.deactivateuserAPI()
            
