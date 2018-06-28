'''
Created on 22-Feb-2018

@author: dattatraya
'''
import os.path
import traceback

import xlrd

from BaseTestClass import BaseTestClass
from BaseTestClass import driver
from CreateLessonDifferentLessons import CreateLessonDifferentLessons
from DeleteLesson import DeleteLesson
from BaseTestClass import projectPath

class LessonCreateDocument:
    



    def lessonWithDocumentUploadCard(self):
        
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        first_sheet = book.sheet_by_name('LessonCreate')
        
        cell1 = first_sheet.cell(26,1)
        lessonname = cell1.value
        
        cell2 = first_sheet.cell(27,1)
        documentpath = cell2.value
        
        cell3 = first_sheet.cell(28,1)
        giveTimetoUploadDocument = cell3.value
        
        try:
            doc=CreateLessonDifferentLessons()
            doc.lessonWithDocument(lessonname, documentpath, giveTimetoUploadDocument)
        except Exception as e:
            traceback.print_exc()
            print (e)
            raise Exception   
            
        finally:
            driver.save_screenshot("ScreenShots/"+lessonname+".png")
            second_sheet = book.sheet_by_name('Login_Credentials')
            cell = second_sheet.cell(1,1)
            url = cell.value
            driver.get(url)
            re=DeleteLesson()
            re.lessonDelete(lessonname)
        

if __name__ == '__main__':
    btc=BaseTestClass()
    btc.UserLogin()
    
    m3=LessonCreateDocument()
    m3.lessonWithDocumentUploadCard()
    