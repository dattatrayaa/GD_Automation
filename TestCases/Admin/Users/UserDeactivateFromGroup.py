'''
Created on 15-Jun-2018

@author: OptisLabs
'''
import time
import traceback

from BaseTestClass import BaseTestClass
from BaseTestClass import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from GroupsPageElements import GroupsPageElements
from UsersPageElements import UsersPageElements
from ExcelFunctions import ExcelFunctions


class UserDeactivateFromGroup:
    
    def create(self,FirstName,LastName,Email,EmployeeId,Password):
        wait=WebDriverWait(driver, 120)
        driver.refresh()
        user=UsersPageElements()
        
        user.AdminFromSideMenuClick()
        print "Clicked on Admin"
        
        user.UsersFromSideMenuClick()
        print "clicked on Users"
        
        user.AddOrEditUserButtonClick()
        print "Clicked on Add or editUser"

        
        user.AddAnIndividualUserButtonClick()
        print "Clicked on Add An individual User"
        time.sleep(1)
        wait.until(EC.visibility_of_element_located((By.XPATH,user.AddUserPageHeaderXpath())))
        
        print "Verifying Add user Page"
        if driver.find_element_by_xpath(user.AddUserPageHeaderXpath()).is_displayed():
            print("Add user Page is displayed")
        else:
            print ""
            raise Exception
        
        
        print "Verifying First Name field"
        fn=wait.until(EC.visibility_of_element_located((By.ID,user.FirstNameFieldID())))
        if fn.is_displayed():
            print(" First Name field displayed")
        else:
            print ""
            raise Exception
        fn.send_keys(FirstName)
        print "FirstName is Entered ::"+FirstName
        
        
        
        print "Last NAme verifying"
        if driver.find_element_by_id(user.LastNameFieldID()).is_displayed():
            print(" Last Name field displayed")
        else:
            print ""
            raise Exception
        driver.find_element_by_id(user.LastNameFieldID()).send_keys(LastName)
        print "Last Name is Entered ::"+LastName
        
        
        print "Email verifying"
        if driver.find_element_by_id(user.EmailFieldID()).is_displayed():
            print("Email field displayed")
        else:
            print ""
            raise Exception
        driver.find_element_by_id(user.EmailFieldID()).send_keys(Email)
        print "Email is Entered ::"+Email
        
        
        print "Employee ID verifying"
        if driver.find_element_by_id(user.EmployeeIDFieldID()).is_displayed():
            print("Employee ID field displayed")
        else:
            print ""
            raise Exception
        driver.find_element_by_id(user.EmployeeIDFieldID()).send_keys(EmployeeId)
        print "Employee ID  is Entered ::"+EmployeeId
        
        
        
        print "Inherited Role Verifying"
        if driver.find_element_by_xpath(user.InHeritedRoleFieldXpath()).is_displayed():
            print("Inherited Role field displayed")
        else:
            print ""
            raise Exception
        
        print "Password Field is Verifying"
        if driver.find_element_by_id(user.PassWordFieldID()).is_displayed():
            print("Password field displayed")
        else:
            print ""
            raise Exception
        driver.find_element_by_id(user.PassWordFieldID()).send_keys(Password)
        print "Password is Entered ::"+Password
        
        
        user.AddButtonClick()
        print "Clicked on add button"
        time.sleep(2)

        user.SaveButtonClick()        
        print "Clicked on Save"
        
        wait.until(EC.visibility_of_element_located((By.XPATH,user.UsersPageHeader())))
        
        
        print "Searching for the Created User"
        user.SearchForUserInGrid(FirstName)
        
        
        user.CheckUserDisplayedInGrid(FirstName) 
  
    
    
    def groupCreateForCampaign(self,groupName,FirstName,FirstName1):
        
        driver.refresh()
        wait=WebDriverWait(driver, 120)
        
        group=GroupsPageElements()
        
        group.adminSideMenuUnexpanded()
        print "Clicked on admin icon"
         
        group.groupSideMenuExpanded()  
        print "Clicked on Group icon"
        
        
        print "Checking Group page is displayed"
        if driver.find_element_by_xpath(group.groupPageHeader()).is_displayed():
            print "Group page is displayed successfully"
        else:
            print "Group page is not displayed"
            raise Exception
        
        
        group.createGroupButton()
        print "Clicked on Create Group button"
        
        group.enteringGroupname(groupName)
        
        print "Group Name entered....."
        
        group.nextButton()
        print "Clicked on Next button"
        
        wait.until(EC.visibility_of_element_located((By.XPATH,group.groupDetailPageHeader())))
        print "Checking group is created"
        
        time.sleep(4)
        headerText=driver.find_element_by_xpath(group.groupDetailPageHeader()).text
        
        if headerText==groupName:
            print "Group created successfully"
            
        else:
            print "Group not created"
            raise Exception
        
        
        print "Adding user to Group by name"
        group.addByNameButton()
        
        group.addByName(FirstName)
        
        group.closeAddByNameTextField()
        
        print "Adding second user"
        group.addByNameButton()
        group.addByName(FirstName1)
        
        print "Verifying user is added to group"
        group.groupAddedInList(FirstName)
        group.groupAddedInList(FirstName1)
        print "Both Users adeed "
        
        
        group.saveButton()
        print "Clicked on Save button"

        group.saveButtonPopup()
        print "Clicked on Save from popup"
        
        
        print "Checking Created Group is displayed in Grid"
        group.groupsLinkFromBreadCrumb()
        
        print "Searching Group"
        group.createdGroupDisplayedInGrid(groupName)
         
        
        driver.refresh()
    
    
    def userDeactivate(self,FirstName):
        
        user=UsersPageElements()
        wait=WebDriverWait(driver, 120)
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
        
    def CheckUserInGroupsPage(self,groupName,FirstName):
        
        driver.refresh()
        wait=WebDriverWait(driver, 120)
        
        group=GroupsPageElements()
        
        group.adminSideMenuUnexpanded()
        print "Clicked on admin icon"
         
        group.groupSideMenuExpanded()  
        print "Clicked on Group icon"
        
        
        print "Checking Group page is displayed"
        if driver.find_element_by_xpath(group.groupPageHeader()).is_displayed():
            print "Group page is displayed successfully"
        else:
            print "Group page is not displayed"
            raise Exception
        
        print "Searching for group in grid"
        wait.until(EC.visibility_of_element_located((By.XPATH,group.searchGroupTextFieldXpath())))
        
        print "Searching Group"
        group.createdGroupDisplayedInGrid(groupName)
        
        driver.find_element_by_xpath(group.groupInGrid(groupName)).click()
        print "Clicked on Group"
        
        print "Checking Deactivated User is displayed in Grid"
        
        
        userInGrid=wait.until(EC.visibility_of_element_located((By.XPATH,group.usersInGridOFUserDetails())))
        
        
        if userInGrid.text!=FirstName:
            print "Deactivated user is not displayed in this group"
        else:
            raise Exception('Deactivated user is still displayed in this group')
        
    
    
    def UserDeactivateFromGroupMain(self):
        
        exc=ExcelFunctions()
        
        exc.OpenExcelFile('TestData.xlsx')
        
        exc.OpenSheet('UsersPage')
        
        FirstName=exc.getCellData(61, 1)
        
        FirstNameId = FirstName.split("_")
        emp = FirstNameId[0]+"_"
        ids = FirstNameId[1]
        empId = int(ids)+1
        FirstNameUpdated= emp+str(empId)
        
        LastName = exc.getCellData(62, 1)
        
        LastNameID = LastName.split("_")
        emp = LastNameID[0]+"_"
        ids = LastNameID[1]
        empId = int(ids)+1
        LastNameUpdated= emp+str(empId)
        
        
        
        Email = exc.getCellData(63, 1)
        
        EmailId = Email.split("_")
        emp = EmailId[0]+"_"
        ids = EmailId[1]
        remaining="_"+EmailId[2]
        empId = int(ids)+1
        EmailIdUpdated= emp+str(empId)+remaining
        
        EmployeeId = exc.getCellData(64, 1)
        
        Employee = EmployeeId.split("_")
        emp = Employee[0]+"_"
        ids = Employee[1]
        empId = int(ids)+1
        EmployeeIdUpdated= emp+str(empId)
        
        Password = exc.getCellData(65, 1)
        
        
        
        FirstName1=exc.getCellData(67, 1)
        
        FirstNameId = FirstName1.split("_")
        emp = FirstNameId[0]+"_"
        ids = FirstNameId[1]
        empId = int(ids)+1
        FirstNameUpdated1= emp+str(empId)
        
        LastName1 = exc.getCellData(68, 1)
        
        LastNameID = LastName1.split("_")
        emp = LastNameID[0]+"_"
        ids = LastNameID[1]
        empId = int(ids)+1
        LastNameUpdated1= emp+str(empId)
        
        
        
        Email1 = exc.getCellData(69, 1)
        
        EmailId = Email1.split("_")
        emp = EmailId[0]+"_"
        ids = EmailId[1]
        remaining="_"+EmailId[2]
        empId = int(ids)+1
        EmailIdUpdated1= emp+str(empId)+remaining
        
        EmployeeId1 = exc.getCellData(70, 1)
        
        Employee = EmployeeId1.split("_")
        emp = Employee[0]+"_"
        ids = Employee[1]
        empId = int(ids)+1
        EmployeeIdUpdated1= emp+str(empId)
        
        
        groupName=exc.getCellData(66, 1)
        groupNameId = groupName.split("_")
        emp = groupNameId[0]+"_"
        ids = groupNameId[1]
        empId = int(ids)+1
        groupNameUpdated= emp+str(empId)
        
        
        
        
        
        exc.OpenExcelFile('TestData.xlsx')
        exc.OpenSheet("Login_Credentials")
        
        url=exc.getCellData(1, 1)
        username=exc.getCellData(3, 1)
        password=exc.getCellData(3, 2)
        
        
        
        
        #updating user values
        exc.updateExcelFileName('TestData.xlsx')
        exc.updateExcelSheetName('UsersPage')
        
        exc.updateCellData(FirstNameUpdated, 62, 2)
        exc.updateCellData(LastNameUpdated, 63, 2)
        exc.updateCellData(EmailIdUpdated, 64, 2)
        exc.updateCellData(EmployeeIdUpdated, 65 , 2)
        
        exc.updateCellData(FirstNameUpdated1, 68, 2)
        exc.updateCellData(LastNameUpdated1, 69, 2)
        exc.updateCellData(EmailIdUpdated1, 70, 2)
        exc.updateCellData(EmployeeIdUpdated1,71, 2)
        exc.updateCellData(groupNameUpdated,67,2)
        exc.SaveExcelFile('TestData.xlsx')
        
        
        
        
        try:
            
          
            t=UserDeactivateFromGroup()
            print "\nCreating New User\n"
            
            t.create(FirstName, LastName, Email, EmployeeId, Password)
            t.create(FirstName1, LastName1, Email1, EmployeeId1, Password)
            
            t.groupCreateForCampaign(groupName, FirstName, FirstName1)
            print "\nCreating Lesson\n"
             
            t.userDeactivate(FirstName)
            
            t.CheckUserInGroupsPage(groupName, FirstName)
            
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
    
    ut=UserDeactivateFromGroup()
    ut.UserDeactivateFromGroupMain()



    
