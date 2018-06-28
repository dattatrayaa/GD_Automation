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
from CreateLessonDifferentLessons import CreateLessonDifferentLessons
from CreateTrackComman import CreateTrackComman
from DeleteTag import DeleteTag
from BaseTestClass import projectPath
class TagTrackLessonImage():
    def lessonImageAssignTag(self):
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        first_sheet = book.sheet_by_name('TagTrackLesson')
        cell1 = first_sheet.cell(18,1)
        titleOfTrack = cell1.value
        
        cell2 = first_sheet.cell(19,1)
        Imagefilepath = cell2.value
        
        cell2 = first_sheet.cell(20,1)
        description = cell2.value
        
        cell2 = first_sheet.cell(21,1)
        tagName = cell2.value
        
        cell2 = first_sheet.cell(18,3)
        lessonname= cell2.value
        
      
        cell2 = first_sheet.cell(22,1)
        expectedSuccessText= cell2.value
        
       
        cell2 = first_sheet.cell(19,3)
        ImagefilepathforLesson = cell2.value
        
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        first_sheet = book.sheet_by_name('AssignCreateTag')
        
        # read a cell
        cell = first_sheet.cell(2,2)
        TagName = cell.value
        
        cell = first_sheet.cell(2,3)
        ExpectedSuccessMessage = cell.value
        
        cell = first_sheet.cell(2,4)
        ExpectedTrackMessage = cell.value
     
        cell1 = first_sheet.cell(2,5)
        ExpectedAddLessonMessage =cell1.value
        
         
        
        first_sheet = book.sheet_by_name('TagTrackLesson')
        
        cell1 = first_sheet.cell(18,1)
        TrackName = cell1.value
        
        
        try:
            cd=CreateLessonDifferentLessons()
            cd.lessonWithImage(lessonname, ImagefilepathforLesson)
            
            ct=CreateTrackComman()
            ct.createTrack(titleOfTrack, Imagefilepath, description, tagName, lessonname, expectedSuccessText)
            
            img=TagPageElements()
            img.tagCreation(TagName)
            img.addlesson(lessonname)
            img.addTrack(TrackName)  
            img.library(TagName)
            img.lessonLibrary(lessonname)
            img.trackLibray(TrackName)
            
            
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
    #btc.UserLogin()
    
  #  m1=TagTrackLessonImage()
  #  m1.lessonImageAssignTag()
       
