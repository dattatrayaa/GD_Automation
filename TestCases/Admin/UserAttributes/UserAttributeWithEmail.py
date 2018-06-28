'''
Created on 26-Feb-2018

@author: Sheethu C
'''
from operator import contains
import os.path
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

class UserAttributeWithEmail():
    
    def createEmailAttributewithRequest(self):
        print "Reading data from excel sheet"
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        first_sheet = book.sheet_by_name('User_Attributes')
        print("Fetching the Attribute Name from Excel Sheet\n")
        # read a cell
        cell = first_sheet.cell(8,1)
        AttributeName = cell.value
        print AttributeName
        
        
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/a")))
        driver.find_element_by_xpath("html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/a").click()
        print "Clicked on admin icon"
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]")))
        driver.find_element_by_xpath("html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]").click()
        print "Clicked on Admin"
        driver.find_element_by_xpath("html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/div/ul/li[1]").click()
        print "Clicked on User Attribute"
        driver.find_element_by_xpath("html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/div/ul/li[4]").click()
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[2]/div/header/h1")))
        print "User attribute Page Loaded"
        driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/header/div/div").click()
        print "Clicked on Create attribute"
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[2]/div/header/h1")))
        print "Add new custom attribute page loaded"
        print "verifying Details heading"
        if driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/div[2]/h2").is_displayed():
            print("Details Heading is  displayed")
        else:
            print ""
            raise Exception
        print "Verifying Attribute Name"
        ele =driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/div[2]/div[1]/div[1]/div/label").text
        if ele =="Attribute name":
          print("Attribute Name field is  displayed")
        else:
            print ""
            raise Exception  
        print "Entering attribute Name"
        
        driver.find_element_by_id("attribute-name").send_keys(AttributeName)
        print "Entered Attribute Name :"+AttributeName
        print "Verifying API Name field"
        if driver.find_element_by_id("attribute-api-name").is_displayed():
            print("API Name field is  displayed")
        else:
            print ""
            raise Exception
        print "Verifying Attribute Name and API NAme is matching"
        ele =driver.find_element_by_id("attribute-api-name").get_attribute('value')
        print ele
        if ele ==AttributeName:
          print("Attribute Name and API Name is Matching")
        else:
            print ""
            raise Exception  
        print "selecting Attribute as required"
        driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/div[2]/div[2]/div/div/label").click()
        driver.execute_script("window.scrollTo(750, document.body.scrollHeight)")
        print "Selected Email Type"
        driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/div[3]/div/div/div/div[4]/label").click()
        print "clicking on Save Button"
        driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/div[4]/button").click()
        wait.until(EC.visibility_of_element_located((By.XPATH,"//tbody/tr/td[1]/a[.='"+AttributeName+"']")))
        print "Verifying the created attribute in the list"
        ele =driver.find_element_by_xpath("//tbody/tr/td[1]/a[.='"+AttributeName+"']")
        print ele.text
        if ele.text == AttributeName :
            print("Attribute Name and API Name is Matching")
        else:
            print ""
            raise Exception
        print "user Attribute Email Type with required option is Created"
        print "clicking on Home"
        first_sheet = book.sheet_by_name('Login_Credentials')
        print("Fetching the Attribute Name from Excel Sheet\n")
        # read a cell
        cell = first_sheet.cell(1,1)
        HomeURL = cell.value
        print HomeURL
        driver.get(HomeURL)
        wait.until(EC.visibility_of_element_located((By.ID,"global-header-search")))
        print "Home Page Loaded"
        
        
    def createEmailAttributeWithReq(self):
        try:
            book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
            first_sheet = book.sheet_by_name('User_Attributes')
            print("Fetching the Attribute Name from Excel Sheet\n")
            # read a cell
            cell = first_sheet.cell(8,1)
            AttributeName = cell.value
            obj= UserAttributeWithEmail()
            obj.createEmailAttributewithRequest()
            od =DeleteAttributes()
            od.attributeDelete(AttributeName)
        
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
    
