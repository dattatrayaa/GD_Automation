'''
Created on 03-Apr-2018

@author: dattatraya
'''

import os.path
import time
import traceback

from BaseTestClass import BaseTestClass
from BaseTestClass import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xlrd

from CampaignPageElements import CampPage
from CreateLessonDifferentLessons import CreateLessonDifferentLessons
from DeleteLesson import DeleteLesson
from PlanAssignmentForPageElements import PlanAssignmentForPageElements
from BaseTestClass import projectPath

class AssignCampEditTrigger:
    
    def campEditTrigger(self,campaignTitle,campDescription,lessonName):
        
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
        
        
        planPageEle=PlanAssignmentForPageElements()
        
        planPageEle.triggredRadioButton()
        wait.until(EC.visibility_of_element_located((By.XPATH,planPageEle.NewHireOnBoarding())))
        
        print "Clicked on Triggered"
        
        #Checking New hire on boarding is selected 
        if driver.find_element_by_xpath("//input[@id='trigger-new-hire']").is_selected():
            print "Radio button New Hire Onboarding is selected"
        else:
            print "Radio button New Hire Onboarding is not selected"
            raise Exception
        
        
        print "Saving Trigger"
        
        planPageEle.saveTrigger()
        
        
        
        wait.until(EC.visibility_of_element_located((By.XPATH,planPageEle.confirmPopupYesSaveButton())))
        driver.find_element_by_xpath(planPageEle.confirmPopupYesSaveButton()).click()
        
        print "Clicked on Yes,Save button from pop up"
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,"(//tbody/tr[1]/td[1]/div/span)[1]")))
            print "Trigger is displayed in Campaign details page"
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
            
            
            
    def deleteTrigger(self,campaignTitle,actualDeleteTriggerText):
        
        elements=CampPage()
        driver.refresh()
        wait=WebDriverWait(driver, 60)
        
        
        print "\n\nCreating Campaign"
        wait.until(EC.visibility_of_element_located((By.XPATH,elements.campaignButtonFromSideMenuXpath())))
        elements.campaignButtonFromSideMenu()
        
        wait.until(EC.visibility_of_element_located((By.XPATH,elements.createCampaignButtonXpath())))

        if elements.campaignsPageHeaderText()=="Campaigns":
            print "Campaigns page displayed"
        else:
            print "Campaigns page is not displayed"
            raise Exception
        
        
        print "Clicking on Campaign link from Campaigns grid"
        try:
            elements.CampaignLinkFromCampaignGrid(campaignTitle)
        except Exception:
            print "Campaign link not displayed"
            raise Exception
        
        print "Clicked on Campaign from grid"
        
        
        time.sleep(4)
        
        try:
            elements.editTriggerButton("1")
            print "Clicked on Edit trigger button"
        except Exception:
            print "Edit button for trigger is not displayed"
            raise Exception
        
        
        
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/div[2]/header/div/button")))
            print "Edit trigger page is displayed"
        except Exception:
            print "Edit trigger page is not displayed"
            raise Exception
                
        time.sleep(6)
            
        print "Deleting trigger" 
        deleteTriggerButton=wait.until(EC.element_to_be_clickable((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/div[2]/header/div/button")))
        deleteTriggerButton.click()
        
        print "Verify Delete Trigger popup is displayed"
        headerDeleteTrigger=wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[4]/div/div/div[1]/h3")))
        
        
        if headerDeleteTrigger.text==actualDeleteTriggerText:
            print "The Text in header is ::"+headerDeleteTrigger.text
        else:
            print "Header Text is not displayed properly in popup"
            raise Exception
        
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[4]/div/div/div[2]/div[2]/button[1]")))
            print "Delete trigger button is displayed"
        except Exception:
            print "Delete trigger button is not displayed"
            raise Exception
        
        deletebutton=wait.until(EC.element_to_be_clickable((By.XPATH,"html/body/div[4]/div/div/div[2]/div[2]/button[1]")))
        deletebutton.click()
        print "Clicked on Delete trigger button from pop up"
        
        wait.until(EC.invisibility_of_element_located((By.XPATH,"html/body/div[4]/div/div/div[1]")))
        
        
        time.sleep(3)
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,"//h1/em[.='"+campaignTitle+"']")))
        except Exception:
            print "Campaign detail page is not displayed"
            raise Exception
        print "Campaign details page is displayed"
        
        
        try:
            trig=wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/div[3]/div/h3/span[contains(.,'0')]")))
            print "In trigger section '"+trig.text+"' is displayed"
        except Exception:
            print "Trigger is still displayed in Campaign details page"
            raise Exception
        
        print "Trigger is deleted successfully"
        
        
        campaignPage=wait.until(EC.element_to_be_clickable((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/div[1]/a")))
        campaignPage.click()
        
        
        print "Checking for this campaign trigger status displayed as 'N' in campaigns grid"
        wait.until(EC.visibility_of_element_located((By.XPATH,"(//tr/td[1]/a[.='"+campaignTitle+"']/../../td[2])[1]")))
        hasTrigger=driver.find_element_by_xpath("(//tr/td[1]/a[.='"+campaignTitle+"']/../../td[2])[1]").text
        
        if hasTrigger=="N":
            print "'"+hasTrigger+"' displayed in Has trigger column"
        else:
            print "Invalid data in Has trigger column"
            raise Exception
        
        
        
    
    
    
    def assignCampEditTriggerDeleteTrigger(self):
        
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        first_sheet = book.sheet_by_name('CampAssign')
        
        
        #Campaign
        cell1 = first_sheet.cell(431,1)
        campaignTitle = cell1.value
        
        cell1 = first_sheet.cell(432,1)
        campDescription = cell1.value
        
        
        
        cell1 = first_sheet.cell(433,1)
        lessonName = cell1.value
        
        
        cell2 = first_sheet.cell(434,1)
        questionCard= cell2.value
        
        cell2 = first_sheet.cell(435,1)
        ans1= cell2.value
        
        cell2 = first_sheet.cell(436,1)
        ans2= cell2.value
        
        cell2 = first_sheet.cell(437,1)
        actualDeleteTriggerText= cell2.value
        
        #For Original User
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        s_sheet = book.sheet_by_name('Login_Credentials')
        
        cell = s_sheet.cell(1,1)
        url = cell.value
        
        cell = s_sheet.cell(3,1)
        username = cell.value
        
        cell = s_sheet.cell(3,2)
        password = cell.value
        
        try:
            
            print "\nCreating a lesson\n"
            ot=CreateLessonDifferentLessons()
            ot.lessonWithQuestion(lessonName, questionCard, ans1, ans2)
            
            
            print "\nCreating Campaign\n"
            lk=AssignCampEditTrigger()
            lk.campEditTrigger(campaignTitle, campDescription, lessonName)
            
            lk.deleteTrigger(campaignTitle, actualDeleteTriggerText)
            
            
            
            print "\n----Text Execution Completed----\n"
            
            
        except Exception as e:
            traceback.print_exc()
            print (e)
            raise Exception 
         
        finally: 
            driver.save_screenshot("ScreenShots/AssignCampEditTrigger.png") 
            second_sheet = book.sheet_by_name('Login_Credentials')
            cell = second_sheet.cell(1,1)
            url = cell.value
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
            
if __name__ == '__main__':
    
    btc=BaseTestClass()
    btc.UserLogin()
    
    ne=AssignCampEditTrigger()
    ne.assignCampEditTriggerDeleteTrigger()
            
                   
        
        
        
        