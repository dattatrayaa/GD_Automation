'''
Created on 24-Jul-2018

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
from CommonRoleXpath import CommonRoleXpath
class RoleNameCheck():
    def createroleVerification(self,RoleName,Description):
        createrole =CommonRoleXpath()
        wait=WebDriverWait(driver, 80)

        wait.until(EC.visibility_of_element_located((By.XPATH,createrole.adminSideMenu())))
        driver.find_element_by_xpath(createrole.adminSideMenu()).click()
        print "Clicked on admin page"
        wait.until(EC.visibility_of_element_located((By.XPATH,createrole.roleSideMenu())))
        driver.find_element_by_xpath(createrole.roleSideMenu()).click()
        print "Clicked on Role icon"
        wait.until(EC.visibility_of_element_located((By.XPATH,createrole.createRole())))
        driver.find_element_by_xpath(createrole.createRole()).click()
        print "Clicked on Create role Button"
        time.sleep(4)
        createrole.roleCreation(RoleName,Description)
        print "Creating Role with Description"
        createrole.adminClick()
        print "Clicked on Administrator "
        ch=CommonRoleXpath()
        ch.checkAdministrator()
        time.sleep(4)
        print "Checking Check box selection"
        chk=CommonRoleXpath()
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
        name =driver.find_element_by_xpath("html/body/div[1]/div/div[3]/div[2]/div/header/h1/em/div/span/div[.='"+RoleName+"']").text
        if name == RoleName:
            print "Edit Role"+RoleName+"is displaying"
        else:
            print "Edit Role"+RoleName+"is not displaying"
            raise Exception
        createrole.roleSave()
        print "Clicked on Save Role Button"
        print "Searching for the Created Role in the List"
        createrole.roleSearch(RoleName)
        
    def editRoleNameVerification(self,RoleName):
        createrole =CommonRoleXpath()
        wait=WebDriverWait(driver,80)
        driver.refresh()
        wait.until(EC.visibility_of_element_located((By.XPATH,createrole.adminSideMenu())))
        driver.find_element_by_xpath(createrole.adminSideMenu()).click()
        print "Clicked on admin page"
        wait.until(EC.visibility_of_element_located((By.XPATH,createrole.roleSideMenu())))
        driver.find_element_by_xpath(createrole.roleSideMenu()).click()
        createrole.roleSearch(RoleName)
        driver.find_element_by_xpath("//table/tbody/tr/td[.='"+RoleName+"']/span/a").click()
        time.sleep(6)
        name =driver.find_element_by_xpath("html/body/div[1]/div/div[3]/div[2]/div/header/h1/em/div/span/div[.='"+RoleName+"']").text
        
        if name == RoleName:
            print "Edit Role"+RoleName+"is displaying"
        else:
            print "Edit Role"+RoleName+"is not displaying"
            raise Exception
        driver.find_element_by_xpath("html/body/div[1]/div/div[3]/div[2]/div/div[1]/a").click()
    def mainCheckRoleName(self):  
        try:   
            book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
            sheet=book.sheet_by_name('UserAssignToRole')
            cell = sheet.cell(30,1)
            RoleName = cell.value
            cell = sheet.cell(31,1)
            Description = cell.value
            obj2= RoleNameCheck()
            obj2.createroleVerification(RoleName,Description)  
            obj2.editRoleNameVerification(RoleName)
           
        except Exception as e:
            traceback.print_exc()
            print (e)
            raise Exception
        
        finally:
            rolede=DeleteRole()
            rolede.roleDelete(RoleName)  
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
if __name__ == '__main__':
    
    obj11= RoleNameCheck()
    obj12= BaseTestClass()
    obj12.userLogin()
    obj11.mainCheckRoleName()