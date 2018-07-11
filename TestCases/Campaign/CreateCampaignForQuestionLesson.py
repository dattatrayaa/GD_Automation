'''
Created on 28-Feb-2018

@author: dattatraya
'''
import os
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
from BaseTestClass import projectPath

class CreateCampaignForQuestionLesson:
    
    def createCampaignForQuestionLesson(self,campaignTitle,campDescription,lessonName,actualSuccessMessage,numberOfAttempts):
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
        
        elements.makeThisAsAGradedCampaign()
        
        #Setting Max number of attempts
        elements.setAMaxNoOfAttempts(numberOfAttempts)
        
        
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
       

    
       


    def createCampaignQuestionLesson(self):
       
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        first_sheet = book.sheet_by_name('CreateCampaigns')
        
        #Campaign Data
        cell1 = first_sheet.cell(44,1)
        campaignTitle = cell1.value
        
        cell1 = first_sheet.cell(45,1)
        campDescription = cell1.value
        
        cell1 = first_sheet.cell(46,1)
        actualSuccessMessage = cell1.value
        
        cell1 = first_sheet.cell(48,1)
        lessonName = cell1.value
        
        cell1 = first_sheet.cell(49,1)
        questionCard = cell1.value
        
        cell1 = first_sheet.cell(50,1)
        ans1 = cell1.value
        
        cell1 = first_sheet.cell(51,1)
        ans2 = cell1.value
        
        cell1 = first_sheet.cell(52,1)
        numberOfAttempts = cell1.value
        
        
        
        
        try:
            print "\n\n----This test case creates campaign with----\n1. Question lesson\n"
            cd=CreateLessonDifferentLessons() 
            cd.lessonWithQuestion(lessonName, questionCard, ans1, ans2)
            
            
                       
            newobj=CreateCampaignForQuestionLesson()
            newobj.createCampaignForQuestionLesson(campaignTitle, campDescription, lessonName, actualSuccessMessage, numberOfAttempts)
        
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
                lesdel.lessonDelete(lessonName)
            except Exception:
                driver.get(url)
        
        
