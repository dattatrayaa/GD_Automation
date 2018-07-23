'''
Created on 23-Jul-2018

@author: OptisLabs
'''
import os.path
import time
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
from DeleteTrack import DeleteTrack
from TracksPageElements import TracksPageElements


class TrackEditDetailsValidation:
    
    
    def TrackEditAfterPublish(self,titleOfTrack,description, tagName, lessonName1,lessonName2):
        
        driver.refresh()
        wait=WebDriverWait(driver, 180)
        track=TracksPageElements()
        
        print "Clicking on Lessons button from side menu"
        track.lessonsButton()
        
        print "Clicking on Track button from side menu"
        track.tracksButton()
        wait.until(EC.visibility_of_element_located((By.XPATH,track.trackInGrid(titleOfTrack))))
        print "Clicking on Edit button of Track '"+titleOfTrack+"'"
        
        try:
            edit=wait.until(EC.visibility_of_element_located((By.XPATH,track.EditButton(titleOfTrack))))
            edit.click()
            print "Clicked on Edit button of Track '"+titleOfTrack
        except Exception as e:
            print e
            traceback.print_exc()
            raise Exception("Failed to click on Edit button of Track link")
    
    
        
        print "Verifying all the details are displayed"
        ele=wait.until(EC.visibility_of_element_located((By.XPATH,track.trackTitle())))  
        if ele.text==titleOfTrack:
            print "Valid title '"+titleOfTrack+"' displayed in Title text field"
        else:
            raise Exception("Invalid title displayed in Title text field")
        
        
        eled=wait.until(EC.visibility_of_element_located((By.XPATH,track.trackDescription())))  
        if description in eled.text:
            print "Valid description '"+description+"' displayed in Description text field"
        else:
            raise Exception("Invalid description displayed in Title text field")
        
        
        try:
            tag=wait.until(EC.visibility_of_element_located((By.XPATH,track.tagInEditTrackPage(tagName))))  
            print "Tag '"+tag.text+"' is displayed"
        except Exception as e:
            print e
            traceback.print_exc()
            raise Exception("Tag is not displayed")
        
        
        
        print "Checking lesson name displayed"
        lessonTextAddedToGrid=driver.find_element_by_xpath(track.lessonInGrid()).text
        if lessonTextAddedToGrid==lessonName1:
            print "Lesson '"+lessonName1+"' is displayed in grid of tracks page"
        else:
            raise Exception("Lesson is not displayed")

        
        print "Checking Disabled Publish revisions button is displayed"
        try:
            publishRev=wait.until(EC.visibility_of_element_located((By.XPATH,track.publishRevisionsButton())))  
            print "Disabled button is displayed"
        except Exception as e:
            print e
            traceback.print_exc()
            raise Exception("Button is not disabled")
        
        if "Publish Revisions" in publishRev:
            print "Publish revision button is displayed with disabled status"
        else:
            raise Exception("Publish revision button is not displayed")
        
        print "Verified all previous details displayed as expected"
        
        
        print "Removing old lesson and adding new lesson"
        try:
            remove=wait.until(EC.visibility_of_element_located((By.XPATH,track.removeLessonFromTrack())))  
            remove.click()
        except Exception as e:
            print e
            traceback.print_exc()
            raise Exception("Failed to click on Remove lesson button")
        
        try:
            remove=wait.until(EC.visibility_of_element_located((By.XPATH,track.removeLessonPopup())))  
            remove.click()
        except Exception as e:
            print e
            traceback.print_exc()
            raise Exception("Failed to click on Remove lesson button from popup")
        
        print "Checking lesson is removed successfully"
        try:
            addLessonE=wait.until(EC.visibility_of_element_located((By.XPATH,track.AddLessonButtonEmptyState()))) 
            print "Add lesson button is displayed in Empty state of Lessons container" 
        except Exception as e:
            print e
            traceback.print_exc()
            raise Exception("Failed to click on Remove lesson button from popup") 
        
        
        try:
            addLessonE.click()
            print "Clicked on Add lesson button"
        except Exception as e:
            print e
            traceback.print_exc()
            raise Exception("Failed to click on Add lesson button from empty state container")
        
        try:
            searchLesson=wait.until(EC.visibility_of_element_located((By.XPATH,track.serchLesson())))
            print "Add lessons pop up  id displayed"
        except Exception:
            raise Exception("Add lessons pop up is not displayed")
        try:
            print "Searching for first lesson in Add lessons pop up"
            searchLesson.send_keys(lessonName2)
            track.searchedLessonAdd(lessonName2)
        except Exception as e:
            print e
            traceback.print_exc()
            raise Exception
        time.sleep(2)
        
        print "Adding to Track"
        track.addingToTrack()
        
            
            
        
        
    
    
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
        
        
        try:
            print "\nCreating Lesson\n"
            cd=CreateLessonDifferentLessons()
            cd.lessonWithText(lessonName, textCard)
            
            print "\nCreating Track\n"
            ct=CreateTrackComman()
            ct.createTrack(titleOfTrack, Imagefilepath, description, tagName, lessonName, expectedSuccessText)
            
            
            
          
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
    
    





