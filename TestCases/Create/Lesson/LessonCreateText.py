'''
Created on 20-Feb-2018

@author: dattatraya
'''


import os.path
import time

from BaseTestClass import BaseTestClass
from BaseTestClass import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xlrd
from CreateLessonDifferentLessons import CreateLessonDifferentLessons
from BaseTestClass import projectPath
class LessonCreateText:
    
    
    
    
    def lessonWithTextCard(self):
        
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        first_sheet = book.sheet_by_name('LessonCreate')
        
        cell1 = first_sheet.cell(1,1)
        lessonname = cell1.value
        
        cell2 = first_sheet.cell(2,1)
        textCardText = cell2.value
        
        try:
            obj1=CreateLessonDifferentLessons()
            obj1.lessonWithText(lessonname, textCardText)
         
        finally:   
            second_sheet = book.sheet_by_name('Login_Credentials')
            cell = second_sheet.cell(1,1)
            url = cell.value
            driver.get(url)

        
if __name__ == '__main__':
    btc=BaseTestClass()
    btc.UserLogin()
    obj11=LessonCreateText()
    obj11.lessonWithTextCard()
    