'''
Created on 02-Mar-2018

@author: dattatraya
'''
import os.path
import time
import traceback

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
from CreateLessonDifferentLessons import CreateLessonDifferentLessons
from BaseTestClass import projectPath

class CreateCampaignForFourLessonsThree:
    
    def createCampaignFourLessonsCombiThree(self,campaignTitle,campDescription,actualSuccessMessage,lessonName1,lessonName2,lessonName3,lessonName4,minPassingScore,numberOfAttempts):
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
        print "Title entered ::campTitle"
        
        elements.descriptionField(campDescription)
        print "Description entered ::campDescription"
        
        print "Adding Lesson"
        #Add lesson button
        elements.addlessonButton()
        
        #Waiting until first lesson in pop is displayed
        wait.until(EC.visibility_of_element_located((By.XPATH,elements.FirstLessonWaitXpath())))
        
        #Searching lesson by its name
        print "Searching first lesson"
        elements.searchLesson(lessonName1)
        elements.waitUntilSearchedLessonDisplayed(lessonName1)
        elements.selectSearchedLesson(lessonName1)
        print "First lesson selected"
        
        print "Searching second lesson"
        elements.searchLesson(lessonName2)
        elements.waitUntilSearchedLessonDisplayed(lessonName2)
        elements.selectSearchedLesson(lessonName2)
        print "Second lesson selected"
        
        print "Searching Third lesson"
        elements.searchLesson(lessonName3)
        elements.waitUntilSearchedLessonDisplayed(lessonName3)
        elements.selectSearchedLesson(lessonName3)
        print "Second Third selected"
        
        print "Searching Fourth lesson"
        elements.searchLesson(lessonName4)
        elements.waitUntilSearchedLessonDisplayed(lessonName4)
        elements.selectSearchedLesson(lessonName4)
        print "Second Fourth selected"
       
        
        #waiting until add to campaign button is click able
        wait.until(EC.element_to_be_clickable((By.XPATH,elements.AddToCampaign_ButtonXpath())))
        
        #Clicking on Add to Campaign button
        elements.addToCampaignButton()
        
        #Verifying Added lesson is displayed in Grid
        print "\nVerifying Added first lesson is displayed in Grid"
        if elements.firstLessonInGrid()==lessonName1:
            print "Lesson displayed in grid  ::"+lessonName1
        else:
            print "Lesson not displayed in grid"
            raise Exception
            
        print "\nVerifying Added second lesson is displayed in Grid"
        if elements.secondLessonInGrid()==lessonName2:
            print "Lesson displayed in grid  ::"+lessonName2
        else:
            print "Lesson not displayed in grid"
            raise Exception
            
            
        print "\nVerifying Added Third lesson is displayed in Grid"
        if elements.thirdLessonInGrid()==lessonName3:
            print "Lesson displayed in grid  ::"+lessonName3
        else:
            print "Lesson not displayed in grid"
            raise Exception
            
            
        print "\nVerifying Added Fourth lesson is displayed in Grid"
        if elements.fourthLessonInGrid()==lessonName4:
            print "Lesson displayed in grid  ::"+lessonName4
        else:
            print "Lesson not displayed in grid"
            raise Exception
        
        
        
        print "Making This as a Graded campaign"    
        elements.makeThisAsAGradedCampaign()
        
        elements.setMinimumPassingScore(minPassingScore)
        
        print "Setting maximum no of attempts"
        elements.setAMaxNoOfAttempts(numberOfAttempts)
        
        print "Minimum Passing score set"
        
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
    


    def allCardstwoTime(self,lessonName,textCard,Imagefilepath1,videoPath, timeToUploadVideo,documentPath,timetoUploadDoc,questionCard, ans1, ans2):
        
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
        
        time.sleep(2)
        #objfore.docCard(documentPath, timetoUploadDoc)
        #objfore.docCard(documentPath, timetoUploadDoc)
         
         
        objfore.quesCard(questionCard, ans1, ans2)
        objfore.quesCard(questionCard, ans1, ans2)
        
        objfore.textCard(textCard)
        time.sleep(2)
        print "All Cards inserted"
        
        print "Publishing lesson"
        
        time.sleep(4)
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
    
        
    
    def createCampaignWithFourLessonsThree(self):
       
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        first_sheet = book.sheet_by_name('CreateCampaigns')
        
        #Campaign Data
        cell1 = first_sheet.cell(223,1)
        campaignTitle = cell1.value
        
        cell1 = first_sheet.cell(224,1)
        campDescription = cell1.value
        
        cell1 = first_sheet.cell(225,1)
        actualSuccessMessage = cell1.value
        
        cell1 = first_sheet.cell(226,1)
        minPassingScore = cell1.value
        
        cell1 = first_sheet.cell(227,1)
        numberOfAttempts = cell1.value
        
        #Lesson Data
        cell1 = first_sheet.cell(229,1)
        lessonName1 = cell1.value
        
        cell1 = first_sheet.cell(230,1)
        lessonName2 = cell1.value
        
        cell1 = first_sheet.cell(231,1)
        lessonName3 = cell1.value
        
        cell1 = first_sheet.cell(232,1)
        lessonName4 = cell1.value
        
        
        cell1 = first_sheet.cell(233,1)
        textCard = cell1.value
        
        cell1 = first_sheet.cell(234,1)
        Imagefilepath1 = cell1.value
        
        cell1 = first_sheet.cell(235,1)
        videoPath = cell1.value
        
        cell1 = first_sheet.cell(236,1)
        timeToUploadVideo = cell1.value
        
        cell1 = first_sheet.cell(237,1)
        documentPath = cell1.value
        
        cell1 = first_sheet.cell(236,1)
        timetoUploadDoc = cell1.value
        
        cell1 = first_sheet.cell(238,1)
        timeToUploaddocument = cell1.value
        
        cell1 = first_sheet.cell(239,1)
        questionCard = cell1.value
        
        cell1 = first_sheet.cell(240,1)
        ans1 = cell1.value
        
        cell1 = first_sheet.cell(241,1)
        ans2 = cell1.value
        
        
        
        try:
            print "\n\n----This Test case creates campaigns with Four Lesson----\n1. Document\n2. Question\n3. All Cards\n4. All Cards two times\n"
            cd=CreateLessonDifferentLessons()
            cd.lessonWithDocument(lessonName1, documentPath, timeToUploaddocument)
            cd.lessonWithQuestion(lessonName2, questionCard, ans1, ans2)
            
            newobj=CreateCampaignForFourLessonsThree()
            newobj.allCardsOneTime(lessonName3, textCard, Imagefilepath1, videoPath, timeToUploadVideo, documentPath, timetoUploadDoc, questionCard, ans1, ans2)
            newobj.allCardstwoTime(lessonName4, textCard, Imagefilepath1, videoPath, timeToUploadVideo, documentPath, timetoUploadDoc, questionCard, ans1, ans2)
            newobj.createCampaignFourLessonsCombiThree(campaignTitle, campDescription, actualSuccessMessage, lessonName1, lessonName2, lessonName3, lessonName4, minPassingScore, numberOfAttempts)
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
                lesdel=DeleteLesson()
                lesdel.lessonDelete(lessonName1)
                lesdel.lessonDelete(lessonName2)
                lesdel.lessonDelete(lessonName3)
                lesdel.lessonDelete(lessonName4)
            except Exception:
                driver.get(url)
        
        
        

    
