'''
Created on 27-Feb-2018

@author: Sheethu C
'''
import os.path
import time
import traceback

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xlrd
from BaseTestClass import driver
from DeleteLesson import DeleteLesson
from BlankLessonOne import BlankLessonOne
from DeleteTag import DeleteTag
from TagPageElements import TagPageElements
from BaseTestClass import projectPath
from BaseTestClass import lesnPath
class LibraryLessonCombinedLesson():
    
    
    def tagLessonCombined(self):    
    
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        first_sheet = book.sheet_by_name('TagLessonCreate')
        
        cell1 = first_sheet.cell(32,0)
        blankLessonOnename = cell1.value
        
        cell2 = first_sheet.cell(32,1)
        blankLessonOneTextCardText = cell2.value
        
        cell3 = first_sheet.cell(32,2)
        blankLessonOneQuestion = cell3.value
        
        cell4 = first_sheet.cell(32,3)
        blankLessonOneQuestionOption1 = cell4.value
        
        cell5 = first_sheet.cell(32,4)
        blankLessonOneQuestionOption2 = cell5.value
        
        cell6 = first_sheet.cell(32,5)
        blankLessonOneImageCard1 = cell6.value
        
        
        cell7 = first_sheet.cell(32,6)
        blankLessonOneUploadLink = cell7.value
        
        cell8 = first_sheet.cell(32,7)
        blankLessonOneImageCard2 = cell8.value
        
        cell9 = first_sheet.cell(32,8)
        blankLessonOneVideoCard = cell9.value
        
          
        cell10 = first_sheet.cell(32,9)
        blankLessonOneDocumentCard = cell10.value
        
        first_sheet = book.sheet_by_name('AssignCreateTag')
        print("Fetching the Attribute Name from Excel Sheet\n")
        # read a cell
        cell = first_sheet.cell(30,2)
        TagName = cell.value
        print TagName
        
        cell = first_sheet.cell(30,3)
        ExpectedSuccessMessage = cell.value
        print ExpectedSuccessMessage
        
        cell = first_sheet.cell(30,5)
        ExpectedAddLessonMessage = cell.value
        try:
            obj11=TagPageElements()
            obj1=BlankLessonOne()
            obj1.lessonWithTitletCard(blankLessonOnename)
            obj1.lessonWithTextCard(blankLessonOneTextCardText)
            obj1.addDocumentCard(blankLessonOneDocumentCard,200)
            obj1.addQuestionCard(blankLessonOneQuestion,blankLessonOneQuestionOption1,blankLessonOneQuestionOption2)
            obj1.addImageCard(blankLessonOneImageCard1,blankLessonOneUploadLink,blankLessonOneImageCard2,600)
            obj1.addVideoCard(blankLessonOneVideoCard,600)
            obj11.tagCreation(TagName)
            obj11.addlesson(blankLessonOnename)
            obj11.library(TagName)
            obj11.lessonLibrary(blankLessonOnename)
            
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
                lesdel.lessonDelete(blankLessonOnename) 
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
            

