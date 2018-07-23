'''
Created on 10-Jul-2018

@author: OptisLabs
'''
import os
import time

from BaseTestClass import BaseTestClass
from BaseTestClass import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xlrd

from DeleteLesson import DeleteLesson
from LessonsPageElements import LessonsPageElements
import traceback


class LessonsUIOperationVideoCard:
    
    def lessonUioperationVideo(self,lessonName,videoPath,timeToUploadVideo,videoPath1):
        print "\nCreating lesson with one card"
        wait=WebDriverWait(driver, 120)
        driver.refresh()
        print "Clicking on Lessons button from side menu"
        
        lessons=LessonsPageElements()
        lessons.lessonsButtonSideMenuUnexpanded()
     
        print "Click on Create lesson button"
        lessons.createLessonButton()
        
        print "Verifying Create new lesson tab is displayed"
        
        
        if lessons.createANewLessonPopupHeader()== "Create a new lesson":
            print("Create a new lesson tab is displayed")
        else:
            print ""
            raise Exception
        
               
        
        lessons.clickOnBlankLesson()
        print "Clicked on Blank lesson"
        
        print "Creating New lesson"
        
        lessons.settingLessonName(lessonName)
        print "Entered lesson name ::"+lessonName
    
        print "Click on (+) icon"
        
        lessons.addCardPlusiCon()
        
        print "Clicking on Video card"
        lessons.videoCardClick()
        
        #Uploading Video
        print "Uploading Video"
        lessons.videoUploadInVideoCard(videoPath)
        
        videoContainerlocator_afterupload=WebDriverWait(driver, timeToUploadVideo).until(EC.visibility_of_element_located((By.XPATH,lessons.waitTillVideoUploadReCheckStatusButtonXpath())))
        
        
        if(videoContainerlocator_afterupload.is_displayed()):
            
            print "Successfully uploaded the Video file"
            
        else:
            print "Failed to upload the Video file"
            raise Exception
        try:
            while WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,lessons.waitTillVideoUploadReCheckStatusButtonXpath()))):
                #wait.until(EC.visibility_of_element_located((By.XPATH,lessons.waitTillVideoUploadReCheckStatusButtonXpath())))
                driver.find_element_by_xpath(lessons.waitTillVideoUploadReCheckStatusButtonXpath()).click()
        except Exception:
            print "Video displayed"
        
        print "Video displayed in video card"
        print "Length of video"
        ele=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.lengthOfVideo())))
        print "Length of video displayed "+str(ele.text)
        
        
        print "Playing video"
        try:
            play=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.playButtonVideo())))
            play.click()
        except Exception:
            print "Failed to click on Play button"
            raise Exception("Failed to click on Play button")
        print "Clicked on Play button"
        
        print "Enlarging video"
        try:
            lessons.enlargeVideoToggle()
        except Exception:
            print traceback
            print "Failed to click on Enlarge to fit toggle"
            raise Exception("Failed to click on Enlarge to fit toggle")
        print "Clicked on Enlarge to fit toggle"
        
        
        print "Verifying Video is enlarged"
        enlarge=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.videoEnargement())))
        fullscreen=enlarge.get_attribute("class")
        if "full-screen-video" in fullscreen:
            print "Video displayed in full screen mode"
        else:
            print "Video not displayed in full screen"
            raise Exception("Video not displayed in full screen")
        
        
        print "Making video to normal size"
        try:
            lessons.enlargeVideoToggle()
        except Exception:
            print traceback
            print "Failed to click on Enlarge to fit toggle"
            raise Exception("Failed to click on Enlarge to fit toggle")
        
        print "Checking in Preview video is displayed"
        try:
            lessons.previewButton()
            print "Clicked on Preview button"
        except Exception:
            print "Failed to click on Preview Button"
            raise Exception
        
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,lessons.videoInDesktopPreview())))
            print "Video displayed in Desktop preview"
        except Exception:
            print "Video not displayed in Desktop preview"
            raise Exception("Video not displayed in Desktop preview")
        
        print "Closing preview"
        try:
            ele=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.closePreview())))
            ele.click()
            print "Preview closed"
        except Exception:
            print "Preview not closed"
            raise Exception("Preview not closed")
        
        print "Deleting current video"
        lessons.deleteVideoFromVideoCard()
        
        print "Verifying Video is deleted from Video Card"
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,lessons.browsefileLinkVideoCard())))
            print "Video deleted successfully"
        except Exception:
            print traceback
            print "Failed to delete video"
            raise Exception("Failed to delete video")
        
        
        print "Checking card is deleted after clicking on Delete card"
        print "Taking Current count of Cards"
        count=str(lessons.CountOfAllCardDisplayed())
        print "Total number of cards displayed as ::"+count
        time.sleep(2)
        d=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.deleteCardLink())))        
        d.click()
        print "Clicked on Delete Card"
        countafterDelete=str(lessons.CountOfAllCardDisplayed())
        print countafterDelete
        print "Verifying Card is deleted"
        if count!=countafterDelete:
            print "Verified, card is deleted successfully ::"+countafterDelete
        else:
            print "Card is not deleted"
            raise Exception
        
        print "Adding Video Card again"   
        
        print "Click on (+) icon"
        
        lessons.addCardPlusiCon()
        
        print "Clicking on Video card"
        lessons.videoCardClick()
        
        #Uploading Video
        print "Uploading Video"
        lessons.videoUploadInVideoCard(videoPath)
        
        videoContainerlocator_afterupload=WebDriverWait(driver, timeToUploadVideo).until(EC.visibility_of_element_located((By.XPATH,lessons.waitTillVideoUploadReCheckStatusButtonXpath())))
        
        
        if(videoContainerlocator_afterupload.is_displayed()):
            
            print "Successfully uploaded the Video file"
            
        else:
            print "Failed to upload the Video file"
            raise Exception
        try:
            while WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,lessons.waitTillVideoUploadReCheckStatusButtonXpath()))):
                #wait.until(EC.visibility_of_element_located((By.XPATH,lessons.waitTillVideoUploadReCheckStatusButtonXpath())))
                driver.find_element_by_xpath(lessons.waitTillVideoUploadReCheckStatusButtonXpath()).click()
        except Exception:
            print "Video displayed"
        
        print "Video displayed in video card"
        
        print "Changing video"
        #Uploading Video
        print "Uploading new Video"
        lessons.videoUploadInVideoCard(videoPath1)
        
        videoContainerlocator_afterupload=WebDriverWait(driver, timeToUploadVideo).until(EC.visibility_of_element_located((By.XPATH,lessons.waitTillVideoUploadReCheckStatusButtonXpath())))
        
        
        if(videoContainerlocator_afterupload.is_displayed()):
            
            print "Successfully uploaded the Video file"
            
        else:
            print "Failed to upload the Video file"
            raise Exception
        
        
        
        time.sleep(2)
        print "Publishing lesson"
        lessons.readyToPublishButtonClick()
        
        print "Clicked on publish button"
        lessons.publishButtonClick()

        print "Lesson published"
        
        lessons.backButton()
        
        #Verifying created lesson is displayed in list
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"(//tbody/tr/td[2]/a[.='"+lessonName+"'])[1]")))

        if driver.find_element_by_xpath("(//tbody/tr/td[2]/a[.='"+lessonName+"'])[1]").is_displayed():
            
            print "\nLesson is displayed in Grid ::"+lessonName
            
        else:
            print "Lesson not displaying in grid"
            raise Exception
        
        
        lessons.expandSideMenu()
        
        
        
        
    def lessonUiOpearationOnVideoCardMain(self):
        
        book=xlrd.open_workbook(os.path.join('TestData.xlsx'))
        first_sheet = book.sheet_by_name('LessonCreate')
        
        cell1 = first_sheet.cell(59,1)
        lessonName = cell1.value
        
        cell2 = first_sheet.cell(60,1)
        videoPath = cell2.value
        
        cell2 = first_sheet.cell(61,1)
        timeToUploadVideo = cell2.value
        
        cell2 = first_sheet.cell(62,1)
        videoPath1 = cell2.value
        
        
        
        
        try:
            print "\nThis Test case Tests the UI operations and functionality of Image Card\n"
            li=LessonsUIOperationVideoCard()
            li.lessonUioperationVideo(lessonName, videoPath, timeToUploadVideo, videoPath1)
            print "\n Test Execution completed\n"
        finally:  
            second_sheet = book.sheet_by_name('Login_Credentials')
            cell = second_sheet.cell(1,1)
            url = cell.value
            driver.get(url)
            
            try:
                delLesson=DeleteLesson()
                delLesson.lessonDelete(lessonName)
            except Exception:
                driver.get(url)



if __name__ == '__main__':
    
    b=BaseTestClass()
    b.UserLogin()
    
    text=LessonsUIOperationVideoCard()
    text.lessonUiOpearationOnVideoCardMain()
    
    
    

