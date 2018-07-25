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
from CreateUserXpath import CreateUserXpath
from BaseTestClass import projectPath
class UserLearnerCountVerification():
    def learnerCount(self):
        user=CreateUserXpath()
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,user.adminSideMenu())))
        driver.find_element_by_xpath(user.adminSideMenu()).click()
        print "Clicked on Admin icon"
        wait.until(EC.visibility_of_element_located((By.XPATH,user.rolesidemenu())))
        driver.find_element_by_xpath(user.rolesidemenu()).click()
        print "clicked on roles page"
        #waiting for the learner role
        wait.until(EC.visibility_of_element_located((By.XPATH,user.learnerRole())))
        time.sleep(6)
        wait.until(EC.visibility_of_element_located((By.XPATH,user.learnerRolecount())))
        #Checking the count of Role learner in roles page
        rolecount= driver.find_element_by_xpath(user.learnerRolecount()).text
        #navigating to the Users Page
        driver.refresh()
        wait.until(EC.visibility_of_element_located((By.XPATH,user.adminSideMenu())))
        driver.find_element_by_xpath(user.adminSideMenu()).click()
        #checking users count in users page
        wait.until(EC.visibility_of_element_located((By.XPATH,user.usersideMenu())))
        driver.find_element_by_xpath(user.usersideMenu()).click()
        wait.until(EC.visibility_of_element_located((By.XPATH,user.userscount())))
        user =driver.find_element_by_xpath(user.userscount()).text
        time.sleep(4)
        userc =(user.split(' '))
        usercount=userc[0]
        print usercount
        time.sleep(4)
        print "Navigate to roles page"
        #checking the count
        if usercount == rolecount:
            print "Number of roles for Learners and Number of Learners users are matching"
        else:
            print "Number of roles for Learners and Number of Learners users are not matching"
            raise Exception
    def mainCountVerification(self):
        try :
            ob =UserLearnerCountVerification()
            ob.learnerCount()
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
    obj1= UserLearnerCountVerification()
    obj1.mainCountVerification() 
    
    
        
        