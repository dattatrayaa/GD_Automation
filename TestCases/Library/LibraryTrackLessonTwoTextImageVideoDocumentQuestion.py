'''
Created on 26-Feb-2018

@author: Sheethu C
'''
from operator import contains
import os.path
import time
import traceback

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.support.ui import WebDriverWait
import xlrd
from BaseTestClass import driver
from DeleteLesson import DeleteLesson
from TagPageElements import TagPageElements
from CreateTrackComman import CreateTrackComman
from CreateLessonDifferentCards import CreateLessonDifferentCards
from DeleteTag import DeleteTag
from LessonsPageElements import LessonsPageElements
from BaseTestClass import projectPath
class LibraryTrackLessonTwoTextImageVideoDocumentQuestion():
    
    
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
    def tagtrackWithAllCardTwoTime(self):
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        first_sheet = book.sheet_by_name('TagTrackLesson')
        cell1 = first_sheet.cell(125,1)
        titleOfTrack = cell1.value
        cell1 = first_sheet.cell(125,1)
        TrackName = cell1.value
        cell2 = first_sheet.cell(119,1)
        Imagefilepath = cell2.value
        cell2 = first_sheet.cell(120,1)
        description = cell2.value
        cell2 = first_sheet.cell(121,1)
        tagName = cell2.value
        cell2 = first_sheet.cell(127,1)
        expectedSuccessText= cell2.value
        cell2 = first_sheet.cell(126,1)
        lessonName = cell2.value
        cell2 = first_sheet.cell(119,3)
        textCard = cell2.value
        cell2 = first_sheet.cell(120,3)
        Imagefilepath1 = cell2.value
        cell2 = first_sheet.cell(121,3)
        videoPath = cell2.value
        cell2 = first_sheet.cell(122,3)
        timeToUploadVideo = cell2.value
        cell2 = first_sheet.cell(123,3)
        documentPath= cell2.value
        cell2 = first_sheet.cell(124,3)
        questionCard = cell2.value
        cell3 = first_sheet.cell(125,3)
        ans1 = cell3.value
        cell4 = first_sheet.cell(126,3)
        ans2 = cell4.value
        cell2 = first_sheet.cell(122,3)
        timetoUploadDoc = cell2.value
        first_sheet = book.sheet_by_name('AssignCreateTag')
        cell = first_sheet.cell(7,2)
        TagName = cell.value
        cell = first_sheet.cell(7,3)
        ExpectedSuccessMessage = cell.value
        cell = first_sheet.cell(7,4)
        ExpectedTrackMessage = cell.value
       
        cell = first_sheet.cell(7,5)
        ExpectedAddLessonMessage = cell.value
        
        
        
        try:
            tr=TagTrackLessonTwoTextImageVideoDocumentQuestion()
            tr.allCardstwoTime(lessonName, textCard, Imagefilepath1, videoPath, timeToUploadVideo, documentPath, timetoUploadDoc, questionCard, ans1, ans2)
            
            print "\nCreating Track\n"
            ct=CreateTrackComman()
            ct.createTrack(titleOfTrack, Imagefilepath, description, tagName, lessonName, expectedSuccessText)
            
            tri=TagPageElements()
            tri.tagCreation(TagName)
            tri.addlesson(lessonName)
            tri.addTrack(TrackName)  
            tri.library(TagName)
            tri.lessonLibrary(lessonName)
            tri.trackLibray(TrackName)
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
                lesdel.lessonDelete(lessonName) 
            except Exception:
                driver.get(url)
            driver.get(url)
            try:
                WebDriverWait(driver, 5).until(EC.alert_is_present())

                alert = driver.switch_to.alert
                alert.accept()
                print("alert accepted")
            except Exception:
                print("no alert")

#if __name__ == '__main__':
  #  btc=BaseTestClass()
   # btc.UserLogin()
    
  #  m1=TagTrackLessonTwoTextImageVideoDocumentQuestion()
  #  m1.tagtrackWithAllCardTwoTime()
