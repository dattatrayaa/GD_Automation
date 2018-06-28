'''
Created on 30-Mar-2018

@author: Sheethu C
'''
import os.path
import time
import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xlrd
from BaseTestClass import BaseTestClass
from BaseTestClass import driver
from DeleteRole import DeleteRole
from RoleXpathElements import RoleXpathElements
from BaseTestClass import projectPath
class AssignAdministratorAll():
    def createAssignAdministratorAllRole(self,RoleName,Description):
        createrole =RoleXpathElements()
        wait=WebDriverWait(driver, 80)
        driver.refresh()
        wait.until(EC.visibility_of_element_located((By.XPATH,createrole.adminSideMenu())))
        driver.find_element_by_xpath(createrole.adminSideMenu()).click()
        print "Clicked on admin page"
        print "Clicked on Role icon"
        wait.until(EC.visibility_of_element_located((By.XPATH,createrole.roleSideMenu())))
        driver.find_element_by_xpath(createrole.roleSideMenu()).click()
        wait.until(EC.visibility_of_element_located((By.XPATH,createrole.createRole())))
        driver.find_element_by_xpath(createrole.createRole()).click()
        time.sleep(4)
        print "Clicked on Create role Button"
        createrole.roleCreation(RoleName,Description)
        print "clicked on Next Button"
        #Assign click
        createrole.assignClick()
        #administrator click
        createrole.adminClick()
        print "Verifying assign and administrator selected"
        ch=RoleXpathElements()
        ch.checkAssign()
        time.sleep(4)
        ch.checkAdministrator()
        time.sleep(4)
        print "Checking Check box selection"
        chk=RoleXpathElements()
        chk.checkboxUser()
        print "User is selected"
        chk.checkboxContent()
        print "Content Manger is selected"
        chk.checkboxRoles()
        print "Roles is selected"
        chk.checkboxTag()
        print "Tags is selected"
        chk.checkboxBranding()
        print "Branding is selected"
        chk.checkboxIntegration()
        print "Integration is selected"
        
        createrole.roleSave()
        print "Clicked on Save Role Button"
        print "Searching for the Created Role in the List"
        time.sleep(4)
        createrole.roleSearch(RoleName)
    def createAssignAdministratorAllMain(self):  
        try:   
            book=xlrd.open_workbook(os.path.join('Test_DataTestData.xlsx'))
            sheet=book.sheet_by_name('Role')
            cell = sheet.cell(210,1)
            RoleName = cell.value
            cell = sheet.cell(211,1)
            Description = cell.value
            book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
            first_sheet = book.sheet_by_name('UserAssignToRole')
            cell = first_sheet.cell(1,1)
            FirstName = cell.value
            obj2= AssignAdministratorAll()
            obj2.createAssignAdministratorAllRole(RoleName,Description)
            User=RoleXpathElements()
            User.CreateUserAssign()
            User.searchRole(RoleName,FirstName)
            User.deactivateUser(FirstName)
            rolede=DeleteRole()
            rolede.roleDelete(RoleName)  
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
    
    obj11= AssignAdministratorAll()
    obj12= BaseTestClass()
    obj12.UserLogin()
    obj11.createAssignAdministratorAllMain()