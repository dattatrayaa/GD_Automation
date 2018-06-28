'''
Created on 23-Apr-2018

@author: Sheethu C
'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xlrd

from BaseTestClass import driver

class CreateUserXpath:
    
    def adminSideMenu(self):
        time.sleep(2)
        return "(//a[@href='/admin/users'])[1]"
    def usersideMenu(self):
        time.sleep(3)
        return "html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/div/ul/li[1]"
    
    def addEditUserButton(self):
        time.sleep(3)
        return "html/body/div/div/div[3]/div[2]/div/header/div/div/a"
    
    def addAnIndividualUser(self):
        time.sleep(3)
        return "html/body/div/div/div[3]/div[2]/div/header/div"
    def addUserPageWait(self):
        time.sleep(3)
        return "html/body/div/div/div[3]/div[2]/div/header"
    def firstName(self):
        time.sleep(3)
        return "create-edit-user-search-firstName"
    def lastName(self):
        time.sleep(3)
        return "create-edit-user-search-lastName"
    def email(self):
        time.sleep(3)
        return "create-edit-user-search-username"
    
    def employeId(self):
        time.sleep(3)
        return "create-edit-user-search-employeeId"
    
    def inheritedRole(self):
        time.sleep(3)
        return "html/body/div/div/div[3]/div[2]/div/div[2]/div/div/div[1]/div[6]/div"
    
    def directRoleDisplay(self):
        time.sleep(3)
        return "html/body/div/div/div[3]/div[2]/div/div[2]/div/div/div[1]/div[5]/div/div/div"
    
    def directCreatorRole(self):
        time.sleep(3)
        return "//div[@role='option' and .='Creator']"
    def directLearnAdminRole(self):
        time.sleep(3)
        return "//div[@role='option' and .='Learning Administrator']"
    
    def directMasterAdminRole(self):
        time.sleep(3)
        return "//div[@role='option' and .='Master Administrator']"
    
    def password(self):
        time.sleep(3)
        return "create-edit-user-search-new-password"
    
    def addButton(self):
        time.sleep(3)
        return "//button[.='Add']"
    
    def saveButton(self):
        time.sleep(3)
        return "//button[.='Save']"
    
    def userPageWait(self):
        time.sleep(3)
        return "html/body/div/div/div[3]/div[2]/div/header/h1"
    def searchInGrid(self,Email,FirstName):
        time.sleep(3)
        wait=WebDriverWait(driver, 50)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[2]/div/header/h1")))
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[1]/div/div[3]/div[2]/div/div/div[4]/table/tbody/tr[1]/td[1]")))
        driver.find_element_by_id("search-users").send_keys(FirstName)
        time.sleep(4)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//table/tbody/tr/td[.='"+Email+"']/../td[2]/a")))
        ele =driver.find_element_by_xpath("//table/tbody/tr/td[.='"+Email+"']/../td[2]/a").text
        if(ele==FirstName):
            print("Created User Verified")
        else:
            print ""
            raise Exception  
       
    def profileClick(self):
        time.sleep(3)
        return ".//*[@id='content']/div/div[1]/div/nav/div[2]/a/span[3]"
    
    def signOut(self):
        time.sleep(3)
        return ".//*[@id='content']/div/div[1]/div[2]/div[2]/a"
    
    def loginUserName(self):
        time.sleep(3)
        return "username"
    
    def loginPassword(self):
        time.sleep(3)
        return "password"
    def submitButton(self):
        time.sleep(3)
        return "submitButton"
    
    def currentPassword(self):
        time.sleep(3)
        return "currentPassword"
    def newPassword(self):
        time.sleep(3)
        return "newPassword"
    def newSubmit(self):
        time.sleep(3)
        return "html/body/div[2]/div/div/div[2]/div[1]/div[2]/button"
    
    def homepageSearchWait(self):
        time.sleep(3)
        return "global-header-search"
    
    def homeicon(self):
        time.sleep(3)
        return "html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[1]"
    def libraryicon(self):
        time.sleep(3)
        return "html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[2]"
    def createicon(self):
        time.sleep(3)
        return "html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[3]"
    def campaignicon(self):
        time.sleep(3)
        return "html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[4]"

    def reportsicon(self):
        time.sleep(3)
        return "html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[5]"

    def adminicon(self):
        time.sleep(3)
        return "html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]"
    def usericon(self):
        time.sleep(3)
        return "html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/div/ul/li[1]/a"
    def groupicon(self):
        time.sleep(3)
        return "html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/div/ul/li[1]/a"
    def rolesicon(self):
        time.sleep(3)
        return "html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/div/ul/li[3]/a"
    def attributeicon(self):
        time.sleep(3)
        return "html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/div/ul/li[4]/a"
    def tagicon(self):
        time.sleep(3)
        return "html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/div/ul/li[5]/a"
    def contentmanagericon(self):
        time.sleep(3)
        return "html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/div/ul/li[6]/a"
    def integrationicon(self):
        time.sleep(3)
        return "html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/div/ul/li[7]/a"
    def brandingicon(self):
        time.sleep(3)
        return "html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/div/ul/li[8]/a"

    def createUserSignout(self):
        time.sleep(3)
        return ".//*[@id='content']/div/div[1]/div[1]/nav/div[2]/a/span[3]"
    
    def createlessoncombo(self):
        time.sleep(3)
        return "html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[3]"
    
    def VerifyLearnersideMenu(self):
        time.sleep(3)
        return "//a[@href='/admin/tags']"
    
    def adminIconforLearnAdmin(self):
        time.sleep(3)
        return "html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[5]"
    
    def tagIconforLearnAdmin(self):
        time.sleep(3)
        return "html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[5]/div/ul/li[1]/a"
    
    def contentIconforLearnAdmin(self):
        time.sleep(3)
        return "html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[5]/div/ul/li[2]/a"
    
    def learnerHome(self):
        time.sleep(3)
        return ".//*[@id='content']/div/div[1]/div/nav/div[1]/a[2]/span"
    def learnerLibrary(self):
        time.sleep(3)
        return ".//*[@id='content']/div/div[1]/div/nav/div[1]/a[3]/span"