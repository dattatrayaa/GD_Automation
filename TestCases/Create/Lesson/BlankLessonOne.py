'''
Created on Feb 20, 2018

@author: QA
'''
from os.path import os
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import wait, expected_conditions as EC
import xlrd
from selenium.webdriver.support.ui import WebDriverWait
from BaseTestClass import driver
from BaseTestClass import BaseTestClass
import traceback
from DeleteLesson import DeleteLesson
from BaseTestClass import projectPath
from CreateLessonDifferentCards import CreateLessonDifferentCards
class BlankLessonOne:
    
    def lessonWithTitletCard(self,lesson_title):   
        
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@href='/create/lessons']")))

        print "Clicking on Lessons button from side menu"
        driver.find_element_by_xpath("//a[@href='/create/lessons']").click()
    
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/header/div/button")))  
        
        print "Clicking on Create Lesson button from lessons page"
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[2]/div/header/div/button").click()
       
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[4 or 2]/div/div/div[2]/div[2]/div/div")))  
        
        print "Clicking on BlankLesson + icon from Create a new lesson pop up"
        driver.find_element_by_xpath("html/body/div[4 or 2]/div/div/div[2]/div[2]/div/div").click()
       
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[1]/div[1]/span")))  
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/h1/textarea").send_keys(lesson_title)
        print "Entering the lesson title in title card as"+" "+lesson_title
          
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saving...']")))
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saved']"))) 
        
        
    def lessonWithTextCard(self,TextContent):   
        
        wait=WebDriverWait(driver, 60)
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div").click()
        
        print "Clicking on Add card + icon"  
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div").click()
        
        print "Clicking on Text card"    
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saving...']")))
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saved']"))) 
        
        element = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div")
        webdriver.ActionChains(driver).move_to_element(element).click().send_keys(TextContent).perform()
        
        print "Entering the text as"+ " "+TextContent 
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saving...']")))
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saved']"))) 
        
    def addQuestionCard(self,questionCard,ans1,ans2):
        
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div"))) 
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div").click()
        
        print "Clicking on Add card + icon"  
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[5]/div[1]/div").click()
        
        print "Question card selected"
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='question-answer-input-0']")))
        
        print "Entering question"
        ele=driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/p/textarea")
        ele.send_keys(questionCard)
        
        print "Entering first answer"
        driver.find_element_by_xpath(".//*[@id='question-answer-input-0']").send_keys(ans1)
        
        print "Entering Second answer"
        driver.find_element_by_xpath(".//*[@id='question-answer-input-1']").send_keys(ans2)
          
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saving...']")))
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saved']"))) 
        
    def addImageCard(self,Imagefilepath1,linkname,Imagefilepath2,time):
        
        wait=WebDriverWait(driver, time)
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div").click()
        
        print "Clicking on Add card + icon"
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[1]/div").click()
        
        print "Image card selected"
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div[1]/h4/div/span[2]")))
        #driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div[1]/h4/div[1]/span[2]/div").click()
        #print "Clicking on browse for your file link"
     
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saving...']")))
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saved']"))) 
        
        print "Going to upload the image file"
        driver.find_element_by_css_selector('input[type="file"]').send_keys(Imagefilepath1)
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[1]/img")))
        
        imageContainerlocator_after1upload= driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[1]/img")
        
        if(imageContainerlocator_after1upload.is_displayed()):
            print 'Successfully uploaded the image1 file'
        else:
            print "Failed to upload the image1 file"
            raise Exception 
        

    def addVideoCard(self,videoName,time):
        
        wait=WebDriverWait(driver, time)
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div")))
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div").click()
        
        print "Clicking on Add card + icon"
        driver.find_element_by_xpath("html/body/div/div/div/div[3]/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[1]").click()
        
        #Uploading Video
        print "Uploading Video"
        driver.find_element_by_css_selector('input[type="file"]').send_keys(videoName)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[1]/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div[1]/button")))
        
        videoContainerlocator_afterupload= driver.find_element_by_xpath("html/body/div[1]/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div[1]/button")
        
        if(videoContainerlocator_afterupload.is_displayed()):
            print 'Successfully uploaded the Video file'
        else:
            print "Failed to upload the Video file"
            raise Exception
        
        driver.find_element_by_xpath("html/body/div[1]/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div[1]/button").click()
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div")))
     
        
    def addDocumentCard(self,document1Path,delay):
        
       
       docmnt=CreateLessonDifferentCards()
       docmnt.docCard(document1Path,delay)
        
        
        
    def publishLesson(self,lesson_title): 
        
        wait=WebDriverWait(driver, 60)
        wait.until(EC.element_to_be_clickable((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/button")))
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/button").click()
        
        print "Clicking on READY TO PUBLISH button"
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div/div[1]/section[3]/div/button[1]")))
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div/div[1]/section[3]/div/button[1]").click()
        
        print "Clicking on PUBLISH button"
        #print "Validating the success message after publish"
        # wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[2]/div/div/span[2]"))) 
        
        # actual_success_message= driver.find_element_by_xpath(".//*[@id='content']/div/div/div[2]/div/div/span[2]").text
        
        #expected_success_message= "You have successfully published \"" + lesson_title + "\""; 
        
        #if(expected_success_message==actual_success_message):
            #print "The success message is displaying as"+ " "+expected_success_message
        # else:
        #  print "The success message is not displaying as expected"
            
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[1]/a").click()
        print "Clicking on EXIT button"
             
        print "Verifying lesson displayed in Grid"
        wait.until(EC.visibility_of_element_located((By.XPATH,"(//tbody/tr/td[2]/a[.='"+lesson_title+"'])[1]")))

        if driver.find_element_by_xpath("(//tbody/tr/td[2]/a[.='"+lesson_title+"'])[1]").is_displayed():
            print "Lesson is displayed in Grid ::"+lesson_title
        else:
            print "Lesson not displaying in grid"
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[1]/div/nav/div/div[4]").click()
        
    def blankLessonOneMain(self):    
        
        try :
            book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
            first_sheet = book.sheet_by_name('MultiCardLesson')
            
            cell1 = first_sheet.cell(1,0)
            blankLessonOnename = cell1.value
            
            cell2 = first_sheet.cell(1,1)
            blankLessonOneTextCardText = cell2.value
            
            cell3 = first_sheet.cell(1,2)
            blankLessonOneQuestion = cell3.value
            
            cell4 = first_sheet.cell(1,3)
            blankLessonOneQuestionOption1 = cell4.value
            
            cell5 = first_sheet.cell(1,4)
            blankLessonOneQuestionOption2 = cell5.value
            
            cell6 = first_sheet.cell(1,5)
            blankLessonOneImageCard1 = cell6.value
            
            
            cell7 = first_sheet.cell(1,6)
            blankLessonOneUploadLink = cell7.value
            
            cell8 = first_sheet.cell(1,7)
            blankLessonOneImageCard2 = cell8.value
            
            cell9 = first_sheet.cell(1,8)
            blankLessonOneVideoCard = cell9.value
            
              
            cell10 = first_sheet.cell(1,9)
            blankLessonOneDocumentCard = cell10.value
            
            
            obj1 = BlankLessonOne()
            obj1.lessonWithTitletCard(blankLessonOnename)
            obj1.lessonWithTextCard(blankLessonOneTextCardText)
            obj1.addDocumentCard(blankLessonOneDocumentCard,200)
            obj1.addQuestionCard(blankLessonOneQuestion,blankLessonOneQuestionOption1,blankLessonOneQuestionOption2)
            obj1.addImageCard(blankLessonOneImageCard1,blankLessonOneUploadLink,blankLessonOneImageCard2,600)
            obj1.addVideoCard(blankLessonOneVideoCard,600)
            
            obj1.publishLesson(blankLessonOnename)
            #lesdel= DeleteLesson()
            #lesdel.lessonDelete(blankLessonOnename)
            print "TEST CASE EXECUTED SUCCESSFULLY COMPLETED"
         
        except Exception as e:
            traceback.print_exc()
            print (e)
            raise Exception
           
        finally:  
            print "clicking on Home"
            book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
            first_sheet = book.sheet_by_name('Login_Credentials')
            print("Fetching the Attribute Name from Excel Sheet\n")
            
            # read a cell
            cell = first_sheet.cell(1,1)
            HomeURL = cell.value
            print HomeURL
            driver.get(HomeURL)
            wait=WebDriverWait(driver, 80)
            wait.until(EC.visibility_of_element_located((By.ID,"global-header-search")))
            print "Home Page Loaded"
if __name__ == '__main__':
    
    o=BlankLessonOne()
    obj12= BaseTestClass()
    obj12.UserLogin()
    o.blankLessonOneMain()   
