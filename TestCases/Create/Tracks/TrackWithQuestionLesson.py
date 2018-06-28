'''
Created on 23-Feb-2018

@author: dattatraya
'''


import os.path
import traceback

from BaseTestClass import BaseTestClass
from BaseTestClass import driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xlrd

from CreateLessonDifferentLessons import CreateLessonDifferentLessons
from CreateTrackComman import CreateTrackComman
from DeleteLesson import DeleteLesson
from BaseTestClass import projectPath

class TrackWithQuestionLesson:
    
    
    
       
    def lessonWithQuestionAnswerCard(self):
        
        
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        first_sheet = book.sheet_by_name('TrackCreate')
        
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
     
        try:     
            cd=CreateLessonDifferentLessons()
            cd.lessonWithQuestion(lessonname, question, ans1, ans2)
            
            ct=CreateTrackComman()
            ct.createTrack(titleOfTrack, Imagefilepath, description, tagName, lessonname, expectedSuccessText)
            
        
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
                d.lessonDelete(lessonname)
            except Exception:
                driver.get(url)
        

if __name__ == '__main__':
    btc=BaseTestClass()
    btc.UserLogin()
    
    m1=TrackWithQuestionLesson()
    m1.lessonWithQuestionAnswerCard()
       
