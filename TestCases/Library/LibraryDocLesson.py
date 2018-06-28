'''
Created on 27-Feb-2018

@author: Sheethu C
'''
from operator import contains
import os.path
import pdb
import thread
import time
import traceback

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from xlrd import book
import xlrd
from DeleteLesson import DeleteLesson
from BaseTestClass import driver
from BaseTestClass import BaseTestClass
from CreateLessonDifferentLessons import CreateLessonDifferentLessons
from DeleteTag import DeleteTag
from TagPageElements import TagPageElements
from BaseTestClass import projectPath
class LibraryDocLesson():
    
    
        
    def taglessonWithDocumentUploadCard(self):
        
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        first_sheet = book.sheet_by_name('TagLessonCreate')
        
        cell1 = first_sheet.cell(26,1)
        lessonname = cell1.value
        
        cell2 = first_sheet.cell(27,1)
        documentpath = cell2.value
        
        cell3 = first_sheet.cell(28,1)
        giveTimetoUploadDocument = cell3.value
        
        first_sheet = book.sheet_by_name('AssignCreateTag')
        print("Fetching the Attribute Name from Excel Sheet\n")
        # read a cell
        cell = first_sheet.cell(28,2)
        TagName = cell.value
        print TagName
        
        cell = first_sheet.cell(28,3)
        ExpectedSuccessMessage = cell.value
        print ExpectedSuccessMessage
        
        cell = first_sheet.cell(28,5)
        ExpectedAddLessonMessage = cell.value
        
        
        try:
            doc=TagPageElements()
            do=CreateLessonDifferentLessons()
            do.lessonWithDocument(lessonname, documentpath, giveTimetoUploadDocument)
            doc.tagCreation(TagName)
            doc.addlesson(lessonname)
            doc.library(TagName)
            doc.lessonLibrary(lessonname)
            
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
            
if __name__ == '__main__':
        btc=BaseTestClass()
        btc.UserLogin()
        m3 = TagDocLesson()
        m3.taglessonWithDocumentUploadCard()
    
