'''
Created on 27-Mar-2018

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
from BaseTestClass import excelPath
from RoleXpathElements import RoleXpathElements
class RoleLearnCreateRole():
    
    def createLearnCreateRole(self,RoleName,Description):
        craeterrole =RoleXpathElements()
        wait=WebDriverWait(driver, 80)
        driver.refresh()
        wait.until(EC.visibility_of_element_located((By.XPATH,craeterrole.adminSideMenu())))
        driver.find_element_by_xpath(craeterrole.adminSideMenu()).click()
        print "Clicked on admin page"
        wait.until(EC.visibility_of_element_located((By.XPATH,craeterrole.roleSideMenu())))
        driver.find_element_by_xpath(craeterrole.roleSideMenu()).click()
        print "Clicked on Role icon"
        wait.until(EC.visibility_of_element_located((By.XPATH,craeterrole.createRole())))
        driver.find_element_by_xpath(craeterrole.createRole()).click()
        print "Clicked on Create role Button"
        craeterrole.roleCreation(RoleName,Description)
        
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[1]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/div[1]/div")))
        wait.until(EC.element_to_be_clickable((By.XPATH,"html/body/div[1]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/div[1]/div")))
        elemm=driver.find_element_by_xpath("html/body/div[1]/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/div[1]/div")
        webdriver.ActionChains(driver).move_to_element(elemm).perform()
        driver.execute_script("arguments[0].click()", elemm)
        time.sleep(3)
        ch=RoleXpathElements()
        ch.checkCreate()
        time.sleep(4)
        craeterrole.roleSave()
        print "Clicked on Save Role Button"
        print "Searching for the Created Role in the List"
        craeterrole.roleSearch(RoleName)
    def createLearnCreateMain(self):  
         try:   
            book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
            sheet=book.sheet_by_name('Role')
            cell = sheet.cell(191,1)
            RoleName = cell.value
            cell = sheet.cell(192,1)
            Description = cell.value
            book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
            first_sheet = book.sheet_by_name('UserAssignToRole')
            cell = first_sheet.cell(3,1)
            FirstName = cell.value
            obj2= RoleLearnCreateRole()
            obj2.createLearnCreateRole(RoleName,Description) 
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
    
    obj11= LearnCreateRole()
    obj12= BaseTestClass()
    obj12.UserLogin()
    obj11.createLearnCreateMain()