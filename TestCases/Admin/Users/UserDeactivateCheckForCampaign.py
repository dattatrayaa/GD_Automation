'''
Created on 14-Jun-2018

@author: dattatraya
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
from ExcelFunctions import ExcelFunctions
from PlanAssignmentForPageElements import PlanAssignmentForPageElements
from UsersPageElements import UsersPageElements
from DeleteLesson import DeleteLesson


class UserDeactivateCheckForCampaign:
    
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
        
        
    def campaignToCheckDeactivatedUserShowing(self,campaignTitle,campDescription,lessonName,FirstName,minPassingScore,numberOfAttempts):
        
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
        
        
        print "Setting minimum passing score"
        elements.makeThisAsAGradedCampaign()
        elements.setMinimumPassingScore(minPassingScore)
        print "Setting maximum number of attempts"
        elements.setAMaxNoOfAttempts(numberOfAttempts)
        
        
        
        wait.until(EC.element_to_be_clickable((By.XPATH,elements.SaveAndExit_ButtonXpath())))
        print "Clicking on Save & Exit button"
        elements.saveAndPlanAssignmentbutton()
        
        planAssign=PlanAssignmentForPageElements()
        if campaignTitle in planAssign.planAssignmentHeader():
            print "'"+planAssign.planAssignmentHeader()+"' is displayed"
        else:
            print "Plan Assignment page is not displayed"
            raise Exception
        time.sleep(4)
        
        print "Assigning assignment to a user"
        selectUser=wait.until(EC.visibility_of_element_located((By.XPATH,planAssign.AddGroupTextField())))
        webdriver.ActionChains(driver).move_to_element(selectUser).click(selectUser).send_keys(FirstName).perform()
        time.sleep(4)
        message=wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@class='Select-noresults']")))
        print message.text
        print "Check No Matches found message is displayed"
        if message.text in "No matches found":
            print "Message  :"+message.text
        else:
            raise Exception('Deactivated User is available for Campaign')
        
    
        print "User is not available for Assignments"
    
    
    
    
    def UserDeactivatedAvailableForCampaignMain(self):
        
        exc=ExcelFunctions()
        
        exc.OpenExcelFile('TestData.xlsx')
        
        exc.OpenSheet('UsersPage')
        
        FirstName=exc.getCellData(25, 1)
        
        
        FirstNameId = FirstName.split("_")
        emp = FirstNameId[0]+"_"
        ids = FirstNameId[1]
        empId = int(ids)+1
        FirstNameUpdated= emp+str(empId)
        
        LastName = exc.getCellData(26, 1)
        
        LastNameID = LastName.split("_")
        emp = LastNameID[0]+"_"
        ids = LastNameID[1]
        empId = int(ids)+1
        LastNameUpdated= emp+str(empId)
        
        
        
        Email = exc.getCellData(27, 1)
        
        EmailId = Email.split("_")
        emp = EmailId[0]+"_"
        ids = EmailId[1]
        remaining="_"+EmailId[2]
        empId = int(ids)+1
        EmailIdUpdated= emp+str(empId)+remaining
        
        EmployeeId = exc.getCellData(28, 1)
        
        Employee = EmployeeId.split("_")
        emp = Employee[0]+"_"
        ids = Employee[1]
        empId = int(ids)+1
        EmployeeIdUpdated= emp+str(empId)
        
        Password = exc.getCellData(29, 1)
        
        NewPassword=exc.getCellData(29, 1)
        
        campaignTitle=exc.getCellData(30, 1)
        campDescription=exc.getCellData(31, 1)
        minPassingScore=exc.getCellData(32, 1)
        numberOfAttempts=exc.getCellData(33, 1)
        
        
        lessonName=exc.getCellData(34, 1)
        questionCard=exc.getCellData(35, 1)
        ans1=exc.getCellData(36, 1)
        ans2=exc.getCellData(37, 1)
        
        
        
        exc.OpenExcelFile('TestData.xlsx')
        exc.OpenSheet("Login_Credentials")
        
        url=exc.getCellData(1, 1)
        username=exc.getCellData(3, 1)
        password=exc.getCellData(3, 2)
        
        
        
        
        #updating user values
        exc.updateExcelFileName('TestData.xlsx')
        exc.updateExcelSheetName('UsersPage')
        
        exc.updateCellData(FirstNameUpdated, 26, 2)
        exc.updateCellData(LastNameUpdated, 27, 2)
        exc.updateCellData(EmailIdUpdated, 28, 2)
        exc.updateCellData(EmployeeIdUpdated, 29    , 2)
        
        exc.SaveExcelFile('TestData.xlsx')
        
        
        
        
        try:
            
          
            t=UserDeactivateCheckForCampaign()
            print "\nCreating New User\n"
            
            Cr=CreateLearner()
            Cr.createNewLearnerMain(FirstName, LastName, Email, EmployeeId, Password, NewPassword, url, username, password) 
            
            print "\nDeactivating User\n" 
            t.userDeactivate(FirstName)
            
            print "\n Checking whether Deactivated User is available for Campaign\n"    
            print "\nCreating Lesson\n"
            lesson=CreateLessonDifferentLessons()
            lesson.lessonWithQuestion(lessonName, questionCard, ans1, ans2)
             
            t.campaignToCheckDeactivatedUserShowing(campaignTitle, campDescription, lessonName, FirstName, minPassingScore, numberOfAttempts)  
            
            
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
    
    ut=UserDeactivateCheckForCampaign()
    ut.UserDeactivatedAvailableForCampaignMain()







