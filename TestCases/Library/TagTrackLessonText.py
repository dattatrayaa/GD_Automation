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
from DeleteTag import DeleteTag
from BaseTestClass import driver
from TagPageElements import TagPageElements
from CreateTrackComman import CreateTrackComman
from CreateLessonDifferentLessons import CreateLessonDifferentLessons
from BaseTestClass import projectPath
class TagTrackLessonText():
    def assignLessonAndTrackForTagTrackLessonText(self):
        try:
            
            book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
            first_sheet = book.sheet_by_name('AssignCreateTag')
            print("Fetching the Attribute Name from Excel Sheet\n")
            cell = first_sheet.cell(1,2)
            tagName = cell.value
            first_sheet = book.sheet_by_name('TagTrackLesson')
            print("Fetching the Attribute Name from Excel Sheet\n")
            cell = first_sheet.cell(1,3)
            lessonName = cell.value
            cell2 = first_sheet.cell(2,3)
            textCard= cell2.value
            cell1 = first_sheet.cell(1,1)
            titleOfTrack = cell1.value
            cell2 = first_sheet.cell(3,1)
            description = cell2.value
            cell = first_sheet.cell(1,3)
            lessonname = cell.value
            cell2 = first_sheet.cell(5,1)
            expectedSuccessText= cell2.value
            cell2 = first_sheet.cell(2,1)
            Imagefilepath = cell2.value
            cd=CreateLessonDifferentLessons()
            cd.lessonWithText(lessonname, textCard)
            
            ct=CreateTrackComman()
            ct.createTrack(titleOfTrack, Imagefilepath, description, tagName, lessonname, expectedSuccessText)

            
            
            tracklsn= TagPageElements()
            tracklsn.tagCreation(tagName)
            tracklsn.addlesson(lessonname)
            tracklsn.addTrack(titleOfTrack)  
            tracklsn.library(tagName)
            tracklsn.lessonLibrary(lessonname)
            tracklsn.trackLibray(titleOfTrack)
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

            wait=WebDriverWait(driver, 80)
            wait.until(EC.visibility_of_element_located((By.ID,"global-header-search")))
            print "Home Page Loaded"
            
        
        
        
        
        
        
        
        
        
        
