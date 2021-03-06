'''
Created on 09-Apr-2018

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
from BaseTestClass import projectPath
from BaseTestClass import BaseTestClass
from BaseTestClass import driver
from DeleteRole import DeleteRole
from RoleXpathElements import RoleXpathElements

class RoleLearnAssignCreateReportAdministratorBranding():
    
    def createLearnAssignCreateReportAdministratorBranding(self,RoleName,Description):
        createroles =RoleXpathElements()
        wait=WebDriverWait(driver, 80)
        driver.refresh()
        wait.until(EC.visibility_of_element_located((By.XPATH,createroles.adminSideMenu())))
        driver.find_element_by_xpath(createroles.adminSideMenu()).click()
        print "Clicked on admin page"
        wait.until(EC.visibility_of_element_located((By.XPATH,createroles.roleSideMenu())))
        driver.find_element_by_xpath(createroles.roleSideMenu()).click()
        print "Clicked on Role icon"
        wait.until(EC.visibility_of_element_located((By.XPATH,createroles.createRole())))
        driver.find_element_by_xpath(createroles.createRole()).click()
        print "Clicked on Create role Button"
        createroles.roleCreation(RoleName,Description)
        createroles.createClick()
        createroles.assignClick()
        createroles.reportClick()
        createroles.adminClick()
        print "Clicked on Administrator "
        time.sleep(3)
        ch=RoleXpathElements()
        ch.checkCreate()
        time.sleep(4)
        ch.checkAssign()
        time.sleep(4)
        ch.checkReport()
        time.sleep(4)
        ch.checkAdministrator()
        time.sleep(4)
        #User
        createroles.userClick()
           
        
        #Content
        createroles.contentClick()
        
        
        #role
        createroles.roleClick()
        
        
        #Tag
        createroles.tagClick()
        
        
        #integrate
        createroles.integrateClick()
        
        chk=RoleXpathElements()
        chk.checkboxBranding()
        print "Branding is selected"
        createroles.roleSave()
        print "Clicked on Save Role Button"
        print "Searching for the Created Role in the List"
        createroles.roleSearch(RoleName)
    def createLearnAssignCreateReportAdministratorBrandingMain(self):
        from BaseTestClass import excelPath  
        try:   
            book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
            sheet=book.sheet_by_name('Role')
            cell = sheet.cell(464,1)
            RoleName = cell.value
            cell = sheet.cell(465,1)
            Description = cell.value
            book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
            first_sheet = book.sheet_by_name('UserAssignToRole')
            cell = first_sheet.cell(3,1)
            FirstName = cell.value
            obj2= RoleLearnAssignCreateReportAdministratorBranding()
            obj2.createLearnAssignCreateReportAdministratorBranding(RoleName,Description)
            User=RoleXpathElements()
            User.CreateUserLearn()
            User.searchRole(RoleName,FirstName)
            User.deactivateUser(FirstName)
            rolede=DeleteRole()
            rolede.roleDelete(RoleName)
      
     
            #if any alert box occurs it will accept the alert
            #if any alert box occurs it will accept the alert
        except Exception as e:
            traceback.print_exc()
            print (e)
            raise Exception   
        finally: 
            User=RoleXpathElements() 
            User.updateUserLearn() 
            second_sheet = book.sheet_by_name('Login_Credentials')
            cell = second_sheet.cell(1,1)
            url = cell.value
            driver.get(url)
            #if any alert box occurs it will accept the alert
            try:
                WebDriverWait(driver, 5).until(EC.alert_is_present())

                alert = driver.switch_to.alert
                alert.accept()
                print("alert accepted")
            except Exception:
                print("no alert")
        
if __name__ == '__main__':
    
    obj11= LearnAssignCreateReportAdministratorBranding()
    obj12= BaseTestClass()
    obj12.UserLogin()
    obj11.createLearnAssignCreateReportAdministratorBrandingMain()