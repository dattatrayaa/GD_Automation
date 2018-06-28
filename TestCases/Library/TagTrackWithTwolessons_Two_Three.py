'''
Created on 02-Mar-2018

@author: Sheethu C
'''
'''
Created on 26-Feb-2018

@author: Sheethu C
'''
import os.path
import time
import traceback

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xlrd
from DeleteTag import DeleteTag
from BaseTestClass import driver
from CreateLessonDifferentLessons import CreateLessonDifferentLessons
from DeleteLesson import DeleteLesson
from LessonsPageElements import LessonsPageElements
from BaseTestClass import BaseTestClass
from TagPageElements import TagPageElements
from TracksPageElements import TracksPageElements
from BaseTestClass import projectPath
class TagTrackWithTwolessons_Two_Three():  
    
    def createTrackwithImgAndVideoLesson(self,titleOfTrack,Imagefilepath,description,tagName,lessonNameforImgcard,lessonNameforVidcard,expectedSuccessText):
        print "\nCreating track with one lesson contains Text Card"
        driver.refresh()
        wait=WebDriverWait(driver, 120)
        track=TracksPageElements()
        
        print "Clicking on Lessons button from side menu"
        track.lessonsButton()
        
        print "Clicking on Track button from side menu"
        track.tracksButton()
        
        track.createTracksButton()
        
        print "Entering title"
        titlefield=wait.until(EC.visibility_of_element_located((By.XPATH,track.trackTitle())))
        titlefield.send_keys(titleOfTrack)
        print "Title entered ::"+titleOfTrack
        
        driver.find_element_by_css_selector('input[type="file"]').send_keys(Imagefilepath)
        print "waiting to upload image"
        wait.until(EC.visibility_of_element_located((By.XPATH,track.imageDisplayed())))
        print "Image uploaded"
        
        print "Entering Description"
        driver.find_element_by_xpath(track.trackDescription()).send_keys(description)
        print "Description entered ::"+description 
        
        
        print "Adding tag"
        addTags=driver.find_element_by_xpath(track.addingTag())
        webdriver.ActionChains(driver).move_to_element(addTags).click().send_keys(tagName).perform()
        
        option=wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='react-select-2--option-0']")))
        webdriver.ActionChains(driver).move_to_element(option).click(option).perform()
        
        driver.find_element_by_xpath(track.trackDescription()).send_keys(" ")
        
        
        print "\nAdding created two lessons"
        
        print "Clicking on Add lessons button"
       
        driver.execute_script("window.scrollTo(0, 0);")
        
        track.addLessonButton()
                
        wait.until(EC.visibility_of_element_located((By.XPATH,track.serchLesson())))
        
        searchLesson=driver.find_element_by_xpath(track.serchLesson())
        print "Searching for first lesson in Add lessons pop up"
        searchLesson.send_keys(lessonNameforImgcard)
        track.searchedLessonAdd(lessonNameforImgcard)
        
        time.sleep(2)
        print "Searching for Second lesson in Add lessons pop up"
        searchLesson.clear()
        searchLesson.send_keys(lessonNameforVidcard)
        track.searchedLessonAdd(lessonNameforVidcard)
        
        print "Adding to Track"
        track.addingToTrack()
        
        print "\nChecking added lesson is selected lesson from Pop up"
        
        
        lessonTextAddedToGrid=driver.find_element_by_xpath("//li[1]/div[2]/div/h4/div").text
        if lessonTextAddedToGrid==lessonNameforImgcard:
            print "Selected Lesson '"+lessonNameforImgcard+"' is displayed in grid of tracks page"
        
        else:
            print "Lesson is not displayed"
            raise Exception
        
        lessonTextAddedToGrid1=driver.find_element_by_xpath("//li[2]/div[2]/div/h4/div").text
        if lessonTextAddedToGrid1==lessonNameforVidcard:
            print "Selected Lesson '"+lessonNameforVidcard+"' is displayed in grid of tracks page"
        
        else:
            print "Lesson is not displayed"
            raise Exception
        
        
        
        
        #Publishing Track
        print "Clicking on Publish Track button"
        
        track.publishButton()        
        print "\nVerifying Success message is displaying"
        
        
        track.successmessage(expectedSuccessText, titleOfTrack)
        
        
        track.sideMenuTracksExpanded()
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"//tbody/tr/td[2]/a[.='"+titleOfTrack+"']")))
        
        trackInGrid=driver.find_element_by_xpath("//tbody/tr/td[2]/a[.='"+titleOfTrack+"']").text
        
        if trackInGrid==titleOfTrack:
            print "Track '"+trackInGrid+"' is displayed in grid"
        else:
            print "Track is not displayed in grid"
            raise Exception
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[1]/div/nav/div/div[4]").click()
    
    
      
    def tagtrackWithTwoLessonsImgandVid(self):
        
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        first_sheet = book.sheet_by_name('TagTrackLesson')
        
        #Track Data
        cell1 = first_sheet.cell(79,1)
        titleOfTrack = cell1.value
        
        cell1 = first_sheet.cell(79,1)
        TrackName = cell1.value
        
        cell2 = first_sheet.cell(80,1)
        Imagefilepath = cell2.value
        
        cell2 = first_sheet.cell(81,1)
        description = cell2.value
        
        cell2 = first_sheet.cell(82,1)
        tagName = cell2.value
        
      
        cell2 = first_sheet.cell(83,1)
        expectedSuccessText= cell2.value
        
        # Lesson Data
        
        cell2 = first_sheet.cell(79,3)
        lessonNameforImgcard = cell2.value
        
        cell2 = first_sheet.cell(80,3)
        Imagefilepath1= cell2.value
        
        cell2 = first_sheet.cell(82,3)
        lessonNameforVidcard= cell2.value
        
        cell2 = first_sheet.cell(83,3)
        videoPath = cell2.value
        
        cell2 = first_sheet.cell(84,3)
        timeToUploadVideo = cell2.value
        
        
        first_sheet = book.sheet_by_name('AssignCreateTag')
        print("Fetching the Attribute Name from Excel Sheet\n")
        # read a cell
        cell = first_sheet.cell(12,2)
        TagName = cell.value
        print TagName
        
        cell = first_sheet.cell(12,3)
        ExpectedSuccessMessage = cell.value
        print ExpectedSuccessMessage
        
        cell = first_sheet.cell(12,4)
        ExpectedTrackMessage = cell.value
       
        cell = first_sheet.cell(12,5)
        ExpectedAddLessonMessage = cell.value
       
        
        print "\n\nSetting Pre-requisite"
        print "Creating Two lessons\n"
         
        try:
            
           
            
            cd=CreateLessonDifferentLessons()
            cd.lessonWithImage(lessonNameforImgcard, Imagefilepath1)
            cd.lessonWithVideo(lessonNameforVidcard, videoPath, timeToUploadVideo)
            
            tr1=TagTrackWithTwolessons_Two_Three()
            tr1.createTrackwithImgAndVideoLesson(titleOfTrack, Imagefilepath, description, tagName, lessonNameforImgcard, lessonNameforVidcard, expectedSuccessText)
         
            
            
            tr1=TagPageElements()
            tr1.tagCreation(TagName)
            tr1.addlesson(lessonNameforImgcard)
            tr1.addlesson(lessonNameforVidcard)
            tr1.addTrack(titleOfTrack)  
            tr1.library(TagName)
            tr1.lessonLibrary(lessonNameforImgcard)
            tr1.lessonLibrary(lessonNameforVidcard)
            tr1.trackLibray(titleOfTrack)
            
            
            
        except Exception as e:
            traceback.print_exc()
            print (e)
            raise Exception
        finally:
            second_sheet = book.sheet_by_name('Login_Credentials')
            cell = second_sheet.cell(1,1)
            url = cell.value
            try:
                tagde =DeleteTag()
                tagde.tagDeletion(tagName)
            except Exception:
                driver.get(url)
            try:
                lesdel= DeleteLesson()
                lesdel.lessonDelete(lessonNameforVidcard)
                lesdel.lessonDelete(lessonNameforImgcard)  
            except Exception:
                driver.get(url)
            driver.get(url)
            try:
                WebDriverWait(driver, 5).until(EC.alert_is_present())

                alert = driver.switch_to.alert
                alert.accept()
                print("alert accepted")
            except Exception:
                print("no alert")

if __name__ == '__main__':
    
    obj11= TagTrackWithTwolessons_Two_Three()
    obj12= BaseTestClass()
    obj12.UserLogin()
    obj11.tagtrackWithTwoLessonsImgandVid()