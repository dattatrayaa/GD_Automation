'''
Created on 18-Jul-2018

@author: OptisLabs
'''
import os.path
import traceback

from BaseTestClass import BaseTestClass
from BaseTestClass import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xlrd

from CreateLessonDifferentLessons import CreateLessonDifferentLessons
from CreateTrackComman import CreateTrackComman
from DeleteLesson import DeleteLesson
from TracksPageElements import TracksPageElements
from DeleteTrack import DeleteTrack


class  TrackDeleteLesson:
    
    
    def trackAfterLessonDeletion(self,titleOfTrack,expectedValidationMessage):
        driver.refresh()
        wait=WebDriverWait(driver, 180)
        track=TracksPageElements()
        
        print "Clicking on Lessons button from side menu"
        track.lessonsButton()
        
        print "Clicking on Track button from side menu"
        track.tracksButton()
        
        print "Clicking on Track '"+titleOfTrack+"'"
        
        try:
            tr=wait.until(EC.visibility_of_element_located((By.XPATH,track.trackInGrid(titleOfTrack))))
            tr.click()
            print "Clicked on Track '"+titleOfTrack
        except Exception as e:
            print e
            traceback.print_exc()
            raise Exception("Failed to click on Track link")
        
        print "Checking for validation message displayed"
        
        print "Checking title is displayed"
        
        try:
            ele=wait.until(EC.visibility_of_element_located((By.XPATH,track.objectiveDeletedTitleOfTrack())))
        except Exception as e:
            print e
            traceback.print_exc()
            raise Exception("Title not displayed for deleted Lessons Track")
        
        try:
            ele=wait.until(EC.visibility_of_element_located((By.XPATH,track.objectiveDeleted())))
        except Exception as e:
            print e
            traceback.print_exc()
            raise Exception("No validation message is displayed")
        
        if ele.text==expectedValidationMessage:
            print "Validation message '"+expectedValidationMessage+"' displayed"
        else:
            raise Exception("Validation message is not displayed")
        
                
        
        
        
        
        
        
    def trackDeleteLessonCheckInTrackPageMain(self):
        
        book=xlrd.open_workbook(os.path.join('TestData.xlsx'))
        first_sheet = book.sheet_by_name('TrackCreate')
        
        cell1 = first_sheet.cell(170,1)
        titleOfTrack = cell1.value
        
        cell2 = first_sheet.cell(171,1)
        Imagefilepath = cell2.value
        
        cell2 = first_sheet.cell(172,1)
        description = cell2.value
        
        cell2 = first_sheet.cell(173,1)
        tagName = cell2.value
        
        cell2 = first_sheet.cell(174,1)
        lessonName= cell2.value
        
        cell2 = first_sheet.cell(175,1)
        textCard= cell2.value
        
        cell2 = first_sheet.cell(176,1)
        expectedSuccessText= cell2.value
        
        cell2 = first_sheet.cell(177,1)
        expectedValidationMessage= cell2.value
        
        
        try:
            print "\nCreating Lesson\n"
            cd=CreateLessonDifferentLessons()
            cd.lessonWithText(lessonName, textCard)
            
            print "\nCreating Track\n"
            ct=CreateTrackComman()
            ct.createTrack(titleOfTrack, Imagefilepath, description, tagName, lessonName, expectedSuccessText)
            
            print "\nDeleting lesson\n"
            lessondelete=DeleteLesson()
            lessondelete.lessonDelete(lessonName)
            
            print "\nNow Check in Tracks page validation message is displayed instead lesson"
            cr=TrackDeleteLesson()
            cr.trackAfterLessonDeletion(titleOfTrack, expectedValidationMessage)
            
          
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
                t=DeleteTrack()
                t.mainDelete(titleOfTrack)
            except Exception:
                driver.get(url)



if __name__ == '__main__':
    u1=BaseTestClass()
    u1.UserLogin()
    obj=TrackDeleteLesson()
    obj.trackDeleteLessonCheckInTrackPageMain()
    
    



