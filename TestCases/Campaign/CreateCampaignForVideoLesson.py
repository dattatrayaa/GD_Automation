'''
Created on 28-Feb-2018

@author: dattatraya
'''
import os
import time
import traceback

from BaseTestClass import BaseTestClass
from BaseTestClass import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xlrd

from CampaignPageElements import CampPage
from CreateLessonDifferentLessons import CreateLessonDifferentLessons
from DeleteLesson import DeleteLesson
from BaseTestClass import projectPath
class CreateCampaignForVideoLesson:
    
    def createCampaignForVideoLesson(self,campaignTitle,campDescription,lessonName,actualSuccessMessage):
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
        elements.searchLesson(lessonName)
        
        #Waiting until lesson displayed
        elements.waitUntilSearchedLessonDisplayed(lessonName)
        
        #selecting searched lesson
        elements.selectSearchedLesson(lessonName)
        
        #waiting until add to campaign button is click able
        wait.until(EC.element_to_be_clickable((By.XPATH,elements.AddToCampaign_ButtonXpath())))
        
        #Clicking on Add to Campaign button
        elements.addToCampaignButton()
        
        #Verifying Added lesson is displayed in Grid
        print "\nVerifying Added lesson is displayed in Grid"
        if elements.firstLessonInGrid()==lessonName:
            print "Lesson displayed in grid"
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
        
        print "\n----Text Execution Completed----\n"
    
    
    
        
        
        
    def createCampaignVideoLesson(self):
       
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        first_sheet = book.sheet_by_name('CreateCampaigns')
        
        #Campaign Data
        cell1 = first_sheet.cell(26,1)
        campaignTitle = cell1.value
        
        cell1 = first_sheet.cell(27,1)
        campDescription = cell1.value
        
        cell1 = first_sheet.cell(28,1)
        actualSuccessMessage = cell1.value
        
        cell1 = first_sheet.cell(30,1)
        lessonName = cell1.value
        
        cell1 = first_sheet.cell(31,1)
        videoPath = cell1.value
        
        cell1 = first_sheet.cell(32,1)
        timeToUploadVideo = cell1.value
        
        
        try:
            print "\n\n----This test case creates campaign with----\n1. Video lesson\n"
            cd=CreateLessonDifferentLessons()
            cd.lessonWithVideo(lessonName, videoPath, timeToUploadVideo)
            
            newobj=CreateCampaignForVideoLesson()
            newobj.createCampaignForVideoLesson(campaignTitle, campDescription, lessonName, actualSuccessMessage)
        
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
                lesdel= DeleteLesson()
                lesdel.lessonDelete(lessonName)
            except Exception:
                driver.get(url)
                
                
                
                
if __name__=='__main__':
    btc=BaseTestClass()
    btc.UserLogin()
    
    r=CreateCampaignForVideoLesson()
    r.createCampaignVideoLesson()
           
        
