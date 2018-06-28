'''
Created on 25-Apr-2018

@author: dattatraya
'''

import time

from BaseTestClass import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from MyDefinedExceptions import ErrorSavingLessonException

class LessonsPageElements:
    
    def lessonsButtonSideMenuUnexpanded(self):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@href='/create/lessons']")))
        driver.find_element_by_xpath("//a[@href='/create/lessons']").click()
    
    def createLessonButton(self):
        wait=WebDriverWait(driver, 60)
        create=wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/header/div/button")))
        create.click()
        
    def createANewLessonPopupHeader(self):
        wait=WebDriverWait(driver, 60)
        pop=wait.until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[4 or 2]/div/div/div[1]/h3")))
        return pop.text
    
    def clickOnBlankLesson(self):
        wait=WebDriverWait(driver, 60)
        blank=wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[4 or 2]/div/div/div[2]/div[2]/div")))
        webdriver.ActionChains(driver).move_to_element(blank).click(blank).perform()
        
        
    def settingLessonName(self,lessonName):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/h1/textarea")))
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/h1/textarea").send_keys(lessonName)
        
    def readyToPublishButtonClick(self):
        wait=WebDriverWait(driver, 60)
        publishbutton=wait.until(EC.element_to_be_clickable((By.XPATH,"html/body/div/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/button")))
        driver.execute_script("arguments[0].click();",publishbutton)

    def publishButtonClick(self):
        wait=WebDriverWait(driver, 60)
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH,"html/body/div/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div/div[1]/section[3]/div/button[1]")))
            driver.find_element_by_xpath("html/body/div/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div/div[1]/section[3]/div/button[1]").click()
        except Exception:
            driver.refresh()
            time.sleep(4)
            publishbutton=wait.until(EC.element_to_be_clickable((By.XPATH,"html/body/div/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/button")))
            driver.execute_script("arguments[0].click();",publishbutton)
            time.sleep(2)
            driver.execute_script("arguments[0].click();",publishbutton)
            
            wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div/div[1]/section[3]/div/button[1]")))
            wait.until(EC.element_to_be_clickable((By.XPATH,"html/body/div/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div/div[1]/section[3]/div/button[1]")))
            driver.find_element_by_xpath("html/body/div/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div/div[1]/section[3]/div/button[1]").click()
            

    def backButton(self):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[1]/a")))
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[1]/a").click() 
        
        
    def expandSideMenu(self):
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[1]/div/nav/div/div[4]").click()
        
        
        
    def addCardPlusiCon(self):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div/span")))
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div/span").click() 
        
    def textCardClick(self):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div/div[3]/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]")))
        driver.find_element_by_xpath("html/body/div/div/div/div[3]/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]").click() 
        
    def imageCardClick(self):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div/div[3]/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[1]")))
        driver.find_element_by_xpath("html/body/div/div/div/div[3]/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[1]").click() 
        
    def videoCardClick(self):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[1]/div/div/div[3]/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[1]")))
        driver.find_element_by_xpath("html/body/div[1]/div/div/div[3]/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[1]").click() 
        
    def documentCardClick(self):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[1]/div/div/div[3]/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[4]/div[1]")))
        driver.find_element_by_xpath("html/body/div[1]/div/div/div[3]/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[4]/div[1]").click() 
        
    def questionCardClick(self):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[1]/div/div/div[3]/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[5]/div[1]")))
        driver.find_element_by_xpath("html/body/div[1]/div/div/div[3]/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[5]/div[1]").click() 
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='question-answer-input-0']")))
        
    def textCardEnteringText(self,textCard):
        wait=WebDriverWait(driver, 60)
        textCardelement=wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@class='text']/div/div[1]/div")))
        webdriver.ActionChains(driver).move_to_element(textCardelement).click().send_keys(textCard).perform()
        
    def waitTillLessonSaved(self):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saving...']")))
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saved']")))
        except Exception:
            raise ErrorSavingLessonException
            
    def textCardVerifyTextEnteredXpath(self):
        return ".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/span/span"
    
    def imageUploadInImageCard(self,Imagefilepath1):
        driver.find_element_by_css_selector('input[type="file"]').send_keys(Imagefilepath1)
        
    def waitTillImageDisplayedXpath(self):
        return ".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[1]/img"
        
    def videoUploadInVideoCard(self,videoPath):
        driver.find_element_by_css_selector('input[type="file"]').send_keys(videoPath)  
    
    def waitTillVideoUploadReCheckStatusButtonXpath(self):
        return "html/body/div[1]/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div[1]/button"
    
    def readyToPublishButtonXpath(self):
        return "html/body/div[1]/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/button"
    
    def documentUploadDocumentCard(self,documentPath):
        driver.find_element_by_css_selector('input[type="file"]').send_keys(documentPath)
        
    def questionEnterQuestionCard(self,questionCard):
        questionArea=driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/p/textarea")
        questionArea.send_keys(questionCard)
        
    def answerOneQuestionCard(self):
        answer1=driver.find_element_by_xpath(".//*[@id='question-answer-input-0']")
        return answer1
        
    def answerTwoQuestionCard(self):
        answer2=driver.find_element_by_xpath(".//*[@id='question-answer-input-1']")
        return answer2
        
    def addAnswerChoice(self):
        wait=WebDriverWait(driver, 60)
        ansChoice=wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@class='question-add']/div/span")))
        ansChoice.click()
        
    def answerThreeQuestionCard(self,ans2):
        answer3=driver.find_element_by_xpath(".//*[@id='question-answer-input-2']")
        return answer3
        
    def answerFourQuestionCard(self,ans2):
        answer4=driver.find_element_by_xpath(".//*[@id='question-answer-input-4']")
        return answer4
        
    def questionAreaXpath(self):
        return ".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/p/textarea"
    
        
        
        
     
        
