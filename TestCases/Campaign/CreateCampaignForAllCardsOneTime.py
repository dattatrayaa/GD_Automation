'''
Created on 28-Feb-2018

@author: dattatraya
'''
import os.path
import time
import traceback

from BaseTestClass import BaseTestClass
from BaseTestClass import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xlrd

from CampaignPageElements import CampPage
from CreateLessonDifferentCards import CreateLessonDifferentCards
from LessonsPageElements import LessonsPageElements
from DeleteLesson import DeleteLesson
from BaseTestClass import projectPath

class CreateCampaignForAllCardsOneTime:
    
    
    def createCampaignLessonAllCards(self,campaignTitle,campDescription,lessonName,actualSuccessMessage):
        elements=CampPage()
        
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
        
        
        print "Clicking on Create Campaign button"
        wait.until(EC.visibility_of_element_located((By.XPATH,elements.createCampaignButtonXpath())))
        elements.createCampaignButton()
        
        
        wait.until(EC.visibility_of_element_located((By.XPATH,elements.Camp_titleXpath())))
        print "Create Campaign page is displayed"
        
                  
        elements.titleTextField(campaignTitle)
        print "Title entered ::campTitle"
        
        elements.descriptionField(campDescription)
        print "Description entered ::campDescription"
        
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
        
        #Verifying Added lesson is displayed in Grid
        print "\nVerifying Added lesson is displayed in Grid"
        if elements.firstLessonInGrid()==lessonName:
            print "Lesson displayed in grid"
        else:
            print "Lesson not displayed in grid"
        
        wait.until(EC.element_to_be_clickable((By.XPATH,elements.SaveAndExit_ButtonXpath())))
        #Clicking on save & exit button
        print "Clicking on save & exit button"
        elements.saveAndExitButton()
        
        '''#verifying success message
        print "\nVerifying success message"
        
        if elements.successMessage()==actualSuccessMessage:
            print "Message '"+actualSuccessMessage+"' is displayed"
        else:
            print "Success message is not displayed properly"
            raise Exception'''
        
        #Verifying campaign detail page is displayed
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
        
        print "\n----Text Execution Completed----\n"
    
    def allCardsOneTime(self,lessonName,textCard,Imagefilepath1,videoPath, timeToUploadVideo,documentPath,timetoUploadDoc,questionCard, ans1, ans2):
        print "\nCreating lesson with one card"
        wait=WebDriverWait(driver, 60)
        driver.refresh()
        print "Clicking on Lessons button from side menu"
        
        lessons=LessonsPageElements()
        lessons.lessonsButtonSideMenuUnexpanded()
     
        print "Click on Create lesson button"
        lessons.createLessonButton()
        
        print "Verifying Create new lesson tab is displayed"
        
        
        if lessons.createANewLessonPopupHeader()== "Create a new lesson":
            print("Create a new lesson tab is displayed")
        else:
            print ""
            raise Exception
        
               
        
        lessons.clickOnBlankLesson()
        print "Clicked on Blank lesson"
        
        print "Creating New lesson"
        lessons.settingLessonName(lessonName)
        print "Entered lesson name ::"+lessonName
      
        #Text Card
        objll=CreateLessonDifferentCards()
         
        objll.textCard(textCard)
        objll.imageCard(Imagefilepath1)
        objll.videoCard(videoPath, timeToUploadVideo)
        #objll.docCard(documentPath, timetoUploadDoc)
        objll.quesCard(questionCard, ans1, ans2)
        objll.textCard(textCard)
        time.sleep(2)
        print "All Cards inserted"
        
        print "Publishing lesson"
        
        print "Publishing lesson"
        
        time.sleep(2)
        print "Publishing lesson"
        lessons.readyToPublishButtonClick()
        
        print "Clicked on publish button"
        lessons.publishButtonClick()

        print "Lesson published"
        
        
        lessons.backButton()
        
        #Verifying created lesson is displayed in list
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"(//tbody/tr/td[2]/a[.='"+lessonName+"'])[1]")))

        if driver.find_element_by_xpath("(//tbody/tr/td[2]/a[.='"+lessonName+"'])[1]").is_displayed():
            
            print "\nLesson is displayed in Grid ::"+lessonName
            
        else:
            print "Lesson not displaying in grid"
            raise Exception
        
        
        lessons.expandSideMenu()
    
    
    
    
    def createCampaignAllCardsOneTimeLesson(self):
       
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        first_sheet = book.sheet_by_name('CreateCampaigns')
        
        #Campaign Data
        cell1 = first_sheet.cell(55,1)
        campaignTitle = cell1.value
        
        cell1 = first_sheet.cell(56,1)
        campDescription = cell1.value
        
        cell1 = first_sheet.cell(57,1)
        actualSuccessMessage = cell1.value
        
        cell1 = first_sheet.cell(59,1)
        lessonName = cell1.value
        
        cell1 = first_sheet.cell(60,1)
        textCard = cell1.value
        
        cell1 = first_sheet.cell(61,1)
        Imagefilepath1 = cell1.value
        
        cell1 = first_sheet.cell(62,1)
        videoPath = cell1.value
        
        cell1 = first_sheet.cell(63,1)
        timeToUploadVideo = cell1.value
        
        cell1 = first_sheet.cell(64,1)
        documentPath = cell1.value
        
        cell1 = first_sheet.cell(63,1)
        timetoUploadDoc = cell1.value
        
        cell1 = first_sheet.cell(65,1)
        questionCard = cell1.value
        
        cell1 = first_sheet.cell(66,1)
        ans1 = cell1.value
        
        cell1 = first_sheet.cell(67,1)
        ans2 = cell1.value
        
        
        try:
            print "\n\n----This Test case creates campaigns with all lesson cards----\n\n"
            newobj=CreateCampaignForAllCardsOneTime()
            newobj.allCardsOneTime(lessonName, textCard, Imagefilepath1, videoPath, timeToUploadVideo, documentPath, timetoUploadDoc, questionCard, ans1, ans2)
            newobj.createCampaignLessonAllCards(campaignTitle, campDescription, lessonName, actualSuccessMessage)
         
        except Exception as e:
            traceback.print_exc()
            print (e)
            raise Exception  
           
        finally:
            second_sheet = book.sheet_by_name('Login_Credentials')
            cell = second_sheet.cell(1,1)
            url = cell.value
            driver.get(url)
            try:
                oj=DeleteLesson()
                oj.lessonDelete(lessonName)
            except Exception:
                driver.get(url)
        
if __name__ == '__main__':
    
    btc=BaseTestClass()
    btc.UserLogin()
    
    newObj=CreateCampaignForAllCardsOneTime()
    newObj.createCampaignAllCardsOneTimeLesson()        
    
