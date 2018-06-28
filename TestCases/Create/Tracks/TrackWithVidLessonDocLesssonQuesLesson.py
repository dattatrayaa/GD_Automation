'''
Created on 26-Feb-2018

@author: dattatraya
'''
import os.path
import time
import traceback

from BaseTestClass import BaseTestClass
from BaseTestClass import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xlrd

from CreateLessonDifferentLessons import CreateLessonDifferentLessons
from DeleteLesson import DeleteLesson
from TracksPageElements import TracksPageElements
from BaseTestClass import projectPath

class TrackWithVidLessonDocLesssonQuesLesson:
    
    def createTrackwithVidDocAndQuesLesson(self,titleOfTrack,Imagefilepath,description,tagName,lessonNameforVidcard,lessonNameforDoccard,lessonNameforQuescard,expectedSuccessText):
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
        searchLesson.send_keys(lessonNameforVidcard)
        track.searchedLessonAdd(lessonNameforVidcard)
        
        time.sleep(2)
        print "Searching for Second lesson in Add lessons pop up"
        searchLesson.clear()
        searchLesson.send_keys(lessonNameforDoccard)
        track.searchedLessonAdd(lessonNameforDoccard)
        
        time.sleep(2)
        print "Searching for Third lesson in Add lessons pop up"
        searchLesson.clear()
        searchLesson.send_keys(lessonNameforQuescard)
        track.searchedLessonAdd(lessonNameforQuescard)
        
        
        
     
        print "Adding to Track"
        track.addingToTrack()
        
        print "\nChecking added lesson is selected lesson from Pop up"
        
        
        lessonTextAddedToGrid=driver.find_element_by_xpath("//li[1]/div[2]/div/h4/div").text
        if lessonTextAddedToGrid==lessonNameforVidcard:
            print "Selected Lesson '"+lessonNameforVidcard+"' is displayed in grid of tracks page"
        
        else:
            print "Lesson is not displayed"
            raise Exception
        
        lessonTextAddedToGrid1=driver.find_element_by_xpath("//li[2]/div[2]/div/h4/div").text
        if lessonTextAddedToGrid1==lessonNameforDoccard:
            print "Selected Lesson '"+lessonNameforDoccard+"' is displayed in grid of tracks page"
        
        else:
            print "Lesson is not displayed"
            raise Exception
        
        lessonTextAddedToGrid2=driver.find_element_by_xpath("//li[3]/div[2]/div/h4/div").text
        if lessonTextAddedToGrid2==lessonNameforQuescard:
            print "Selected Lesson '"+lessonNameforQuescard+"' is displayed in grid of tracks page"
        
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
        
        
        
    def trackWithTwoLessonsVidDocQues(self):
        
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        first_sheet = book.sheet_by_name('TrackCreate')
        
        #Track Data
        cell1 = first_sheet.cell(88,1)
        titleOfTrack = cell1.value
        
        cell2 = first_sheet.cell(89,1)
        Imagefilepath = cell2.value
        
        cell2 = first_sheet.cell(90,1)
        description = cell2.value
        
        cell2 = first_sheet.cell(91,1)
        tagName = cell2.value
        
      
        cell2 = first_sheet.cell(92,1)
        expectedSuccessText= cell2.value
        
        # Lesson Data
        
        cell2 = first_sheet.cell(88,3)
        lessonNameforVidcard= cell2.value
        
        cell2 = first_sheet.cell(89,3)
        videoPath = cell2.value
        
        cell2 = first_sheet.cell(90,3)
        timeToUploadVideo = cell2.value
        
        cell2 = first_sheet.cell(92,3)
        lessonNameforDoccard = cell2.value
        
        cell2 = first_sheet.cell(93,3)
        documentPath= cell2.value
        
        cell2 = first_sheet.cell(94,3)
        timeToUploaddocument = cell2.value
        
        cell2 = first_sheet.cell(96,3)
        lessonNameforQuescard = cell2.value
        
        cell2 = first_sheet.cell(97,3)
        questionCard = cell2.value
        
        cell3 = first_sheet.cell(98,3)
        ans1 = cell3.value
        
        cell4 = first_sheet.cell(99,3)
        ans2 = cell4.value
     
       
        
        print "\n\nSetting Pre-requisite"
        print "Creating Two lessons\n"
     
        try:     
            ol=CreateLessonDifferentLessons()
            ol.lessonWithVideo(lessonNameforVidcard, videoPath, timeToUploadVideo)
            ol.lessonWithDocument(lessonNameforDoccard, documentPath, timeToUploaddocument)
            ol.lessonWithQuestion(lessonNameforQuescard, questionCard, ans1, ans2)
            
            tr1=TrackWithVidLessonDocLesssonQuesLesson()
            tr1.createTrackwithVidDocAndQuesLesson(titleOfTrack, Imagefilepath, description, tagName, lessonNameforVidcard, lessonNameforDoccard, lessonNameforQuescard, expectedSuccessText)
        except Exception as e:
            traceback.print_exc()
            print (e)
            raise Exception   
          
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
                lesdel= DeleteLesson()
                lesdel.lessonDelete(lessonNameforVidcard)
                lesdel.lessonDelete(lessonNameforDoccard)
                lesdel.lessonDelete(lessonNameforQuescard)
            except Exception:
                driver.get(url)
                
                
                
if __name__ == '__main__':
    
    btc=BaseTestClass()
    btc.UserLogin()
    m1=TrackWithVidLessonDocLesssonQuesLesson()
    m1.trackWithTwoLessonsVidDocQues()
