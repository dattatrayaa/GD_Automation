'''
Created on 23-Apr-2018

@author: Sheethu C
'''

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xlrd

from BaseTestClass import driver

class CreateAttributeXpath:
    
    def adminSideMenu(self):
        time.sleep(2)
        return "(//a[@href='/admin/users'])[1]"
    
    def attributeMenu(self):
        time.sleep(2)
        return "html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/div/ul/li[4]"
    def attributePagewait(self):
        time.sleep(2)
        return "html/body/div/div/div[3]/div[2]/div/header/h1"
    def createAttributeButton(self):
        time.sleep(2)
        return "html/body/div[1]/div/div[3]/div[2]/div/header/div/div"
    
    def addCAtrributePageDisplay(self):
        time.sleep(2)
        return "html/body/div[1]/div/div[3]/div[2]/div/header/h1"
    
    def attributeName(self):
        time.sleep(2)
        return "attribute-name"
    def apiName(self):
        time.sleep(2)
        return "attribute-api-name"
    
    def requiredField(self):
        time.sleep(2)
        return "html/body/div[1]/div/div[3]/div[2]/div/div[2]/div[2]/div/div/label/span[2]"
    
    def text(self):
        time.sleep(2)
        return "html/body/div[1]/div/div[3]/div[2]/div/div[3]/div/div/div/div[1]/label/span[2]"
    def number(self):
        time.sleep(2)
        return "html/body/div[1]/div/div[3]/div[2]/div/div[3]/div/div/div/div[2]/label/span[2]"
    
    def date(self):
        time.sleep(2)
        return "html/body/div[1]/div/div[3]/div[2]/div/div[3]/div/div/div/div[3]/label/span[2]"
    def email(self):
        time.sleep(2)
        return "html/body/div[1]/div/div[3]/div[2]/div/div[3]/div/div/div/div[4]/label/span[2]"
    
    def checkbox(self):
        time.sleep(2)
        return "html/body/div[1]/div/div[3]/div[2]/div/div[3]/div/div/div/div[5]/label/span[2]"
    
    def userReference(self):
        time.sleep(2)
        return "html/body/div[1]/div/div[3]/div[2]/div/div[3]/div/div/div/div[6]/label/span[2]"
    def list(self):
        time.sleep(2)
        return "html/body/div[1]/div/div[3]/div[2]/div/div[3]/div/div/div/div[7]/label/span[2]"
    def addToList(self):
        time.sleep(2)
        return "html/body/div[1]/div/div[3]/div[2]/div/div[3]/div/div/div[2]/div/button"
    
    def additem(self):
        time.sleep(2)
        return "html/body/div/div/div[3]/div[2]/div/div[3]/div/div/div[2]/div[2]/div/div/textarea"
    def addButton(self):
        time.sleep(2)
        return "html/body/div/div/div[3]/div[2]/div/div[3]/div/div/div[2]/div[2]/button[1]"
    def waitaddItem(self):
        time.sleep(2)
        return "html/body/div/div/div[3]/div[2]/div/div[3]/div/div/div[2]/div[3]/div"
    def saveButton(self):
        time.sleep(2)
        return "html/body/div/div/div[3]/div[2]/div/div[4]/button['Add']"
    
    def searchInGrid(self,AttributeName):
        time.sleep(2)
        wait=WebDriverWait(driver,60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//tbody/tr/td[1]/a[.='"+AttributeName+"']")))
        print "Verifying the created attribute in the list"
        ele =driver.find_element_by_xpath("//tbody/tr/td[1]/a[.='"+AttributeName+"']")
        print ele.text
        if ele.text == AttributeName :
            print("Attribute Name and API Name is Matching")
        else:
            print ""
            raise Exception
    
    def attributenameInGrid(self,AttributeName):
        time.sleep(2)
        return "//table/tbody/tr/td[.='"+AttributeName+"']/a"
    def attributeDelete(self,AttributeName):
        time.sleep(2)
        return "//table/tbody/tr/td[.='"+AttributeName+"']/a/../../td[5]/button"
    
    def popUpDeleteButton(self):
        time.sleep(2)
        return "html/body/div[4]/div/div/div[2]/div[2]/button[1]"
    
    def deleteafterwait(self):
        time.sleep(2)
        return "html/body/div/div/div[2]/div/div/span"
    def attributeVerifyName(self):
        ele =driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/div[2]/div[1]/div[1]/div/label").text
        if ele =="Attribute name":
            print("Attribute Name field is  displayed")
        else:
            print ""
            raise Exception  
        print "Entering attribute Name"
    
    
    
    
    
    
    