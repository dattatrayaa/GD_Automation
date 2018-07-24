'''
Created on 24-Jul-2018

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
from CreateLessonDifferentLessons import CreateLessonDifferentLessons

class LessonWithSameNameValidation:
    
    
    def lessonWithImage(self,lessonName,Imagefilepath1,newLessonName):
        
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
        e.imageCard(Imagefilepath1)
        
        
        
        time.sleep(2)
        print "Publishing lesson"
        lessons.readyToPublishButtonClick()
        print "Clicked on Ready to publish button"
        
        lessons.publishButtonClick()
        print "Clicked on Publish button"
        
        print "Checking validation message is displayed"
        try:
            ele=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.validationMessageForDuplicateTitle())))
            ele.click()
        except Exception as e:
            print e
            traceback.print_exc()
            raise Exception("Validation message is not displayed")
        print ele.text  
        if "We couldn't publish your lesson because..." in ele.text:
            print "Message '"+ele.text+"' is displayed successfully"
        else:
            raise Exception("Validation message displayed is not valid")
        
        print "Clicking on Edit button displayed to change title"
        try:
            ele=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.titleEditButton())))
            ele.click()
            print "Clicked on Edit button"
        except Exception as e:
            print e
            traceback.print_exc()
            raise Exception("Validation message is not displayed")
        print newLessonName
        print "Changing title"
        try:
            lessons.settingLessonName(newLessonName)
            print "new lesson name set as: "+lessonName+newLessonName
        except Exception as e:
            print e
            traceback.print_exc()
            raise Exception("Failed to set the new title")
        
        print "Publishing lesson"
        lessons.readyToPublishButtonClick()
        print "Clicked on Ready to publish button"
        
        lessons.publishButtonClick()
        print "Clicked on Publish button"
        
        print "Lesson published"
        
        lessons.backButton()
        
        print "Verifying lesson displayed in Grid"
        try:
            lessons.lessonInGrid(lessonName+newLessonName)
            print "Lesson displayed in Grid"
        except Exception as e:
            print e
            traceback.print_exc()
            raise Exception("Lesson not displayed in grid")
        
        
        lessons.expandSideMenu()
        
        
        
        
    
    
    def lessonWithSameNameValidationMain(self):
        
        book=xlrd.open_workbook(os.path.join('TestData.xlsx'))
        first_sheet = book.sheet_by_name('LessonCreate')
        
        cell1 = first_sheet.cell(103,1)
        lessonName = cell1.value
        
        cell2 = first_sheet.cell(104,1)
        textCard = cell2.value
        
        cell2 = first_sheet.cell(105,1)
        Imagefilepath1 = cell2.value
        
        newLessonName="new"
        
        try:
            print "\nCreating two different lessons with same Name\n"
            cr=CreateLessonDifferentLessons()
            print "\nFirst lesson\n"
            cr.lessonWithText(lessonName, textCard)
            
            print "\nNow creating second lesson with same name and verifying validation message is displayed"
            
            
            li=LessonWithSameNameValidation()
            li.lessonWithImage(lessonName, Imagefilepath1, newLessonName)
        finally:  
            second_sheet = book.sheet_by_name('Login_Credentials')
            cell = second_sheet.cell(1,1)
            url = cell.value
            driver.get(url)
            
            try:
                delLesson=DeleteLesson()
                delLesson.lessonDelete(lessonName)
                delLesson.lessonDelete(lessonName+newLessonName)
            except Exception:
                driver.get(url)



if __name__ == '__main__':
    
    b=BaseTestClass()
    b.UserLogin()
    
    r=LessonWithSameNameValidation()
    r.lessonWithSameNameValidationMain()
    
    

    

    
    
    
    