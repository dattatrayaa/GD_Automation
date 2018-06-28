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
from TagPageElements import TagPageElements
from DeleteTag import DeleteTag
from CreateLessonDifferentLessons import CreateLessonDifferentLessons
from CreateTrackComman import CreateTrackComman
from BaseTestClass import projectPath
class TagTrackLessonVideo():
    
        
    def lessonVideoAssignTag(self):
        
        
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        
        first_sheet = book.sheet_by_name('TagTrackLesson')
        
        cell1 = first_sheet.cell(26,1)
        titleOfTrack = cell1.value
        
        cell1 = first_sheet.cell(27,1)
        Imagefilepath = cell1.value
        
        cell1 = first_sheet.cell(28,1)
        description = cell1.value
        
        cell1 = first_sheet.cell(29,1)
        tagName = cell1.value
        
        cell1 = first_sheet.cell(26,3)
        lessonname= cell1.value
        
      
        cell1 = first_sheet.cell(30,1)
        expectedSuccessText= cell1.value
        
       
        cell1 = first_sheet.cell(27,3)
        videoPath = cell1.value
        
        cell1 = first_sheet.cell(28,3)
        timeToUploadVideo = cell1.value
        
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        first_sheet = book.sheet_by_name('AssignCreateTag')
        print("Fetching the Attribute Name from Excel Sheet\n")
        # read a cell
        cell = first_sheet.cell(3,2)
        TagName = cell.value
        print TagName
        
        cell = first_sheet.cell(3,3)
        ExpectedSuccessMessage = cell.value
        print ExpectedSuccessMessage
        cell = first_sheet.cell(3,4)
        ExpectedTrackMessage = cell.value
       
        cell = first_sheet.cell(3,5)
        ExpectedAddLessonMessage = cell.value
         
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        first_sheet = book.sheet_by_name('TagTrackLesson')
        
        cell = first_sheet.cell(26,1)
        
        TrackName = cell.value
        cell = first_sheet.cell(26,1)
        ExpectedSuccessMessage = cell.value
        try:
           
            cd=CreateLessonDifferentLessons()
            cd.lessonWithVideo(lessonname, videoPath, timeToUploadVideo)
            
            ct=CreateTrackComman()
            ct.createTrack(titleOfTrack, Imagefilepath, description, tagName, lessonname, expectedSuccessText)
            
            vid=TagPageElements()
            vid.tagCreation(TagName)
            vid.addlesson(lessonname)
            vid.addTrack(titleOfTrack)  
            vid.library(TagName)
            vid.lessonLibrary(lessonname)
            vid.trackLibray(titleOfTrack)
            
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
  #  btc.UserLogin()
    
  #  m1=TagTrackLessonVideo()
  #  m1.lessonVideoAssignTag()
       
