'''
Created on 26-Mar-2018

@author: geethukn
'''

from operator import contains
import os.path

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import wait, expected_conditions as EC
from selenium.webdriver.support.select import Select
import xlrd

from BaseTestClass import BaseTestClass
from BaseTestClass import WebDriverWait
from BaseTestClass import driver


class APIUserCreationwithBlankEmail:
    
    def userCreationwithBlankEmail(self):
        print "Reading data from excel sheet"
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        sheet1=book.sheet_by_name('API testing')
        print("Fetching the LastName from Excel Sheet\n")
        #Read from Excel to search
        cell1 = sheet1.cell(24,1)
        searchlastName = cell1.value
        #Clicking on Admin Menu from Grovo Application
        wait=WebDriverWait(driver,90)
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/a")))
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/a").click()   
        wait.until(EC.visibility_of_element_located((By.ID,"search-users")))
        driver.find_element_by_id("search-users").send_keys(searchlastName)
        #Verify the search result
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/div/div[3]")))
        search = driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[2]/div/div/div[3]")
        if(search.is_displayed()):
            print "No results were found for "+"\""+searchlastName+"\""+"."
        else:
            print"Search Result found"
            raise Exception
            print Exception
        #Expectedresult = "0 users"+"match your search "+"\""+searchlastName+"\""+""
        #Actualresult =driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[2]/div/div/div[2]/h3").text
        
        #if(Expectedresult == Actualresult):
            #print"No results were found for "+"\""+searchlastName+"\""+"."
        #else:
            #print"Search Result found"
              
        driver.find_element_by_xpath(".//*[@id='content']/div/div[1]/div/nav/div[2]/a/span[3]").click()
        print "Clicked on SignOut Dropdown"
        driver.find_element_by_xpath(".//*[@id='content']/div/div[1]/div[2]/div[2]/a").click()
        print "Clicked on signOut Button"
        #wait.until(EC.visibility_of_element_located((By.ID,"username"))) 
               
    def againuserLogin(self):
        
        print "Reading data from excel sheet"
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        
        # print number of sheets
        print("Number of WorkSheets :")
        print book.nsheets
    
        first_sheet = book.sheet_by_name('Login_Credentials')
        
        print("Fetching the URL, username and password from Excel Sheet\n")
        # read a cell
        cell = first_sheet.cell(1,1)
        url = cell.value
        print url
        
        cell = first_sheet.cell(3,1)
        username = cell.value
        print username
        
        cell = first_sheet.cell(3,2)
        password = cell.value
        print password  
        
        driver.get(url)
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
        if driver.title == "Grovo":
            print("Grovo Application URL Opened")
        else:
            raise Exception.message

        print "Grovo Sign-In page is displayed"
        
        print "Entering User name"
        driver.find_element_by_xpath(".//*[@id='username']").send_keys(username)
       
        print "Entering Password"
        element.send_keys(password)
        
        element.send_keys(Keys.TAB)
        print "Clicking on Sign_In button"
        driver.find_element_by_xpath("//*[@id='submitButton']").click()
        
        print "Successfully Logged Into Grovo Application"
    
        
    def UserCreationwithBlankEmailId(self):
        try:
            obj=APIUserCreationwithBlankEmail()
            obj.userCreationwithBlankEmail()
            obj.againuserLogin() 
            
        finally:
            book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
            second_sheet = book.sheet_by_name('Login_Credentials')
            cell = second_sheet.cell(1,1)
            url = cell.value
            driver.get(url) 
            
            
            
if __name__ == '__main__':
    ob= BaseTestClass()
    ob.UserLogin()
    obj1= APIUserCreationwithBlankEmail()
    obj1.userCreationwithBlankEmail()
    obj1.againuserLogin()
   
    print "Test executed successfully"