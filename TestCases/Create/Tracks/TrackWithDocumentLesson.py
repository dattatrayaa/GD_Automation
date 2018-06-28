'''
Created on 23-Feb-2018

@author: dattatraya
'''
import os.path
import time
import traceback

from BaseTestClass import BaseTestClass
from BaseTestClass import driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xlrd
from DeleteLesson import DeleteLesson
from CreateLessonDifferentLessons import CreateLessonDifferentLessons
from CreateTrackComman import CreateTrackComman
from BaseTestClass import projectPath

class TrackWithDocumentLesson:
    
        
        
       
    def lessonWithDocumentCard(self):
        
        
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        first_sheet = book.sheet_by_name('TrackCreate')
        
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
        
        try:     
            cd=CreateLessonDifferentLessons()
            cd.lessonWithDocument(lessonname, documentPath, timeToUploaddocument)
            
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
    
    m1=TrackWithDocumentLesson()
    m1.lessonWithDocumentCard()
