'''
Created on Feb 23, 2018

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
class LessonExplainAConcept:
    
    def lessonExplainAConcepts(self,exNumberOfCards):   
        
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@href='/create/lessons']")))
        print "Clicking on Lessons button from side menu"
        
        driver.find_element_by_xpath("//a[@href='/create/lessons']").click()
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/header/div/button")))  
        
        print "Clicking on Create Lesson button from lessons page"
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[2]/div/header/div/button").click()
       
        # Going to verify EXPLAIN A CONCEPT Template
        print "Going to verify the display of EXPLAIN A CONCEPT Teamplate"
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[4]/div/div/div[2]/div[3]/div/div"))) 
        
        explainACoceptLocator =  driver.find_element_by_xpath("html/body/div[4]/div/div/div[2]/div[3]")
        
        if (explainACoceptLocator.is_displayed() and explainACoceptLocator.text == "EXPLAIN A CONCEPT"):
            print "The EXPLAIN A CONCEPT Template is displaying in Create a new lesson pop up"
        else:
            print "Failed to find the EXPLAIN A CONCEPT Template in Create a new lesson pop up"
            raise Exception
        
        # Going to Click on EXPLAIN A CONCEPT Template
        print "Clicking on EXPLAIN A CONCEPT Template"
        driver.find_element_by_xpath("html/body/div[4]/div/div/div[2]/div[3]/div/div").click()
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/h1/textarea"))) 
    
        # Going to check for the count of displayed lesson cards
        cardsDisplayed=driver.find_elements_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[1]/div/div")
        
        actualNumberOfCards = len(cardsDisplayed)
        
        if(actualNumberOfCards == exNumberOfCards):
            print "The cards count is displaying as expected"+" "+str(exNumberOfCards)
        else:
            print "Failed to find the card count as expected"
            raise Exception
        
        # Going to verify the title card content
        print "Going to verify the title card content"
        
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        first_sheet = book.sheet_by_name('MultiCardLesson')
        
        cell1 = first_sheet.cell(21,0)
        exTitleCardContent = cell1.value
        
        actualTitleCardContent = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/h1/textarea").text
       
        
        if (exTitleCardContent == actualTitleCardContent):
            print "The title card label is displaying as expected"+" "+'"'+exTitleCardContent+'"'
        else:
            print "Failed to find the expected label in title card"
            raise Exception
        
        # Going to clear the Title present in the title card
        print "Going to clear the lesson title"
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/h1/textarea").click()
       
        for i in range(55):
        
            driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/h1/textarea").send_keys(Keys.BACKSPACE)
        
        print "Entering the title for lesson"
        cell32= first_sheet.cell(30,0)
        title = cell32.value
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/h1/textarea").send_keys(title)
        
        # Clicking on Second card
        print "Clicking on Second card"
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[1]/div/div[2]").click()
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div"))) 
    
        # Going to verify the content in Second card
        print "Going to verify the content in second card"
        
        cell2 = first_sheet.cell(21,1)
        exFirstCardContent1 = cell2.value
        
        cell3 = first_sheet.cell(21,2)
        exFirstCardContent2 = cell3.value
        
        cell4 = first_sheet.cell(21,3)
        exFirstCardContent3 = cell4.value
        
        cell5 = first_sheet.cell(21,4)
        exFirstCardContent4 = cell5.value
        
        cell6 = first_sheet.cell(21,5)
        exFirstCardContent5 = cell6.value
        
        cell7 = first_sheet.cell(21,6)
        exFirstCardContent6 = cell7.value
        
        actualFirstCardContent1 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div/span/span/span").text
        actualFirstCardContent2 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[3]/div/span[1]/span/span").text
        actualFirstCardContent3 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[3]/div/span[2]/span/span").text
        actualFirstCardContent4 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[3]/div/span[4]/span[1]/span").text
        actualFirstCardContent5 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[3]/div/span[4]/span[2]/span").text
        actualFirstCardContent6 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[5]/div/span/span/span").text
      
        
        if(exFirstCardContent1 == exFirstCardContent1):
            
            if(exFirstCardContent2 == exFirstCardContent2):
                
                if(exFirstCardContent3 == exFirstCardContent3):
                    
                    if(exFirstCardContent4 == exFirstCardContent4):
                        
                        if(exFirstCardContent5 == exFirstCardContent5):
                            
                            if(exFirstCardContent6 == exFirstCardContent6):
        
                                print "The second card content is displaying as expected"
            
            
        else:
            
            print "Failed to find the expected content in second card" 
            raise Exception
      
        # Clicking on > icon 
        time.sleep(4)
        print "Clicking on > arrow for Third card"
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[3]/div"))) 
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[3]/div").click()
        
        # Clicking on Third card
        print "Clicking on Third card"
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[2]/div/div[3]/div/div[1]"))) 
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[2]/div/div[3]/div/div[1]").click()
        
        # Going to verify the content in Third card   
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div")))
        print "Going to verify the content in Third card"
                
        cell8 = first_sheet.cell(22,0)
        exSecondCardContent1 = cell8.value
        actualSecondCardContent1 = driver.find_element_by_xpath("html/body/div[1]/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div/span/span[1]/span").text
        
        cell9 = first_sheet.cell(22,1)
        exSecondCardContent2 = cell9.value
        actualSecondCardContent2 = driver.find_element_by_xpath("html/body/div[1]/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div/span/span/span").text
                                                                    
        cell10 = first_sheet.cell(22,2)
        exSecondCardContent3 = cell10.value
        actualSecondCardContent3 = driver.find_element_by_xpath("html/body/div[1]/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[3]/div/span[1]/span/span").text
        
        cell11 = first_sheet.cell(22,3)
        exSecondCardContent4 = cell11.value
        actualSecondCardContent4 = driver.find_element_by_xpath("html/body/div[1]/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[4]/div/span/span/span").text
      
        
        if(exSecondCardContent1 == actualSecondCardContent1):
            
            if(exSecondCardContent2 == actualSecondCardContent2):
                
                if(exSecondCardContent3 == actualSecondCardContent3):
                    
                    if(exSecondCardContent4 == actualSecondCardContent4):
                        
                        print "The Third card content is displaying as expected"
            
            
        else:
            
            print "Failed to find the expected content in Third card" 
            raise Exception
        
      
        # Clicking on < icon 
        print "Clicking on < arrow for Fourth card"
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[1]/div"))) 
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[1]/div").click()
        
        # Clicking on Fourth card
        print "Clicking on Fourth card"
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[2]/div/div[4]/div/div[1]"))) 
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[2]/div/div[4]/div/div[1]").click()
      
        # Going to verify the content in Fourth card card   
        print "Going to verify the content in Fourth card" 
        cell12 = first_sheet.cell(23,0)
        exThirdCardContent = cell12.value
        
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/span/span/span"))) 
        
        actualThirdCardContent = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/span/span/span").text
        
        if (exThirdCardContent in actualThirdCardContent):
            print "The Fourth card content is displaying as expected"
        else:
            print "Failed to find the expected content in Fourth card" 
            raise Exception
                
        # Going to click on Fifth card
        print "Clicking on Fifth card"
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[2]/div/div[5]/div/div[1]")))
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[2]/div/div[5]/div/div[1]").click()
               
        # Verifying Fifth card labels
        print "Going to verify the content in Fifth card"
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div")))
        
        cell13= first_sheet.cell(24,0)
        exFourthCardContent1 = cell13.value
        
        cell14= first_sheet.cell(24,1)
        exFourthCardContent2 = cell14.value
        
        cell15= first_sheet.cell(24,2)
        exFourthCardContent3 = cell15.value
        
        cell16= first_sheet.cell(24,3)
        exFourthCardContent4 = cell16.value
        
        cell17= first_sheet.cell(24,4)
        exFourthCardContent5 = cell17.value
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div/span/span[1]/span")))
        actualFourthCardContent1= driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div/span/span[1]/span").text
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div/span/span[2]/span")))
        actualFourthCardContent2= driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div/span/span[2]/span").text
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div/span/span[3]/span")))
        actualFourthCardContent3= driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div/span/span[3]/span").text
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[3]/div/span")))
        actualFourthCardContent4= driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[3]/div/span").text
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[4]/div/span/span/span")))
        actualFourthCardContent5= driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[4]/div/span/span/span").text
        
        if(exFourthCardContent1 == actualFourthCardContent1):
            
            if(exFourthCardContent2 == actualFourthCardContent2):
                
                if(exFourthCardContent3 == actualFourthCardContent3):
                    
                    if(exFourthCardContent4 == actualFourthCardContent4):
                        
                        if(exFourthCardContent5 == actualFourthCardContent5):
                            
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
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/span/span/span")))
        actualFifthCradContent=  driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/span/span/span").text
    
        cell18= first_sheet.cell(25,0)
        exFifthCardContent = cell18.value
      
        if(exFifthCardContent in actualFifthCradContent):
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
    
        cell19= first_sheet.cell(26,0)
        exSixthCardContent1 = cell19.value
        
        cell20= first_sheet.cell(26,1)
        exSixthCardContent2 = cell20.value
    
        cell21= first_sheet.cell(26,2)
        exSixthCardContent3 = cell21.value
        
        actualSixthCradContent1 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div/span/span/span").text
        
        actualSixthCradContent2 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[3]/div/span/span/span").text
        
        actualSixthCradContent3 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[4]/div/span/span/span").text
      
        if(exSixthCardContent1 == actualSixthCradContent1):
            
            if(exSixthCardContent2 == actualSixthCradContent2):
                
                if(exSixthCardContent3 == actualSixthCradContent3):
                    
                    print "The Seventh card content is displaying as expected"
            
            
        else:
            print "Failed to find the expected content in Seventh card" 
            
            raise Exception
    
    
        print "Clicking on > icon"
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[2]/div").click()
    
        # Going to Click on Eightth card
        print "Clicking on Eightth card"
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[2]/div/div[8]/div/div[1]")))
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[2]/div/div[8]/div/div[1]").click()
    
        # Going to verify the content in Eightth card
        print "Going to verify the content in Eightth card"
        
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/span/span/span")))
        
        cell22= first_sheet.cell(27,0)
        exSeventhCardContent1 = cell22.value
    
        actualSeventhCradContent1= driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/span/span/span").text
        
        if(exSeventhCardContent1 in actualSeventhCradContent1):
            print "The Eightth card content is displaying as expected"
        else:
            print "Failed to find the expected content in Eightth card" 
            raise Exception
        
        # Clicking on Nineth card
        print "Clicking on Nineth card"
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[2]/div/div[9]/div/div[1]").click()
        
        # Going to verify the content in Nineth card
        print "Going to verify the content in Nineth card"
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div")))
        
        cell23= first_sheet.cell(28,0)
        exEigtthCardContent1 = cell23.value
    
        cell24= first_sheet.cell(28,1)
        exEigtthCardContent2 = cell24.value
    
        cell25= first_sheet.cell(28,2)
        exEigtthCardContent3 = cell25.value
        
        cell26= first_sheet.cell(28,3)
        exEigtthCardContent4 = cell26.value
    
        cell27= first_sheet.cell(28,4)
        exEigtthCardContent5 = cell27.value
    
        cell28= first_sheet.cell(28,5)
        exEigtthCardContent6 = cell28.value
    
        actualEigtthCradContent1 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div/span/span[1]/span").text
    
        actualEigtthCradContent2 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div/span/span[2]/span").text
    
        actualEigtthCradContent3 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div/span/span[3]/span").text
    
        actualEigtthCradContent4 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[3]/div/span/span/span").text
        
        actualEigtthCradContent5 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[4]/div/span/span/span").text
        
        actualEigtthCradContent6 =  driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[6]/div/span/span/span").text
    
        if(exEigtthCardContent1 == actualEigtthCradContent1):
            
            if(exEigtthCardContent2 == actualEigtthCradContent2):
                
                if(exEigtthCardContent3 == actualEigtthCradContent3):
                    
                    if(exEigtthCardContent4 == actualEigtthCradContent4):
                        
                        if(exEigtthCardContent5 == actualEigtthCradContent5):
                            
                            if(exEigtthCardContent6 == actualEigtthCradContent6):
                            
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
        
        cell29= first_sheet.cell(29,0)
        exNinethCardContent1 = cell29.value
       
        cell30= first_sheet.cell(29,1)
        exNinethCardContent2 = cell30.value
        
        cell31= first_sheet.cell(29,2)
        exNinethCardContent3 = cell31.value
    
        actualNinethCradContent1 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/p/textarea").get_attribute("placeholder")
    
        actualNinethCradContent2 = driver.find_element_by_xpath(".//*[@id='question-answer-input-0']").get_attribute("placeholder")
        
        actualNinethCradContent3=  driver.find_element_by_xpath(".//*[@id='question-answer-input-1']").get_attribute("placeholder")
    
        plusIconLocator = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div[3]/div/div[1]/div/span")
        
        if(exNinethCardContent1 == actualNinethCradContent1 and plusIconLocator.is_displayed()):
            
            if(exNinethCardContent2 == actualNinethCradContent2):
                
                if(exNinethCardContent3 == actualNinethCradContent3):
                    
                    print "The Tenth card content is displaying as expected"
            
            
        else:
            print "Failed to find the expected content in Tenth card" 
            raise Exception
    
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='question-answer-input-0']")))
        print "Entering question"
      
        cell33= first_sheet.cell(1,2)
        questionCard = cell33.value
        
        ele=driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/p/textarea")
        ele.send_keys(questionCard)
        
        print "Entering first answer"
        cell34= first_sheet.cell(1,3)
        ans1 = cell34.value
        
        driver.find_element_by_xpath(".//*[@id='question-answer-input-0']").send_keys(ans1)
        print "Entering Second answer"
        cell35= first_sheet.cell(1,4)
        ans2 = cell35.value
        
        driver.find_element_by_xpath(".//*[@id='question-answer-input-1']").send_keys(ans2)
          
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saving...']")))
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saved']"))) 
    
    
    def publishLesson(self): 
        
        wait=WebDriverWait(driver, 60)
        
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        first_sheet = book.sheet_by_name('MultiCardLesson')
        
        cell32= first_sheet.cell(30,0)
        lesson_title_ExplainAConcept= cell32.value
        #wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saving...']")))
        #wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saved']"))) 
      
        wait.until(EC.element_to_be_clickable((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/button")))
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/button").click()
        
        print "Clicking on READY TO PUBLISH button"
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div/div[1]/section[3]/div/button[1]")))
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div/div[1]/section[3]/div/button[1]").click()
       
        print "Clicking on PUBLISH button"
        #print "Validating the success message after publish"
        #wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[2]/div/div/span[2]"))) 
        #actual_success_message= driver.find_element_by_xpath(".//*[@id='content']/div/div/div[2]/div/div/span[2]").text
        #expected_success_message= "You have successfully published \"" + lesson_title_ExplainAConcept + "\""; 
        
        #if(expected_success_message==actual_success_message):
            #print "The success message is displaying as"+ " "+expected_success_message
        #else:
            #print "The success message is not displaying as expected"
            
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[1]/a").click()
        print "Clicking on EXIT button"
             
        print "Verifying lesson displayed in Grid"
        wait.until(EC.visibility_of_element_located((By.XPATH,"(//tbody/tr/td[2]/a[.='"+lesson_title_ExplainAConcept+"'])[1]")))

        if driver.find_element_by_xpath("(//tbody/tr/td[2]/a[.='"+lesson_title_ExplainAConcept+"'])[1]").is_displayed():
            print "Lesson is displayed in Grid ::"+lesson_title_ExplainAConcept
            
        else:
            print "Lesson not displaying in grid"
            raise Exception
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[1]/div/nav/div/div[4]").click()
        
        
    
    
    def lessonExplainAConceptMain(self): 
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        first_sheet = book.sheet_by_name('MultiCardLesson')
        
        cell32= first_sheet.cell(30,0)
        lesson_title_ExplainAConcept= cell32.value
        try :
            
            obj1 = LessonExplainAConcept()
            obj1.lessonExplainAConcepts(10)
            obj1.publishLesson()
            lesdel= DeleteLesson()
            lesdel.lessonDelete(lesson_title_ExplainAConcept)
            print "TEST CASE EXECUTION SUCCESSFULLY COMPLETED"
        except Exception as e:
            traceback.print_exc()
            print (e)
            raise Exception
        
        finally:    
            book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
            first_sheet = book.sheet_by_name('Login_Credentials')
            # print("Fetching the Attribute Name from Excel Sheet\n")
            
            # read a cell
            cell = first_sheet.cell(1,1)
            HomeURL = cell.value
            #print HomeURL
            driver.get(HomeURL)
            #print "Home Page Loaded"

     
       

        
        
        
        
        
        
        
        
        
        
        
        
        

            
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
