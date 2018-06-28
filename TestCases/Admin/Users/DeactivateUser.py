'''
Created on 12-Mar-2018

@author: QA
'''
from operator import contains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xlrd
import time
import os.path
from BaseTestClass import driver
class DeactivateUser():
    def userDeactivation(self):
        i=0
        for i in range(4):
        
            print "Reading data from excel sheet"
            book=xlrd.open_workbook(os.path.join('TestData.xlsx'))
            sheet1=book.sheet_by_name('CreateuserfromUI')
            print("Fetching the LastName from Excel Sheet\n")
            #Read from Excel to search
            cell1 = sheet1.cell(i+1,1)
            searchfirstName = cell1.value
            print searchfirstName
            cell2 =sheet1.cell(i+1,2)
            searchlastName = cell2.value
            print searchlastName
            SearchName =searchfirstName+" "+searchlastName
            print SearchName
            #Clicking on Admin Menu from Grovo Application
            
            driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/a").click()
            wait=WebDriverWait(driver,80)
            wait.until(EC.visibility_of_element_located((By.ID,"search-users")))
            driver.find_element_by_id("search-users").send_keys(SearchName)
            wait=WebDriverWait(driver,80)
            #To click on FirstName link
            wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[2]/div/div/div[4]/table/tbody/tr[1]")))
            driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[2]/div/div/div[4]/table/tbody/tr/td[1]/a").click()
            wait=WebDriverWait(driver,80)
            driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[2]/div/header/div/button").click()
            wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div/div/div[2]/div[2]/button[1]")))
            driver.find_element_by_xpath("html/body/div[2]/div/div/div[2]/div[2]/button[1]").click()  
            wait.until(EC.visibility_of_element_located((By.ID,"search-users")))
            driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[1]/div/nav/div/div[4]").click()
            print "All Created users are Deactivated"  
    def createdUserDeactivation(self):
        try :
            ob =DeactivateUser()
            ob.userDeactivation()
           
            
        finally:  
            print "clicking on Home"
            book=xlrd.open_workbook(os.path.join('TestData.xlsx'))
            first_sheet = book.sheet_by_name('Login_Credentials')
            print("Fetching the Attribute Name from Excel Sheet\n")
            # read a cell
            cell = first_sheet.cell(1,1)
            HomeURL = cell.value
            print HomeURL
            driver.get(HomeURL)
            
            print "Home Page Loaded"

