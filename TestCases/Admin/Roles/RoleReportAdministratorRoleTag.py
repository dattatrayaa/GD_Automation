'''
Created on 05-Apr-2018

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

from BaseTestClass import BaseTestClass
from BaseTestClass import driver
from DeleteRole import DeleteRole
from BaseTestClass import projectPath
from RoleXpathElements import RoleXpathElements

class RoleReportAdministratorRoleTag():
    
    def createReportAdministratorRoleTag(self,RoleName,Description):
        createrole =RoleXpathElements()
        wait=WebDriverWait(driver, 80)
        driver.refresh()
        wait.until(EC.visibility_of_element_located((By.XPATH,createrole.adminSideMenu())))
        driver.find_element_by_xpath(createrole.adminSideMenu()).click()
        print "Clicked on admin page"
        wait.until(EC.visibility_of_element_located((By.XPATH,createrole.roleSideMenu())))
        driver.find_element_by_xpath(createrole.roleSideMenu()).click()
        print "Clicked on Role icon"
        wait.until(EC.visibility_of_element_located((By.XPATH,createrole.createRole())))
        driver.find_element_by_xpath(createrole.createRole()).click()
        print "Clicked on Create role Button"
        createrole.roleCreation(RoleName,Description)
        #report
        createrole.reportClick()
        #admin
        createrole.adminClick()
        
        print "Clicked on Administrator "
        time.sleep(3)
        ch=RoleXpathElements()
        ch.checkReport()
        time.sleep(4)
        ch.checkAdministrator()
        time.sleep(4)
        #User
        createrole.userClick()
        
        #Integrate
        createrole.integrateClick()
        
        #content
        createrole.contentClick()
        
        #Brand
        createrole.brandingClick()
        
        print "Checking Check box selection"
        chk=RoleXpathElements()
        chk.checkboxRoles()
        print "Roles is selected"
        chk.checkboxTag()
        print "Tags is selected"
        createrole.roleSave()
        print "Clicked on Save Role Button"
        print "Searching for the Created Role in the List"
        createrole.roleSearch(RoleName)
    def maincreateReportAdminRoleTag(self): 
        from BaseTestClass import excelPath 
        try:   
            book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
            sheet=book.sheet_by_name('Role')
            cell = sheet.cell(384,5)
            RoleName = cell.value
            cell = sheet.cell(385,5)
            Description = cell.value
            book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
            first_sheet = book.sheet_by_name('UserAssignToRole')
            cell = first_sheet.cell(2,1)
            FirstName = cell.value
            obj2= RoleReportAdministratorRoleTag()
            obj2.createReportAdministratorRoleTag(RoleName,Description)  
            User=RoleXpathElements()
            User.CreateUserReport()
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
            User.updateUserReport()   
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
    
    obj11= ReportAdministratorRoleTag()
    obj12= BaseTestClass()
    obj12.UserLogin()
    obj11.maincreateReportAdminRoleTag()