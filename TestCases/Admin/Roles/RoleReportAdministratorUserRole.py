'''
Created on 05-Apr-2018

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

class RoleReportAdministratorUserRole():
    
    def createReportAdministratorUserRole(self,RoleName,Description):
        createroel =RoleXpathElements()
        wait=WebDriverWait(driver, 80)
        driver.refresh()
        wait.until(EC.visibility_of_element_located((By.XPATH,createroel.adminSideMenu())))
        driver.find_element_by_xpath(createroel.adminSideMenu()).click()
        print "Clicked on admin page"
        wait.until(EC.visibility_of_element_located((By.XPATH,createroel.roleSideMenu())))
        driver.find_element_by_xpath(createroel.roleSideMenu()).click()
        print "Clicked on Role icon"
        wait.until(EC.visibility_of_element_located((By.XPATH,createroel.createRole())))
        driver.find_element_by_xpath(createroel.createRole()).click()
        print "Clicked on Create role Button"
        createroel.roleCreation(RoleName,Description)
        #report
        createroel.reportClick()
        #admin
        createroel.adminClick()
       
        print "Clicked on Administrator "
        time.sleep(3)
        ch=RoleXpathElements()
        ch.checkReport()
        time.sleep(4)
        ch.checkAdministrator()
        time.sleep(4)
        #content
        createroel.contentClick()
        
        #brand
        createroel.brandingClick()
        
        
        #Tag
        createroel.tagClick()
        
        #integrate
        createroel.integrateClick()
        
        print "Checking Check box selection"
        chk=RoleXpathElements()
        chk.checkboxUser()
        print "User is selected"
        chk.checkboxRoles()
        print "Roles is selected"
        createroel.roleSave()
        print "Clicked on Save Role Button"
        print "Searching for the Created Role in the List"
        createroel.roleSearch(RoleName)
    def createReportAdministratorUserRoleMain(self): 
        from BaseTestClass import excelPath 
        try:   
            book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
            sheet=book.sheet_by_name('Role')
            cell = sheet.cell(412,1)
            RoleName = cell.value
            cell = sheet.cell(413,1)
            Description = cell.value
            book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
            first_sheet = book.sheet_by_name('UserAssignToRole')
            cell = first_sheet.cell(2,1)
            FirstName = cell.value
            obj2= RoleReportAdministratorUserRole()
            obj2.createReportAdministratorUserRole(RoleName,Description)  
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
    
    obj11= ReportAdministratorUserRole()
    obj12= BaseTestClass()
    obj12.UserLogin()
    obj11.createReportAdministratorUserRoleMain()