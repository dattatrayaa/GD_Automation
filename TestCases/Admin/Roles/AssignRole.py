'''
Created on 26-Mar-2018

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
from RoleXpathElements import RoleXpathElements
class AssignRole():
    
    def createAssignRole(self,RoleName,Description):
        creatrerole= RoleXpathElements()
        wait=WebDriverWait(driver, 80)
        driver.refresh()
        wait.until(EC.visibility_of_element_located((By.XPATH,creatrerole.adminSideMenu())))
        driver.find_element_by_xpath(creatrerole.adminSideMenu()).click()
        print "Clicked on admin page"
        wait.until(EC.visibility_of_element_located((By.XPATH,creatrerole.roleSideMenu())))
        driver.find_element_by_xpath(creatrerole.roleSideMenu()).click()
        print "Clicked on Role icon"
        wait.until(EC.visibility_of_element_located((By.XPATH,creatrerole.createRole())))
        driver.find_element_by_xpath(creatrerole.createRole()).click()
        print "Clicked on Create role Button"
        time.sleep(4)
        creatrerole.roleCreation(RoleName,Description)
        #assign
        creatrerole.assignClick()
        creatrerole.roleSave()
        time.sleep(3)
        print "Searching for the Created Role in the List"
        creatrerole.roleSearch(RoleName)
    def assignRoleMain(self):  
        try:   
            book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
            sheet=book.sheet_by_name('Role')
            cell = sheet.cell(206,1)
            RoleName = cell.value
            cell = sheet.cell(207,1)
            Description = cell.value
            book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
            first_sheet = book.sheet_by_name('UserAssignToRole')
            cell = first_sheet.cell(1,1)
            FirstName = cell.value
            
            
            obj2= AssignRole()
            obj2.createAssignRole(RoleName,Description) 
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
    
    obj11= AssignRole()
    obj12= BaseTestClass()
    obj12.UserLogin()
    obj11.assignRoleMain()