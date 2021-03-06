'''
Created on 08-Mar-2018

@author: dattatraya
'''
import os.path
import time
import traceback

from BaseTestClass import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xlrd

from CampaignPageElements import CampPage
from CreateLessonDifferentLessons import CreateLessonDifferentLessons
from DeleteLesson import DeleteLesson
from TracksPageElements import TracksPageElements
from BaseTestClass import projectPath

class CampaignTrackTextLessonImageLesson:
    
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
         
        
        
    def campWithTrackTextLessonImgLesson(self,campaignTitle,campDescription,trackName,actualSuccessMessage,ownDuration):
        elements=CampPage()
        
        wait=WebDriverWait(driver, 60)
        
        driver.refresh()
        print "\n\nCreating Campaign"
        wait.until(EC.visibility_of_element_located((By.XPATH,elements.campaignButtonFromSideMenuXpath())))
        elements.campaignButtonFromSideMenu()
        
        wait.until(EC.visibility_of_element_located((By.XPATH,elements.createCampaignButtonXpath())))

        if elements.campaignsPageHeaderText()=="Campaigns":
            print "Campaigns page displayed"
        else:
            print "Campaigns page is not displayed"
            raise Exception
        
        
        print "Clicking on Create Campaign button"
        wait.until(EC.visibility_of_element_located((By.XPATH,elements.createCampaignButtonXpath())))
        elements.createCampaignButton()
        
        
        wait.until(EC.visibility_of_element_located((By.XPATH,elements.Camp_titleXpath())))
        print "Create Campaign page is displayed"
        
                  
        elements.titleTextField(campaignTitle)
        print "Title entered ::campTitle"
        
        elements.descriptionField(campDescription)
        print "Description entered ::campDescription"
        
        print "Adding Track"
        #Add Track 
        
        elements.addTrackButton()
        
        #Searching track and adding
        elements.searchTracksAndSelect(trackName)
        
        #Adding to Campaign
        elements.addToCampaignTrack()
        
        
        #Verifying Added Track is displayed in Grid
        print "\nVerifying Added Track is displayed in Grid"
        if trackName in elements.firstTrackInGrid():
            print "Track displayed in grid"
        else:
            print "Track not displayed in grid"
            
        
        print "Setting Own duration"
        elements.setOwnDuration(ownDuration)
        
        
        wait.until(EC.element_to_be_clickable((By.XPATH,elements.SaveAndExit_ButtonXpath())))
        #Clicking on save & exit button
        print "Clicking on save & exit button"
        elements.saveAndExitButton()
        
        
        
        #Verifying campaign detail page is displayed
        print "\nVerifying campaign detail page is displayed"
        
        if elements.campaignDetailPageHeaderText()==campaignTitle:
            print "Campaign detail page is displayed"
        else:
            print "Campaign detail page is not displayed"
            raise Exception
        
        print "\n----Text Execution Completed----\n"
        
    def CampaignForTrackWithTextLessonImageLesson(self):
        
        
        
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        first_sheet = book.sheet_by_name('CreateCampaigns')
        
        cell1 = first_sheet.cell(178,4)
        campaignTitle = cell1.value
        
        cell1 = first_sheet.cell(179,4)
        campDescription = cell1.value
        
        cell1 = first_sheet.cell(180,4)
        actualSuccessMessage = cell1.value
        
        cell2 = first_sheet.cell(183,4)
        ownDuration= cell2.value
        
        
        #Track
        cell1 = first_sheet.cell(185,4)
        titleOfTrack = cell1.value
        
        cell2 = first_sheet.cell(186,4)
        Imagefilepath = cell2.value
        
        cell2 = first_sheet.cell(187,4)
        description = cell2.value
        
        cell2 = first_sheet.cell(188,4)
        tagName = cell2.value
        
        cell2 = first_sheet.cell(189,4)
        expectedSuccessText= cell2.value
        
        
        #Lesson
        cell2 = first_sheet.cell(191,4)
        lessonName1= cell2.value
        
        cell2 = first_sheet.cell(192,4)
        textCard= cell2.value
        
        cell2 = first_sheet.cell(193,4)
        lessonName2= cell2.value
        
        cell2 = first_sheet.cell(194,4)
        Imagefilepath1= cell2.value
        
        
      
        
        try:
            #lesson Creation
            ol=CreateLessonDifferentLessons()
            ol.lessonWithText(lessonName1, textCard)
            ol.lessonWithImage(lessonName2, Imagefilepath1)
            
                        
            #Track Creation
            obj2=CampaignTrackTextLessonImageLesson()
            obj2.createTrackwithTxtAndImgLesson(titleOfTrack, Imagefilepath, description, tagName, lessonName1, lessonName2, expectedSuccessText)
            
            #Campaign Creation
            
            obj2.campWithTrackTextLessonImgLesson(campaignTitle, campDescription, titleOfTrack, actualSuccessMessage, ownDuration)       
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
                lesdel.lessonDelete(lessonName1)
                lesdel.lessonDelete(lessonName2)
            except Exception:
                driver.get(url)
    
