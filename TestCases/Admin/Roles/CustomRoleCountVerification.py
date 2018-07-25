'''
Created on 23-Jul-2018

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
from BaseTestClass import projectPath
from RoleXpathElements import RoleXpathElements
class CustomRoleCountVerification():
    def customRoleCount(self):
        wait= WebDriverWait(driver,80)
        role=RoleXpathElements()
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,role.adminSideMenu())))
        driver.find_element_by_xpath(role.adminSideMenu()).click()
        print "Clicked on Admin icon"
        wait.until(EC.visibility_of_element_located((By.XPATH,role.roleSideMenu())))
        driver.find_element_by_xpath(role.roleSideMenu()).click()
        time.sleep(4)
        #Custom role Count before clicking
        wait.until(EC.visibility_of_element_located((By.XPATH,role.befrecustomrolecount())))
        befreCount=driver.find_element_by_xpath(role.befrecustomrolecount()).text
        #clicking on Customrole tab
        role.customroletabclick()
        wait.until(EC.visibility_of_element_located((By.XPATH,role.aftercustomcount())))
        aftercount=driver.find_element_by_xpath(role.aftercustomcount()).text
        print aftercount
        wait.until(EC.visibility_of_element_located((By.XPATH,role.rolecount())))
        actualcount =driver.find_element_by_xpath(role.rolecount()).text
        print actualcount
        #checking with the before custom role tab clicking count and actual count
        if befreCount == actualcount:
            print "Count  of custom Role before clicking custom Tab and Actuall count are matching"
        else:
            print "Count  of custom Role before clicking custom Tab and Actuall count are not matching"
            raise Exception
        #checking with the after clicking custom role tab and Actual count
        if aftercount == actualcount:
            print "Count of custom role after clicking custom tab and acutal count are matching"
        else:
            print "Count of custom role after clicking custom role tab and actual count are not matching" 
            raise Exception
        
    def mainCountVerificationForCustomRoles(self):
        try :
            ob =CustomRoleCountVerification()
            ob.customRoleCount()
        except Exception as e:
            traceback.print_exc()
            print (e)
            raise Exception    
        finally:  
            print "clicking on Home"
            book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
            first_sheet = book.sheet_by_name('Login_Credentials')
            print("Fetching the Attribute Name from Excel Sheet\n")
            # read a cell
            cell = first_sheet.cell(1,1)
            HomeURL = cell.value
            print HomeURL
            driver.get(HomeURL)
            print "Home Page Loaded"
            
if __name__ == '__main__':
    ob= BaseTestClass()
    ob.userLogin()
    obj1= CustomRoleCountVerification()
    obj1.mainCountVerificationForCustomRoles() 
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        