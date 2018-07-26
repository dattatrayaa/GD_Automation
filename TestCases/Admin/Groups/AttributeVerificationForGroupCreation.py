'''
Created on 25-Jul-2018

@author: Sheethu C
'''
import os.path
import time
import traceback
from BaseTestClass import BaseTestClass
from BaseTestClass import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xlrd
from BaseTestClass import projectPath
from CampaignPageElements import CampPage
from CreateLearnerNew import CreateLearner
from CreateLessonDifferentLessons import CreateLessonDifferentLessons
from DeleteLesson import DeleteLesson
from CreateAttributeXpath import CreateAttributeXpath
from GroupsPageElements import GroupsPageElements
class AttributeVerificationForGroupCreation:
    def createTextAttribute(self,AttributeName):
        createAttribute =CreateAttributeXpath()
        wait=WebDriverWait(driver, 60)
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
        print "Selected Text Type"
        driver.find_element_by_xpath(createAttribute.text()).click()
        driver.execute_script("window.scrollTo(650, document.body.scrollHeight)")
        print "clicking on Save Button"
        driver.find_element_by_xpath(createAttribute.saveButton()).click()
        time.sleep(4)
        createAttribute.searchInGrid(AttributeName)
    def groupCreateForAttribute(self,groupName,attributeName1):
        driver.refresh()
        wait=WebDriverWait(driver, 60)
        
        group=GroupsPageElements()
        
        group.adminSideMenuUnexpanded()
        print "Clicked on admin icon"
         
        group.groupSideMenuExpanded()  
        print "Clicked on Group icon"
        
        
        print "Checking Group page is displayed"
        if driver.find_element_by_xpath(group.groupPageHeader()).is_displayed():
            print "Group page is displayed successfully"
        else:
            print "Group page is not displayed"
            raise Exception
        
        
        group.createGroupButton()
        print "Clicked on Create Group button"
        
        group.enteringGroupname(groupName)
        
        print "Group Name entered....."
        
        group.nextButton()
        print "Clicked on Next button"
        
        wait.until(EC.visibility_of_element_located((By.XPATH,group.groupDetailPageHeader())))
        print "Checking group is created"
        
        time.sleep(4)
        headerText=driver.find_element_by_xpath(group.groupDetailPageHeader()).text
        
        if headerText==groupName:
            print "Group created successfully"
            
        else:
            print "Group not created"
            raise Exception
        
        
        print "Adding user to Group by name"
        
        group.AddByAttributes()
        
        print "Checking all option is selected"
        if group.AllOptionSelected()=="all":
            print "all is selected"
        else:
            print "all is not selected"
            raise Exception
        
        
        print "Adding User by attribute"
        group.AttributeNameEnter(attributeName1)
        group.ValueSelect(attributeName1)
        print "Selected "+attributeName1
        
        print "Clicking on Preview button"
        group.PreviewGroupButtonClick()
        
        group.saveButton()
        print "Clicked on Save button"

        group.saveButtonPopup()
        print "Clicked on Save from popup"
        
        
        print "Checking Created Group is displayed in Grid"
        group.groupsLinkFromBreadCrumb()
        
        print "Searching Group"
        group.createdGroupDisplayedInGrid(groupName)
         
        
        driver.refresh()   
    def mainAttributeVerificationForGroupCreation(self):
        try:
            book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
            first_sheet = book.sheet_by_name("Groups")
            
            cell = first_sheet.cell(225,1)
            attributeName = cell.value
            
            cell = first_sheet.cell(224,1)
            groupName = cell.value
            
        
            book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
            second_sheet = book.sheet_by_name('Login_Credentials')
            cell = second_sheet.cell(1,1)
            url = cell.value
        
            cell = second_sheet.cell(3,1)
            username = cell.value
        
            cell = second_sheet.cell(3,2)
            password = cell.value
            
            print "Creating attribute"
            atr=AttributeVerificationForGroupCreation()
            atr.createTextAttribute(attributeName)
            print "Group Creating"
            atr.groupCreateForAttribute(self,groupName,attributeName)
            
            
        except Exception as e:
            traceback.print_exc()
            print (e)
            raise Exception   
          
        finally:
           
            
            second_sheet = book.sheet_by_name('Login_Credentials')
            cell = second_sheet.cell(1,1)
            url = cell.value
            driver.get(url)
            try:
                WebDriverWait(driver, 5).until(EC.alert_is_present())

                alert = driver.switch_to.alert
                alert.accept()
                print("alert accepted")
            except Exception:
                print("no alert")
    
        
        
        
if __name__=='__main__':
    
    btc=BaseTestClass()
    btc.userLogin() 

    gr=AttributeVerificationForGroupCreation()
    gr.mainAttributeVerificationForGroupCreation()      
            