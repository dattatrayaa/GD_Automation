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
from DeleteTag import DeleteTag
from CreateLessonDifferentCards import CreateLessonDifferentCards
from LessonsPageElements import LessonsPageElements
from CreateTrackComman import CreateTrackComman
from BaseTestClass import projectPath
class LibraryTracklessonFiveTextImageQuestion():
    
    def createLessonTxtImgQue(self,lessonName,textCard,Imagefilepath1,questionCard, ans1, ans2):
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
        objforThis.imageCard(Imagefilepath1)
        objforThis.imageCard(Imagefilepath1)
        objforThis.imageCard(Imagefilepath1)
        objforThis.imageCard(Imagefilepath1)
        objforThis.imageCard(Imagefilepath1)
        
        #Question card
        objforThis.quesCard(questionCard, ans1, ans2)
        objforThis.quesCard(questionCard, ans1, ans2)
        objforThis.quesCard(questionCard, ans1, ans2)
        objforThis.quesCard(questionCard, ans1, ans2)
        objforThis.quesCard(questionCard, ans1, ans2)
        objforThis.textCard(textCard)
        time.sleep(2)
        
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
    
    
    def taglessonWithTextImageQuestionCard(self):
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        first_sheet = book.sheet_by_name('TagTrackLesson')
        
        #Track Data
        cell1 = first_sheet.cell(43,1)
        titleOfTrack = cell1.value
        
        cell1 = first_sheet.cell(43,1)
        TrackName = cell1.value
        
        cell2 = first_sheet.cell(44,1)
        Imagefilepath = cell2.value
        
        cell2 = first_sheet.cell(45,1)
        description = cell2.value
        
        cell2 = first_sheet.cell(46,1)
        tagName = cell2.value
        
      
        cell2 = first_sheet.cell(47,1)
        expectedSuccessText= cell2.value
        
        # Lesson Data
        cell2 = first_sheet.cell(43,3)
        lessonname= cell2.value
        
        cell2 = first_sheet.cell(44,3)
        textCard= cell2.value
        
        cell2 = first_sheet.cell(45,3)
        Imagefilepath1= cell2.value
       
        cell2 = first_sheet.cell(46,3)
        questionCard = cell2.value
        
        cell3 = first_sheet.cell(47,3)
        ans1 = cell3.value
        
        cell4 = first_sheet.cell(48,3)
        ans2 = cell4.value
        
        first_sheet = book.sheet_by_name('AssignCreateTag')
       
        cell = first_sheet.cell(8,2)
        TagName = cell.value
        print TagName
        
        cell = first_sheet.cell(8,3)
        ExpectedSuccessMessage = cell.value
        print ExpectedSuccessMessage
       
        cell = first_sheet.cell(8,4)
        ExpectedTrackMessage = cell.value
       
        cell = first_sheet.cell(8,5)
        ExpectedAddLessonMessage = cell.value 
     
     
        try:
           
            qu=TagTracklessonFiveTextImageQuestion()
            qu.createLessonTxtImgQue(lessonname, textCard, Imagefilepath1, questionCard, ans1, ans2)
            
            
            ct=CreateTrackComman()
            ct.createTrack(titleOfTrack, Imagefilepath, description, tagName, lessonname, expectedSuccessText)
        
            que=TagPageElements()
            driver.refresh()
            que.tagCreation(TagName)
            que.addlesson(lessonname)
            que.addTrack(TrackName)  
            que.library(TagName)
            que.lessonLibrary(lessonname)
            que.trackLibray(TrackName)
            
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
                tagde.tagDeletion(TagName)
            except Exception:
                driver.get(url)
            try:
                lesdel= DeleteLesson()
                lesdel.lessonDelete(lessonname) 
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
    
   # btc=BaseTestClass()
    #btc.UserLogin()
   # m1=TagTracklessonFiveTextImageQuestion()
  #  m1.taglessonWithTextImageQuestionCard()
