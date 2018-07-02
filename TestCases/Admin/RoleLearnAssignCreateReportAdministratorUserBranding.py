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

from BaseTestClass import BaseTestClass

from BaseTestClass import driver
from DeleteRole import DeleteRole
from BaseTestClass import projectPath
from RoleXpathElements import RoleXpathElements
class RoleLearnAssignCreateReportAdministratorUserBranding():
    
    def createLearnAssignCreateReportAdministratorUserBranding(self,RoleName,Description):
        craeterole =RoleXpathElements()
        wait=WebDriverWait(driver, 80)
        driver.refresh()
        wait.until(EC.visibility_of_element_located((By.XPATH,craeterole.adminSideMenu())))
        driver.find_element_by_xpath(craeterole.adminSideMenu()).click()
        print "Clicked on admin page"
        wait.until(EC.visibility_of_element_located((By.XPATH,craeterole.roleSideMenu())))
        driver.find_element_by_xpath(craeterole.roleSideMenu()).click()
        print "Clicked on Role icon"
        wait.until(EC.visibility_of_element_located((By.XPATH,craeterole.createRole())))
        driver.find_element_by_xpath(craeterole.createRole()).click()
        print "Clicked on Create role Button"
        craeterole.roleCreation(RoleName,Description)
        
        craeterole.createClick()
        craeterole.assignClick()
        craeterole.reportClick()
        craeterole.adminClick()
        print "Clicked on Administrator "
        ch=RoleXpathElements()
        ch.checkCreate()
        time.sleep(4)
        ch.checkAssign()
        time.sleep(4)
        ch.checkReport()
        time.sleep(4)
        ch.checkAdministrator()
        time.sleep(4)
        time.sleep(3)
        #content
        craeterole.contentClick()
       
        #role
        craeterole.roleClick()
        
        
        #Tag
        craeterole.tagClick()
        
        #integrate
        craeterole.integrateClick()
       
        chk=RoleXpathElements()
        chk.checkboxUser()
        print "User is selected"
        chk.checkboxBranding()
        print "Branding is selected"
        craeterole.roleSave()
        print "Clicked on Save Role Button"
        print "Searching for the Created Role in the List"
        craeterole.roleSearch(RoleName)
    def createLearnAssignCreateReportAdministratorUserBrandingMain(self): 
        from BaseTestClass import excelPath 
        try:   
            book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
            sheet=book.sheet_by_name('Role')
            cell = sheet.cell(468,5)
            RoleName = cell.value
            cell = sheet.cell(469,5)
            Description = cell.value
            book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
            first_sheet = book.sheet_by_name('UserAssignToRole')
            cell = first_sheet.cell(3,1)
            FirstName = cell.value
            obj2= RoleLearnAssignCreateReportAdministratorUserBranding()
            obj2.createLearnAssignCreateReportAdministratorUserBranding(RoleName,Description)  
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
    
    obj11= LearnAssignCreateReportAdministratorUserBranding()
    obj12= BaseTestClass()
    obj12.UserLogin()
    obj11.createLearnAssignCreateReportAdministratorUserBrandingMain()