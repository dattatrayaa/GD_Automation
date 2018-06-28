'''
Created on 26-Feb-2018

@author: Sheethu C
'''
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
class UserAttributeListWithoutReq():
    
    def createListAttributewithoutReq(self):
        createAttribute=CreateAttributeXpath()
        print "Reading data from excel sheet"
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        first_sheet = book.sheet_by_name('User_Attributes')
        print("Fetching the Attribute Name from Excel Sheet\n")
        # read a cell
        cell = first_sheet.cell(13,1)
        AttributeName = cell.value
        print AttributeName
        cell = first_sheet.cell(13,3)
        EnterItem = cell.value
        print EnterItem
        
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
        print "Selected List  Type"
        driver.find_element_by_xpath(createAttribute.list()).click()
        print "Clicking on Add to list"
        driver.find_element_by_xpath(createAttribute.addToList()).click()
        print "Enter A new item"
        driver.find_element_by_xpath(createAttribute.additem()).send_keys(EnterItem)
        print "entered Item is "+EnterItem
        print "Clicking On Add Button"
        wait.until(EC.visibility_of_element_located((By.XPATH,createAttribute.addButton())))
        driver.find_element_by_xpath(createAttribute.addButton()).click()
        wait.until(EC.visibility_of_element_located((By.XPATH,createAttribute.waitaddItem())))
        print "clicking on Save Button"
        driver.find_element_by_xpath(createAttribute.saveButton()).click()
        time.sleep(4)
        createAttribute.searchInGrid(AttributeName)
        
       
    def createListAttributeWithoutRequiredField(self):
        try:
            book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
            first_sheet = book.sheet_by_name('User_Attributes')
            print("Fetching the Attribute Name from Excel Sheet\n")
            # read a cell
            cell = first_sheet.cell(13,1)
            AttributeName = cell.value
            ob =UserAttributeListWithoutReq()
            ob.createListAttributewithoutReq()
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
