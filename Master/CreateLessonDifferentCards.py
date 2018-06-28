'''
Created on 07-Mar-2018

@author: dattatraya
'''


import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from BaseTestClass import driver
from BaseTestClass import projectPath
from LessonsPageElements import LessonsPageElements


lesson=LessonsPageElements()
class CreateLessonDifferentCards:
    
    def textCard(self,textCard):
        
        
        print "Text card"
        print "Click on (+) icon"
        lesson.addCardPlusiCon()
    
        lesson.textCardClick()
        print "Clicked on Text Card"
            
        print "Entering Text in Text card" 
        lesson.textCardEnteringText(textCard)
        
        lesson.waitTillLessonSaved()
            
        #Verifying entered text is displaying text card
        print "Verifying entered text is displaying text card"
            
        textAfterEntering=driver.find_element_by_xpath(lesson.textCardVerifyTextEnteredXpath()).text
            
        if textAfterEntering==textCard:
            print "Verified Text '"+textCard+"' is displayed in Text Card"
        else:
            print "Text not displayed in Text card"
            raise Exception
        
    def imageCard(self,Imagefilepath1):
        print "\nUploading Image"
        wait=WebDriverWait(driver, 120)
        print "Click on (+) icon"
        
        lesson.addCardPlusiCon()
        
        print "Clicking on Image card"
        lesson.imageCardClick()
        
        print "Uploading image"
        lesson.imageUploadInImageCard(Imagefilepath1)
        
        print "Verifying Image is uploaded"
        imageContainerlocator_after1upload=wait.until(EC.visibility_of_element_located((By.XPATH,lesson.waitTillImageDisplayedXpath())))
        
        
        if(imageContainerlocator_after1upload.is_displayed()):
            
            print 'Successfully uploaded the image1 file'
            
        else:
            print "Failed to upload the image1 file"
            raise Exception
        
    def videoCard(self,videoPath,timeToUploadVideo):
        print "Click on (+) icon"
        wait=WebDriverWait(driver, 100)
        
        lesson.addCardPlusiCon()
        
        print "Clicking on Video card"
        lesson.videoCardClick()
        
        #Uploading Video
        print "Uploading Video"
        lesson.videoUploadInVideoCard(videoPath)
        
        videoContainerlocator_afterupload=WebDriverWait(driver,300).until(EC.visibility_of_element_located((By.XPATH,lesson.waitTillVideoUploadReCheckStatusButtonXpath())))
        
        
        if(videoContainerlocator_afterupload.is_displayed()):
            
            print "Successfully uploaded the Video file"
            
        else:
            print "Failed to upload the Video file"
            raise Exception
        
        
        driver.find_element_by_xpath(lesson.waitTillVideoUploadReCheckStatusButtonXpath()).click()
        
        wait.until(EC.visibility_of_element_located((By.XPATH,lesson.readyToPublishButtonXpath())))
        
        
    
    
    def docCard(self,documentPath,timetoUploadDoc):
        print "Document"
        print "Click on (+) icon"
        
        lesson.addCardPlusiCon()
        
        #Clicking on Document card
        lesson.documentCardClick()
        
        
        #Uploading Document
        print "Uploading Document"
        lesson.documentUploadDocumentCard(documentPath)
            
        
        WebDriverWait(driver, timetoUploadDoc).until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div[1]/button")))
        time.sleep(20)
        try:
            recheck=driver.find_element_by_xpath("html/body/div/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div[1]/button")
            webdriver.ActionChains(driver).move_to_element(recheck).click(recheck).perform()
        except Exception:
            WebDriverWait(driver, timetoUploadDoc).until(EC.visibility_of_element_located((By.XPATH,"(//div[@class='textLayer'])[1]")))
                    
        
        WebDriverWait(driver, timetoUploadDoc).until(EC.visibility_of_element_located((By.XPATH,"(//div[@class='textLayer'])[1]")))
        
            
        documentContainerlocator_afterupload= driver.find_element_by_xpath("(//div[@class='textLayer'])[1]")
        if(documentContainerlocator_afterupload.is_displayed()):
                
            print "Successfully uploaded the Document file"
                
        else:
            print "Failed to upload the Document file"
            raise Exception('Failed to upload Document file')
       
            
        
    def quesCard(self,questionCard,ans1,ans2):
        print "\nInserting Question card"
        wait=WebDriverWait(driver, 60)

        print "Click on (+) icon"
        
        lesson.addCardPlusiCon()
        
        lesson.questionCardClick()
                
        print "Question card selected"
        
        
        print "Entering question"
        lesson.questionEnterQuestionCard(questionCard)
        print "Question entered ::"
        
        print "Entering first answer"
        lesson.answerOneQuestionCard().send_keys(ans1)
        print "First Answer entered "
        print "Entering Second answer"
        lesson.answerTwoQuestionCard().send_keys(ans2)
        print "Second Answer entered "
        
        

        questionArea=driver.find_element_by_xpath(lesson.questionAreaXpath())
        
        print "\nVerifying All the data entered is displaying in fields"
        
        if questionArea.text==questionCard:
            print "Question ::"+questionCard
        else:
            print "Question is not displayed"
            raise Exception
        
        
        if lesson.answerOneQuestionCard().text==ans1:
            print "Answer 1 ::"+ans1
        else:
            print "Answer 1 is not displayed"
            raise Exception
        
        if lesson.answerTwoQuestionCard().text==ans2:
            print "Answer 2 ::"+ans2
        else:
            print "Answer 2 is not displayed"
            raise Exception


