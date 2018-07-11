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
from BaseTestClass import projectPath

class CreateCampaignForTextAndImageLesson:
    
    def createCampaignTxtAndImageLessons(self,campaignTitle,campDescription,actualSuccessMessage,lessonNameForTextLesson,lessonNameforImageLesson):
        elements=CampPage()
        driver.refresh()
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
        
        print "Adding Lesson"
        #Add lesson button
        elements.addlessonButton()
        
        #Waiting until first lesson in pop is displayed
        wait.until(EC.visibility_of_element_located((By.XPATH,elements.FirstLessonWaitXpath())))
        
        #Searching lesson by its name
        print "Searching first lesson"
        elements.searchLesson(lessonNameForTextLesson)
        elements.waitUntilSearchedLessonDisplayed(lessonNameForTextLesson)
        elements.selectSearchedLesson(lessonNameForTextLesson)
        print "First lesson selected"
        
        print "Searching second lesson"
        elements.searchLesson(lessonNameforImageLesson)
        elements.waitUntilSearchedLessonDisplayed(lessonNameforImageLesson)
        elements.selectSearchedLesson(lessonNameforImageLesson)
        print "Second lesson selected"
       
        
        #waiting until add to campaign button is click able
        wait.until(EC.element_to_be_clickable((By.XPATH,elements.AddToCampaign_ButtonXpath())))
        
        #Clicking on Add to Campaign button
        elements.addToCampaignButton()
        
        #Verifying Added lesson is displayed in Grid
        print "\nVerifying Added first lesson is displayed in Grid"
        if elements.firstLessonInGrid()==lessonNameForTextLesson:
            print "Lesson displayed in grid  ::"+lessonNameForTextLesson
        else:
            print "Lesson not displayed in grid"
            
        '''print "\nVerifying Added second lesson is displayed in Grid"
        if elements.secondLessonInGrid()==lessonNameforImageLesson:
            print "Lesson displayed in grid  ::"+lessonNameforImageLesson
        else:
            print "Lesson not displayed in grid"'''
            
            
        
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
    
    
    
    
    def createCampaignWithTextLessonImageLesson(self):
       
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        first_sheet = book.sheet_by_name('CreateCampaigns')
        
        #Campaign Data
        cell1 = first_sheet.cell(121,1)
        campaignTitle = cell1.value
        
        cell1 = first_sheet.cell(122,1)
        campDescription = cell1.value
        
        cell1 = first_sheet.cell(123,1)
        actualSuccessMessage = cell1.value
        
        cell1 = first_sheet.cell(125,1)
        lessonNameForTextLesson = cell1.value
        
        cell1 = first_sheet.cell(126,1)
        textCard = cell1.value
        
        cell1 = first_sheet.cell(127,1)
        lessonNameforImageLesson = cell1.value
        
        cell1 = first_sheet.cell(128,1)
        Imagefilepath1 = cell1.value
        
      
        
        try:
            print "\n\n----This test case creates campaign with----\n1. Text lesson\n2. Image lesson\n"
            cd=CreateLessonDifferentLessons()
            cd.lessonWithText(lessonNameForTextLesson, textCard)
            cd.lessonWithImage(lessonNameforImageLesson, Imagefilepath1)
            
            
            newobj=CreateCampaignForTextAndImageLesson()
            newobj.createCampaignTxtAndImageLessons(campaignTitle, campDescription, actualSuccessMessage, lessonNameForTextLesson, lessonNameforImageLesson)
            
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
                lesdel.lessonDelete(lessonNameForTextLesson)
                lesdel.lessonDelete(lessonNameforImageLesson)
            except Exception:
                driver.get(url)
        
        
        

