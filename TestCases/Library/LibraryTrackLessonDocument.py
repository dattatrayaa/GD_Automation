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
from DeleteLesson import DeleteLesson
from BaseTestClass import driver
from CreateTrackComman import CreateTrackComman
from CreateLessonDifferentLessons import CreateLessonDifferentLessons
from DeleteTag import DeleteTag
from TagPageElements import TagPageElements
from BaseTestClass import projectPath
class LibraryTrackLessonDocument():
    def lessonWithDocumentAssignTag(self):
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        first_sheet = book.sheet_by_name('TagTrackLesson')
        
        cell1 = first_sheet.cell(34,1)
        titleOfTrack = cell1.value
        
        cell2 = first_sheet.cell(35,1)
        Imagefilepath = cell2.value
        
        cell2 = first_sheet.cell(36,1)
        description = cell2.value
        
        cell2 = first_sheet.cell(37,1)
        tagName = cell2.value
        
        cell2 = first_sheet.cell(34,3)
        lessonname= cell2.value
        
      
        cell2 = first_sheet.cell(38,1)
        expectedSuccessText= cell2.value
        
       
        cell2 = first_sheet.cell(35,3)
        documentPath = cell2.value
        
        cell2 = first_sheet.cell(36,3)
        timeToUploaddocument = cell2.value
        
        cell1 = first_sheet.cell(34,1)
        TrackName = cell1.value
        
        first_sheet = book.sheet_by_name('AssignCreateTag')
        # read a cell
        cell = first_sheet.cell(4,2)
        TagName = cell.value
        print TagName
        
        cell = first_sheet.cell(4,3)
        ExpectedSuccessMessage = cell.value
        print ExpectedSuccessMessage
        
        cell = first_sheet.cell(4,4)
        ExpectedTrackMessage = cell.value
       
        cell = first_sheet.cell(4,5)
        ExpectedAddLessonMessage = cell.value
        
        try:     
            doc=TagPageElements()
            cd=CreateLessonDifferentLessons()
            cd.lessonWithDocument(lessonname, documentPath, timeToUploaddocument)
            ct=CreateTrackComman()
            ct.createTrack(titleOfTrack, Imagefilepath, description, tagName, lessonname, expectedSuccessText)
            doc.tagCreation(TagName)
            doc.addlesson(lessonname)
            doc.addTrack(TrackName)  
            doc.library(TagName)
            doc.lessonLibrary(lessonname)
            doc.trackLibray(TrackName)
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
   # btc.UserLogin()
    
   # m1=CreateTagTrackLessonDocument()
   # m1.lessonWithDocumentAssignTag()
