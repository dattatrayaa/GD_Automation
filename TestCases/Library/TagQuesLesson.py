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
from BaseTestClass import BaseTestClass
from CreateLessonDifferentLessons import CreateLessonDifferentLessons
from TagPageElements import TagPageElements
from DeleteTag import DeleteTag
from BaseTestClass import projectPath
class TagQuesLesson():    
   
    def tagForQuestionCardLessonMain(self):
        
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        first_sheet = book.sheet_by_name('TagLessonCreate')
        
        cell1 = first_sheet.cell(6,1)
        lessonname = cell1.value
        
        cell2 = first_sheet.cell(7,1)
        question = cell2.value
        
        cell3 = first_sheet.cell(8,1)
        ans1 = cell3.value
        
        cell4 = first_sheet.cell(9,1)
        ans2 = cell4.value
        
        cell5 = first_sheet.cell(10,1)
        ans3 = cell5.value
        
        first_sheet = book.sheet_by_name('AssignCreateTag')
        print("Fetching the Attribute Name from Excel Sheet\n")
        # read a cell
        cell = first_sheet.cell(29,2)
        TagName = cell.value
        print TagName
        
        cell = first_sheet.cell(29,3)
        ExpectedSuccessMessage = cell.value
        print ExpectedSuccessMessage
        cell = first_sheet.cell(29,5)
        ExpectedAddLessonMessage = cell.value
        
        
        try:
            que=TagPageElements()
            qu=CreateLessonDifferentLessons()
            qu.lessonWithQuestion(lessonname, question, ans1, ans2)
            que.tagCreation(TagName)
            que.addlesson(lessonname)
            que.library(TagName)
            que.lessonLibrary(lessonname)
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
   obj11=TagQuesLesson()
   obj11.tagForQuestionCardLessonMain()
