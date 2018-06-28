'''
Created on 21-Feb-2018

@author: dattatraya
'''
import os.path
import time

from BaseTestClass import BaseTestClass
from BaseTestClass import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xlrd
from CreateLessonDifferentLessons import CreateLessonDifferentLessons
from BaseTestClass import projectPath


class LessonCreateVideo:
    
        
    def lessonWithVideoUploadCard(self):
        
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        first_sheet = book.sheet_by_name('LessonCreate')
        
        cell1 = first_sheet.cell(20,1)
        lessonname = cell1.value
        
        cell2 = first_sheet.cell(21,1)
        videopath = cell2.value
        
        cell3 = first_sheet.cell(22,1)
        giveTimetoUploadVideo = cell3.value
        
        try:    
            vid=CreateLessonDifferentLessons()
            vid.lessonWithVideo(lessonname, videopath, giveTimetoUploadVideo)
        
        finally:    
            second_sheet = book.sheet_by_name('Login_Credentials')
            cell = second_sheet.cell(1,1)
            url = cell.value
            driver.get(url)
    

if __name__ == '__main__':
    btc=BaseTestClass()
    btc.UserLogin()
    
    m3=LessonCreateVideo()
    m3.lessonWithVideoUploadCard()