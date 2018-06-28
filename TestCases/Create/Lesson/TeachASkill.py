'''
Created on Feb 27, 2018

@author: QA
'''
from os.path import os
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import wait, expected_conditions as EC
from selenium.webdriver.support.select import Select
import xlrd
from BaseTestClass import WebDriverWait
from BaseTestClass import driver
import traceback
from BaseTestClass import BaseTestClass
from DeleteLesson import DeleteLesson
from BaseTestClass import projectPath
class TeachASkill:
    
    def teachASkills(self):   
        
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@href='/create/lessons']")))

        print "Clicking on Lessons button from side menu"
        driver.find_element_by_xpath("//a[@href='/create/lessons']").click()
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/header/div/button")))  
        
        print "Clicking on Create Lesson button from lessons page"
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[2]/div/header/div/button").click()
        
        print "Going to verify the display of TEACH A SKILL Teamplate"
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        first_sheet = book.sheet_by_name('MultiCardLesson')
        
        cell1 = first_sheet.cell(32,0)
        exTemplateNameTeachASkill = cell1.value
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[4]/div/div/div[2]/div[4]/div/div")))
        teachAskillLocator =  driver.find_element_by_xpath("html/body/div[4]/div/div/div[2]/div[4]/h4")
    
        if (teachAskillLocator.is_displayed() and teachAskillLocator.text == exTemplateNameTeachASkill):
            print "The TEACH A SKILL Template is displaying in Create a new lesson pop up"
        else:
            print "Failed to find the TEACH A SKILL Template in Create a new lesson pop up"
            raise Exception
        
        # Clicking on Teach a skill template
        print "Clicking on Teach A Skill template"
        driver.find_element_by_xpath("html/body/div[4]/div/div/div[2]/div[4]/div/div").click()
        
        # Going to verify the number of cards displayed for the template TEACH A SKILL
        print "Going to verify the number of cards displayed for the template TEACH A SKILL"
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[1]/div/div")))
        cardsDisplayedTeachASkill=driver.find_elements_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[1]/div/div")
        
        actualNumberOfCardsTecahASkill = len(cardsDisplayedTeachASkill)
        
        cell2 = first_sheet.cell(33,0)
        exNumberOfCardsTeachASkill = cell2.value
        
        if(actualNumberOfCardsTecahASkill == exNumberOfCardsTeachASkill):
            print "The cards count is displaying as expected"+" "+str(exNumberOfCardsTeachASkill)
        else:
            print "Failed to find the card count as expected"
            raise Exception
        
        # Going to verify the title card content
        print "Going to verify the title card content"
    
        cell3 = first_sheet.cell(33,1)
        exTitleCardContentTeachASkill = cell3.value
        
        actualTitleCardContentTeachASkill = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/h1/textarea").text
        
        if (exTitleCardContentTeachASkill == actualTitleCardContentTeachASkill):
            print "The title card label is displaying as expected"+" "+'"'+exTitleCardContentTeachASkill+'"'
        else:
            print "Failed to find the expected label in title card"
            raise Exception
        
        # Going to clear the Title present in the title card
        print "Going to clear the lesson title"
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/h1/textarea").clear()
       
        print "Entering the title for lesson"
        cell4= first_sheet.cell(33,2)
        titleTeachASkill = cell4.value
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/h1/textarea").send_keys(titleTeachASkill)
        
        # Clicking on Second card
        print "Clicking on Second card"
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[1]/div/div[2]/div/div[1]").click()
        
        # Going to verify the content in second card
        print "Going to verify the content in second card"
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div"))) 
        
        cell5= first_sheet.cell(33,3)
        exSecondCardTeachASkill1 = cell5.value
        
        cell6= first_sheet.cell(33,4)
        exSecondCardTeachASkill2 = cell6.value
        
        cell7= first_sheet.cell(33,5)
        exSecondCardTeachASkill3 = cell7.value
        
        cell8= first_sheet.cell(33,6)
        exSecondCardTeachASkill4 = cell8.value
        
        cell9= first_sheet.cell(33,7)
        exSecondCardTeachASkill5 = cell9.value
        
        cell10= first_sheet.cell(33,8)
        exSecondCardTeachASkill6 = cell10.value
    
        actualSecondCardTeachASkill1 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div/span/span/span").text
        actualSecondCardTeachASkill2 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[3]/div/span[1]/span/span").text
        actualSecondCardTeachASkill3 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[3]/div/span[2]/span[1]/span").text
        actualSecondCardTeachASkill4 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[3]/div/span[2]/span[2]/span").text
        actualSecondCardTeachASkill5 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[3]/div/span[2]/span[3]/span").text
        actualSecondCardTeachASkill6 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[5]/div/span/span/span").text
        
        
        if(exSecondCardTeachASkill1 == actualSecondCardTeachASkill1):
            
            if(exSecondCardTeachASkill2 == actualSecondCardTeachASkill2):
                
                if(exSecondCardTeachASkill3 == actualSecondCardTeachASkill3):
                    
                    if(exSecondCardTeachASkill4 == actualSecondCardTeachASkill4):
                        
                        if(exSecondCardTeachASkill5 == actualSecondCardTeachASkill5):
                            
                            if(exSecondCardTeachASkill6 == actualSecondCardTeachASkill6):
        
                                print "The second card content is displaying as expected"
            
            
        else:
            
            print "Failed to find the expected content in second card" 
            raise Exception
        
        # Clicking on > icon 
        print "Clicking on > arrow for Third card"
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[2]/div"))) 
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[2]/div").click()
        
        # Clicking on Third card
        print "Clicking on Third card"
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[2]/div/div[3]/div/div[1]"))) 
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[2]/div/div[3]/div/div[1]").click()
        
        # Going to verify the content in Third card   
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div")))
        print "Going to verify the content in Third card"
        
        cell11 = first_sheet.cell(34,0)
        exThirdCardTeachASkill1 = cell11.value
        actualThirdCardTeachASkill1 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div/span/span/span").text
        
        cell12 = first_sheet.cell(34,1)
        exThirdCardTeachASkill2 = cell12.value
        actualThirdCardTeachASkill2 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[2]/div/span/span/span").text
        
        if(exThirdCardTeachASkill1 == actualThirdCardTeachASkill1):
            
            if(exThirdCardTeachASkill2 == actualThirdCardTeachASkill2):
                print "The third card content is displaying as expected"
        else:
            print "Failed to find the expected content in third card" 
            raise Exception
        
        # Clicking on < icon 
        print "Clicking on < arrow for Fourth card"
        
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[1]"))) 
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[1]").click()
        
        # Clicking on Fourth card
        print "Clicking on Fourth card"
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[1]/div/div[4]/div/div[1]"))) 
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[1]/div/div[4]/div/div[1]").click()
        
        # Going to verify the content in Fourth card card   
        print "Going to verify the content in Fourth card" 
        cell13 = first_sheet.cell(35,0)
        exFourthCardTeachASkill1 = cell13.value
        actualFourthCardTeachASkill1 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/span/span[1]/span").text
        
        cell14 = first_sheet.cell(35,1)
        exFourthCardTeachASkill2 = cell14.value
        actualFourthCardTeachASkill2 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/span/span[2]/span").text
        
        cell15 = first_sheet.cell(35,2)
        exFourthCardTeachASkill3 = cell15.value
        actualFourthCardTeachASkill3 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/span/span[3]/span").text
        
        if(exFourthCardTeachASkill1 == actualFourthCardTeachASkill1):
            
            if(exFourthCardTeachASkill2 == actualFourthCardTeachASkill2):
                
                if(exFourthCardTeachASkill3 == actualFourthCardTeachASkill3):
                
                    print "The fourth card content is displaying as expected"
        else:
            print "Failed to find the expected content in fourth card" 
            raise Exception
        
        
        
        # Going to click on Fifth card
        print "Clicking on Fifth card"
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[2]/div/div[5]/div/div[1]")))
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[2]/div/div[5]/div/div[1]").click()
        
        # Going to verify the content in fifth card
        print "Going to verify the content in Fifth card"
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div")))
        
        cell16 = first_sheet.cell(36,0)
        exFifthCardTeachASkill1 = cell16.value
        actualFifthCardTeachASkill1 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div/span/span/span").text
        
        cell17 = first_sheet.cell(36,1)
        exFifthCardTeachASkill2 = cell17.value
        actualFifthCardTeachASkill2 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[2]/div/span/span/span").text
        
        if(exFifthCardTeachASkill1 == actualFifthCardTeachASkill1):
            if(exFifthCardTeachASkill2 == actualFifthCardTeachASkill2):
                print "The Fifth card content is displaying as expected"
        else:
            print "Failed to find the expected content in Fifth card" 
            raise Exception
        
        # Going to click on Sixth card
        print "Clicking on Sixth card"
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[2]/div/div[6]/div/div[1]")))
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[2]/div/div[6]/div/div[1]").click()
        
        # Verifying Sixth card labels
        print "Going to verify the content in Sixth card"
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div")))
        
        cell18 = first_sheet.cell(37,0)
        exSixthCardTeachASkill1 = cell18.value
        actualSixthCardTeachASkill1 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/span/span[1]/span").text
        
        cell19 = first_sheet.cell(37,1)
        exSixthCardTeachASkill2 = cell19.value
        actualSixthCardTeachASkill2 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/span/span[2]/span").text
        
        cell20 = first_sheet.cell(37,2)
        exSixthCardTeachASkill3 = cell20.value
        actualSixthCardTeachASkill3 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/span/span[3]/span").text
        
        if(exSixthCardTeachASkill1 == actualSixthCardTeachASkill1):
            if(exSixthCardTeachASkill2 == actualSixthCardTeachASkill2):
                if(exSixthCardTeachASkill3 == actualSixthCardTeachASkill3):
                    print "The Sixth card content is displaying as expected"
        else:
            print "Failed to find the expected content in Sixth card" 
            raise Exception
        
        # Going to click on Seventh card
        print "Clicking on Seventh card"
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[2]/div/div[7]/div/div[1]")))
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[2]/div/div[7]/div/div[1]").click()
    
        # Verifying the content in Seventh card 
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div")))
        
        cell21 = first_sheet.cell(38,0)
        exSeventhCardTeachASkill1 = cell21.value
        actualSeventhCardTeachASkill1 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div/span/span/span").text
        
        cell22 = first_sheet.cell(38,1)
        exSeventhCardTeachASkill2 = cell22.value
        actualSeventhCardTeachASkill2 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[2]/div/span/span/span").text
        
        if(exSeventhCardTeachASkill1 == actualSeventhCardTeachASkill1):
            if(exSeventhCardTeachASkill2 == actualSeventhCardTeachASkill2):
                print "The Seventh card content is displaying as expected"
        else:
            print "Failed to find the expected content in Seventh card" 
            raise Exception
        
        print "Clicking on Eightth card"
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[2]/div/div[8]/div/div[1]")))
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[2]/div/div[8]/div/div[1]").click()
    
        # Going to verify the content in Eightth card
        print "Going to verify the content in Eightth card"
        
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div")))
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div/div/div/div[2]/button")))
        
        cell23 = first_sheet.cell(39,0)
        exEightthCardTeachASkill1 = cell23.value
        actualEightthCardTeachASkill1 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/span/span/span").text
        
        cell24 = first_sheet.cell(39,1)
        exEightthCardTeachASkill2 = cell24.value
        actualEightthCardTeachASkill2 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div[3]/div/span/span[1]/span").text
        
        
        cell25 = first_sheet.cell(39,2)
        exEightthCardTeachASkill3 = cell25.value
        actualEightthCardTeachASkill3 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div[3]/div/span/span[2]/span").text
        
        deleteButtonEightthCard = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div/div/div/div[2]/button")        
        
        actualchangeLabelEightCard = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div/div/div/div[2]/div/label").text
        
        cell26 = first_sheet.cell(39,3)
        exchangeLabelEightCard = cell26.value
        
        if(exEightthCardTeachASkill1 == actualEightthCardTeachASkill1):
            if(exEightthCardTeachASkill2 == actualEightthCardTeachASkill2):
                if(exEightthCardTeachASkill3 == actualEightthCardTeachASkill3):     
                    if (deleteButtonEightthCard.is_displayed()): 
                        if (actualchangeLabelEightCard == exchangeLabelEightCard): 
                            print "The Eightth card content is displaying as expected"
        else:
            print "Failed to find the expected content in Eightth card" 
            raise Exception
        
        # Clicking on Nineth card
        print "Clicking on Nineth card"
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[2]/div/div[9]/div/div[1]").click()
        
        # Going to verify the content in Nineth card
        print "Going to verify the content in Nineth card"
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div")))
        
        cell27 = first_sheet.cell(40,0)
        exNinethCardTeachASkill1= cell27.value
        actualNinethCardTeachASkill1 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/span/span/span").text
        
        cell28 = first_sheet.cell(40,1)
        exNinethCardTeachASkill2= cell28.value
        actualNinethCardTeachASkill2 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div[3]/div/span/span/span").text
    
        cell29 = first_sheet.cell(40,2)
        exNinethCardTeachASkill3= cell29.value
        actualNinethCardTeachASkill3 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div[5]/div/span/span/span").text
        
        deleteButtonNinethCard = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div/div/div/div[2]/button")
        
        actualchangeLabelNinethCard = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div/div/div/div[2]/div/label").text
        
        cell30 = first_sheet.cell(40,3)
        exchangeLabelNinethCard= cell30.value
        
        if(exNinethCardTeachASkill1 == actualNinethCardTeachASkill1):
            if(exNinethCardTeachASkill2 == actualNinethCardTeachASkill2):
                if(exNinethCardTeachASkill3 == actualNinethCardTeachASkill3):
                    if (deleteButtonNinethCard.is_displayed()): 
                        if (actualchangeLabelNinethCard == exchangeLabelNinethCard): 
                            print "The Nineth card content is displaying as expected"
        else:
            print "Failed to find the expected content in Nineth card" 
            raise Exception
        
        # Clicking on Ten th card
        print "Clicking on Ten th card "
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[2]/div/div[10]/div/div[1]").click()
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saving...']")))
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saved']"))) 
        
        # Going to verify the content in Ten th card
        print "Going to verify the content in Tenth card"
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/p/textarea")))
        
        cell31= first_sheet.cell(41,0)
        exTenthCardTeachASkillContent1 = cell31.value
       
        cell32= first_sheet.cell(41,1)
        exTenthCardTeachASkillContent2 = cell32.value
        
        cell33= first_sheet.cell(41,2)
        exTenthCardTeachASkillContent3 = cell33.value
        
    
        actualTenthCardTeachASkill1 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/p/textarea").get_attribute("placeholder")
    
        actualTenthCardTeachASkill2 = driver.find_element_by_xpath(".//*[@id='question-answer-input-0']").get_attribute("placeholder")
        
        actualTenthCardTeachASkill3=  driver.find_element_by_xpath(".//*[@id='question-answer-input-1']").get_attribute("placeholder")
    
        plusIconLocatorTeachASkill = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div[3]/div/div[1]/div/span")
        
        if(exTenthCardTeachASkillContent1 == actualTenthCardTeachASkill1):
            
            if(exTenthCardTeachASkillContent2 == actualTenthCardTeachASkill2):
                
                if(exTenthCardTeachASkillContent3 == actualTenthCardTeachASkill3):
                    
                    if(plusIconLocatorTeachASkill.is_displayed()):
                    
                        print "The Tenth card content is displaying as expected"
        else:
            
            print  "Failed to find the expected content in Tenth card" 
            raise Exception
    
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='question-answer-input-0']")))
        
        print "Entering question"
        cell34= first_sheet.cell(1,2)
        questionCard = cell34.value
        
        ele=driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/p/textarea")
        ele.send_keys(questionCard)
        
        print "Entering first answer"
        
        cell35= first_sheet.cell(1,3)
        ans1 = cell35.value
        
        driver.find_element_by_xpath(".//*[@id='question-answer-input-0']").send_keys(ans1)
        print "Entering Second answer"
        cell36= first_sheet.cell(1,4)
        ans2 = cell36.value
        
        driver.find_element_by_xpath(".//*[@id='question-answer-input-1']").send_keys(ans2)
          
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saving...']")))
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saved']"))) 
        
        # Clicking on Eleventh th card
    
        print "Clicking on Eleventh card "
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[2]/div/div[11]/div/div[1]").click()
        
        print "Going to verify the content in Eleventh card"
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div")))
        
        cell37= first_sheet.cell(42,0)
        exEleventhCardTeachASkillContent1 = cell37.value
        actualEleventhCardTeachASkillContent1 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div/span/span/span").text
        
        cell38= first_sheet.cell(42,1)
        exEleventhCardTeachASkillContent2 = cell38.value
        actualEleventhCardTeachASkillContent2 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[2]/div/span/span/span").text
        
        if(exEleventhCardTeachASkillContent1 == actualEleventhCardTeachASkillContent1):
            
            if(exEleventhCardTeachASkillContent2 == actualEleventhCardTeachASkillContent2):
                
                print "The Eleventh card content is displaying as expected"
        else:
            
            print  "Failed to find the expected content in Eleventh card" 
            raise Exception
        
        
        # Clicking on Twelve th card
        print "Clicking on Twelve th card "
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[2]/div/div[12]/div/div[1]").click()
        
        print "Going to verify the content in Twelve th card"
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div")))
        
        cell39= first_sheet.cell(43,0)
        exTwelvethCardTeachASkillContent1 = cell39.value
        actualTwelvethCardTeachASkillContent1 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div/span/span[1]/span").text
        
        cell40= first_sheet.cell(43,1)
        exTwelvethCardTeachASkillContent2= cell40.value
        actualTwelvethCardTeachASkillContent2 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div/span/span[2]/span").text
        
        cell41= first_sheet.cell(43,2)
        exTwelvethCardTeachASkillContent3 = cell41.value
        actualTwelevethCardTeachASkillContent3 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div/span/span[3]/span").text
        
        cell42= first_sheet.cell(43,3)
        exEleventhCardTeachASkillContent4 = cell42.value
        actualEleventhCardTeachASkillContent4 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[3]/div/span/span/span").text
        
        cell43= first_sheet.cell(43,4)
        exEleventhCardTeachASkillContent5 = cell43.value
        actualEleventhCardTeachASkillContent5 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[4]/div/span/span/span").text
        
        
        if(exTwelvethCardTeachASkillContent1 == actualTwelvethCardTeachASkillContent1):
            
            if(exTwelvethCardTeachASkillContent2 == actualTwelvethCardTeachASkillContent2):
                
                if(exTwelvethCardTeachASkillContent3 == actualTwelevethCardTeachASkillContent3):
                    
                    if(exEleventhCardTeachASkillContent4 == actualEleventhCardTeachASkillContent4):
                        
                        if(exEleventhCardTeachASkillContent5 == actualEleventhCardTeachASkillContent5):
                    
                            print "The Twelve th card content is displaying as expected"
        else:
            
            print  "Failed to find the expected content in Twelveth card" 
            raise Exception

        
    def publishLesson(self): 
      
        wait=WebDriverWait(driver, 60)
        
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        first_sheet = book.sheet_by_name('MultiCardLesson')
        cell32= first_sheet.cell(33,2)
        lesson_title_TeachASkill = cell32.value
        #wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saving...']")))
        #wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saved']"))) 
      
        wait.until(EC.element_to_be_clickable((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/button")))
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/button").click()
        print "Clicking on READY TO PUBLISH button"
        
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div/div[1]/section[3]/div/button[1]")))
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div/div[1]/section[3]/div/button[1]").click()
        print "Clicking on PUBLISH button"
        
        #print "Validating the success message after publish"
        # wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[2]/div/div/span[2]"))) 
        #actual_success_message= driver.find_element_by_xpath(".//*[@id='content']/div/div/div[2]/div/div/span[2]").text
       # expected_success_message= "You have successfully published \"" + lesson_title_TeachASkill + "\""; 
        
        #if(expected_success_message==actual_success_message):
            #print "The success message is displaying as"+ " "+expected_success_message
        #else:
            #print "The success message is not displaying as expected"
            
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[1]/a").click()
        print "Clicking on EXIT button"
             
        print "Verifying lesson displayed in Grid"
        wait.until(EC.visibility_of_element_located((By.XPATH,"(//tbody/tr/td[2]/a[.='"+lesson_title_TeachASkill+"'])[1]")))

        if driver.find_element_by_xpath("(//tbody/tr/td[2]/a[.='"+lesson_title_TeachASkill+"'])[1]").is_displayed():
            print "Lesson is displayed in Grid ::"+lesson_title_TeachASkill
        else:
            print "Lesson not displaying in grid"
            raise Exception
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[1]/div/nav/div/div[4]").click()
        
    def teachASkillMain(self): 
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        first_sheet = book.sheet_by_name('MultiCardLesson')
        cell32= first_sheet.cell(33,2)
        lesson_title_TeachASkill = cell32.value
        try:
            obj1 = TeachASkill()
            obj1.teachASkills()
            obj1.publishLesson()
            lesdel= DeleteLesson()
            lesdel.lessonDelete(lesson_title_TeachASkill)
            print "TEST CASE EXECUTION SUCCESSFULLY COMPLETED"
        except Exception as e:
            traceback.print_exc()
            print (e)
            raise Exception
            
        finally:
            #print "clicking on Home"
            book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
            first_sheet = book.sheet_by_name('Login_Credentials')
            #print("Fetching the Attribute Name from Excel Sheet\n")
            # read a cell
            cell = first_sheet.cell(1,1)
            HomeURL = cell.value
            #print HomeURL
            driver.get(HomeURL)
            #print "Home Page Loaded"
        
     
       

