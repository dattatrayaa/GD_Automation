'''
Created on 26-Feb-2018

@author: Sheethu C
'''
from operator import contains
import os.path
import time
import traceback

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xlrd

from DeleteAttributes import DeleteAttributes
from BaseTestClass import BaseTestClass
from  BaseTestClass import driver
from BaseTestClass import projectPath
from CreateAttributeXpath import CreateAttributeXpath

class UserAttributeUserReferenceWithReq():
    
    def createUserReferenceAttributewithReq(self):
        createAttribute =CreateAttributeXpath()
        print "Reading data from excel sheet"
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        first_sheet = book.sheet_by_name('User_Attributes')
        print("Fetching the Attribute Name from Excel Sheet\n")
        # read a cell
        cell = first_sheet.cell(12,1)
        AttributeName = cell.value
        print AttributeName
        
        
        wait=WebDriverWait(driver, 80)
        driver.refresh()
        wait.until(EC.visibility_of_element_located((By.XPATH,createAttribute.adminSideMenu())))
        driver.find_element_by_xpath(createAttribute.adminSideMenu()).click()
        print "Clicked on admin icon"
        
        time.sleep(4)
        driver.find_element_by_xpath(createAttribute.attributeMenu()).click()
        wait.until(EC.visibility_of_element_located((By.XPATH,createAttribute.attributePagewait())))
        print "User attribute Page Loaded"
        wait.until(EC.visibility_of_element_located((By.XPATH,createAttribute.createAttributeButton())))
        wait.until(EC.element_to_be_clickable((By.XPATH,createAttribute.createAttributeButton())))
        driver.find_element_by_xpath(createAttribute.createAttributeButton()).click()
        print "Clicked on Create attribute"
        wait.until(EC.visibility_of_element_located((By.XPATH,createAttribute.addCAtrributePageDisplay())))
        print "Add new custom attribute page loaded"
        print "verifying Details heading"
        if driver.find_element_by_xpath(createAttribute.addCAtrributePageDisplay()).is_displayed():
            print("Details Heading is  displayed")
        else:
            print ""
            raise Exception
        print "Verifying Attribute Name"
        time.sleep(4)
        createAttribute.attributeVerifyName()
        time.sleep(4)
        wait.until(EC.visibility_of_element_located((By.ID,createAttribute.attributeName())))
        driver.find_element_by_id(createAttribute.attributeName()).send_keys(AttributeName)
        print "Entered Attribute Name :"+AttributeName
        print "Verifying API Name field"
        if driver.find_element_by_id(createAttribute.apiName()).is_displayed():
            print("API Name field is  displayed")
        else:
            print ""
            raise Exception
        print "Verifying Attribute Name and API NAme is matching"
        ele =driver.find_element_by_id(createAttribute.apiName()).get_attribute('value')
        print ele
        if ele ==AttributeName:
            print("Attribute Name and API Name is Matching")
        else:
            print ""
            raise Exception   
        driver.execute_script("window.scrollTo(750, document.body.scrollHeight)")
        print "Selected User Reference Type"
        driver.find_element_by_xpath(createAttribute.userReference()).click()
        print "selecting Attribute as required"
        driver.find_element_by_xpath(createAttribute.requiredField()).click()
        print "clicking on Save Button"
        driver.find_element_by_xpath(createAttribute.saveButton()).click()
        time.sleep(4)
        createAttribute.searchInGrid(AttributeName)
        
    def createUserReferenceAttributeWithRequiredField(self):
        
        try:
            book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
            first_sheet = book.sheet_by_name('User_Attributes')
            print("Fetching the Attribute Name from Excel Sheet\n")
            # read a cell
            cell = first_sheet.cell(12,1)
            AttributeName = cell.value
            ob =UserAttributeUserReferenceWithReq()
            ob.createUserReferenceAttributewithReq()
            od =DeleteAttributes()
            od.attributeDelete(AttributeName)
        except Exception as e:
            traceback.print_exc()
            print (e)
            raise Exception  
        
        finally:    
            print "clicking on Home"
            book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
            first_sheet = book.sheet_by_name('Login_Credentials')
            print("Fetching the Attribute Name from Excel Sheet\n")
            # read a cell
            cell = first_sheet.cell(1,1)
            HomeURL = cell.value
            print HomeURL
            driver.get(HomeURL)
            wait=WebDriverWait(driver, 80)
            wait.until(EC.visibility_of_element_located((By.ID,"global-header-search")))
            print "Home Page Loaded"
            
