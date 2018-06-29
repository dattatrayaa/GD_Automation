'''
Created on 23-Feb-2018

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
from BaseTestClass import projectPath

class APIBasicInformationValidData:
    
    def userCreationWithValidData(self):
        print "Reading data from excel sheet"
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        sheet1=book.sheet_by_name('API testing')
        print("Fetching the LastName from Excel Sheet\n")
        #Read from Excel to search
        cell1 = sheet1.cell(1,1)
        searchlastName = cell1.value
        #Clicking on Admin Menu from Grovo Application
        wait=WebDriverWait(driver,80)
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/a")))
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/a").click()   
            
        wait.until(EC.visibility_of_element_located((By.ID,"search-users")))
        driver.find_element_by_id("search-users").send_keys(searchlastName)
        #To click on FirstName link
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/div/div[4]/table/tbody/tr/td[2]/a")))
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[2]/div/div/div[4]/table/tbody/tr/td[2]/a").click()
        #To verify FirstName field 
        print"Verify FirstName field"
        wait.until(EC.visibility_of_element_located((By.ID,"create-edit-user-search-firstName")))
        firstNamelocator=driver.find_element_by_id("create-edit-user-search-firstName")
        firstName =firstNamelocator.get_attribute("value") 
        if not firstName:
            print"FirstName field is empty"
        else:
            print"FirstName is present :" +firstName
        #To verify LastName field 
        print"Verify LastName field"  
        wait=WebDriverWait(driver,80)
        lastNamelocator =driver.find_element_by_id("create-edit-user-search-lastName")
        lastName=lastNamelocator.get_attribute("value")
        if not lastName:
            print"LastName field is empty"
        else:
            print"LastName is present : "+lastName
        #To verify Email field 
        print"Verify Email field"  
        wait=WebDriverWait(driver,80)
        emaillocator =driver.find_element_by_id("create-edit-user-search-username")
        global email
        email =emaillocator.get_attribute("value")
        if not email:
            print"Email field is empty"
        else:
            print"Email is present : "+email
        #To verify Employee ID field 
        print"Verify Employee ID field"  
        wait=WebDriverWait(driver,80)
        employeeidlocator =driver.find_element_by_id("create-edit-user-search-employeeId")
        employeeid=employeeidlocator.get_attribute("value")
        if not employeeid:
            print"Employee ID field is empty"
        else:
            print"Employee ID is present : "+employeeid
        #LogOut function     
        wait=WebDriverWait(driver,80)       
        driver.find_element_by_xpath(".//*[@id='content']/div/div[1]/div/nav/div[2]/a/span[3]").click()
        print "Clicked on SignOut Dropdown"
        driver.find_element_by_xpath(".//*[@id='content']/div/div[1]/div[2]/div[2]/a").click()
        print "Clicked on signOut Button"
        wait.until(EC.visibility_of_element_located((By.ID,"username")))
    def Logincreateuser(self):    
        print "Reading data from excel sheet"
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        sheet1=book.sheet_by_name('API testing')
        cell2 = sheet1.cell(1,2)
        Currentpassword = cell2.value
        cell3 = sheet1.cell(1,3)
        Newpassword = cell3.value
        wait=WebDriverWait(driver, 80)
        print "Grovo Sign-In page is displayed"
        print "Enter User name"
        driver.find_element_by_id("username").send_keys(email) 
        print "Enter Password"
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
        element.send_keys(Currentpassword)
        element.send_keys(Keys.TAB)
        print "Clicking on Sign_In button"
        driver.find_element_by_xpath("//*[@id='submitButton']").click()
        wait.until(EC.visibility_of_element_located((By.ID,"currentPassword")))
        driver.find_element_by_id("currentPassword").send_keys(Currentpassword)
        print "Current Password is entered :"+Currentpassword
        driver.find_element_by_id("newPassword").send_keys(Newpassword)
        print "New Password is entered :"+Newpassword
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div/div/div[2]/div[1]/div[2]/button")))
        driver.find_element_by_xpath("html/body/div[2]/div/div/div[2]/div[1]/div[2]/button").click()
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[1]/div/nav/div[1]/a[2]/span")))
        print "Home Page is Loaded"
        expectedresult = "Home"
        expectedresult1="Library"
        actualresult = driver.find_element_by_xpath(".//*[@id='content']/div/div[1]/div/nav/div[1]/a[2]/span").text
        actualresult1 = driver.find_element_by_xpath(".//*[@id='content']/div/div[1]/div/nav/div[1]/a[3]/span").text
        if(expectedresult == actualresult):
            if(expectedresult1==actualresult1):
                print"User is able to login and Dashboard is displayed.."
        else:
            print"User not able to login.."
            raise Exception
            print Exception    
        wait=WebDriverWait(driver, 80)
        print "Sign out "
        ele =driver.find_element_by_xpath(".//*[@id='content']/div/div[1]/div[1]/nav/div[2]/a/span[3]")
        driver.execute_script('arguments[0].click()',ele)
        elem=driver.find_element_by_xpath("html/body/div/div/div[1]/div[2]/div[2]/a")
        driver.execute_script('arguments[0].click()',elem)
        
    def againuserLogin(self):
        
        print "Reading data from excel sheet"
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        
        # print number of sheets
        print("Number of WorkSheets :")
        print book.nsheets
    
        # print sheet names
        #print("Name of WorkSheets :")
        #print book.sheet_names()
        
        # get the first worksheet
        first_sheet = book.sheet_by_name('Login_Credentials')
        
        # read a row
        #print("First Row Data in 1st WorkSheet :")
        #print first_sheet.row_values(0)
        
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
        
        print "Successfully Loged Into Grovo Application"
    
        
    def BasicInformationValidData(self):
        try:
            obj=APIBasicInformationValidData()
            obj.userCreationWithValidData()
            obj.Logincreateuser()
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
    obj1= APIBasicInformationValidData()
    obj1.userCreationWithValidData()
    obj1.Logincreateuser()
    obj1.againuserLogin()
   
    print "Test executed successfully"