'''
Created on 26-Feb-2018

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
from LessonsPageElements import LessonsPageElements
from DeleteLesson import DeleteLesson
from BaseTestClass import projectPath

class TrackWithAllCardsOne:
    
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
    
   
        
       
    def trackWithAllCards(self):
        
        
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        first_sheet = book.sheet_by_name('TrackCreate')
        
        #Track Data
        cell1 = first_sheet.cell(118,1)
        titleOfTrack = cell1.value
        
        cell2 = first_sheet.cell(119,1)
        Imagefilepath = cell2.value
        
        cell2 = first_sheet.cell(120,1)
        description = cell2.value
        
        cell2 = first_sheet.cell(121,1)
        tagName = cell2.value
        
      
        cell2 = first_sheet.cell(122,1)
        expectedSuccessText= cell2.value
        
        # Lesson Data
        
        cell2 = first_sheet.cell(118,3)
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
        
        cell2 = first_sheet.cell(122,3)
        timetoUploadDoc = cell2.value
         
        cell2 = first_sheet.cell(124,3)
        questionCard = cell2.value
        
        cell3 = first_sheet.cell(125,3)
        ans1 = cell3.value
        
        cell4 = first_sheet.cell(126,3)
        ans2 = cell4.value
        
        
        try:
            print "\nCreating Lesson\n"
            tri=TrackWithAllCardsOne()
            tri.allCardsOneTime(lessonName, textCard, Imagefilepath1, videoPath, timeToUploadVideo, documentPath, timetoUploadDoc, questionCard, ans1, ans2)
            
            print "\nCreate Track\n"
            ct=CreateTrackComman()
            ct.createTrack(titleOfTrack, Imagefilepath, description, tagName, lessonName, expectedSuccessText)
        
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
    
    m1=TrackWithAllCardsOne()
    m1.trackWithAllCards()
    