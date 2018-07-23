'''
Created on 15-Jun-2018

@author: Optislabs
'''
import time
import traceback

from BaseTestClass import BaseTestClass
from BaseTestClass import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from CampaignPageElements import CampPage
from CreateLearnerNew import CreateLearner
from CreateLessonDifferentLessons import CreateLessonDifferentLessons
from DeleteLesson import DeleteLesson
from ExcelFunctions import ExcelFunctions
from GroupsPageElements import GroupsPageElements
from PlanAssignmentForPageElements import PlanAssignmentForPageElements
from UsersPageElements import UsersPageElements
from ManageAssignMentForPageElements import ManageAssignMentForPageElements


class UserDeactivateFromCampTriggered:
    
    
    
    def campaignToGroupTriggered(self,campaignTitle,campDescription,lessonName,groupName,minPassingScore,numberOfAttempts):
        
        elements=CampPage()
        
        wait=WebDriverWait(driver, 60)
        
        driver.refresh()
        print "\n\nCreating Campaign"
        wait.until(EC.visibility_of_element_located((By.XPATH,elements.campaignButtonFromSideMenuXpath())))
        elements.campaignButtonFromSideMenu()
        
        wait.until(EC.visibility_of_element_located((By.XPATH,elements.createCampaignButtonXpath())))

        if elements.campaignsPageHeaderText()=="Campaigns":
            print "Campaigns page displayed"
        else:
            print "Campaigns page is not displayed"
            raise Exception
        
        
        print "Clicking on Create Campaign button"
        wait.until(EC.visibility_of_element_located((By.XPATH,elements.createCampaignButtonXpath())))
        elements.createCampaignButton()
        
        
        wait.until(EC.visibility_of_element_located((By.XPATH,elements.Camp_titleXpath())))
        print "Create Campaign page is displayed"
        
                  
        elements.titleTextField(campaignTitle)
        print "Title entered"
        
        elements.descriptionField(campDescription)
        print "Description entered"
        
        print "Adding Lesson"
        #Add lesson button
        elements.addlessonButton()
        
        #Waiting until first lesson in pop is displayed
        wait.until(EC.visibility_of_element_located((By.XPATH,elements.FirstLessonWaitXpath())))
        
        #Searching lesson by its name
        elements.searchLesson(lessonName)
        
        #Waiting until lesson displayed
        elements.waitUntilSearchedLessonDisplayed(lessonName)
        
        #selecting searched lesson
        elements.selectSearchedLesson(lessonName)
        
        #waiting until add to campaign button is click able
        wait.until(EC.element_to_be_clickable((By.XPATH,elements.AddToCampaign_ButtonXpath())))
        
        #Clicking on Add to Campaign button
        elements.addToCampaignButton()
        
        
        time.sleep(2)
        #Verifying Added lesson is displayed in Grid
        print "\nVerifying Added lesson is displayed in Grid"
        if elements.firstLessonInGrid()==lessonName:
            print "Lesson displayed in grid"
        else:
            print "Lesson not displayed in grid"
            raise Exception
        
        
        print "Making this as a Graded campaign"
        elements.makeThisAsAGradedCampaign()
        print "Settng minimum passing score"
        elements.setMinimumPassingScore(minPassingScore)
        print "Setting maximum no of attempts"
        elements.setAMaxNoOfAttempts(numberOfAttempts)
        
        
        wait.until(EC.element_to_be_clickable((By.XPATH,elements.SaveAndExit_ButtonXpath())))
        print "Clicking on Save and plan assignmet button"
        elements.saveAndPlanAssignmentbutton()
        
        
        
        #Verifying Plan assignment for page is displayed
        print "Verifying Plan assignment for page is displayed"
        if campaignTitle in elements.planAssignementForHeaderText():
            print "Page '"+elements.planAssignementForHeaderText()+"' is displayed"
        else:
            print "Plan assignment page is not displayed"
            raise Exception
        
        
        #Checking One time triggered radio button is selected by Default
        if driver.find_element_by_xpath("//input[@id='assignment-one-time']").is_selected():
            print "Radio button One Time triggered is selected"
        else:
            print "Radio button is not selected"
            raise Exception
        
        
        
        print "Clicking on Triggered radio button"
        planAssignPage=PlanAssignmentForPageElements()
        
        planAssignPage.triggredRadioButton()
        
        wait.until(EC.visibility_of_element_located((By.XPATH,planAssignPage.NewHireOnBoarding())))
        
        print "Clicked on Triggered"
        
        #Checking New hire on boarding is selected 
        if driver.find_element_by_xpath("//input[@id='trigger-new-hire']").is_selected():
            print "Radio button New Hire Onboarding is selected"
        else:
            print "Radio button New Hire Onboarding is not selected"
            raise Exception
        
        

        
        print "Selecting New to group"
        driver.find_element_by_xpath(planAssignPage.NewtoGroup()).click()
        wait.until(EC.visibility_of_element_located((By.XPATH,planAssignPage.AddGroupTextField()))) 
        
        searchGroups=driver.find_element_by_xpath(planAssignPage.AddGroupTextField())
        
        webdriver.ActionChains(driver).move_to_element(searchGroups).click().send_keys(groupName).perform()
        groupdisplayed=wait.until(EC.visibility_of_element_located((By.XPATH,"(//div[@role='option']/span)[1]")))
        
        webdriver.ActionChains(driver).move_to_element(groupdisplayed).click().perform()
        
        
        print "Checking Group is displayed in Grid"
        
        if driver.find_element_by_xpath("//table/tbody/tr/td[1]/a").text==groupName:
            print "Group '"+groupName+"' is displayed in grid"
        else:
            print "Group is not displayed in Grid"
            raise Exception
        
        
        print "Clicking on checkbox 'Also assign to learners who currently match this criteria' "
        
        driver.find_element_by_xpath(planAssignPage.CheckBoxCurrentUserMatching()).click()
        wait.until(EC.visibility_of_element_located((By.XPATH,planAssignPage.YourCriteriaMatchesBox())))
        
        
        
        print "Saving Trigger"
        planAssignPage.saveTrigger()
        
        
        wait.until(EC.visibility_of_element_located((By.XPATH,planAssignPage.confirmPopupYesSaveButton())))
        driver.find_element_by_xpath(planAssignPage.confirmPopupYesSaveButton()).click()
        
        print "Clicked on Yes,Save button from pop up"
        
        print "Checking for In Campaign details page Trigger is displayed"
        try:
            elements.TriggerDisplayedInGridForGroup(groupName)
            print "Trigger with group name '"+groupName+"' is displayed in Campaign details page"
        except Exception:
            print "Trigger is not displayed"
            raise Exception
        
        
        #Verifying Campaign Detail page is displayed
        print "\nVerifying campaign detail page is displayed"
        
        if elements.campaignDetailPageHeaderText()==campaignTitle:
            print "Campaign detail page is displayed"
        else:
            print "Campaign detail page is not displayed"
            raise Exception
        
        #verifying in Campaigns displayed in Campaigns grid
        elements.searchingForlesson(campaignTitle)
        
        if elements.actualCampTitleINGrid()==campaignTitle:
            print "Campaign '"+campaignTitle+"' displayed in Grid"
        
        else:
            print "Campaign is not displayed in Grid"
            raise Exception
        
         
         
        print "\nVerifying 'Y' is displayed for created triggred campaign"
        hasTrigger=driver.find_element_by_xpath("(//tr/td[1]/a[.='"+campaignTitle+"']/../../td[2])[1]").text
        
        if hasTrigger=="Y":
            print "'Y' displayed in Has trigger column"
        else:
            print "Invalid data in Has trigger column"
            
            
            
    def groupCreateForCampaign(self,groupName,FirstName):
        
        driver.refresh()
        wait=WebDriverWait(driver, 60)
        
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
        
        print "Verifying user is added to group"
        group.groupAddedInList(FirstName)
        
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
    
    
    
    def CheckInCampaignUserStatusDeactivated(self,campaignTitle,groupName):
        
        elements=CampPage()
        
        wait=WebDriverWait(driver, 60)
        
        driver.refresh()
        print "\n\nCreating Campaign"
        wait.until(EC.visibility_of_element_located((By.XPATH,elements.campaignButtonFromSideMenuXpath())))
        elements.campaignButtonFromSideMenu()
        
        wait.until(EC.visibility_of_element_located((By.XPATH,elements.createCampaignButtonXpath())))

        if elements.campaignsPageHeaderText()=="Campaigns":
            print "Campaigns page displayed"
        else:
            print "Campaigns page is not displayed"
            raise Exception
        
        print "Clicking on link of campaign created"
        elements.CampaignLinkFromCampaignGrid(campaignTitle)
        
        
        print "Verifying Campaign details page is displayed"
        if elements.campaignDetailPageHeaderText()==campaignTitle:
            print "Header Text '"+elements.campaignDetailPageHeaderText()+"' is displayed"
        else:
            print "Header Text not displayed"
            raise Exception
        
        
        time.sleep(2)
        print "Clicking on Group name present in Assigned to column ::"+groupName
        
        elements.groupInAssignedToColumnClick(groupName)
        print "Clicked on "+groupName+" link"
        
        m=ManageAssignMentForPageElements()
        wait.until(EC.visibility_of_element_located((By.XPATH,m.campaignNameInOverviewSection(campaignTitle))))
        
        print "Verifying Manage Assignment for page is displayed"
        
        
        header=wait.until(EC.visibility_of_element_located((By.XPATH,m.HeaderTextManageAssign())))
        print header.text
        if "Manage assignment for: "+groupName ==header.text:
            print "'"+header.text+"' is displayed in Header"
        else:
            print "Header Text is not displayed is not valid"
            raise Exception
        
        try:
            tr=wait.until(EC.visibility_of_element_located((By.XPATH,m.deactivatedUserText())))
            print "Deactivated text is displayed as ::"+tr.text
        except:
            raise Exception('Deactivated Status is not displayed')
        
    
    
    
    
    def UserDeactivatedFromTriggeredCampaign(self):
        
        exc=ExcelFunctions()
        
        exc.OpenExcelFile('TestData.xlsx')
        
        exc.OpenSheet('UsersPage')
        
        FirstName=exc.getCellData(43, 1)
        
        
        FirstNameId = FirstName.split("_")
        emp = FirstNameId[0]+"_"
        ids = FirstNameId[1]
        empId = int(ids)+1
        FirstNameUpdated= emp+str(empId)
        
        LastName = exc.getCellData(44, 1)
        
        LastNameID = LastName.split("_")
        emp = LastNameID[0]+"_"
        ids = LastNameID[1]
        empId = int(ids)+1
        LastNameUpdated= emp+str(empId)
        
        
        
        Email = exc.getCellData(45, 1)
        
        EmailId = Email.split("_")
        emp = EmailId[0]+"_"
        ids = EmailId[1]
        remaining="_"+EmailId[2]
        empId = int(ids)+1
        EmailIdUpdated= emp+str(empId)+remaining
        
        EmployeeId = exc.getCellData(46, 1)
        
        Employee = EmployeeId.split("_")
        emp = Employee[0]+"_"
        ids = Employee[1]
        empId = int(ids)+1
        EmployeeIdUpdated= emp+str(empId)
        
        Password = exc.getCellData(47, 1)
        
        NewPassword=exc.getCellData(47, 1)
        
        groupName=exc.getCellData(48, 1)
        groupNameId = groupName.split("_")
        emp = groupNameId[0]+"_"
        ids = groupNameId[1]
        empId = int(ids)+1
        GroupNameUpdated= emp+str(empId)
        
        
        
        #campaign details
        campaignTitle=exc.getCellData(49, 1)
        campDescription=exc.getCellData(50, 1)
        minPassingScore=exc.getCellData(51, 1)
        numberOfAttempts=exc.getCellData(52, 1)
        
        
        lessonName=exc.getCellData(53, 1)
        questionCard=exc.getCellData(54, 1)
        ans1=exc.getCellData(55, 1)
        ans2=exc.getCellData(56, 1)
        
        
        
        
        
        exc.OpenExcelFile('TestData.xlsx')
        exc.OpenSheet("Login_Credentials")
        
        url=exc.getCellData(1, 1)
        username=exc.getCellData(3, 1)
        password=exc.getCellData(3, 2)
        
        
        
        
        #updating user values
        exc.updateExcelFileName('TestData.xlsx')
        exc.updateExcelSheetName('UsersPage')
        
        exc.updateCellData(FirstNameUpdated, 44, 2)
        exc.updateCellData(LastNameUpdated, 45, 2)
        exc.updateCellData(EmailIdUpdated, 46, 2)
        exc.updateCellData(EmployeeIdUpdated, 47, 2)
        exc.updateCellData(GroupNameUpdated, 49, 2)
        
        exc.SaveExcelFile('TestData.xlsx')
        
        
        
        
        try:
            
          
            t=UserDeactivateFromCampTriggered()
            print "\nCreating New User\n"
            
            Cr=CreateLearner()
            Cr.createNewLearnerMain(FirstName, LastName, Email, EmployeeId, Password, NewPassword, url, username, password) 
            
            t.groupCreateForCampaign(groupName, FirstName)
            print "\nCreating Lesson\n"
            lesson=CreateLessonDifferentLessons()
            lesson.lessonWithQuestion(lessonName, questionCard, ans1, ans2)
             
            print "\nCreating Campaign\n"
            t.campaignToGroupTriggered(campaignTitle, campDescription, lessonName, groupName, minPassingScore, numberOfAttempts)
            
            print "\n Deactivating User from application\n"
            t.userDeactivate(FirstName)
            
            print "\nChecking in Manage assignment page user displayed as deactivated\n"
            t.CheckInCampaignUserStatusDeactivated(campaignTitle, groupName)
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
                
            
            
            wait=WebDriverWait(driver, 60)
            unDropDown=wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[1]/div[1]/nav/div[2]/a/span[3]")))
            driver.execute_script('arguments[0].click()',unDropDown)
            
            signOut=driver.find_element_by_xpath("html/body/div/div/div[1]/div[2]/div[2]/a")
            driver.execute_script('arguments[0].click()',signOut)
            
            
            
            element = wait.until(EC.presence_of_element_located((By.ID, "password")))
            
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
            
            print "Successfully Logged Into Users account"
            time.sleep(3)
            
            
            try:
                d=DeleteLesson()
                d.lessonDelete(lessonName) 
            except Exception:
                driver.get(url)
                
                
            
            
        
        
        
if __name__=='__main__':
    
    btc=BaseTestClass()
    btc.UserLogin() 
    
    ut=UserDeactivateFromCampTriggered()
    ut.UserDeactivatedFromTriggeredCampaign()



