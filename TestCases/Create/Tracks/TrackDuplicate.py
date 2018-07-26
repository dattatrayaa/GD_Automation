'''
Created on 19-Jul-2018

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


class TrackDuplicate:
    
    def Trackduplication(self,titleOfTrack,lessonName):
        
        driver.refresh()
        wait=WebDriverWait(driver, 180)
        track=TracksPageElements()
        
        print "Clicking on Lessons button from side menu"
        track.lessonsButton()
        
        print "Clicking on Track button from side menu"
        track.tracksButton()
        
        print "Clicking on Track '"+titleOfTrack+"'"
        
        try:
            tr=wait.until(EC.visibility_of_element_located((By.XPATH,track.duplicateButton(titleOfTrack))))
            tr.click()
            print "Clicked on Duplicate button of Track '"+titleOfTrack
        except Exception as e:
            print e
            traceback.print_exc()
            raise Exception("Failed to click on Duplicate Track link")
        
        print "Verifying Pop up displayed"
        
        try:
            t=wait.until(EC.visibility_of_element_located((By.XPATH,track.duplicateTrackPopupHeader())))
            print "Pop up '"+t.text+"' is displayed"
        except Exception as e:
            print e
            traceback.print_exc()
            raise Exception("Duplicate Track pop up is not displayed")
        
        print "Verifying name of track displayed with Copy string"
        
        try:
            ti=wait.until(EC.visibility_of_element_located((By.XPATH,track.duplicateTrackPopupTitle())))
            print "Pop up is displayed"
        except Exception as e:
            print e
            traceback.print_exc()
            raise Exception("Duplicate Track pop up is not displayed")
        
        print ti.get_attribute("value")
        if ti.get_attribute("value") == "Copy of "+titleOfTrack:
            print "Title '"+ti.text+"' is displayed"
        
        else:
            raise Exception("Duplicate title not displayed")
        
        print "Clicking on Save button"
        track.duplicatePopupSaveButton()
        print "Clicked on SAVE button"
        wait.until(EC.invisibility_of_element_located((By.XPATH,track.duplicateTrackPopupHeader())))
        
        track.trackInGrid("Copy of "+titleOfTrack)
        
        print "Duplicate track is created successfully"
        
        print "Clicking on Track 'Copy of "+titleOfTrack+"'"
        
        try:
            tr=wait.until(EC.visibility_of_element_located((By.XPATH,track.trackInGrid("Copy of "+titleOfTrack))))
            tr.click()
            print "Clicked on Track 'Copy of "+titleOfTrack
        except Exception as e:
            print e
            traceback.print_exc()
            raise Exception("Failed to click on Track link")
        
        print "Checking Lesson Name displayed is similar"
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, track.lessonInTrackDetailPage(lessonName))))
        except Exception:
            traceback.print_exc()
            raise Exception("Lesson Title not displayed in Track details page")
        
        print "Lesson '"+lessonName+"'displayed in Track details page"
        
        print "Hence Verified duplicate Track is created"
        
        
        
        
        
        
        
        
        
    
    def trackDuplicateMain(self):
        
        book=xlrd.open_workbook(os.path.join('TestData.xlsx'))
        first_sheet = book.sheet_by_name('TrackCreate')
        
        cell1 = first_sheet.cell(213,1)
        titleOfTrack = cell1.value
        
        cell2 = first_sheet.cell(214,1)
        Imagefilepath = cell2.value
        
        cell2 = first_sheet.cell(215,1)
        description = cell2.value
        
        cell2 = first_sheet.cell(216,1)
        tagName = cell2.value
        
        cell2 = first_sheet.cell(217,1)
        lessonName= cell2.value
        
        cell2 = first_sheet.cell(218,1)
        textCard= cell2.value
        
        cell2 = first_sheet.cell(219,1)
        expectedSuccessText= cell2.value
        
        
        try:
            print "\nCreating Lesson\n"
            cd=CreateLessonDifferentLessons()
            cd.lessonWithText(lessonName, textCard)
            
            print "\nCreating Track\n"
            ct=CreateTrackComman()
            ct.createTrack(titleOfTrack, Imagefilepath, description, tagName, lessonName, expectedSuccessText)
            
            
            print "\nNow Clicking on Duplicate button of track '"+titleOfTrack+"'"
            cr=TrackDuplicate()
            cr.Trackduplication(titleOfTrack, lessonName)
            
          
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
    obj=TrackDuplicate()
    obj.trackDuplicateMain()
    
    


