'''
Created on 26-Feb-2018

@author: Sheethu C
'''
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
from TagPageElements import TagPageElements
from CreateLessonDifferentLessons import CreateLessonDifferentLessons
from CreateTrackComman import CreateTrackComman
from DeleteTag import DeleteTag
from BaseTestClass import projectPath
class LibraryTrackLessonQuestion():
    
    
        
    def taglessonWithQuestionAnswerCard(self):
        
        
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        first_sheet = book.sheet_by_name('TagTrackLesson')
       
        
        cell1 = first_sheet.cell(10,1)
        titleOfTrack = cell1.value
        
        cell2 = first_sheet.cell(11,1)
        Imagefilepath = cell2.value
        
        cell2 = first_sheet.cell(12,1)
        description = cell2.value
        
        cell2 = first_sheet.cell(13,1)
        tagName = cell2.value
        
        cell2 = first_sheet.cell(10,3)
        lessonname= cell2.value
        
      
        cell2 = first_sheet.cell(14,1)
        expectedSuccessText= cell2.value
        
       
        cell2 = first_sheet.cell(11,3)
        question = cell2.value
        
        cell3 = first_sheet.cell(12,3)
        ans1 = cell3.value
        
        cell4 = first_sheet.cell(13,3)
        ans2 = cell4.value
     
        
        cell1 = first_sheet.cell(10,1)
        TrackName = cell1.value
        
        first_sheet = book.sheet_by_name('AssignCreateTag')
        print("Fetching the Attribute Name from Excel Sheet\n")
        # read a cell
        cell = first_sheet.cell(5,2)
        TagName = cell.value
        print TagName
        
        cell = first_sheet.cell(5,3)
        ExpectedSuccessMessage = cell.value
        print ExpectedSuccessMessage
        
        cell = first_sheet.cell(5,4)
        ExpectedTrackMessage = cell.value
       
        cell = first_sheet.cell(5,5)
        ExpectedAddLessonMessage = cell.value
        
        
        
     
        try:     
            cd=CreateLessonDifferentLessons()
            cd.lessonWithQuestion(lessonname, question, ans1, ans2)
            
            ct=CreateTrackComman()
            ct.createTrack(titleOfTrack, Imagefilepath, description, tagName, lessonname, expectedSuccessText)
            que=TagPageElements()
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
  #  btc=BaseTestClass()
   # btc.UserLogin()
    
   # m1=TagTrackLessonQuestion()
  #  m1.taglessonWithQuestionAnswerCard()
       
