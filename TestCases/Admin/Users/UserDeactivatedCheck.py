'''
Created on 11-Jun-2018

@author: dattatraya
'''
import traceback

from BaseTestClass import BaseTestClass
from BaseTestClass import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from ExcelFunctions import ExcelFunctions
from UsersPageElements import UsersPageElements
from CreateLearnerNew import CreateLearner


class UserDeactivatedCheck:
    
    
    def CheckUserDeactivated(self,FirstName):
        
        user=UsersPageElements()
        wait=WebDriverWait(driver, 60)
        driver.refresh()
        
        user.AdminFromSideMenuClick()
        print "CLicked on Admin Menu"
        
        user.UsersFromSideMenuClick()
        print "Clicked On Users from Side Menu"
        
        wait.until(EC.visibility_of_element_located((By.XPATH,user.HeaderTextUsersPageXpath())))
        
        print "Search for user"
        user.SearchForUserInGrid(FirstName)
        
        
        print "Clicking on Users check box"
        user.checkboxSelectInUsersGrid(1)
        
        print "clicking on Deactivate User button displayed at bottom popup"
        user.deactivateLinkAtBottom()
        
        user.deactivateButtonFromPopup()
        print "Clicked on Deactivate button from pop up"
        
    def CheckUserIsableTOLogin(self,Email,Password):
        print "\n-Checking whether user is able to login to the application-"
        
        wait=WebDriverWait(driver, 60)
        driver.refresh()
        
        print "Logging out"
        print "Clicking on Username Dropdown"
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[1]/div[1]/nav/div[2]/a/span[3]")))
        ele =driver.find_element_by_xpath(".//*[@id='content']/div/div[1]/div[1]/nav/div[2]/a/span[3]")
        driver.execute_script('arguments[0].click()',ele)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[1]/div[2]/div[2]/a")))
        elem=driver.find_element_by_xpath("html/body/div/div/div[1]/div[2]/div[2]/a")
        driver.execute_script('arguments[0].click()',elem)
        
        print "Clicked on Sign Out option"
        
        wait.until(EC.presence_of_element_located((By.ID, "password")))
        
        element = wait.until(EC.presence_of_element_located((By.ID, "password")))
        if driver.title == "Grovo":
            print("Grovo Application URL Opened")
        else:
            raise Exception.message

        print "Grovo Sign-In page is displayed"
        
        print "Entering User name"
        driver.find_element_by_xpath(".//*[@id='username']").send_keys(Email)
       
        print "Entering Password"
        element.send_keys(Password)
        
        element.send_keys(Keys.TAB)
        print "Clicking on Sign_In button"
        driver.find_element_by_xpath("//*[@id='submitButton']").click()
        
        print "Verify Validation error message is displayed"
        msg=wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div/div[2]/div/div[1]/div")))
        
        if msg.text=="It looks like your account is no longer active.":
            print "Message '"+msg.text+"' is displayed"
        else:
            raise Exception('Validation message is not displayed')
        
        btc=BaseTestClass()
        btc.UserLogin()
    
    def CheckingUserInDeactivatedList(self,FirstName,LastName):
        user=UsersPageElements()
        wait=WebDriverWait(driver, 60)
        driver.refresh()
        
        user.AdminFromSideMenuClick()
        print "CLicked on Admin Menu"
        
        user.UsersFromSideMenuClick()
        print "Clicked On Users from Side Menu"
        
        wait.until(EC.visibility_of_element_located((By.XPATH,user.HeaderTextUsersPageXpath())))
        
        print "Clicking on Deactivated Users list"
        user.seeDeactivatedUsersLink()
        
        print "Searching deactivated User"
        user.searchDeactivatedUsers(FirstName)
        
        print "Verifying user is displayed in Grid or not"
        user.checkDeactivatedUser(LastName)
        
        print "Hence verified user is displayed in Deactivated users list"
        
        
        
        
        
    def UserDeactivateMain(self):
        
        exc=ExcelFunctions()
        
        exc.OpenExcelFile('TestData.xlsx')
        
        exc.OpenSheet('UsersPage')
        
        FirstName=exc.getCellData(17, 1)
        
        
        FirstNameId = FirstName.split("_")
        emp = FirstNameId[0]+"_"
        ids = FirstNameId[1]
        empId = int(ids)+1
        FirstNameUpdated= emp+str(empId)
        
        LastName = exc.getCellData(18, 1)
        
        LastNameID = LastName.split("_")
        emp = LastNameID[0]+"_"
        ids = LastNameID[1]
        empId = int(ids)+1
        LastNameUpdated= emp+str(empId)
        
        
        
        Email = exc.getCellData(19, 1)
        
        EmailId = Email.split("_")
        emp = EmailId[0]+"_"
        ids = EmailId[1]
        remaining="_"+EmailId[2]
        empId = int(ids)+1
        EmailIdUpdated= emp+str(empId)+remaining
        
        EmployeeId = exc.getCellData(20, 1)
        
        Employee = EmployeeId.split("_")
        emp = Employee[0]+"_"
        ids = Employee[1]
        empId = int(ids)+1
        EmployeeIdUpdated= emp+str(empId)
        
        Password = exc.getCellData(21, 1)
        
        NewPassword=exc.getCellData(21, 1)
        
        
        exc.OpenExcelFile('TestData.xlsx')
        exc.OpenSheet("Login_Credentials")
        url=exc.getCellData(1, 1)
        username=exc.getCellData(3, 1)
        password=exc.getCellData(3, 2)
        
        
        #updating user values
        exc.updateExcelFileName('TestData.xlsx')
        exc.updateExcelSheetName('UsersPage')
        
        exc.updateCellData(FirstNameUpdated, 18, 2)
        exc.updateCellData(LastNameUpdated, 19, 2)
        exc.updateCellData(EmailIdUpdated, 20, 2)
        exc.updateCellData(EmployeeIdUpdated,21, 2)
        
        exc.SaveExcelFile('TestData.xlsx')
        
        
        
        
        try:
            
          
            t=UserDeactivatedCheck()
            print "\nCreating New User\n"
            
            Cr=CreateLearner()
            Cr.createNewLearnerMain(FirstName, LastName, Email, EmployeeId, Password, NewPassword, url, username, password)  
            
            print "\nDeactivating User through checkbox selection\n"
            t.CheckUserDeactivated(FirstName)
            
            print "\nCheck user displayed in Deactivated list\n"
            t.CheckingUserInDeactivatedList(FirstName, LastName)
            
            print "\nChecking Validation error message displayed while logging in\n"
            t.CheckUserIsableTOLogin(Email, Password)
            print "\nTest Execution completed"
            
            
        except Exception as e:
            traceback.print_exc()
            print (e)
            raise Exception   
          
        finally:
            exc.OpenSheet('Login_Credentials')  
            url = exc.getCellData(1,1)
            driver.get(url)
            try:
                WebDriverWait(driver, 5).until(EC.alert_is_present())

                alert = driver.switch_to.alert
                alert.accept()
                print("alert accepted")
            except Exception:
                print("no alert")
                
                
            
            
        
        
        
if __name__=='__main__':
    
    btc=BaseTestClass()
    btc.UserLogin() 
    
    dec=UserDeactivatedCheck()
    dec.UserDeactivateMain()

        
        
        
        
        
        
        
        
        
        
        
        
        
