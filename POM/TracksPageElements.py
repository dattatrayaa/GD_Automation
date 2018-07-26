'''
Created on 24-Apr-2018

@author: dattatraya
'''
import time

from BaseTestClass import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from __main__ import traceback


class TracksPageElements:
    
    def lessonsButton(self):
        wait=WebDriverWait(driver, 60)
        but=wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@href='/create/lessons']")))
        but.click()
        
    def tracksButton(self):
        wait=WebDriverWait(driver, 60)
        but=wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@href='/create/tracks']")))
        but.click()
    def createTracksButton(self):
        wait=WebDriverWait(driver, 60)
        but=wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/header/div/a")))
        but.click()   
    def trackTitle(self):
        return ".//*[@id='title']"
    
    def imageDisplayed(self):
        return ".//*[@id='content']/div/div[3]/div[2]/div/div/div[2]/div[1]/div[2]/div/div/div/div/div[1]/img"
     
     
    def trackDescription(self):
        return ".//*[@id='description']"

    def addingTag(self):
        return "//div[@class='Select-placeholder']"
    
    
    def addLessonButton(self):
        wait=WebDriverWait(driver, 60)
        but=wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div/button")))
        but.click()
    def serchLesson(self):
        return "//input[@id='search-lessons-in-modal']"

    def searchedLessonAdd(self,lessonName):
        wait=WebDriverWait(driver, 60)
        searchedLesson=wait.until(EC.visibility_of_element_located((By.XPATH,"//li/div[2]/h4[.='"+lessonName+"']/../../div[1]/div")))
        searchedLesson.click()
        print "Lesson '"+lessonName+"' selected"
    
    
    def addingToTrack(self):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[4 or 2]/div/div/div[2]/div[3]/button[1]")))
        driver.find_element_by_xpath("/html/body/div[4 or 2]/div/div/div[2]/div[3]/button[1]").click()
        
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/div/div[2]/div[2]/div[1]/div/ul/li/div[2]/div/h4/div")))
    
    def publishButton(self):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/div/div[2]/div[2]/div[3]/button")))
        b=wait.until(EC.element_to_be_clickable((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/div/div[2]/div[2]/div[3]/button")))
        b.click()
        time.sleep(2)
    def successmessage(self,expectedSuccessText,titleOfTrack):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[2]/div/div/span")))
        actualSuccessText=driver.find_element_by_xpath(".//*[@id='content']/div/div[2]/div/div/span").text
        
        if actualSuccessText==expectedSuccessText:
            print "Success message '"+actualSuccessText+"' is displayed"
        else:
            print "failed to display expected success message"
            raise Exception
        
        
        print "\nVerifying Creates track '"+titleOfTrack+"' is displayed in Tracks grid"
    
    def sideMenuTracksExpanded(self):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[3]/div[1]/div/nav/div/div[2]/div[3]/div/ul/li[2]/a")))
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[1]/div/nav/div/div[2]/div[3]/div/ul/li[2]/a").click()
    
    
    
    def trackInGrid(self,titleOfTrack):
        return "(//table/tbody/tr/td[2]/a[.='"+titleOfTrack+"'])[1]"
    
    def objectiveDeleted(self):
        return "//h3[@class='objective-hero-subheading u-text-center']"
    
    def objectiveDeletedTitleOfTrack(self):
        return "//h2[@class='objective-hero-title u-text-center']"
    
    def GetLinkButton(self):
        return "/html[1]/body[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/button[1]"
    
    def GetLinkOption(self):
        return "//div[@class='Select-value get-link-option']"
    
    def GetLinkOptionValue(self):
        return "html/body/div[1]/div/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div[1]/div[2]/div/div[2]"
    
    
    def GetLinkCopyButton(self):
        wait=WebDriverWait(driver, 60)
        ele=wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[1]/div/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div[3]/button")))
        ele.click()
    
    def titleInTrackDetailPage(self):
        return "//h2[@class='objective-hero-title']"
    
    def lessonInTrackDetailPage(self,lessonName):
        return "//*[@id='content']/div/div[3]/div[2]/div/div[2]/div/div/div[2]/div/ul/li/a/div[2]/div[contains(.,'"+lessonName+"')]"
    
    def titleInEditTrackPage(self):
        return "//*[@id='content']/div/div[3]/div[2]/div/div/header/h1/em"
    
    def lessonInEditTrackPage(self,lessonName):
        return "//*[@id='content']/div/div[3]/div[2]/div/div/div[2]/div[2]/div[1]/div/ul/li/div[2]/div/h4/div[.='"+lessonName+"']"
    
    def duplicateButton(self,titleOfTrack):
        return "(//table/tbody/tr/td[2]/a[.='"+titleOfTrack+"']/../../td[4]/button[.='Duplicate'])[1]"
    
    def duplicateTrackPopupHeader(self):
        return "//h3[contains(text(),'Duplicate track')]"
    
    def duplicateTrackPopupTitle(self):
        return "//input[@id='objective-title-duplicate']"
    
    def duplicatePopupSaveButton(self):
        wait=WebDriverWait(driver, 60)
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,"//button[.='Save']")))
            driver.find_element_by_xpath("//button[.='Save']").click()
        except Exception as e:
            print e
            traceback.print_exc()
            raise Exception("Failed to click on Save button")
        
    def EditButton(self,titleOfTrack):
        return "//table/tbody/tr/td[2]/a[.='"+titleOfTrack+"']/../../td[4]/a[.='Edit']"
            
    def tagInEditTrackPage(self,tagName):
        return "//div[@class='Select-value']/span[contains(.,'"+tagName+"')]"
            
    def lessonInGrid(self):
        return "//li[1]/div[2]/div/h4/div"  
            
    def publishRevisionsButton(self):
        return "//button[@class='btn primary-cta-branding u-ml24 is-disabled is-disabled']"
    
    def removeLessonFromTrack(self):
        return "//button[@class='u-text-link-blue']"        
            
    def removeLessonPopup(self):
        return "/html[1]/body[1]/div[4 or 2]/div[1]/div[1]/div[2]/div[1]/button[1]"           
            
    def AddLessonButtonEmptyState(self):
        return "//button[@class='btn primary-cta-branding']"     
            
    
        