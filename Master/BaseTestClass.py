'''
Created on 21-Feb-2018

@author: Optislabs
'''
import os.path
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import xlrd


driver=webdriver.Chrome()


class BaseTestClass:
    
    def UserLogin(self):
    
        print "Opening Browser"
        
        driver.maximize_window()
        
        print "Reading data from excel sheet"
        book=xlrd.open_workbook(os.path.join('TestData.xlsx'))
        
        # print number of sheets
        print("Number of WorkSheets :")
        print book.nsheets
    
        # print sheet names
        #print("Name of WorkSheets :")
        #print book.sheet_names()
        
        # get the first worksheet
        first_sheet = book.sheet_by_name('Login_Credentials')
        
        # read a row
        #print("First Row Data in 1st WorkSheet :")
        #print first_sheet.row_values(0)
        
        print("Fetching the URL, username and password from Excel Sheet\n")
        # read a cell
        cell = first_sheet.cell(1,1)
        url = cell.value
        print url
        
        cell = first_sheet.cell(3,1)
        username = cell.value
        print username
        
        cell = first_sheet.cell(3,2)
        password = cell.value
        print password  
        
        driver.get(url)
        element = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.ID, "password")))
        if driver.title == "Grovo":
            print("Grovo Application URL Opened")
        else:
            raise Exception.message

        print "Grovo Sign-In page is displayed"
        
        print "Entering User name"
        driver.find_element_by_xpath(".//*[@id='username']").send_keys(username)
       
        print "Entering Password"
        element.send_keys(password)
        
        element.send_keys(Keys.TAB)
        print "Clicking on Sign_In button"
        driver.find_element_by_xpath("//*[@id='submitButton']").click()
        
        print "Successfully Loged Into Grovo Application"
        time.sleep(5)
        
    def UserLoginWithUrl(self,url,username,password):
    
        print "Opening Browser"
        
        driver.maximize_window()
        
        driver.get(url)
        element = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.ID, "password")))
        if driver.title == "Grovo":
            print("Grovo Application URL Opened")
        else:
            raise Exception.message

        print "Grovo Sign-In page is displayed"
        
        print "Entering User name"
        driver.find_element_by_xpath(".//*[@id='username']").send_keys(username)
       
        print "Entering Password"
        element.send_keys(password)
        
        element.send_keys(Keys.TAB)
        print "Clicking on Sign_In button"
        driver.find_element_by_xpath("//*[@id='submitButton']").click()
        
        print "Successfully Loged Into Grovo Application"
        time.sleep(5)
        
        



    
