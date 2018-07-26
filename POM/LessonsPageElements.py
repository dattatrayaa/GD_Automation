'''
Created on 25-Apr-2018

@author: dattatraya
'''

import time

from BaseTestClass import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from MyDefinedExceptions import ErrorSavingLessonException
from __builtin__ import Exception
import traceback


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
    
    def selectingText(self):
        return "//div[@class='text']/div/div[1]/div"
    
    def textSettingsbox(self):
        return "//div[@class='rich-text-setting']"
    
    def textUrlLink(self):
        return "//html//div[@class='u-height-100-percent']/div[1]"
    
    def linkTextBox(self):
        return "(//input[@type='text'])[2]"
    
    def linkTickmark(self):
        return "//button[@class='btn btn-transparent-no-border embedded-link-btn']"
    
    def removingLinkTextCard(self):
        return "//button[@class='btn btn-transparent-no-border embedded-link-btn']"
    
    def previewButton(self):
        wait=WebDriverWait(driver, 60)
        pre=wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@class='bottom-cell right-cell']//span//button[@class='btn btn-secondary btn-responsive']")))
        pre.click()
    
    def linkInPreviewofTextCard(self):
        return "//div[@class='card-viewer-container clearfix']//p//span[@class='text-huge']//u"    
    
    def closePreview(self):
        return "//div[@class='full-screen-close-icon']"
    
    def TextSettingsMovingToMid(self):
        return "//div[@class='toggle-action has-left-border']"
    
    def TextSettingsMovingToRight(self):
        return "//html//div[@class='page-content-outer clearfix is-expanded-on-desktop']//div[4]" 
    
    def fontSizeToggle(self):
        return "//span[@class='toggle-font-size']"
    
    def fontSizeToggleOption(self):
        return "//span[.='Small']/../../li/span[.='Normal']/../../li/span[.='Large']/../../li/span[.='Huge']"
    
    def fontSizeToggleHuge(self):
        return "//span[.='Huge']"
    
    def checkFontSizeHuge(self):
        wait=WebDriverWait(driver, 60)
        ele=wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/span")))
        return ele
    
    def bulletTOText(self):
        return "//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[6]"
    
    def NumberBulletTOText(self):
        return "//html//div[7]"
    
    def boldText(self):
        return "//html//div[8]"
    
    def ItalicText(self):
        return "//html//div[9]"
    
    def underline(self):
        return "//html//div[10]"
    
    def fontColor(self):
        return "//html//div[11]/span[1]"
    
    
    def imageUploadInBgTextCard(self,Imagefilepath1):
        driver.find_element_by_css_selector('input[type="file"]').send_keys(Imagefilepath1)
        
    def textCardDeleteBgImageButton(self):
        return "//button[@class='btn btn-small btn-transparent-no-border u-ml8']" 
    
    def showWhiteBox(self):
        return "//*[@id='content']/div/div/div[3]/div[2]/div/div/div[1]/div[2]/div[1]/div[1]/label/span[2]/span"
    
    def showWhiteBoxUnchecked(self):
        return "//*[@id='content']/div/div/div[3]/div[2]/div/div/div[1]/div[2]/div[1]/div[1]/label/span[2]"
    
    def checkWhiteBoxdisabled(self):
        return "//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div"
    
    def addInlineImageCheckBox(self):
        return "//label[@for='add-inline-image']//span[@class='checkbox-check']"
    
    def inlineImageBox(self):
        return "//div[@class='u-relative u-height-100-percent u-width-100-percent']"
    
    def addingInlineImage(self,Imagefilepath1):
        driver.find_element_by_css_selector('input[type="file"]').send_keys(Imagefilepath1)
        
    def inlineImageDisplayed(self):
        return "//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div/div/div/div[1]/img"
    
    def changeImageButtonInlineBox(self):
        wait=WebDriverWait(driver, 60)
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,"//label[contains(.,'Change')]")))
            print "Change Image button displayed"
        except Exception:
            print "Change Image button not displayed"
            raise Exception
        
    def DeleteImageButtonInlineBox(self):
        wait=WebDriverWait(driver, 60)
        try:
            delete=wait.until(EC.visibility_of_element_located((By.XPATH,"//button[@class='btn btn-transparent btn-icon']")))
            print "Delete Image button displayed"
            return delete
        except Exception:
            print "Delete Image button not displayed"
            raise Exception
    
    def adjustTextBoxLayOut(self):
        return "//button[@class='u-text-link-light-blue small-left-padding']"
    
    def topLeftLayOut(self):
        return "//html//div[@class='setting-layout-container']/div[2]"    
    
    def topRightLayOut(self):
        return "//html//div[@class='setting-layout-container']/div[3]"
    
    def bottomRightLayOut(self):
        return "//*[@id='content']/div/div/div[3]/div[2]/div/div/div[1]/div[2]/div[2]/div[4]"
    
    def bottomLeftLayOut(self):
        return "//*[@id='content']/div/div/div[3]/div[2]/div/div/div[1]/div[2]/div[2]/div[5]"
    
    def centerLayout(self):
        return "//html//div[@class='page-sidebar is-inline']//div[6]"
    
    def checkingTextBoxHidden(self):
        wait=WebDriverWait(driver, 60)
        try:
            wait.until(EC.invisibility_of_element_located((By.XPATH,"//html//div[@class='page-sidebar is-inline']//div[6]")))
            print"Adjust layout text box is hidden successfully"
        except Exception:
            print "Failed to hide Check"
            raise Exception
    
    
    
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
    
    def enalargeToFitToggle(self):
        wait=WebDriverWait(driver, 60)
        try:
            enlarge=wait.until(EC.visibility_of_element_located((By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]")))
            enlarge.click()
        except Exception:
            print "Failed to click on Enlarge to fit toggle button"
            raise Exception
    
    def ImageCardBGColor(self):
        return "//button[@class='color-preview-box']"
    
    def settingRGBcolor(self,r,g,b):
        wait=WebDriverWait(driver, 60)
        try:
            red=wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='color-picker-r']")))
            red.clear()
            red.send_keys(str(r))
        except Exception:
            print "Failed to set r value"
            raise Exception
        try:
            green=driver.find_element(By.XPATH, "//input[@id='color-picker-g']")
            green.clear()
            green.send_keys(str(g))
        except Exception:
            print "Falied to set g value"
            raise Exception
        
        try:
            blue=driver.find_element(By.XPATH, "//input[@id='color-picker-b']")
            blue.clear()
            blue.send_keys(str(b))
        except Exception:
            print "Failed to set b value"
            raise Exception
        print "Background Color rgb("+str(r)+", "+str(g)+", "+str(b)+") has been set "
    
    def checkingRGBColorImgCardBG(self,r,g,b):
        wait=WebDriverWait(driver, 60)
        rgb=wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div")))
        text=rgb.get_attribute("style")
        print text
        print "rgb("+str(int(r))+", "+str(int(g))+", "+str(int(b))+")"
        if "rgb("+str(int(r))+", "+str(int(g))+", "+str(int(b))+")" in text:
            print "Verified, Bg color displayed properly"
        else:
            print "RGB color is not displayed properly"
            raise Exception
    def deleteImageImgCard(self):
        wait=WebDriverWait(driver, 60)
        delImg=wait.until(EC.visibility_of_element_located((By.XPATH,"//button[@class='btn btn-transparent btn-icon']")))
        try:
            delImg.click()
        except Exception:
            print "Failed to Click on Delete Image button"
            raise Exception

    def ImgCardImgDeleteCheck(self):
        wait=WebDriverWait(driver, 60)
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='u-text-link-blue u-inline-block u-relative u-cursor-pointer']")))
            print "Successfully image is deleted"
        except Exception:
            print "Failed to delete Image from image card"
            raise Exception
    
        
    def deleteCardLink(self):
        return "//button[@class='btn btn-transparent-no-border']"
    
    
    def DesktopPreviewOfImageCard(self):
        wait=WebDriverWait(driver, 60)
        try:
            wait.until(EC.visibility_of_all_elements_located((By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/img[1]")))
            print "Image Displayed In desktop preview"
        except Exception:
            print "Failed to Show image in Preview of Image card in Desktop view"
            raise Exception
    def mobilePreviewButton(self):  
        wait=WebDriverWait(driver, 60)
        try:
            mobile=wait.until(EC.visibility_of_all_elements_located((By.XPATH,"//*[@id='content']/div/div/div[4]/div[1]/div[2]/button[2]")))
            webdriver.ActionChains(driver).move_to_element(mobile).click(mobile).perform()
            print "Clicked on Mobile preview button"
        except Exception:
            print traceback
            print "Failed to click on Mobile preview button in Preview pop up"
            raise Exception

        
    def MobilePreviewOfImageCard(self):
        wait=WebDriverWait(driver, 60)
        try:
            wait.until(EC.visibility_of_all_elements_located((By.XPATH,"//img[@class='fit-to-width elastic-image']")))
            print "Image Displayed In Mobile preview"
        except Exception:
            print "Failed to Show image in Preview of Image card in Mobile View"
            raise Exception

    
    def CountOfAllCardDisplayed(self):
        wait=WebDriverWait(driver, 60)
        allcards=wait.until(EC.visibility_of_all_elements_located((By.XPATH,"//div[@class='card-preview-container horizontal']/div")))
        t=len(allcards)
        return t
        
        
    def videoUploadInVideoCard(self,videoPath):
        driver.find_element_by_css_selector('input[type="file"]').send_keys(videoPath)  
    
    def waitTillVideoUploadReCheckStatusButtonXpath(self):
        return "html/body/div[1]/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div[1]/button"
    
    def changeVideoButton(self):
        return "//div[@class='btn btn-transparent']"
    
    def videoDisplayed(self):
        return "//div[@class='u-relative u-height-100-percent u-width-100-percent']//video[@preload='auto']"
    
    def playButtonVideo(self):
        return "//div[@class='u-relative u-height-100-percent u-width-100-percent']//span[@class='card-overlay-button']"
    
    def lengthOfVideo(self):
        return "/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/span[2]"
    
    def enlargeVideoToggle(self):
        wait=WebDriverWait(driver, 60)
        enlarge=wait.until(EC.visibility_of_element_located((By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]")))
        enlarge.click()
        
    def videoEnargement(self): 
        return "//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div"   
    
    def videoInDesktopPreview(self):
        return "//div[@class='card-container interactive-media-card']//video[@preload='auto']"
    
    def VideoInMobilePreview(self):
        return "/html[1]/body[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/video[1]"
    
    def deleteVideoFromVideoCard(self):
        wait=WebDriverWait(driver, 60)
        try:
            deletevideo=wait.until(EC.visibility_of_element_located((By.XPATH,"//button[@class='btn btn-transparent btn-icon']")))
            deletevideo.click()
        except Exception:
            print traceback
            print "Failed to delete video"
            raise Exception("Failed to delete video")
        
    def browsefileLinkVideoCard(self):
        return "//span[@class='u-text-link-blue u-inline-block u-relative u-cursor-pointer']"
    
        
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
    
    def titlebackgroundColor(self):
        return "//html//div[1]/div[1]/div[2]/button[1]"
        
    def colorpickerHex(self):  
        return "//input[@id='color-picker-hex']" 
     
    def titleCardBackgroundImage(self,Imagefilepath1):
        driver.find_element_by_css_selector('input[type="file"]').send_keys(Imagefilepath1)
    
    def BgImgdeletebuttonTitlecard(self):   
        return "//button[@class='btn btn-small btn-transparent-no-border u-ml8']" 
    
    def giphyButton(self):
        return "//button[@class='setting-btn giphy-btn']"
    
    def giphypopupHeader(self):
        return "//h3[contains(.,'Search all the GIFs')]"
    
    def selectFirstGiphy(self):
        return "//html//li[1]/div[1]"
    
    def saveButtonGIF(self):
        return "//button[.='Save']"
    
    def cancelButtonGIF(self):
        return "//button[.='Cancel']"
    
    def GetLinkButton(self):
        try:
            wait=WebDriverWait(driver, 60)
            getlink=wait.until(EC.visibility_of_element_located((By.XPATH,"//button[@class='get-link-button btn btn-secondary btn-responsive']")))
            getlink.click()
        except Exception as e:
            traceback.print_exc()
            print (e)
            print "Failed to click on Get link button"
            raise Exception("Failed to click on Get link button")
    def getlinKUnpublishedDraft(self):
        wait=WebDriverWait(driver, 60)
        status=wait.until(EC.visibility_of_element_located((By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[3]/div[3]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/div[1]/span[1]")))
        return status.text
        
    def GetLinkCopyButton(self):
        try:
            wait=WebDriverWait(driver, 60)
            getlink=wait.until(EC.visibility_of_element_located((By.XPATH,"//button[@class='btn primary-cta-branding btn-cta']")))
            print "Copy button is displayed successfully"
            getlink.click()
            print "Clicked on Copy button"
        except Exception as e:
            traceback.print_exc()
            print (e)
            print "Failed to click on Get link button"
            raise Exception("Failed to click on Get link button")
        
    def linkDisplayed(self):
        return "//input[@class='u-text-truncate']"
    
    def GetLinkStatusButton(self):
        return "//div[@class='Select-value get-link-option']"
    
    def lessonBuilderOption(self):
        return "html/body/div[1]/div/div/div[3]/div[3]/div[1]/div[3]/div[2]/div/div[1]/div/div[1]/div[2]/div/div[2]"
    
    def everyoneToggle(self):
        try:
            wait=WebDriverWait(driver, 60)
            wait.until(EC.visibility_of_element_located((By.XPATH,"//h3[contains(.,'Everyone')]/../div/div[@class='slide-toggle is-on']")))
            toggle=wait.until(EC.element_to_be_clickable((By.XPATH,"//h3[contains(.,'Everyone')]/../div/div[@class='slide-toggle is-on']")))
            toggle.click()
            wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@class='Select-placeholder']")))
        except Exception as e:
            traceback.print_exc()
            print e
            raise Exception
    def BuiltByEnterpriseTab(self):
        
        try:
            wait=WebDriverWait(driver, 60)
            wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id='content']/div/div[3]/div[2]/div/ul/li[2]/a")))
            builtBY=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='content']/div/div[3]/div[2]/div/ul/li[2]/a")))
            bu=builtBY.text
            builtBY.click()
            return bu
        except Exception as e:
            traceback.print_exc()
            print e
            raise Exception("Failed to click on Built by enterprise tab")
    
        
    def SearchLessonTextField(self,lessonName):
         
        try:
            wait=WebDriverWait(driver, 60)
            search=wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='search-lessons-in-table']")))
            search.send_keys(lessonName)
        except Exception as e:
            traceback.print_exc()
            print e
            raise Exception("Failed to click on Built by enterprise tab")
        
    def lessonInGrid(self,lessonName):
        try:
            wait=WebDriverWait(driver, 60)
            wait.until(EC.visibility_of_element_located((By.XPATH,"(//tbody/tr/td[2]/a[.='"+lessonName+"'])[1]")))
        except Exception as e:
            traceback.print_exc()
            print e
            raise Exception("Failed to search lesson")
    def lessonInGridXpath(self,lessonName):
        return "//table/tbody/tr/td[2]/a[.='"+lessonName+"']"    
    
    def editLessonButton(self,lessonName):
        return "//table/tbody/tr/td[2]/a[.='"+lessonName+"']/../../td[4]/a"
    
    def publishedStatus(self,lessonName):
        return "//table/tbody/tr/td[2]/a[.='"+lessonName+"']/../../td[.='Published']"
    
    def noresultFound(self):
        try:
            wait=WebDriverWait(driver, 60)
            noresult=wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id='content']/div/div[3]/div[2]/div/div[.='Sorry, no results were found.']")))
            return noresult
        except Exception as e:
            traceback.print_exc()
            print e
            raise Exception("Failed to search lesson")
        
    def duplicateLesson(self,lessonName):
        try:
            wait=WebDriverWait(driver, 60)
            ele=wait.until(EC.visibility_of_element_located((By.XPATH,"//tr/td[2]/a[contains(.,'"+lessonName+"')]/../../td[4]/button[.='Duplicate']")))
            ele.click()
            print "Clicked on duplicate button of '"+lessonName+"'"
        except Exception as e:
            print e
            traceback.print_exc()
            raise Exception("failed to click on Duplicate button")
        
    def duplicateLessonPopup(self):
        return "//h3[contains(text(),'Duplicate lesson')]"
        
        
    def DuplicateLessonName(self):
        return "//input[@id='lesson-title-duplicate']"
        
    def duplicateLessonSaveButton(self):
        try:
            wait=WebDriverWait(driver, 60)
            save=wait.until(EC.visibility_of_element_located((By.XPATH,"//button[contains(text(),'Save')]")))
            save.click()
        except Exception as e:
            traceback.print_exc()
            print e
            raise Exception("failed to click on save button of Duplicate Lesson pop up")
        
    def lessonTitleInBuilder(self): 
        return "//textarea[@placeholder='Lesson Title']"   
        
    def nextCard(self): 
        try:
            wait=WebDriverWait(driver, 60)
            save=wait.until(EC.visibility_of_element_located((By.XPATH,"//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[1]/div/div/div/div[2]")))
            save.click()
        except Exception as e:
            traceback.print_exc()
            print e
            raise Exception("Failed to click on Next Card")

    def validationMessageForDuplicateTitle(self):
        return "//div[@class='lesson-validation-header']"

    def titleEditButton(self):
        return "//button[@class='u-float-right u-cursor-pointer u-text-link-blue']"
    
    def groupNameForPublish(self):
        return "//div[@class='Select-placeholder']"
    
    def SelectGroupFromPublishPopup(self,groupName):
        return "//div[@role='option']/span[contains(.,'"+groupName+"')]"

    def groupInGridDisplay(self,groupName):
        return "//div[@class='content-access-flex' and contains(.,'"+groupName+"')]"




        
        