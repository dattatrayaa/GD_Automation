'''
Created on 23-Feb-2018

@author: dattatraya
'''

import os.path
import time
import traceback

from BaseTestClass import BaseTestClass
from BaseTestClass import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xlrd

from CreateLessonDifferentCards import CreateLessonDifferentCards
from CreateTrackComman import CreateTrackComman
from DeleteLesson import DeleteLesson
from LessonsPageElements import LessonsPageElements
from BaseTestClass import projectPath

class TrackWithTxtVidQueLesson:
    
    def createLessonTxtVidQue(self,lessonName,textCard,videoPath,timeToUploadVideo,questionCard, ans1, ans2):
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
        objforThis=CreateLessonDifferentCards()
        
        objforThis.textCard(textCard)
        objforThis.textCard(textCard)
        objforThis.textCard(textCard)
        objforThis.textCard(textCard)
        objforThis.textCard(textCard)
        
        #Image card
        objforThis.videoCard(videoPath, timeToUploadVideo)
        objforThis.videoCard(videoPath, timeToUploadVideo)
        objforThis.videoCard(videoPath, timeToUploadVideo)
        objforThis.videoCard(videoPath, timeToUploadVideo)
        objforThis.videoCard(videoPath, timeToUploadVideo)
        
        
        #Question card
        objforThis.quesCard(questionCard, ans1, ans2)
        objforThis.quesCard(questionCard, ans1, ans2)
        objforThis.quesCard(questionCard, ans1, ans2)
        objforThis.quesCard(questionCard, ans1, ans2)
        objforThis.quesCard(questionCard, ans1, ans2)
        objforThis.textCard(textCard)
        
        print "All Cards inserted"
        
        
        print "Publishing lesson"
        
        time.sleep(4)
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
        
    
         
        
    def lessonWithTextVideoQuestionCard(self):
        
        
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        first_sheet = book.sheet_by_name('TrackCreate')
        
        #Track Data
        cell1 = first_sheet.cell(60,1)
        titleOfTrack = cell1.value
        
        cell2 = first_sheet.cell(61,1)
        Imagefilepath = cell2.value
        
        cell2 = first_sheet.cell(62,1)
        description = cell2.value
        
        cell2 = first_sheet.cell(63,1)
        tagName = cell2.value
        
      
        cell2 = first_sheet.cell(64,1)
        expectedSuccessText= cell2.value
        
        # Lesson Data
        cell2 = first_sheet.cell(60,3)
        lessonname= cell2.value
        
        cell2 = first_sheet.cell(61,3)
        textCard= cell2.value
        
        cell2 = first_sheet.cell(62,3)
        videoPath= cell2.value
       
        cell2 = first_sheet.cell(63,3)
        questionCard = cell2.value
        
        cell3 = first_sheet.cell(64,3)
        ans1 = cell3.value
        
        cell4 = first_sheet.cell(65,3)
        ans2 = cell4.value
        
        cell4 = first_sheet.cell(66,3)
        timeToUploadVideo= cell4.value
     
     
        try:
                 
            que=TrackWithTxtVidQueLesson()
            que.createLessonTxtVidQue(lessonname, textCard, videoPath, questionCard, ans1, ans2,200)
            
            t=CreateTrackComman()
            t.createTrack(titleOfTrack, Imagefilepath, description, tagName, lessonname, expectedSuccessText)
            
            
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
                d=DeleteLesson()
                d.lessonDelete(lessonname)
            except Exception:
                driver.get(url)
                

if __name__ == '__main__':
    btc=BaseTestClass()
    btc.UserLogin()
    
    m1=TrackWithTxtVidQueLesson()
    m1.lessonWithTextVideoQuestionCard()
       

        
