'''
Created on 22-Feb-2018

@author: dattatraya
'''
import os.path

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xlrd

from BaseTestClass import BaseTestClass
from BaseTestClass import driver
from CreateLessonDifferentLessons import CreateLessonDifferentLessons
from BaseTestClass import projectPath

class LessonCreateQuestion():
    
    
    
       
    def lessonWithQuestionAnswerCard(self):
        
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        first_sheet = book.sheet_by_name('LessonCreate')
        
        cell1 = first_sheet.cell(6,1)
        lessonname = cell1.value
        
        cell2 = first_sheet.cell(7,1)
        questionCard = cell2.value
        
        cell3 = first_sheet.cell(8,1)
        ans1 = cell3.value
        
        cell4 = first_sheet.cell(9,1)
        ans2 = cell4.value
        
        
        try:
            que=CreateLessonDifferentLessons()
            que.lessonWithQuestion(lessonname, questionCard, ans1, ans2)
          
        finally:    
            second_sheet = book.sheet_by_name('Login_Credentials')
            cell = second_sheet.cell(1,1)
            url = cell.value
            driver.get(url)
    

if __name__ == '__main__':
    btc=BaseTestClass()
    btc.UserLogin()
    
    m1=LessonCreateQuestion()
    m1.lessonWithQuestionAnswerCard()