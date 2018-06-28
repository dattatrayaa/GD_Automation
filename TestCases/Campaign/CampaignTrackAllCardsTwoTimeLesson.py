'''
Created on 07-Mar-2018

@author: dattatraya
'''

import os.path
import traceback

from BaseTestClass import BaseTestClass
from BaseTestClass import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xlrd

from CampaignPageElements import CampPage
from CreateLessonDifferentCards import CreateLessonDifferentCards
from CreateTrackComman import CreateTrackComman
from DeleteLesson import DeleteLesson
from LessonsPageElements import LessonsPageElements
from BaseTestClass import projectPath

class CampaignTrackAllCardsTwoTimeLesson:
   
    def allCardsTwoTime(self,lessonName,textCard,Imagefilepath1,videoPath, timeToUploadVideo,documentPath,timetoUploadDoc,questionCard, ans1, ans2):
        
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
        objfore=CreateLessonDifferentCards()
         
        objfore.textCard(textCard)
        objfore.textCard(textCard)
        
        objfore.imageCard(Imagefilepath1)
        objfore.imageCard(Imagefilepath1)
        
        objfore.videoCard(videoPath, timeToUploadVideo)
        objfore.videoCard(videoPath, timeToUploadVideo)
        
        #objfore.docCard(documentPath, timetoUploadDoc)
        #objfore.docCard(documentPath, timetoUploadDoc)
        
        objfore.quesCard(questionCard, ans1, ans2)
        objfore.quesCard(questionCard, ans1, ans2)
        
        objfore.textCard(textCard)
        print "All Cards inserted"
        
        
        print "All Cards inserted"
        
        
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
        
    
    def campWithAllcardsTwotime(self,campaignTitle,campDescription,trackName,actualSuccessMessage,minPassingScore,numberOfAttempts,ownDuration):
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
        print "Title entered ::campTitle"
        
        elements.descriptionField(campDescription)
        print "Description entered ::campDescription"
        
        print "Adding Track"
        #Add Track 
        
        elements.addTrackButton()
        
        #Searching track and adding
        elements.searchTracksAndSelect(trackName)
        
        #Adding to Campaign
        elements.addToCampaignTrack()
        
        
        #Verifying Added Track is displayed in Grid
        print "\nVerifying Added Track is displayed in Grid"
        if trackName in elements.firstTrackInGrid():
            print "Track displayed in grid"
        else:
            print "Track not displayed in grid"
            
        
        print "Setting Own duration"
        elements.setOwnDuration(ownDuration)
        
        #Making as Graded campaign
        print "Making this as a graded campaign"
        elements.makeThisAsAGradedCampaign()
        
        print "setting minimum passing score"
        elements.setMinimumPassingScore(minPassingScore)    
        
        print "Setting max no of attempts"
        elements.setAMaxNoOfAttempts(numberOfAttempts)
        
        
        wait.until(EC.element_to_be_clickable((By.XPATH,elements.SaveAndExit_ButtonXpath())))
        #Clicking on save & exit button
        print "Clicking on save & exit button"
        elements.saveAndExitButton()
        
        
        
        #Verifying campaign detail page is displayed
        print "\nVerifying campaign detail page is displayed"
        
        if elements.campaignDetailPageHeaderText()==campaignTitle:
            print "Campaign detail page is displayed"
        else:
            print "Campaign detail page is not displayed"
            raise Exception
        
        print "\n----Text Execution Completed----\n"
    
    
    def CampaignForTrackWithAllCardsTwoTime(self):
        
        
        
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        first_sheet = book.sheet_by_name('CreateCampaigns')
        
        cell1 = first_sheet.cell(82,5)
        campaignTitle = cell1.value
        
        cell1 = first_sheet.cell(83,5)
        campDescription = cell1.value
        
        cell1 = first_sheet.cell(84,5)
        actualSuccessMessage = cell1.value
        
        
        #Track
        cell1 = first_sheet.cell(86,5)
        trackName = cell1.value
        
        cell2 = first_sheet.cell(87,4)
        Imagefilepath = cell2.value
        
        cell2 = first_sheet.cell(88,5)
        description = cell2.value
        
        cell2 = first_sheet.cell(89,4)
        tagName = cell2.value
        
        cell2 = first_sheet.cell(90,5)
        expectedSuccessText= cell2.value
        
        
        #Lesson
        cell2 = first_sheet.cell(92,5)
        lessonName= cell2.value
        
        cell2 = first_sheet.cell(93,4)
        textCard= cell2.value
        
        cell2 = first_sheet.cell(94,4)
        Imagefilepath1= cell2.value
        
        cell2 = first_sheet.cell(95,4)
        videoPath= cell2.value
        
        cell2 = first_sheet.cell(96,4)
        timeToUploadVideo= cell2.value
        
        cell2 = first_sheet.cell(97,4)
        documentPath= cell2.value
        
        cell2 = first_sheet.cell(98,4)
        questionCard= cell2.value
        
        cell2 = first_sheet.cell(99,4)
        ans1= cell2.value
        
        cell2 = first_sheet.cell(100,4)
        ans2= cell2.value
        
        cell2 = first_sheet.cell(101,4)
        minPassingScore= cell2.value
        
        cell2 = first_sheet.cell(102,4)
        numberOfAttempts= cell2.value
        
        cell2 = first_sheet.cell(103,4)
        ownDuration= cell2.value
        
        cell2 = first_sheet.cell(104,4)
        timetoUploadDoc= cell2.value
      
        
        try:
            #lesson Creation
            obj2=CampaignTrackAllCardsTwoTimeLesson()
            obj2.allCardsTwoTime(lessonName, textCard, Imagefilepath1, videoPath, timeToUploadVideo, documentPath, timetoUploadDoc, questionCard, ans1, ans2)           
                        
            #Track Creation
            obj1=CreateTrackComman()
            obj1.createTrack(trackName, Imagefilepath, description, tagName, lessonName, expectedSuccessText)
            
            #Campaign Creation
            
            obj2.campWithAllcardsTwotime(campaignTitle, campDescription, trackName, actualSuccessMessage, minPassingScore, numberOfAttempts, ownDuration)
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
                WebDriverWait(driver, 5).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')

                alert = driver.switch_to.alert
                alert.accept()
                print("alert accepted")
            except Exception:
                print("no alert")
            try:
                lesdel= DeleteLesson()
                lesdel.lessonDelete(lessonName)
            except Exception:
                driver.get(url)
    
if __name__ == '__main__':
    
    btc=BaseTestClass()
    btc.UserLogin()
    
    newObj=CampaignTrackAllCardsTwoTimeLesson()
    newObj.CampaignForTrackWithAllCardsTwoTime()
       

    
    
