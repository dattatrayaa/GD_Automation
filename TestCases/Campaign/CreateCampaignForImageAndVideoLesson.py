'''
Created on 01-Mar-2018

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
from DeleteLesson import DeleteLesson
from CreateLessonDifferentLessons import CreateLessonDifferentLessons
from BaseTestClass import BaseTestClass
from BaseTestClass import projectPath

class CreateCampaignForImageAndVideoLesson:

    def createCampaignImageAndVideoLessons(self,campaignTitle,campDescription,actualSuccessMessage,lessonName1,lessonName2):
        elements=CampPage()
        driver.refresh()
        wait=WebDriverWait(driver, 60)
        
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
        
        print "Adding Lesson"
        #Add lesson button
        elements.addlessonButton()
        
        #Waiting until first lesson in pop is displayed
        wait.until(EC.visibility_of_element_located((By.XPATH,elements.FirstLessonWaitXpath())))
        
        #Searching lesson by its name
        print "Searching first lesson"
        elements.searchLesson(lessonName1)
        elements.waitUntilSearchedLessonDisplayed(lessonName1)
        elements.selectSearchedLesson(lessonName1)
        print "First lesson selected"
        
        print "Searching second lesson"
        elements.searchLesson(lessonName2)
        elements.waitUntilSearchedLessonDisplayed(lessonName2)
        elements.selectSearchedLesson(lessonName2)
        print "Second lesson selected"
       
        
        #waiting until add to campaign button is click able
        wait.until(EC.element_to_be_clickable((By.XPATH,elements.AddToCampaign_ButtonXpath())))
        
        #Clicking on Add to Campaign button
        elements.addToCampaignButton()
        
        #Verifying Added lesson is displayed in Grid
        print "\nVerifying Added first lesson is displayed in Grid"
        if elements.firstLessonInGrid()==lessonName1:
            print "Lesson displayed in grid  ::"+lessonName1
        else:
            print "Lesson not displayed in grid"
            
        print "\nVerifying Added second lesson is displayed in Grid"
        if elements.secondLessonInGrid()==lessonName2:
            print "Lesson displayed in grid  ::"+lessonName2
        else:
            print "Lesson not displayed in grid"
            
            
        
        wait.until(EC.element_to_be_clickable((By.XPATH,elements.SaveAndExit_ButtonXpath())))
        #Clicking on save & exit button
        print "Clicking on save & exit button"
        elements.saveAndExitButton()
        
        '''#verifying success message
        print "\nVerifying success message"
        
        if elements.successMessage()==actualSuccessMessage:
            print "Message '"+actualSuccessMessage+"' is displayed"
        else:
            print "Success message is not displayed properly"
            raise Exception'''
        
        #Verifying campaign detail page is displayed
        print "\nVerifying campaign detail page is displayed"
        
        if elements.campaignDetailPageHeaderText()==campaignTitle:
            print "Campaign detail page is displayed"
        else:
            print "Campaign detail page is not displayed"
            raise Exception
        
        #verifying in Campaigns displayed in Campaigns grid
        elements.searchingForlesson(campaignTitle)
        
        if elements.actualCampTitleINGrid()==campaignTitle:
            print "Campaign '"+campaignTitle+"' displayed in Grid"
        
        else:
            print "Campaign is not displayed in Grid"
            raise Exception
        
        print "\n----Text Execution Completed----\n"
        
    
        
    def createCampaignWithImageLessonVideoLesson(self):
       
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        first_sheet = book.sheet_by_name('CreateCampaigns')
        
        #Campaign Data
        cell1 = first_sheet.cell(132,1)
        campaignTitle = cell1.value
        
        cell1 = first_sheet.cell(133,1)
        campDescription = cell1.value
        
        cell1 = first_sheet.cell(134,1)
        actualSuccessMessage = cell1.value
        
        cell1 = first_sheet.cell(136,1)
        lessonName1 = cell1.value
        
        cell1 = first_sheet.cell(137,1)
        Imagefilepath1 = cell1.value
        
        cell1 = first_sheet.cell(138,1)
        lessonName2 = cell1.value
        
        cell1 = first_sheet.cell(139,1)
        videoPath = cell1.value
        
        cell1 = first_sheet.cell(140,1)
        timeToUploadVideo = cell1.value
        
        
        
        try:
            print "\n\n----This test case creates campaign with----\n1. Image lesson\n2. Video lesson\n"
            
            cd=CreateLessonDifferentLessons()
            cd.lessonWithImage(lessonName1, Imagefilepath1)
            cd.lessonWithVideo(lessonName2, videoPath, timeToUploadVideo)
            
            newobj=CreateCampaignForImageAndVideoLesson()
            newobj.createCampaignImageAndVideoLessons(campaignTitle, campDescription, actualSuccessMessage, lessonName1, lessonName2)
            
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
                lesdel=DeleteLesson()
                lesdel.lessonDelete(lessonName1)
                lesdel.lessonDelete(lessonName2)
            except Exception:
                driver.get(url)
                
if __name__=='__main__':
    btc=BaseTestClass()
    btc.UserLogin()
    
    u=CreateCampaignForImageAndVideoLesson()
    u.createCampaignWithImageLessonVideoLesson()
