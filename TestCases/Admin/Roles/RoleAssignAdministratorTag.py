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
from BaseTestClass import projectPath
from BaseTestClass import BaseTestClass
from BaseTestClass import driver
from DeleteRole import DeleteRole
from RoleXpathElements import RoleXpathElements
from BaseTestClass import excelPath
class AssignAdministratorTag():
    
    def createAssignAdministratorTag(self,RoleName,Description):
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
        time.sleep(4)
        createrole.roleCreation(RoleName,Description)
        #assign
        createrole.assignClick()
        #admin
        createrole.adminClick()
        
        print "Clicked on Administrator "
        ch=RoleXpathElements()
        ch.checkAssign()
        time.sleep(4)
        ch.checkAdministrator()
        time.sleep(4)
        #user
        createrole.userClick()
        
        #Content
        createrole.contentClick()
        
        #role
        createrole.roleClick()
        
       
        #Branding
        createrole.brandingClick()
        
        
        
        #Integrate
        createrole.integrateClick()
        
        print "Checking Check box selection"
        chk=RoleXpathElements()
        chk.checkboxTag()
        print "Tags is selected"
        createrole.roleSave()
        print "Clicked on Save Role Button"
        print "Searching for the Created Role in the List"
        createrole.roleSearch(RoleName)
    def createAssignAdministratorTagMain(self):  
        try:   
            book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
            sheet=book.sheet_by_name('Role')
            cell = sheet.cell(352,1)
            RoleName = cell.value
            cell = sheet.cell(353,1)
            Description = cell.value
            book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
            first_sheet = book.sheet_by_name('UserAssignToRole')
            cell = first_sheet.cell(1,1)
            FirstName = cell.value
            obj2= AssignAdministratorTag()
            obj2.createAssignAdministratorTag(RoleName,Description)
            User=RoleXpathElements()
            User.CreateUserAssign()
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
            User.updateUserAssign()    
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
    
    obj11= AssignAdministratorTag()
    obj12= BaseTestClass()
    obj12.UserLogin()
    obj11.createAssignAdministratorTagMain()