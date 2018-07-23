'''
Created on 16-Jul-2018

@author: OptisLabs
'''

import traceback
import os
import time

from BaseTestClass import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xlrd

from CreateLessonDifferentCards import CreateLessonDifferentCards
from LessonsPageElements import LessonsPageElements
from DeleteLesson import DeleteLesson
from BaseTestClass import BaseTestClass

class LessonDuplicateForPublish:
    
    def lessonForDuplicateDraftStatus(self,lessonName,textCard,DuplicateDefaultLessonName):
        
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
        
        
        
        e=CreateLessonDifferentCards()
        e.textCard(textCard)
        
        
        
        time.sleep(10)
        
        time.sleep(2)
        print "Publishing lesson"
        lessons.readyToPublishButtonClick()
        
        print "Clicked on publish button"
        lessons.publishButtonClick()

        print "Lesson published"
        
        print "Clicking on Back button"
        lessons.backButton()
        
        print "Verifying Lesson displayed in grid"
        #Verifying created lesson is displayed in list
        lessons.lessonInGrid(lessonName)
        print "Lesson displayed in Grid"
        
    
        print "Clicking on Duplicate button of lessons '"+lessonName+"'"
        
        lessons.duplicateLesson(lessonName)
        
        print "Checking pop up is displayed"
        try:
            ele=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.duplicateLessonPopup())))
            print "Pop up '"+ele.text+"' pop up is displayed"
        except Exception as e:
            print e
            traceback.print_exc()
            raise Exception("Pop up is not displayed")
        
        print "Checking The lesson Title displayed with 'Copy' String"
        try:
            ele=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.DuplicateLessonName())))
            
        except Exception:
            traceback.print_exc()
            raise Exception("Lesson name not displayed in popup")
        attr=ele.get_attribute("value")
        print DuplicateDefaultLessonName+lessonName
        if attr==DuplicateDefaultLessonName+lessonName:
            print "Lesson '"+attr+"' displayed"
        else:
            raise Exception("Duplicate lesson name not displayed properly")
        
        
        print "Click on Save"
        lessons.duplicateLessonSaveButton()
        print "Clicked on Save button"
        
        ele=wait.until(EC.invisibility_of_element_located((By.XPATH,lessons.duplicateLessonPopup())))
        
        print "Checking lesson displayed in Grid"
        lessons.lessonInGrid(DuplicateDefaultLessonName+lessonName)
        print "lesson displayed in Grid"
        
    
    def editingDupllicateLessonAndPublish(self,lessonName,textCard,DuplicateDefaultLessonName):
        wait=WebDriverWait(driver, 60)
        driver.refresh()
        print "Clicking on Lessons button from side menu"
        
        lessons=LessonsPageElements()
        lessons.lessonsButtonSideMenuUnexpanded()
     
        print "Clicking on Edit lesson button"
        
        try:
            wait=WebDriverWait(driver, 60)
            ele=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.editLessonButton(DuplicateDefaultLessonName+lessonName))))
            ele.click()
            print "Clicked on Edit button of Lesson '"+DuplicateDefaultLessonName+lessonName+"' "
        except Exception:
            traceback.print_exc()
            raise Exception("Failed to click on edit button")
        
        print "Verifying title displayed"
        try:
            wait=WebDriverWait(driver, 60)
            ele=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.lessonTitleInBuilder())))
            titlein=ele.get_attribute("value")
            print "Lesson '"+titlein+"' displayed in Lesson builder"
        except Exception:
            traceback.print_exc()
            raise Exception("Failed to click on edit button")
        
        print "Checking in card same text is displayed as previous one"
        
        lessons.nextCard()
        print "Clicked on Text card"
        
        try:
            wait=WebDriverWait(driver, 60)
            ele=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.textCardVerifyTextEnteredXpath())))
            textInCard=ele.text
        except Exception:
            traceback.print_exc()
            raise Exception("Text in text card not displayed properly")
        
        if textCard==textInCard:
            print "Text '"+textCard+"' displayed in Lesson builder"
        else:
            print "Text is not matching with text card"
            raise Exception("Text is not matching with text card")
        
        
        try:
            lessons.readyToPublishButtonClick()
            print "Clicked on Ready to Publish button of Lesson '"+DuplicateDefaultLessonName+lessonName+"' "
        except Exception as e:
            print e
            traceback.print_exc()
            raise Exception("Failed to click on  ready to publish button")
        
        
        try:
            lessons.publishButtonClick()
            print "Clicked on Publish button of Lesson '"+DuplicateDefaultLessonName+lessonName+"' "
        except Exception as e:
            print e
            traceback.print_exc()
            raise Exception("Failed to click on publish button")
        
        print "Clicking on back button"
        lessons.backButton()
        
        print "Checking lesson displayed in Grid with published status"
        
        try:
            wait=WebDriverWait(driver, 60)
            ele=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.publishedStatus(DuplicateDefaultLessonName+lessonName))))
            print "Lesson displayed with '"+ele.text+"' status in Grid"
        except Exception as e:
            print e
            traceback.print_exc()
            raise Exception("Lesson not displayed with status published")
        
        
        
    def LessonDuplicateForDraftStatusMain(self):
        
        book=xlrd.open_workbook(os.path.abspath(os.path.join(os.path.dirname(__file__),'TestData.xlsx')))
        first_sheet = book.sheet_by_name('LessonCreate')
        
        cell1 = first_sheet.cell(97,1)
        lessonName = cell1.value
        
        cell2 = first_sheet.cell(98,1)
        textCard= cell2.value
        
        cell2 = first_sheet.cell(99,1)
        DuplicateDefaultLessonName= cell2.value
        
        try:
            
            print "\nCreating a duplicate lesson with Draft Status\n"
            un=LessonDuplicateForPublish()
            un.lessonForDuplicateDraftStatus(lessonName, textCard, DuplicateDefaultLessonName)
            
            print "\nPublishing created duplicate lesson\n"
            un.editingDupllicateLessonAndPublish(lessonName, textCard,DuplicateDefaultLessonName)
            print "\n----Test Execution Completed----\n"
            
            
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
                d=DeleteLesson()
                d.lessonDelete(lessonName)
                d.lessonDelete(DuplicateDefaultLessonName+lessonName)
            except Exception:
                driver.get(url)
            
            
            
            
if __name__ == '__main__':
    
    btc=BaseTestClass()
    btc.UserLogin()
    
    les=LessonDuplicateForPublish()
    les.LessonDuplicateForDraftStatusMain()
        
        
