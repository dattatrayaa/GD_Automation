'''
Created on 22-Feb-2018

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

from BaseTestClass import driver
from CreateUserXpath import CreateUserXpath
from BaseTestClass import projectPath


class UserCreateLearnerAdministrator():
    
    
    def createLearnerAdminUser(self):
        createuser =CreateUserXpath()
        print "Reading data from excel sheet"
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        first_sheet = book.sheet_by_name('CreateuserfromUI')
        print("Fetching the First Name, LastName,Email,EmployeeId and password from Excel Sheet\n")
        # read a cell
        cell = first_sheet.cell(4,1)
        FirstName = cell.value
        cell = first_sheet.cell(4,2)
        LastName = cell.value
        cell = first_sheet.cell(4,3)
        Email = cell.value
        
        cell = first_sheet.cell(4,4)
        EmployeeId = cell.value
        
        cell = first_sheet.cell(4,5)
        DirectRole = cell.value
        
        cell = first_sheet.cell(4,6)
        Password = cell.value
        
        wait=WebDriverWait(driver, 60)
        driver.refresh()
        wait.until(EC.visibility_of_element_located((By.XPATH,createuser.adminSideMenu())))
        driver.find_element_by_xpath(createuser.adminSideMenu()).click()
        print "Clicked on admin icon"
        wait.until(EC.visibility_of_element_located((By.XPATH,createuser.usersideMenu())))
        driver.find_element_by_xpath(createuser.usersideMenu()).click()
        print "Clicked on Admin"
       
        wait.until(EC.visibility_of_element_located((By.XPATH,createuser.addEditUserButton())))
        wait.until(EC.element_to_be_clickable((By.XPATH,createuser.addEditUserButton())))
        driver.find_element_by_xpath(createuser.addEditUserButton()).click()
        print "Clicked on Add or editUser"
        wait.until(EC.visibility_of_element_located((By.XPATH,createuser.addAnIndividualUser())))
        wait.until(EC.element_to_be_clickable((By.XPATH,createuser.addAnIndividualUser())))
        driver.find_element_by_xpath(createuser.addAnIndividualUser()).click()
        print "Clicked on Add An individual User"
        
        wait.until(EC.visibility_of_element_located((By.XPATH,createuser.addUserPageWait())))
        print "Verifying Add user Page"

        if driver.find_element_by_xpath(createuser.addUserPageWait()).is_displayed():
            print("Add user Page is displayed")
        else:
            print ""
            raise Exception
        print "Verifying First Name field"
        wait.until(EC.visibility_of_element_located((By.ID,createuser.firstName())))
        if driver.find_element_by_id(createuser.firstName()).is_displayed():
            print(" First Name field displayed")
        else:
            print ""
            raise Exception
        driver.find_element_by_id(createuser.firstName()).send_keys(FirstName)
        print "FirstName is Entered ::"+FirstName
        print "Last NAme verifying"
        if driver.find_element_by_id(createuser.lastName()).is_displayed():
            print(" Last Name field displayed")
        else:
            print ""
            raise Exception
        driver.find_element_by_id(createuser.lastName()).send_keys(LastName)
        print "Last Name is Entered ::"+LastName
        print "Email verifying"
        if driver.find_element_by_id(createuser.email()).is_displayed():
            print("Email field displayed")
        else:
            print ""
            raise Exception
        driver.find_element_by_id(createuser.email()).send_keys(Email)
        print "Email is Entered ::"+Email
        
        print "Employee ID verifying"
        if driver.find_element_by_id(createuser.employeId()).is_displayed():
            print("Employee ID field displayed")
        else:
            print ""
            raise Exception
        driver.find_element_by_id(createuser.employeId()).send_keys(EmployeeId)
        print "Employee ID  is Entered ::"+EmployeeId
        print "Inherited Role Verifying"
        if driver.find_element_by_xpath(createuser.inheritedRole()).is_displayed():
            print("Inherited Role field displayed")
        else:
            print ""
            raise Exception
        
        print "Selecting Learning Administrator in Direct Roles"

        dd1=driver.find_element_by_xpath(createuser.directRoleDisplay())
        webdriver.ActionChains(driver).move_to_element(dd1).click().send_keys(DirectRole).perform()
        wait.until(EC.visibility_of_element_located((By.XPATH,createuser.directLearnAdminRole())))
        ele =driver.find_element_by_xpath(createuser.directLearnAdminRole())
        
        webdriver.ActionChains(driver).move_to_element(ele).click().perform()
        
        print "Password Field is Verifying"
        if driver.find_element_by_id(createuser.password()).is_displayed():
            print("Password field displayed")
        else:
            print ""
            raise Exception
        driver.find_element_by_id(createuser.password()).send_keys(Password)
        print "Password is Entered ::"+Password
        
        wait.until(EC.visibility_of_element_located((By.XPATH,createuser.addButton())))
        wait.until(EC.element_to_be_clickable((By.XPATH,createuser.addButton())))
        driver.find_element_by_xpath(createuser.addButton()).click()
        print "Clicked on add button"
        wait.until(EC.visibility_of_element_located((By.XPATH,createuser.saveButton())))
        driver.find_element_by_xpath(createuser.saveButton()).click()
        print "Clicked on Save"
        wait.until(EC.visibility_of_element_located((By.XPATH,createuser.userPageWait())))
        print "Searching for the Created User"
        createuser.searchInGrid(Email,FirstName)
        driver.find_element_by_xpath(createuser.profileClick()).click()
        print "Clicked on Account"
        driver.find_element_by_xpath(createuser.signOut()).click()
        print "Clicked on signOut Button"
        wait.until(EC.visibility_of_element_located((By.ID,createuser.loginUserName())))
        time.sleep(4)
    def createLearnerAdminLogin(self):
        createuser =CreateUserXpath()
        print "Reading data from excel sheet"
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        first_sheet = book.sheet_by_name('CreateuserfromUI')
        print("Fetching the First Name, LastName,Email,EmployeeId and password from Excel Sheet\n")
        # read a cell
        
        cell = first_sheet.cell(4,3)
        Email = cell.value
        print Email
        
        cell = first_sheet.cell(4,6)
        Password = cell.value
        print Password
        
        cell = first_sheet.cell(4,7)
        NewPassword = cell.value
        print NewPassword
        
        
        
        wait=WebDriverWait(driver, 60)
        print "Grovo Sign-In page is displayed"
        
        print "Entering User name"
        driver.find_element_by_id(createuser.loginUserName()).send_keys(Email)
       
        print "Entering Password"
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,createuser.loginPassword())))
        element.send_keys(Password)
        
        element.send_keys(Keys.TAB)
        print "Clicking on Sign_In button"
        driver.find_element_by_id(createuser.submitButton()).click()
        wait.until(EC.visibility_of_element_located((By.ID,createuser.currentPassword())))
        driver.find_element_by_id(createuser.currentPassword()).send_keys(Password)
        print "Current Password is entered :"+Password
        driver.find_element_by_id(createuser.newPassword()).send_keys(NewPassword)
        print "New Password is entered :"+NewPassword
        wait.until(EC.visibility_of_element_located((By.XPATH,createuser.newSubmit())))
        driver.find_element_by_xpath(createuser.newSubmit()).click()
        wait.until(EC.visibility_of_element_located((By.ID,createuser.homepageSearchWait())))
        #wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[3]/div[1]/div/nav/div/div[4]")))
        print "Home Page is Loaded"
        time.sleep(4)
        print "waiting For Admin"
        Admin =driver.find_element_by_xpath(createuser.VerifyLearnersideMenu())
        driver.execute_script('arguments[0].click()',Admin)
        print "Clicked on Admin"
        wait.until(EC.visibility_of_element_located((By.XPATH,createuser.contentIconforLearnAdmin())))
        print "Home Page is Loaded"
        
        #driver.find_element_by_xpath("html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/a").click()
        wait.until(EC.visibility_of_element_located((By.XPATH,createuser.homeicon())))
        Home =driver.find_element_by_xpath(createuser.homeicon())
        Library = driver.find_element_by_xpath(createuser.libraryicon())
        Create = driver.find_element_by_xpath(createuser.createicon())
        campaign = driver.find_element_by_xpath(createuser.campaignicon())
        Admin = driver.find_element_by_xpath(createuser.adminIconforLearnAdmin())
        print "main found"
        Tags = driver.find_element_by_xpath(createuser.tagIconforLearnAdmin())
        print "tags"+Tags.text
        ContentManager =driver.find_element_by_xpath(createuser.contentIconforLearnAdmin())
        print "content"
        if ((Home.is_displayed()) and (Library.is_displayed()) and (Create.is_displayed()) and (campaign.is_displayed()) and (Admin.is_displayed()) and (Tags.is_displayed()) and (ContentManager.is_displayed())):
           
            print "User with Creator Role is able to login and HOME,LIBRARY,CREATE and CAMPAIGN is displaying.."
                        
        else:
            print"Home page not displayed"
            raise Exception 
        
        print "Sign out "
        ele =driver.find_element_by_xpath(createuser.profileClick())
        driver.execute_script('arguments[0].click()',ele)
        elem=driver.find_element_by_xpath(createuser.signOut())
        driver.execute_script('arguments[0].click()',elem)
        wait.until(EC.visibility_of_element_located((By.ID,createuser.loginUserName())))
    def againuserLogin(self):
        createuser =CreateUserXpath()
        print "Reading data from excel sheet"
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        
        first_sheet = book.sheet_by_name('Login_Credentials')
     
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
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,createuser.loginUserName())))
        if driver.title == "Grovo":
            print("Grovo Application URL Opened")
        else:
            raise Exception.message

        print "Grovo Sign-In page is displayed"
        
        print "Entering User name"
        driver.find_element_by_id(createuser.loginUserName()).send_keys(username)
       
        print "Entering Password"
        element.send_keys(password)
        
        element.send_keys(Keys.TAB)
        print "Clicking on Sign_In button"
        driver.find_element_by_id(createuser.submitButton()).click()
        
        print "Successfully Loged Into Grovo Application"
        time.sleep(5)
           
        #again login   
    
    def createLearnerAdminUserAndValidation(self):
        try :
            ob =UserCreateLearnerAdministrator()
            ob.createLearnerAdminUser()
            ob.createLearnerAdminLogin()  
            ob.againuserLogin()
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


       
