'''
Created on Feb 27, 2018

@author: Shavinlal E
'''
from os.path import os
import time
import traceback

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import wait, expected_conditions as EC
from selenium.webdriver.support.select import Select
import xlrd
from DeleteLesson import DeleteLesson
from BaseTestClass import BaseTestClass
from BaseTestClass import WebDriverWait
from BaseTestClass import driver


# create a new Firefox session
class IntroduceATopic:
    
    
    def introduceATopic(self):   
        
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@href='/create/lessons']")))

        print "Clicking on Lessons button from side menu"
        driver.find_element_by_xpath("//a[@href='/create/lessons']").click()
    
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/header/div/button")))  
        print "Clicking on Create Lesson button from lessons page"
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[2]/div/header/div/button").click()
        
        print "Going to verify the display of INTRODUCE A TOPIC Teamplate"
        
        book=xlrd.open_workbook(os.path.join('TestData.xlsx'))
        first_sheet = book.sheet_by_name('MultiCardLesson')
        
        cell1 = first_sheet.cell(44,0)
        exTemplateNameIntroduceATopic = cell1.value
        
        
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div/div/div[2]/div[5]/div/div")))
        introduceATopiclLocator =  driver.find_element_by_xpath("html/body/div[2]/div/div/div[2]/div[5]/h4")
    
        if (introduceATopiclLocator.is_displayed() and introduceATopiclLocator.text == exTemplateNameIntroduceATopic):
            
            print "The INTRODUCE A TOPIC Template is displaying in Create a new lesson pop up"
        
        else:
            
            print "Failed to find the INTRODUCE A TOPIC Template in Create a new lesson pop up"
            raise Exception
    
        
        # Clicking on Introduce a topic template
        
        print "Clicking on INTRODUCE A TOPIC template"
        driver.find_element_by_xpath("html/body/div[2]/div/div/div[2]/div[5]/div/div").click()
        
        
        # Going to verify the number of cards displayed for the template INTRODUCE A TOPIC
        print "Going to verify the number of cards displayed for the template INTRODUCE A TOPIC"
        
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div/div/div")))
        cardsDisplayedIntroduceATopic=driver.find_elements_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div/div/div")
        
        actualNumberOfCardsIntroduceATopic = len(cardsDisplayedIntroduceATopic)
        
        cell2 = first_sheet.cell(45,0)
        exNumberOfCardsIntroduceATopic = cell2.value
      
        
        if(actualNumberOfCardsIntroduceATopic == exNumberOfCardsIntroduceATopic):
            
            print "The cards count is displaying as expected"+" "+str(exNumberOfCardsIntroduceATopic)
        
        
        else:
            
            print "Failed to find the card count as expected"
            raise Exception
        
        
        # Going to verify the title card content
        
        print "Going to verify the title card content"
    
        cell3 = first_sheet.cell(45,1)
        exTitleCardContentIntroduceATopic = cell3.value
        
        actualTitleCardContentIntroduceATopic = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/h1/textarea").text
      
        if (exTitleCardContentIntroduceATopic == actualTitleCardContentIntroduceATopic):
            
            print "The title card label is displaying as expected"+" "+'"'+exTitleCardContentIntroduceATopic+'"'
            
        else:
            
            print "Failed to find the expected label in title card"
            raise Exception
        
        
        # Going to clear the Title present in the title card
        
        print "Going to clear the lesson title"
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/h1/textarea").clear()
        
        
        print "Entering the title for lesson"
        
        cell4= first_sheet.cell(45,2)
        titleIntroduceATopic = cell4.value
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/h1/textarea").send_keys(titleIntroduceATopic)
        
        
        print "Clicking on second card"
        
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div/div/div[2]/div/div[1]")))
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div/div/div[2]/div/div[1]").click()
        
        print "Going to verify the content in second card"
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div")))
       
       
        cell5= first_sheet.cell(45,3)
        exSecondCardContentIntroduceATopic1  = cell5.value
        
        actualSecondCardContentIntroduceATopic1 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div/span/span/span").text
       
       
        cell6= first_sheet.cell(45,4)
        exSecondCardContentIntroduceATopic2  = cell6.value
       
        actualSecondCardContentIntroduceATopic2 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[3]/div/span[1]/span/span").text
       
       
        cell7= first_sheet.cell(45,5)
        exSecondCardContentIntroduceATopic3  = cell7.value
       
        actualSecondCardContentIntroduceATopic3 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[3]/div/span[5]/span/span").text
       
       
        cell8= first_sheet.cell(45,6)
        exSecondCardContentIntroduceATopic4  = cell8.value
       
        actualSecondCardContentIntroduceATopic4 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[3]/div/span[7]/span[1]/span").text
       
       
        cell9= first_sheet.cell(45,7)
        exSecondCardContentIntroduceATopic5  = cell9.value
       
        actualSecondCardContentIntroduceATopic5 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[3]/div/span[7]/span[2]/span").text
       
       
       
        cell10= first_sheet.cell(45,8)
        exSecondCardContentIntroduceATopic6  = cell10.value
       
        actualSecondCardContentIntroduceATopic6 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[5]/div/span").text
       
       
        if(exSecondCardContentIntroduceATopic1 == actualSecondCardContentIntroduceATopic1):
                     
            if(exSecondCardContentIntroduceATopic2 == actualSecondCardContentIntroduceATopic2):
         
                if(exSecondCardContentIntroduceATopic3 == actualSecondCardContentIntroduceATopic3):
                    
                    if(exSecondCardContentIntroduceATopic4 == actualSecondCardContentIntroduceATopic4):
                        
                        if(exSecondCardContentIntroduceATopic5 == actualSecondCardContentIntroduceATopic5):
                            
                            if(exSecondCardContentIntroduceATopic6 == actualSecondCardContentIntroduceATopic6):
                                
                                print "Successfully verified the content in second card"
        
        
        else:
            
            print "Failed to verify the content in second card"
            raise Exception
        
        
        print "Clicking on Third card"
        
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[2]/div/div[3]/div/div[1]")))
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[2]/div/div[3]/div/div[1]").click()
        
        print "Going to verify the contents in Third card"
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div")))
        
        
        cell11= first_sheet.cell(46,0)
        exThirdCardContentIntroduceATopic1  = cell11.value
        
        actualThirdCardContentIntroduceATopic1 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div/span/span/span").text
              
         
              
        cell12= first_sheet.cell(46,1)
        exThirdCardContentIntroduceATopic2  = cell12.value
        
        actualThirdCardContentIntroduceATopic2 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[3]/div/span/span[1]/span").text
               
        
          
        cell13= first_sheet.cell(46,2)
        exThirdCardContentIntroduceATopic3  = cell13.value
        
        actualThirdCardContentIntroduceATopic3 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[3]/div/span/span[2]/span").text
                 
        
          
        cell14= first_sheet.cell(46,3)
        exThirdCardContentIntroduceATopic4 = cell14.value
        
        actualThirdCardContentIntroduceATopic4= driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[3]/div/span/span[3]/span").text
                  
        
        cell15= first_sheet.cell(46,4)
        exThirdCardContentIntroduceATopic5 = cell15.value
        
        actualThirdCardContentIntroduceATopic5= driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[5]/div/span/span/span").text
                   
         
        cell16= first_sheet.cell(46,5)
        exThirdCardContentIntroduceATopic6 = cell16.value
        
        actualThirdCardContentIntroduceATopic6= driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[6]/div/span/span[1]/span").text
                   
          
        cell17= first_sheet.cell(46,6)
        exThirdCardContentIntroduceATopic7 = cell17.value
        
        actualThirdCardContentIntroduceATopic7= driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[6]/div/span/span[2]/span").text
                   
              
        cell18= first_sheet.cell(46,7)
        exThirdCardContentIntroduceATopic8 = cell18.value
        
        actualThirdCardContentIntroduceATopic8= driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[6]/div/span/span[3]/span").text
        
        if(exThirdCardContentIntroduceATopic1 == actualThirdCardContentIntroduceATopic1):
                     
            if(exThirdCardContentIntroduceATopic2 == actualThirdCardContentIntroduceATopic2):
         
                if(exThirdCardContentIntroduceATopic3 == actualThirdCardContentIntroduceATopic3):
                    
                    if(exThirdCardContentIntroduceATopic4 == actualThirdCardContentIntroduceATopic4):
                        
                        if(exThirdCardContentIntroduceATopic5 == actualThirdCardContentIntroduceATopic5):
                            
                            if(exThirdCardContentIntroduceATopic6 == actualThirdCardContentIntroduceATopic6):
                                
                                if(exThirdCardContentIntroduceATopic7 == actualThirdCardContentIntroduceATopic7):
                                
                                    if(exThirdCardContentIntroduceATopic8 == actualThirdCardContentIntroduceATopic8):
                                
                                        print "Successfully verified the content in Third card"
        
        
        else:
            
            print "Failed to verify the content in Third card"
            raise Exception
        
        
        print "Clicking on Fourth card"
        
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[2]/div/div[4]/div/div[1]")))   
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[2]/div/div[4]/div/div[1]").click()   
           
        print "Going to verify the content in Fourth card"
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div")))
           
           
        cell19= first_sheet.cell(47,0)
        exFourthCardContentIntroduceATopic1 = cell19.value   
           
        actualFourthCardContentIntroduceATopic1 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div/span/span/span").text
           
                       
        cell20= first_sheet.cell(47,1)
        exFourthCardContentIntroduceATopic2 = cell20.value   
           
        actualFourthCardContentIntroduceATopic2 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[2]/div/span/span/span").text
           
         
        if (exFourthCardContentIntroduceATopic1 == actualFourthCardContentIntroduceATopic1):
            
            if(exFourthCardContentIntroduceATopic2 == actualFourthCardContentIntroduceATopic2):
                
                print "Successfully verified the content in fourth card"    
          
          
        else: 
            
            print "Failed to verify the content in Fourth card"
            raise Exception
          
          
        print "Clicking on Fifth card" 
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[2]/div/div[5]/div/div[1]")))   
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[2]/div/div[5]/div/div[1]").click()  
          
        print "Going to verify the content in Fifth card" 
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div")))
          
          
        cell21= first_sheet.cell(48,0)
        exFifthCardContentIntroduceATopic1 = cell21.value   
           
        actualFifthCardContentIntroduceATopic1 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div/span/span[1]/span").text
            
          
        cell22= first_sheet.cell(48,1)
        exFifthCardContentIntroduceATopic2 = cell22.value   
           
        actualFifthCardContentIntroduceATopic2 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div/span/span[3]/span").text
            
          
         
        cell23= first_sheet.cell(48,2)
        exFifthCardContentIntroduceATopic3 = cell23.value   
           
        actualFifthCardContentIntroduceATopic3 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div/span/span[4]/span").text
            
          
         
        cell24= first_sheet.cell(48,3)
        exFifthCardContentIntroduceATopic4 = cell24.value   
           
        actualFifthCardContentIntroduceATopic4 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div/span/span[5]/span").text
            
          
        cell25= first_sheet.cell(48,4)
        exFifthCardContentIntroduceATopic5 = cell25.value   
           
        actualFifthCardContentIntroduceATopic5 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[3]/div/span/span/span").text
            
         
         
        cell26= first_sheet.cell(48,5)
        exFifthCardContentIntroduceATopic6 = cell26.value   
           
        actualFifthCardContentIntroduceATopic6 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[4]/div/span/span/span").text
            
         
         
        if(exFifthCardContentIntroduceATopic1 == actualFifthCardContentIntroduceATopic1):
                     
            if(exFifthCardContentIntroduceATopic2 == actualFifthCardContentIntroduceATopic2):
         
                if(exFifthCardContentIntroduceATopic3 == actualFifthCardContentIntroduceATopic3):
                    
                    if(exFifthCardContentIntroduceATopic4 == actualFifthCardContentIntroduceATopic4):
                        
                        if(exFifthCardContentIntroduceATopic5 == actualFifthCardContentIntroduceATopic5):
                            
                            if(exFifthCardContentIntroduceATopic6 == actualFifthCardContentIntroduceATopic6):
                        
                                print "Successfully verified the content in Fifth card"
        
        
        else:
            
            print "Failed to verify the content in Fifth card"
            raise Exception
         
        print "Clicking on Sixth card"
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[2]/div/div[6]/div/div[1]")))   
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[2]/div/div[6]/div/div[1]").click()
         
        print "Going to verify the content in Sixth card" 
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div"))) 
         
         
        cell27= first_sheet.cell(49,0)
        exSixthCardContentIntroduceATopic1 = cell27.value   
           
        actualSixthCardContentIntroduceATopic1 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div/span/span/span").text
            
          
        cell28= first_sheet.cell(49,1)
        exSixthCardContentIntroduceATopic2 = cell28.value   
           
        actualSixthCardContentIntroduceATopic2 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[3]/div/span/span[1]/span").text
            
          
        cell29= first_sheet.cell(49,2)
        exSixthCardContentIntroduceATopic3 = cell29.value   
           
        actualSixthCardContentIntroduceATopic3 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[3]/div/span/span[2]/span").text
            
         
        cell30= first_sheet.cell(49,3)
        exSixthCardContentIntroduceATopic4 = cell30.value   
           
        actualSixthCardContentIntroduceATopic4 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[3]/div/span/span[3]/span").text
            
         
        if(exSixthCardContentIntroduceATopic1 in actualSixthCardContentIntroduceATopic1):
             
            if(exSixthCardContentIntroduceATopic2 == actualSixthCardContentIntroduceATopic2):
                 
                if(exSixthCardContentIntroduceATopic3 == actualSixthCardContentIntroduceATopic3):
                     
                    if(exSixthCardContentIntroduceATopic4 == actualSixthCardContentIntroduceATopic4):
                        
                        print "Successfully verified the content in Sixth card"
         
         
         
        else:
            
            print "Failed to verify the content in Sixth card"
            raise Exception
         
        print "Clicking on Seventh card" 
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[2]/div/div[7]/div/div[1]")))   
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[2]/div/div[7]/div/div[1]").click()
          
         
        print "Going to verify the content in Seventh card" 
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div"))) 
         
         
        cell31= first_sheet.cell(50,0)
        exSeventhCardContentIntroduceATopic1 = cell31.value   
           
        actualSeventhCardContentIntroduceATopic1 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div/span/span/span").text
         
         
        cell32= first_sheet.cell(50,1)
        exSeventhCardContentIntroduceATopic2 = cell32.value   
           
        actualSeventhCardContentIntroduceATopic2 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[2]/div/span/span/span").text
         
        if(exSeventhCardContentIntroduceATopic1 == actualSeventhCardContentIntroduceATopic1):
         
            if(exSeventhCardContentIntroduceATopic2 ==actualSeventhCardContentIntroduceATopic2):
                
                print "Successfully verified the Seventh card content"
            
                
        else:
        
            print "Failed to verify Seventh card content"  
            raise Exception 
              
              
        print "Clicking on Eight th card"     
              
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[2]/div/div[8]/div/div[1]")))   
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[2]/div/div[8]/div/div[1]").click()      
         
        print "Going to verify the content in Eight th card"
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div"))) 
          
         
          
        cell33= first_sheet.cell(51,0)
        exEightthCardContentIntroduceATopic1 = cell33.value   
           
        actualEightthCardContentIntroduceATopic1 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div/span/span[1]/span").text 
         
         
         
        cell34= first_sheet.cell(51,1)
        exEightthCardContentIntroduceATopic2 = cell34.value   
           
        actualEightthCardContentIntroduceATopic2 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div/span/span[2]/span").text 
         
         
        cell35= first_sheet.cell(51,2)
        exEightthCardContentIntroduceATopic3 = cell35.value   
           
        actualEightthCardContentIntroduceATopic3 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div/span/span[3]/span").text 
         
         
        cell36= first_sheet.cell(51,3)
        exEightthCardContentIntroduceATopic4 = cell36.value   
           
        actualEightthCardContentIntroduceATopic4 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[3]/div/span/span/span").text 
         
         
        cell37= first_sheet.cell(51,4)
        exEightthCardContentIntroduceATopic5 = cell37.value   
           
        actualEightthCardContentIntroduceATopic5 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[4]/div/span/span/span").text 
         
          
        if(exEightthCardContentIntroduceATopic1 == actualEightthCardContentIntroduceATopic1):
            
            if(exEightthCardContentIntroduceATopic2 == actualEightthCardContentIntroduceATopic2):
                
                if(exEightthCardContentIntroduceATopic3 == actualEightthCardContentIntroduceATopic3):
                    
                    if(exEightthCardContentIntroduceATopic4 == actualEightthCardContentIntroduceATopic4):
                        
                        if(exEightthCardContentIntroduceATopic5 == actualEightthCardContentIntroduceATopic5):
                            
                            print "Successfully verified the content in Eight th card"
           
        else: 
              
            print "Failed to verify the content in Eight th card"
            raise Exception   
        
        
        print "Clicking on Nineth card"
        
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[2]/div/div[9]/div/div[1]")))   
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[2]/div/div[9]/div/div[1]").click()
    
    
        print "Going to verify the content in Nineth card"
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div")))
        
        
              
        cell38= first_sheet.cell(52,0)
        exNinethCardContentIntroduceATopic1 = cell38.value   
           
        actualNinethCardContentIntroduceATopic1 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div/span/span/span").text 
             
              
              
        cell39= first_sheet.cell(52,1)
        exNinethCardContentIntroduceATopic2 = cell39.value   
           
        actualNinethCardContentIntroduceATopic2 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[2]/div/span/span/span").text 
    
           
                  
        if(exNinethCardContentIntroduceATopic1 == actualNinethCardContentIntroduceATopic1):
            
            if(exNinethCardContentIntroduceATopic2 == actualNinethCardContentIntroduceATopic2):
                
                
                print "Successfully verified the content in Nine th card"
           
        else: 
              
            print "Failed to verify the content in Nine th card"
            raise Exception         
              
              
              
        print "Clicking on Ten th card"    
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[2]/div/div[10]/div/div[1]")))   
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[2]/div/div[10]/div/div[1]").click()
    
         
         
        print "Going to verify the content in Ten th card"
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div")))
             
              
        cell40= first_sheet.cell(53,0)
        exTenthCardContentIntroduceATopic1 = cell40.value   
           
        actualTenthCardContentIntroduceATopic1 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div/span/span[1]/span").text 
    
                 
        cell41= first_sheet.cell(53,1)
        exTenthCardContentIntroduceATopic2 = cell41.value   
           
        actualTenthCardContentIntroduceATopic2 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div/span/span[2]/span").text 
        
              
        cell42= first_sheet.cell(53,2)
        exTenthCardContentIntroduceATopic3 = cell42.value   
           
        actualTenthCardContentIntroduceATopic3 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[3]/div/span").text 
        
                   
          
        cell43= first_sheet.cell(53,2)
        exTenthCardContentIntroduceATopic4 = cell43.value   
           
        actualTenthCardContentIntroduceATopic4 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div[4]/div/span/span/span").text 
        
                    
          
        if(exTenthCardContentIntroduceATopic1 == actualTenthCardContentIntroduceATopic1):
            
            if(exTenthCardContentIntroduceATopic2 == actualTenthCardContentIntroduceATopic2):
                
                if(exTenthCardContentIntroduceATopic3 == actualTenthCardContentIntroduceATopic3):
                    
                    if(exTenthCardContentIntroduceATopic4 == actualTenthCardContentIntroduceATopic4):
                
                
                        print "Successfully verified the content in Ten th card"
           
        else: 
              
            print "Failed to verify the content in Ten th card"
            raise Exception         
               
          
        print "Clicking on Eleven th card"  
          
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[2]/div/div[11]/div/div[1]")))   
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div[2]/div/div[11]/div/div[1]").click()
     
          
        print "Going to verify the content in Eleventh card"
        
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/p/textarea")))

        
        cell44= first_sheet.cell(54,0)
        exEleventhCardIntroduceATopicContent1 = cell44.value
       
        cell45= first_sheet.cell(54,1)
        exEleventhCardIntroduceATopicContent2 = cell45.value
        
        cell46= first_sheet.cell(54,2)
        exEleventhCardIntroduceATopicContent3 = cell46.value
        
    
        actualEleventhCardIntroduceATopic1 = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/p/textarea").get_attribute("placeholder")
    
        actualEleventhCardIntroduceATopic2 = driver.find_element_by_xpath(".//*[@id='question-answer-input-0']").get_attribute("placeholder")
        
        actualEleventhCardIntroduceATopic3=  driver.find_element_by_xpath(".//*[@id='question-answer-input-1']").get_attribute("placeholder")
    
        plusIconLocatorIntroduceATopic = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div[3]/div/div[1]/div/span")
        
   
        
        if(exEleventhCardIntroduceATopicContent1 == actualEleventhCardIntroduceATopic1):
            
            if(exEleventhCardIntroduceATopicContent2 == actualEleventhCardIntroduceATopic2):
                
                if(exEleventhCardIntroduceATopicContent3 == actualEleventhCardIntroduceATopic3):
                    
                    if(plusIconLocatorIntroduceATopic.is_displayed()):
                    
                        print "The Eleventh card content is displaying as expected"
            
            
        else:
            
            print  "Failed to find the expected content in Eleventh card" 
            raise Exception

    
    
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='question-answer-input-0']")))
        print "Entering question"
        
      
        cell47= first_sheet.cell(1,2)
        questionCard = cell47.value
        
        ele=driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/p/textarea")
        ele.send_keys(questionCard)
        
        print "Entering first answer"
        
        cell48= first_sheet.cell(1,3)
        ans1 = cell48.value
        
        driver.find_element_by_xpath(".//*[@id='question-answer-input-0']").send_keys(ans1)
        print "Entering Second answer"
        cell49= first_sheet.cell(1,4)
        ans2 = cell49.value
        
        driver.find_element_by_xpath(".//*[@id='question-answer-input-1']").send_keys(ans2)
          
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saving...']")))
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saved']"))) 
    
    def publishLesson(self): 
            
      
        wait=WebDriverWait(driver, 60)
        
        book=xlrd.open_workbook(os.path.join('TestData.xlsx'))
        first_sheet = book.sheet_by_name('MultiCardLesson')
        cell50= first_sheet.cell(45,2)
        lesson_title_TeachASkill = cell50.value
        #wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saving...']")))
        #wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saved']"))) 
      
        wait.until(EC.element_to_be_clickable((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/button")))
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/button").click()
        print "Clicking on READY TO PUBLISH button"
         
        
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div/div[1]/section[3]/div/button[1]")))
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div/div[1]/section[3]/div/button[1]").click()
        print "Clicking on PUBLISH button"
        
        #print "Validating the success message after publish"
        #wait=WebDriverWait(driver, 60) 
        #wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[2]/div/div/span[2]"))) 
        #actual_success_message= driver.find_element_by_xpath(".//*[@id='content']/div/div/div[2]/div/div/span[2]").text
        #expected_success_message= "You have successfully published \"" + lesson_title_TeachASkill + "\""; 
       
        
        #if(expected_success_message==actual_success_message):
            
           # print "The success message is displaying as expected"+ " "+expected_success_message
            
        #else:
            
           ## print "The success message is not displaying as expected"
            
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
        
          
          
         
              
              
    def introduceATopicMain(self): 
            book=xlrd.open_workbook(os.path.join('TestData.xlsx'))
            first_sheet = book.sheet_by_name('MultiCardLesson')
            cell50= first_sheet.cell(45,2)
            lesson_title_TeachASkill = cell50.value
        
        try: 
            obj1 = IntroduceATopic()
            obj1.introduceATopic()
            obj1.publishLesson()
            lesdel= DeleteLesson()
            lesdel.lessonDelete(lesson_title_TeachASkill)
            print "TEST CASE EXECUTED SUCCESSFULLY COMPLETED"
        except Exception as e:
            traceback.print_exc()
            print (e)
            raise Exception
            
        finally:
            print "clicking on Home"
            book=xlrd.open_workbook(os.path.join('TestData.xlsx'))
            first_sheet = book.sheet_by_name('Login_Credentials')
            print("Fetching the Attribute Name from Excel Sheet\n")
            # read a cell
            cell = first_sheet.cell(1,1)
            HomeURL = cell.value
            print HomeURL
            driver.get(HomeURL)
            print "Home Page Loaded"
     


        
        
        
        
        
        
        
        
