'''
Created on 22-Feb-2018

@author: dattatraya
'''

import os.path
import time
import traceback

from BaseTestClass import BaseTestClass
from BaseTestClass import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xlrd

from CreateLessonDifferentLessons import CreateLessonDifferentLessons
from CreateTrackComman import CreateTrackComman
from DeleteLesson import DeleteLesson
from BaseTestClass import projectPath

class TrackWithTextLesson:
    
    
    
        
        

    def trackWithLessonContainsTextCard(self):
        
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        first_sheet = book.sheet_by_name('TrackCreate')
        
        cell1 = first_sheet.cell(1,1)
        titleOfTrack = cell1.value
        
        cell2 = first_sheet.cell(2,1)
        Imagefilepath = cell2.value
        
        cell2 = first_sheet.cell(3,1)
        description = cell2.value
        
        cell2 = first_sheet.cell(4,1)
        tagName = cell2.value
        
        cell2 = first_sheet.cell(1,3)
        lessonName= cell2.value
        
        cell2 = first_sheet.cell(2,3)
        textCard= cell2.value
        
        cell2 = first_sheet.cell(5,1)
        expectedSuccessText= cell2.value
        
        
        try:
            cd=CreateLessonDifferentLessons()
            cd.lessonWithText(lessonName, textCard)
            
            ct=CreateTrackComman()
            ct.createTrack(titleOfTrack, Imagefilepath, description, tagName, lessonName, expectedSuccessText)
          
        
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
                WebDriverWait(driver, 5).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')

                alert = driver.switch_to.alert
                alert.accept()
                print("alert accepted")
            except Exception:
                print("no alert")
                
            try:
                d=DeleteLesson()
                d.lessonDelete(lessonName)
            except Exception:
                driver.get(url)



if __name__ == '__main__':
    u1=BaseTestClass()
    u1.UserLogin()
    obj=TrackWithTextLesson()
    obj.trackWithLessonContainsTextCard()
    
    
    