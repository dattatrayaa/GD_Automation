'''
Created on 21-Feb-2018

@author: dattatraya
'''

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

import os.path
import xlrd

from BaseTestClass import BaseTestClass
from BaseTestClass import driver
from CreateLessonDifferentLessons import CreateLessonDifferentLessons
from BaseTestClass import projectPath


class LessonCreateImage:
    
        
        
    def lessonWithImageUploadCard(self):
        
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        first_sheet = book.sheet_by_name('LessonCreate')
        
        cell1 = first_sheet.cell(14,1)
        lessonName = cell1.value
        
        cell2 = first_sheet.cell(15,1)
        imagefilepath = cell2.value
        
        try:
            img=CreateLessonDifferentLessons()
            img.lessonWithImage(lessonName, imagefilepath)
            
        finally:  
            driver.save_screenshot("ScreenShots/"+lessonName+".png")
            second_sheet = book.sheet_by_name('Login_Credentials')
            cell = second_sheet.cell(1,1)
            url = cell.value
            driver.get(url)
        

if __name__ == '__main__':
    btc=BaseTestClass()
    btc.UserLogin()
    
    m2=LessonCreateImage()
    m2.lessonWithImageUploadCard()