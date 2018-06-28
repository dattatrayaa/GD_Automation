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
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.support.ui import WebDriverWait
import xlrd
from DeleteTag import DeleteTag
from BaseTestClass import BaseTestClass
from BaseTestClass import driver
from CreateLessonDifferentLessons import CreateLessonDifferentLessons
from DeleteLesson import DeleteLesson
from TracksPageElements import TracksPageElements
from LessonsPageElements import LessonsPageElements
from BaseTestClass import projectPath
from TagPageElements import TagPageElements
class LibraryTrackWithTextImg():
    
    def createTrackwithTxtAndImgLesson(self,titleOfTrack,Imagefilepath,description,tagName,lessonNameforTextcard,lessonNameforImgcard,expectedSuccessText):
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
        searchLesson.send_keys(lessonNameforTextcard)
        track.searchedLessonAdd(lessonNameforTextcard)
        
        time.sleep(2)
        print "Searching for Second lesson in Add lessons pop up"
        searchLesson.clear()
        searchLesson.send_keys(lessonNameforImgcard)
        track.searchedLessonAdd(lessonNameforImgcard)
        
        
     
        print "Adding to Track"
        track.addingToTrack()
        
        print "\nChecking added lesson is selected lesson from Pop up"
        
        
        lessonTextAddedToGrid=driver.find_element_by_xpath("//li[1]/div[2]/div/h4/div").text
        if lessonTextAddedToGrid==lessonNameforTextcard:
            print "Selected Lesson '"+lessonNameforTextcard+"' is displayed in grid of tracks page"
        
        else:
            print "Lesson is not displayed"
            raise Exception
        
        lessonTextAddedToGrid1=driver.find_element_by_xpath("//li[2]/div[2]/div/h4/div").text
        if lessonTextAddedToGrid1==lessonNameforImgcard:
            print "Selected Lesson '"+lessonNameforImgcard+"' is displayed in grid of tracks page"
        
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
        driver.refresh()
    
    
    
    
    def tagTrackWithTwolessonsOneTwo(self):
        
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        first_sheet = book.sheet_by_name('TagTrackLesson')
        
        #Track Data
        cell1 = first_sheet.cell(70,1)
        titleOfTrack = cell1.value
        
        cell1 = first_sheet.cell(70,1)
        TrackName = cell1.value
        
        cell2 = first_sheet.cell(71,1)
        Imagefilepath = cell2.value
        
        cell2 = first_sheet.cell(72,1)
        description = cell2.value
        
        cell2 = first_sheet.cell(73,1)
        tagName = cell2.value
        
      
        cell2 = first_sheet.cell(74,1)
        expectedSuccessText= cell2.value
        
        # Lesson Data
        cell2 = first_sheet.cell(70,3)
        lessonNameforTextcard= cell2.value
        
        cell2 = first_sheet.cell(71,3)
        textCard= cell2.value
        
        cell2 = first_sheet.cell(73,3)
        lessonNameforImgcard = cell2.value
        
        
        cell2 = first_sheet.cell(74,3)
        Imagefilepath1= cell2.value
        
        first_sheet = book.sheet_by_name('AssignCreateTag')
        print("Fetching the Attribute Name from Excel Sheet\n")
        # read a cell
        cell = first_sheet.cell(11,2)
        TagName = cell.value
        print TagName
        
        cell = first_sheet.cell(11,3)
        ExpectedSuccessMessage = cell.value
        print ExpectedSuccessMessage
        
        cell = first_sheet.cell(11,4)
        ExpectedTrackMessage = cell.value
       
        cell = first_sheet.cell(11,5)
        ExpectedAddLessonMessage = cell.value
        
        print "Setting Pre-requisite"
        print "Creating Two lessons\n"
     
        try:
            cd=CreateLessonDifferentLessons()
            cd.lessonWithText(lessonNameforTextcard, textCard)
            cd.lessonWithImage(lessonNameforImgcard, Imagefilepath1)
            tr=LibraryTrackWithTextImg()
            tr.LibraryTrackWithImgText(titleOfTrack, Imagefilepath, description, tagName, lessonNameforTextcard, lessonNameforImgcard, expectedSuccessText)
            tr1=TagPageElements()
            tr1.tagCreation(TagName)
            tr1.addlesson(lessonNameforTextcard)
            tr1.addlesson(lessonNameforImgcard)
            tr1.addTrack(titleOfTrack)  
            tr1.library(TagName)
            tr1.lessonLibrary(lessonNameforTextcard)
            tr1.lessonLibrary(lessonNameforImgcard)
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
                driver.refresh()
                lesdel.lessonDelete(lessonNameforTextcard)
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
    
    obj11= TagTrackWithTwolessonsOneTwo()
    obj12= BaseTestClass()
    obj12.UserLogin()
    obj11.tagTrackWithTwolessonsOneTwo()