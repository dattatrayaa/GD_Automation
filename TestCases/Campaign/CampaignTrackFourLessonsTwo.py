'''
Created on 08-Mar-2018

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
from CreateLessonDifferentLessons import CreateLessonDifferentLessons
from DeleteLesson import DeleteLesson
from LessonsPageElements import LessonsPageElements
from TracksPageElements import TracksPageElements
from BaseTestClass import projectPath

class CampaignTrackFourLessonsTwo:
    
    def createLessonTxtVidQue(self,lessonName,textCard,videoPath,questionCard,ans1,ans2,timeToUploadVideo):
        
        
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
        
        
        objfor=CreateLessonDifferentCards()
        
        #Text Card
        objfor.textCard(textCard)
        objfor.textCard(textCard)
        objfor.textCard(textCard)
        objfor.textCard(textCard)
        objfor.textCard(textCard)
        
        objfor.textCard(textCard)
        objfor.textCard(textCard)
        objfor.textCard(textCard)
        objfor.textCard(textCard)
        objfor.textCard(textCard)
        
        # Video card
        objfor.videoCard(videoPath, timeToUploadVideo)
        objfor.videoCard(videoPath, timeToUploadVideo)
        objfor.videoCard(videoPath, timeToUploadVideo)
        objfor.videoCard(videoPath, timeToUploadVideo)
        objfor.videoCard(videoPath, timeToUploadVideo)
        
        objfor.videoCard(videoPath, timeToUploadVideo)
        objfor.videoCard(videoPath, timeToUploadVideo)
        objfor.videoCard(videoPath, timeToUploadVideo)
        objfor.videoCard(videoPath, timeToUploadVideo)
        objfor.videoCard(videoPath, timeToUploadVideo)
        
       
        time.sleep(4)
        #Question card
        objfor.quesCard(questionCard, ans1, ans2)
        objfor.quesCard(questionCard, ans1, ans2)
        objfor.quesCard(questionCard, ans1, ans2)
        objfor.quesCard(questionCard, ans1, ans2)
        objfor.quesCard(questionCard, ans1, ans2)
        
        objfor.quesCard(questionCard, ans1, ans2)
        objfor.quesCard(questionCard, ans1, ans2)
        objfor.quesCard(questionCard, ans1, ans2)
        objfor.quesCard(questionCard, ans1, ans2)
        objfor.quesCard(questionCard, ans1, ans2)
        objfor.textCard(textCard)
        
       
        
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
    
    
      
      
    def createTrackwithFourLessons(self,titleOfTrack,Imagefilepath,description,tagName,lessonName1,lessonName2,lessonName3,lessonName4,expectedSuccessText):
        print "\nCreating track with one lesson contains Text Card"
        driver.refresh()
        wait=WebDriverWait(driver, 120)
        track=TracksPageElements()
        
        print "Clicking on Lessons button from side menu"
        track.lessonsButton()
        
        print "Clicking on Track button from side menu"
        track.tracksButton()
        
        track.createTracksButton()
        
        print "Entering title"
        titlefield=wait.until(EC.visibility_of_element_located((By.XPATH,track.trackTitle())))
        titlefield.send_keys(titleOfTrack)
        print "Title entered ::"+titleOfTrack
        
        driver.find_element_by_css_selector('input[type="file"]').send_keys(Imagefilepath)
        print "waiting to upload image"
        wait.until(EC.visibility_of_element_located((By.XPATH,track.imageDisplayed())))
        print "Image uploaded"
        
        print "Entering Description"
        driver.find_element_by_xpath(track.trackDescription()).send_keys(description)
        print "Description entered ::"+description 
        
        
        print "Adding tag"
        addTags=driver.find_element_by_xpath(track.addingTag())
        webdriver.ActionChains(driver).move_to_element(addTags).click().send_keys(tagName).perform()
        
        option=wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='react-select-2--option-0']")))
        webdriver.ActionChains(driver).move_to_element(option).click(option).perform()
        
        driver.find_element_by_xpath(track.trackDescription()).send_keys(" ")
        
        
        print "\nAdding created two lessons"
        
        print "Clicking on Add lessons button"
       
        driver.execute_script("window.scrollTo(0, 0);")
        
        track.addLessonButton()
                
        wait.until(EC.visibility_of_element_located((By.XPATH,track.serchLesson())))
        
        searchLesson=driver.find_element_by_xpath(track.serchLesson())
        print "Searching for first lesson in Add lessons pop up"
        searchLesson.send_keys(lessonName1)
        track.searchedLessonAdd(lessonName1)
        
        time.sleep(2)
        print "Searching for Second lesson in Add lessons pop up"
        searchLesson.clear()
        searchLesson.send_keys(lessonName2)
        track.searchedLessonAdd(lessonName2)
        
        time.sleep(2)
        print "Searching for Third lesson in Add lessons pop up"
        searchLesson.clear()
        searchLesson.send_keys(lessonName3)
        track.searchedLessonAdd(lessonName3)
        
        
        
        print "Searching for Fourth lesson in Add lessons pop up"
        searchLesson.clear()
        time.sleep(1)
        searchLesson.send_keys(lessonName4)
        track.searchedLessonAdd(lessonName4)
        
     
        print "Adding to Track"
        track.addingToTrack()
        
        print "\nChecking added lesson is selected lesson from Pop up"
        
        
        lessonTextAddedToGrid=driver.find_element_by_xpath("//li[1]/div[2]/div/h4/div").text
        if lessonTextAddedToGrid==lessonName1:
            print "Selected Lesson '"+lessonName1+"' is displayed in grid of tracks page"
        
        else:
            print "Lesson is not displayed"
            raise Exception
        
        lessonTextAddedToGrid1=driver.find_element_by_xpath("//li[2]/div[2]/div/h4/div").text
        if lessonTextAddedToGrid1==lessonName2:
            print "Selected Lesson '"+lessonName2+"' is displayed in grid of tracks page"
        
        else:
            print "Lesson is not displayed"
            raise Exception
        
        lessonTextAddedToGrid2=driver.find_element_by_xpath("//li[3]/div[2]/div/h4/div").text
        if lessonTextAddedToGrid2==lessonName3:
            print "Selected Lesson '"+lessonName3+"' is displayed in grid of tracks page"
        
        else:
            print "Lesson is not displayed"
            raise Exception
        
        lessonTextAddedToGrid2=driver.find_element_by_xpath("//li[4]/div[2]/div/h4/div").text
        if lessonTextAddedToGrid2==lessonName4:
            print "Selected Lesson '"+lessonName4+"' is displayed in grid of tracks page"
        
        else:
            print "Lesson is not displayed"
            raise Exception
        
        
        
        #Publishing Track
        print "Clicking on Publish Track button"
        
        track.publishButton()        
        print "\nVerifying Success message is displaying"
        
        
        track.successmessage(expectedSuccessText, titleOfTrack)
        
        
        track.sideMenuTracksExpanded()
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"//tbody/tr/td[2]/a[.='"+titleOfTrack+"']")))
        
        trackInGrid=driver.find_element_by_xpath("//tbody/tr/td[2]/a[.='"+titleOfTrack+"']").text
        
        if trackInGrid==titleOfTrack:
            print "Track '"+trackInGrid+"' is displayed in grid"
        else:
            print "Track is not displayed in grid"
            raise Exception
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[1]/div/nav/div/div[4]").click()
         
    def campWithTrackFourLessonsTwo(self,campaignTitle,campDescription,trackName,actualSuccessMessage,ownDuration,minPassingScore,numberOfAttempts):
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
        
        print "Making This as a Graded Campaign"
        elements.makeThisAsAGradedCampaign()
        
        print "Setting Minimum passing score"
        elements.setMinimumPassingScore(minPassingScore)
        
        print "Setting Number of allowed attempts"
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
        
        #verifying in Campaigns displayed in Campaigns grid
        elements.searchingForlesson(campaignTitle)
        
        if elements.actualCampTitleINGrid()==campaignTitle:
            print "Campaign '"+campaignTitle+"' displayed in Grid"
        
        else:
            print "Campaign is not displayed in Grid"
            raise Exception
        
        
        print "\n----Text Execution Completed----\n"    
        
        
        
    def CampaignForTrackWithFourLessonsTwo(self):
        
        
        
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        first_sheet = book.sheet_by_name('CreateCampaigns')
        
        cell1 = first_sheet.cell(276,1)
        campaignTitle = cell1.value
        
        cell1 = first_sheet.cell(277,1)
        campDescription = cell1.value
        
        cell1 = first_sheet.cell(278,1)
        actualSuccessMessage = cell1.value
        
        cell2 = first_sheet.cell(279,1)
        ownDuration= cell2.value
        
        cell2 = first_sheet.cell(280,1)
        minPassingScore= cell2.value
        
        cell2 = first_sheet.cell(281,1)
        numberOfAttempts= cell2.value
        
        #Track
        cell1 = first_sheet.cell(283,1)
        titleOfTrack = cell1.value
        
        cell2 = first_sheet.cell(284,1)
        Imagefilepath = cell2.value
        
        cell2 = first_sheet.cell(285,1)
        description = cell2.value
        
        cell2 = first_sheet.cell(286,1)
        tagName = cell2.value
        
        cell2 = first_sheet.cell(287,1)
        expectedSuccessText= cell2.value
        
        
        #Lesson
        cell2 = first_sheet.cell(289,1)
        lessonName1= cell2.value
        
        
        cell2 = first_sheet.cell(290,1)
        lessonName2= cell2.value
        
        cell2 = first_sheet.cell(291,1)
        lessonName3= cell2.value
        
        cell2 = first_sheet.cell(292,1)
        lessonName4= cell2.value
        
        cell2 = first_sheet.cell(293,1)
        textCard= cell2.value
        
        cell2 = first_sheet.cell(294,1)
        Imagefilepath1= cell2.value
        
        
        cell2 = first_sheet.cell(295,1)
        videoPath= cell2.value
        
        cell2 = first_sheet.cell(296,1)
        timeToUploadVideo= cell2.value
        
        
        cell2 = first_sheet.cell(297,1)
        questionCard= cell2.value
        
        cell2 = first_sheet.cell(298,1)
        ans1= cell2.value
        
        cell2 = first_sheet.cell(299,1)
        ans2= cell2.value
        
      
        
        try:
            #lesson Creation
            obj2=CampaignTrackFourLessonsTwo()
            obj2.createLessonTxtVidQue(lessonName1, textCard, videoPath, questionCard, ans1, ans2, timeToUploadVideo)
            
            ui=CreateLessonDifferentLessons()
            ui.lessonWithText(lessonName2, textCard)
            ui.lessonWithImage(lessonName3, Imagefilepath1)
            ui.lessonWithVideo(lessonName4, videoPath, timeToUploadVideo)
                        
            #Track Creation
            
            obj2.createTrackwithFourLessons(titleOfTrack, Imagefilepath, description, tagName, lessonName1, lessonName2, lessonName3, lessonName4, expectedSuccessText)
            
            #Campaign Creation
            
            obj2.campWithTrackFourLessonsTwo(campaignTitle, campDescription, titleOfTrack, actualSuccessMessage, ownDuration, minPassingScore, numberOfAttempts)
          
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
                lesdel.lessonDelete(lessonName1)
                lesdel.lessonDelete(lessonName2)
                lesdel.lessonDelete(lessonName3)
                lesdel.lessonDelete(lessonName4)
            except Exception:
                driver.get(url)
    
if __name__ == '__main__':
    
    btc=BaseTestClass()
    btc.UserLogin()
    
    ne=CampaignTrackFourLessonsTwo()
    ne.CampaignForTrackWithFourLessonsTwo()
 
 
 
