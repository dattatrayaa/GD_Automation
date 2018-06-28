'''
Created on 27-Feb-2018

@author: Sheethu C
'''
import os.path
import time
import traceback

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xlrd
from DeleteLesson import DeleteLesson
from BaseTestClass import driver
from TagPageElements import TagPageElements
from LessonsPageElements import LessonsPageElements
from CreateLessonDifferentCards import CreateLessonDifferentCards
from TracksPageElements import TracksPageElements
from DeleteTag import DeleteTag
from BaseTestClass import projectPath
class TagTrackWithfourlessonsFourFiveSixSeven():
    def allCardstwoTime(self,lessonName,textCard,Imagefilepath1,videoPath, timeToUploadVideo,documentPath,questionCard, ans1, ans2):
        
        
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
        
        time.sleep(4)
        #objfore.docCard(documentPath, timetoUploadDoc)
        #objfore.docCard(documentPath, timetoUploadDoc)
        
        
        objfore.quesCard(questionCard, ans1, ans2)
        objfore.quesCard(questionCard, ans1, ans2)
        objfore.textCard(textCard)
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
        objFor.docCard(documentPath, timetoUploadDoc)
        objFor.quesCard(questionCard, ans1, ans2)
        objFor.docCard(documentPath, timetoUploadDoc)
        objFor.quesCard(questionCard, ans1, ans2)
        objFor.docCard(documentPath, timetoUploadDoc)
        #Question card
        objFor.quesCard(questionCard, ans1, ans2)
        objFor.docCard(documentPath, timetoUploadDoc)
        objFor.quesCard(questionCard, ans1, ans2)
        objFor.docCard(documentPath, timetoUploadDoc)
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
    def tagtrackTagTrackWithfourlessonsFourFiveSixSeven(self):
        
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        first_sheet = book.sheet_by_name('TagTrackLesson')
        
        #Track Data
        cell1 = first_sheet.cell(157,1) 
        titleOfTrack = cell1.value
        
        cell1 = first_sheet.cell(157,1) 
        TrackName = cell1.value
        
        
        
        cell2 = first_sheet.cell(158,1)
        Imagefilepath = cell2.value
        
        cell2 = first_sheet.cell(159,1)
        description = cell2.value
        
        cell2 = first_sheet.cell(160,1)
        tagName = cell2.value
      
        cell2 = first_sheet.cell(161,1)
        expectedSuccessText= cell2.value
        
        # Lesson Data
        
        cell2 = first_sheet.cell(163,1)
        lessonName1= cell2.value
        
        cell2 = first_sheet.cell(164,1)
        lessonName2 = cell2.value
        
        cell2 = first_sheet.cell(165,1)
        lessonName3 = cell2.value
        
        cell2 = first_sheet.cell(166,1)
        lessonName4 = cell2.value
        
        cell2 = first_sheet.cell(157,3)
        textCard = cell2.value
        
        cell2 = first_sheet.cell(158,3)
        Imagefilepath1 = cell2.value
        
        cell2 = first_sheet.cell(159,3)
        videoPath = cell2.value
        
        cell2 = first_sheet.cell(160,3)
        timeToUploadVideo = cell2.value
        
        cell2 = first_sheet.cell(161,3)
        documentPath = cell2.value
        
        cell2 = first_sheet.cell(162,3)
        timetoUploadDoc = cell2.value
        
        cell2 = first_sheet.cell(163,3)
        questionCard = cell2.value
        
        cell3 = first_sheet.cell(164,3)
        ans1 = cell3.value
        
        cell4 = first_sheet.cell(165,3)
        ans2 = cell4.value
     
       
        
        print "\n\nSetting Pre-requisite"
        print "Creating Two lessons\n"
        
        first_sheet = book.sheet_by_name('AssignCreateTag')
        print("Fetching the Attribute Name from Excel Sheet\n")
        # read a cell
        cell = first_sheet.cell(17,2)
        TagName = cell.value
        print TagName
        
        cell = first_sheet.cell(17,3)
        ExpectedSuccessMessage = cell.value
        print ExpectedSuccessMessage
        
        cell = first_sheet.cell(17,4)
        ExpectedTrackMessage = cell.value
       
        cell = first_sheet.cell(17,5)
        ExpectedAddLessonMessage = cell.value
     
        try:     
            tr1=TagTrackWithfourlessonsFourFiveSixSeven()
            tr1.allCardstwoTime(lessonName1, textCard, Imagefilepath1, videoPath, timeToUploadVideo, documentPath, questionCard, ans1, ans2)
            tr1.createLessonTxtImgQue(lessonName2, textCard, Imagefilepath1, questionCard, ans1, ans2)
            tr1.createLessonVidDocQue(lessonName3, videoPath, documentPath, timetoUploadDoc, questionCard, ans1, ans2, timeToUploadVideo)
            tr1.createLessonTxtVidQue(lessonName4, textCard, videoPath, questionCard, ans1, ans2, timeToUploadVideo)
            
            tr1.createTrackwithFourLessons(titleOfTrack, Imagefilepath, description, tagName, lessonName1, lessonName2, lessonName3, lessonName4, expectedSuccessText)
           
            tr11=TagPageElements()
            tr11.tagCreation(TagName)
            tr11.addlesson(lessonName1)
            tr11.addlesson(lessonName2)
            tr11.addlesson(lessonName3)
            tr11.addlesson(lessonName4)
            tr11.addTrack(titleOfTrack)  
            tr11.library(TagName)
            tr11.lessonLibrary(lessonName1)
            tr11.lessonLibrary(lessonName2)
            tr11.lessonLibrary(lessonName3)
            tr11.lessonLibrary(lessonName4)
            tr11.trackLibray(titleOfTrack)
            
            
            
            
            driver.refresh()
            
            
        except Exception as e:
            traceback.print_exc()
            print (e)
            raise Exception
        finally: 
            second_sheet = book.sheet_by_name('Login_Credentials')
            cell = second_sheet.cell(1,1)
            url = cell.value
            try:
                tagde =DeleteTag()
                tagde.tagDeletion(tagName)
            except Exception:
                driver.get(url)
            try:
                lesdel= DeleteLesson()
                lesdel.lessonDelete(lessonName1)
                lesdel.lessonDelete(lessonName2)
                lesdel.lessonDelete(lessonName3)
                lesdel.lessonDelete(lessonName4) 
            except Exception:
                driver.get(url)
            
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

            
            