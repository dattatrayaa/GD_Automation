'''
Created on 01-Mar-2018

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
from DeleteLesson import DeleteLesson
from CreateLessonDifferentCards import CreateLessonDifferentCards
from LessonsPageElements import LessonsPageElements
from BaseTestClass import projectPath

class CreateCampaignForVidDocQueLesson:
    
    def createCampaignForLessonVideoDocumentQuestion(self,campaignTitle,campDescription,lessonName,actualSuccessMessage,minPassingScore,numberOfAttempts):
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
        
        
        print "Clicking on Create Campaign button"
        wait.until(EC.visibility_of_element_located((By.XPATH,elements.createCampaignButtonXpath())))
        elements.createCampaignButton()
        
        
        wait.until(EC.visibility_of_element_located((By.XPATH,elements.Camp_titleXpath())))
        print "Create Campaign page is displayed"
        
                  
        elements.titleTextField(campaignTitle)
        print "Title entered ::"+campaignTitle
        
        elements.descriptionField(campDescription)
        print "Description entered ::"+campDescription
        
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
            
        
        print "Making This campaign as Graded campaign"    
        elements.makeThisAsAGradedCampaign()
        
        elements.setMinimumPassingScore(str(minPassingScore))
        
        print "Setting maximum number of attempts"
        elements.setAMaxNoOfAttempts(numberOfAttempts)
        
        
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
    
    
    
    def createLessonVidDocQue(self,lessonName,videoPath,documentPath,timetoUploadDoc,questionCard,ans1,ans2,timeToUploadVideo):
        
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
        
        
        
        #Video card
        objFor=CreateLessonDifferentCards()
        objFor.videoCard(videoPath, timeToUploadVideo)
        objFor.videoCard(videoPath, timeToUploadVideo)
        objFor.videoCard(videoPath, timeToUploadVideo)
        objFor.videoCard(videoPath, timeToUploadVideo)
        objFor.videoCard(videoPath, timeToUploadVideo)
        
        #Document
        #objFor.docCard(documentPath, timetoUploadDoc)
        #objFor.docCard(documentPath, timetoUploadDoc)
        #objFor.docCard(documentPath, timetoUploadDoc)
        #objFor.docCard(documentPath, timetoUploadDoc)
        #objFor.docCard(documentPath, timetoUploadDoc)
       
        #Question card
        objFor.quesCard(questionCard, ans1, ans2)
        objFor.quesCard(questionCard, ans1, ans2)
        objFor.quesCard(questionCard, ans1, ans2)
        objFor.quesCard(questionCard, ans1, ans2)
        objFor.quesCard(questionCard, ans1, ans2)
        
       
        print "All Cards inserted"
        
        
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
        
    
    
            
    def createCampaignWithLessonVideoDocumentQuestion(self):
       
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        first_sheet = book.sheet_by_name('CreateCampaigns')
        
        #Campaign Data
        cell1 = first_sheet.cell(105,1)
        campaignTitle = cell1.value
        
        cell1 = first_sheet.cell(106,1)
        campDescription = cell1.value
        
        cell1 = first_sheet.cell(107,1)
        actualSuccessMessage = cell1.value
        
        cell1 = first_sheet.cell(108,1)
        minPassingScore = cell1.value
        
        cell1 = first_sheet.cell(109,1)
        numberOfAttempts = cell1.value
        
        
        #Lesson
        cell1 = first_sheet.cell(111,1)
        lessonName = cell1.value
        
        cell1 = first_sheet.cell(112,1)
        videoPath = cell1.value
        
        cell1 = first_sheet.cell(113,1)
        timeToUploadVideo = cell1.value
        
        cell1 = first_sheet.cell(114,1)
        documentPath = cell1.value
        
        cell1 = first_sheet.cell(113,1)
        timetoUploadDoc = cell1.value
        
        
        cell1 = first_sheet.cell(115,1)
        questionCard = cell1.value
        
        cell1 = first_sheet.cell(116,1)
        ans1 = cell1.value
        
        cell1 = first_sheet.cell(117,1)
        ans2 = cell1.value
        
        
        
        
        
        try:
            print "\n\n----This test case creates campaign with----\n1. Video, Document and Question lesson\n"
            newobj=CreateCampaignForVidDocQueLesson()
            newobj.createLessonVidDocQue(lessonName, videoPath, documentPath, timetoUploadDoc, questionCard, ans1, ans2, timeToUploadVideo)
            newobj.createCampaignForLessonVideoDocumentQuestion(campaignTitle, campDescription, lessonName, actualSuccessMessage, minPassingScore, numberOfAttempts)
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
                lesdel= DeleteLesson()
                lesdel.lessonDelete(lessonName)
            except Exception:
                driver.get(url)
        
if __name__ == '__main__':
    
    btc=BaseTestClass()
    btc.UserLogin()
    
    newObj=CreateCampaignForVidDocQueLesson()
    newObj.createCampaignWithLessonVideoDocumentQuestion()
         
    
