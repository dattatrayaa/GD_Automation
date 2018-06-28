'''
Created on 07-May-2018

@author: Sheethu C
'''

import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xlrd

from  G1BaseTestClass import driver


class TrainingXpath():
    
    def learn(self):
        return "html/body/div[2]/div[2]/div[1]/div[2]/div/a[1]"
    def manage(self):
        return "html/body/div[2]/div[2]/div[1]/div[2]/div/a[3]"
    
    def training(self):
        return "html/body/div[2]/div[3]/ul/li[3]/a"
    def createTraining(self):
        return "html/body/div[1]/div[7]/div/div[2]/div[1]/div/a[2]"
    def createNew(self):
        return "html/body/div[2]/div[7]/div/div[1]/div[1]/div/div/div[2]/div[1]/div[1]/div/a/span"
    def ChapterHead(self):
        return "html/body/div[2]/div[7]/div/div[1]/div[1]/div/div[2]/div[3]/div[1]/div/div/div[2]/div/textarea"
    def doneButton(self):
        return "html/body/div[8]/div[3]/div/a[.='Done']"
    def chapterHead(self):
        return "html/body/div[2]/div[7]/div/div[1]/div[1]/div/div[2]/div[3]/div[1]/div/div/div[1]/div/textarea"
    def descriptionChapter(self):
        return "html/body/div[2]/div[7]/div/div[1]/div[1]/div/div[2]/div[3]/div[1]/div/div/div[2]/div/textarea"
    def addMaterials(self):
        return "html/body/div[2]/div[7]/div/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/a[1]"
    def document(self):
        return "html/body/div[2]/div[7]/div/div[2]/ul/li[3]/a/span[2]"
    def documentHeader(self):
        return "html/body/div[10]/div/div[1]/h3"
    def myLibrary(self):
        return "html/body/div[10]/div/div[2]/div[1]/ul/li[2]/a"
    def inbuiltDocument(self):
        return "html/body/div[9]/div/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/input"
    def expectedDocumentName(self):
        return "html/body/div[10]/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div/label"
    def addButton(self):
        return "html/body/div[10]/div/div[3]/div/a[.='Add']"
    def videoAddButton(self):
        return "html/body/div[10]/div[3]/div/a[.='Add']"
    
    def createvideoAddButton(self):
        return "html/body/div[10]/div/div[3]/div/a['Add']"
    
    def expectedDocName(self):
        return "html/body/div[2]/div[7]/div/div[1]/div[1]/div/div[3]/div[1]/ul/li/div[2]/div/div[1]"
    def headerTraining(self):
        return "html/body/div[2]/div[7]/div/div[1]/div[1]/div/div[3]/div[1]/ul/li/div[2]/div/div[1]/span[2]"
    
    def textareaname(self):
        return "//input[@id='qa-input-name-your-training']"
    
    def trainingCreation(self,Name,descr):
        tpath =TrainingXpath()
        wait =WebDriverWait(driver,60)
        driver.find_element_by_xpath(tpath.manage()).click()
        print "clicked on training"
        wait.until(EC.visibility_of_element_located((By.XPATH,tpath.training())))
        ele =driver.find_element_by_xpath(tpath.training())
        webdriver.ActionChains(driver).move_to_element(ele).click().perform()
        print "clicking on training"
        time.sleep(4)
        wait.until(EC.visibility_of_element_located((By.XPATH,tpath.createTraining())))
        driver.find_element_by_xpath(tpath.createTraining()).click()   
        print "Clicking on Create training icon"
        time.sleep(4)
        wait.until(EC.visibility_of_element_located((By.XPATH,tpath.createNew())))
        driver.find_element_by_xpath(tpath.createNew()).click()  
        print "Clicking on create New"
        time.sleep(4)
        wait.until(EC.visibility_of_element_located((By.XPATH,tpath.textareaname())))
        elem=driver.find_element_by_xpath(tpath.textareaname())
        elem.send_keys(Keys.END)
        driver.find_element_by_xpath(tpath.textareaname()).clear()
        print "Clearing the name of the tarining"
        
        time.sleep(4)
        driver.find_element_by_xpath(tpath.textareaname()).send_keys(Name) 
        time.sleep(4)
        print "Entering name of the training"
        wait.until(EC.visibility_of_element_located((By.XPATH,tpath.doneButton())))
        wait.until(EC.element_to_be_clickable((By.XPATH,tpath.doneButton())))
        driver.find_element_by_xpath(tpath.doneButton()).click()
        time.sleep(4)
        print "Clicking on Done Button"
        wait.until(EC.visibility_of_element_located((By.XPATH,tpath.chapterHead())))
        wait.until(EC.visibility_of_element_located((By.XPATH,tpath.descriptionChapter())))
        driver.find_element_by_xpath(tpath.descriptionChapter()).send_keys(descr) 
        time.sleep(4)
        wait.until(EC.visibility_of_element_located((By.XPATH,tpath.addMaterials())))
        #wait.until(EC.element_to_be_clickable((By.XPATH,txpath.addMaterials())))
        
        time.sleep(4)
    def createGrovoVideo(self):
        tpath =TrainingXpath()
        wait=WebDriverWait(driver,80)
        wait.until(EC.visibility_of_element_located((By.XPATH,tpath.addMaterials())))
        time.sleep(4)
        ele =driver.find_element_by_xpath(tpath.addMaterials())
        webdriver.ActionChains(driver).move_to_element(ele).click(ele).perform()
        time.sleep(4)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[7]/div/div[2]/ul/li[1]/a/span[2]")))
        ele=driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div[2]/ul/li[1]/a/span[2]")
        print "Waiting for the GrovoVideoLesson to display"
        webdriver.ActionChains(driver).move_to_element(ele).click(ele).perform()
        time.sleep(4)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[10]/div[1]/h3")))
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[10]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div/div/p/span[1]")))
        driver.find_element_by_xpath("html/body/div[10]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div/div/p/span[1]").click()
        time.sleep(4)
        driver.find_element_by_xpath("html/body/div[10]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div/input").click()
        time.sleep(4)
        if (driver.find_element_by_xpath("html/body/div[10]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/input").is_selected()):
            print "Video selected "
        else:
            raise Exception
        if (driver.find_element_by_xpath("html/body/div[10]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div[2]/div/input").is_selected()):
            print "Video selected "
        else:
            raise Exception
        wait.until(EC.visibility_of_element_located((By.XPATH,tpath.videoAddButton())))
        ele =driver.find_element_by_xpath(tpath.videoAddButton())
        webdriver.ActionChains(driver).move_to_element(ele).click(ele).perform()
        time.sleep(4)
        wait.until(EC.visibility_of_element_located((By.XPATH,tpath.chapterHead())))
        print "Grovo video Added"
    def createVideo(self,videoPath,timeToUploadVideo):
        tpath =TrainingXpath()
        wait=WebDriverWait(driver, timeToUploadVideo)
        WebDriverWait(driver,60).until(EC.visibility_of_element_located((By.XPATH,tpath.addMaterials())))
        time.sleep(4)
        ele =driver.find_element_by_xpath(tpath.addMaterials())
        webdriver.ActionChains(driver).move_to_element(ele).click(ele).perform()
        WebDriverWait(driver,60).until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[7]/div/div[2]/ul/li[2]/a/span[2]")))
        ele =driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div[2]/ul/li[2]/a/span[2]")
        webdriver.ActionChains(driver).move_to_element(ele).click(ele).perform()
        time.sleep(4) 
        WebDriverWait(driver,60).until(EC.visibility_of_element_located((By.XPATH,"html/body/div[10]/div/div[1]/h3")))  
        time.sleep(6) 
        if (driver.find_element_by_xpath("html/body/div[10]/div/div[2]/div[2]/div[1]/div[1]/h4").is_displayed()):
            print "displayed"
        else:
            driver.find_element_by_xpath("html/body/div[10]/div/div[2]/div[1]/ul/li[1]/a").click()
        time.sleep(4)
        #iframe = driver.find_element_by_id("intercom-frame")
        
        ifram =driver.find_element_by_xpath("html/body/div[10]/div/div[2]/div[2]/div[1]/div[1]/div/iframe")
        driver.switch_to.frame(ifram)
        time.sleep(4)
        print "iframe"
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/form/div/input[@class='lesson_upload ia-lesson-upload-file-input']"))) 
        #ele =driver.find_element_by_xpath("html/body/form/div/input[@class='lesson_upload ia-lesson-upload-file-input']").click() 
        #ele.send_keys(videoPath)
        driver.find_element_by_css_selector('input[type="file"]').send_keys(videoPath)
        time.sleep(timeToUploadVideo)
        driver.switch_to_default_content()
        WebDriverWait(driver,30).until(EC.visibility_of_element_located((By.XPATH,tpath.createvideoAddButton())))
        ele =driver.find_element_by_xpath(tpath.createvideoAddButton())
        webdriver.ActionChains(driver).move_to_element(ele).click(ele).perform()
        time.sleep(4)
        wait.until(EC.visibility_of_element_located((By.XPATH,tpath.chapterHead())))
        print "Video Uploaded Successfully"
    
    def scormUpload(self,ScormOrImageFilePath):
        tpath =TrainingXpath()
        wait=WebDriverWait(driver,60)
        wait.until(EC.visibility_of_element_located((By.XPATH,tpath.addMaterials())))
        time.sleep(4)
        ele =driver.find_element_by_xpath(tpath.addMaterials())
        webdriver.ActionChains(driver).move_to_element(ele).click(ele).perform()
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[7]/div/div[2]/ul/li[6]/a/span[1]")))
                                                                
        ele=driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div[2]/ul/li[6]/a/span[1]")
        print "Waiting for the scorm to display"
        webdriver.ActionChains(driver).move_to_element(ele).click(ele).perform()
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[10]/div/div[1]/h3")))
        print "Going to upload the SCORM"
        ifram =driver.find_element_by_xpath("html/body/div[10]/div/div[2]/div[2]/div[1]/div[1]/div/iframe")
        driver.switch_to.frame(ifram)
        time.sleep(6)                                                              
        driver.find_element_by_css_selector('input[type="file"]').send_keys(ScormOrImageFilePath)
        time.sleep(8)
        driver.switch_to_default_content()
        #WebDriverWait(driver, 600).until(EC.visibility_of_element_located((By.XPATH,"html/body/div[10]/div/div[2]/div[2]/div[1]/div[5]/div/div/label"))) 
        WebDriverWait(driver,80).until(EC.visibility_of_element_located((By.XPATH,tpath.addButton())))
        ele =driver.find_element_by_xpath(tpath.addButton())
        webdriver.ActionChains(driver).move_to_element(ele).click(ele).perform()
        wait.until(EC.visibility_of_element_located((By.XPATH,tpath.chapterHead())))  
    def presentationPPT(self,PPTFilePath):
        tpath =TrainingXpath()
        wait=WebDriverWait(driver,60)
        wait.until(EC.visibility_of_element_located((By.XPATH,tpath.addMaterials())))
        time.sleep(4)
        ele =driver.find_element_by_xpath(tpath.addMaterials())
        webdriver.ActionChains(driver).move_to_element(ele).click(ele).perform()
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[7]/div/div[2]/ul/li[4]/a/span[2]")))
        ele=driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div[2]/ul/li[4]/a/span[2]")
        print "Waiting for the scorm to display"
        webdriver.ActionChains(driver).move_to_element(ele).click(ele).perform()
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[10]/div/div[1]/h3")))
        print "Going to upload the POWER POINT file"
        ifram =driver.find_element_by_xpath("html/body/div[10]/div/div[2]/div[2]/div[1]/div[1]/div/iframe")
        driver.switch_to.frame(ifram)
        time.sleep(6)
        driver.find_element_by_css_selector('input[type="file"]').send_keys(PPTFilePath)
        #WebDriverWait(driver, 600).until(EC.visibility_of_element_located((By.XPATH,"html/body/div[10]/div/div[2]/div[2]/div[1]/div[5]/div/div/label"))) 
        time.sleep(200)
        driver.switch_to_default_content()
        WebDriverWait(driver,60).until(EC.visibility_of_element_located((By.XPATH,tpath.createvideoAddButton())))
        ele =driver.find_element_by_xpath(tpath.createvideoAddButton())
        webdriver.ActionChains(driver).move_to_element(ele).click(ele).perform()
        wait.until(EC.visibility_of_element_located((By.XPATH,tpath.chapterHead())))  
    def documentUpload(self,documentPath):
        txpath =TrainingXpath()
        wait=WebDriverWait(driver,60)
        wait.until(EC.visibility_of_element_located((By.XPATH,txpath.addMaterials())))
        elem =driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/a[1]")
        webdriver.ActionChains(driver).move_to_element(elem).click(elem).perform()
        time.sleep(4)
        print "Clicking on add materials"
        wait.until(EC.element_to_be_clickable((By.XPATH,"html/body/div[2]/div[7]/div/div[2]/ul/li[3]/a/span[1]")))
        ele=driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div[2]/ul/li[3]/a/span[1]")
        webdriver.ActionChains(driver).move_to_element(ele).click(ele).perform()
        
        wait.until(EC.element_to_be_clickable((By.XPATH,txpath.documentHeader())))
        ifram =driver.find_element_by_xpath("html/body/div[10]/div/div[2]/div[2]/div[1]/div[1]/div/iframe")
        driver.switch_to.frame(ifram)
        time.sleep(4)
        print "iframe"
        time.sleep(4)
        driver.find_element_by_css_selector('input[type="file"]').send_keys(documentPath)
        time.sleep(15)
        driver.switch_to_default_content()
        DocName = driver.find_element_by_xpath(txpath.expectedDocumentName())
        ActualDocName =DocName.text
        print "ActualDocName "+ActualDocName
        wait.until(EC.visibility_of_element_located((By.XPATH,txpath.addButton())))
        wait.until(EC.element_to_be_clickable((By.XPATH,txpath.addButton())))
        ele =driver.find_element_by_xpath(txpath.addButton())
        webdriver.ActionChains(driver).move_to_element(ele).click(ele).perform()
        print "Clicked on add button"
        time.sleep(10)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[7]/div/div[1]/div[1]/div/div[2]/div[3]/div[2]/div/a[1]"))) 
    def saveWithoutDueDateStandrad(self):
        wait =WebDriverWait(driver,60)
        time.sleep(4)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[7]/div/div[1]/div[2]/div[1]/a")))
        driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div[1]/div[2]/div[1]/a").click()
        time.sleep(80)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[7]/div/div[1]/div[1]/div/div/div/div[2]/div[1]/div/div[2]/form/div/ul/li[1]/label/input")))
        if (driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div[1]/div[1]/div/div/div/div[2]/div[1]/div/div[2]/form/div/ul/li[1]/label/input").is_selected):
            print "Standrad Is selected"
        else:
            driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div[1]/div[1]/div/div/div/div[2]/div[1]/div/div[2]/form/div/ul/li[1]/label/input").click()
        
        if(driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div[1]/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/ul/li[1]/div[1]/div[2]/div/label/input").is_selected):
            print "No due date is selected"
         
        else:
            driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div[1]/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/ul/li[1]/div[1]/div[2]/div/label/input").click()
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[7]/div/div[1]/div[2]/div[1]/a")))
        driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div[1]/div[2]/div[1]/a").click()
        time.sleep(4)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[7]/div/div/div[1]/div/div/div/div[4]/div[1]/div/div[1]/div[1]/div/label/input")))
        driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div/div[1]/div/div/div/div[4]/div[1]/div/div[1]/div[1]/div/label/input").click()
        time.sleep(4)
        print "Clicked on select ALl"
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[7]/div/div/div[2]/div[1]/a")))
        driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div/div[2]/div[1]/a").click()
        time.sleep(4)
    def createUserWithAllGroups(self,Email,password,RePassword):
        txpath =TrainingXpath()
        wait =WebDriverWait(driver,80)
        wait.until(EC.visibility_of_element_located((By.XPATH,txpath.learn())))
        wait.until(EC.visibility_of_element_located((By.XPATH,txpath.manage())))
        driver.find_element_by_xpath(txpath.manage()).click()
        print "Clicked on Manage"
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[3]/ul/li[2]/a")))
        ele =driver.find_element_by_xpath("html/body/div[2]/div[3]/ul/li[2]/a")
        webdriver.ActionChains(driver).move_to_element(ele).click().perform()         
        print "clicked on people"
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[7]/div/div[2]/div[1]/div[2]/a[1]")))
        driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div[2]/div[1]/div[2]/a[1]").click()
        time.sleep(4)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[7]/div/div/div[1]/div[1]/div[1]/h1")))
        print "Waiting for the Page todisplay"
        ele =driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div/div[1]/div[1]/div[3]/div/div/form/div[4]/textarea")
        ele.send_keys(Email)
        time.sleep(4)
        print "Entering Email"
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[7]/div/div/div[1]/div[2]/div[1]/a")))
        driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div/div[1]/div[2]/div[1]/a").click()
        print "clicking on the next button"
        time.sleep(4)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[7]/div/div/div/div[1]/div[1]/h1")))
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[7]/div/div/div/div[1]/div[6]/div/ul/li[2]/label")))
        driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div/div/div[1]/div[6]/div/ul/li[2]/label").click()
        wait.until(EC.visibility_of_element_located((By.ID,"input-set-password")))
        ele =driver.find_element_by_id("input-set-password")
        webdriver.ActionChains(driver).move_to_element(ele).perform()
        ele.send_keys(password)
        time.sleep(6)
        print "Entering Password"
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[7]/div/div/div/div[1]/div[6]/div/ul/li[2]/div/form/div[1]/div[2]/input[@id='input-set-password-confirm']")))
        elem = driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div/div/div[1]/div[6]/div/ul/li[2]/div/form/div[1]/div[2]/input[@id='input-set-password-confirm']")
        webdriver.ActionChains(driver).move_to_element(elem).perform()
        elem.send_keys(RePassword)
        time.sleep(4)
        print "Entering Recurrent Password"
        ele =driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div/div/div[2]/div[1]/a")
        webdriver.ActionChains(driver).move_to_element(ele).click(ele).perform()
        time.sleep(4)
        print "Clicking on Add people"
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[7]/div/div[2]/div[1]/div[2]/a[1]")))
        print "Adding Power"
        wait.until(EC.visibility_of_element_located((By.XPATH,txpath.manage())))
        driver.find_element_by_xpath(txpath.manage()).click()
        print "Clicked on Manage"
        ele =driver.find_element_by_xpath("html/body/div[2]/div[3]/ul/li[2]/a")
        webdriver.ActionChains(driver).move_to_element(ele).click(ele).perform()
        time.sleep(4)
        print "Clicking on People in the dropdown list"
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[7]/div/div[1]/ul/li[2]/a/span")))
        driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div[1]/ul/li[2]/a/span").click()
        time.sleep(4)
        print "Clicking on people side menu"
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[7]/div/div[1]/ul/li[2]/ul/li[2]/a")))
        driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div[1]/ul/li[2]/ul/li[2]/a").click()
        time.sleep(4)
        print "Clicking on Power side menu"
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[7]/div/div[2]/div[2]/div[1]/div[3]/a")))
        driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div[2]/div[2]/div[1]/div[3]/a").click()
        time.sleep(4)
        print "Clicking on Add admin button"
        wait.until(EC.visibility_of_element_located((By.ID,"qa-input-powers-select-user-search")))
        ele=driver.find_element_by_id("qa-input-powers-select-user-search")
        webdriver.ActionChains(driver).move_to_element(ele).click(ele).perform()
        ele.send_keys(Email)
        ele.send_keys(Keys.ENTER)
        print "Entering email in the search box"
        time.sleep(4)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//label/p[contains(.,'"+Email+"')]")))
        ele =driver.find_element_by_xpath("//label/p[contains(.,'"+Email+"')]")
        webdriver.ActionChains(driver).move_to_element(ele).click(ele).perform()
        
        print "selecting created user"
        time.sleep(4)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[9]/div[3]/div/a[1]")))
        ele =driver.find_element_by_xpath("html/body/div[9]/div[3]/div/a[1]")
        webdriver.ActionChains(driver).move_to_element(ele).click(ele).perform()
        time.sleep(4)
        print "clicking on add button"
        wait.until(EC.visibility_of_element_located((By.ID,"input-platform-search")))
        driver.find_element_by_id("input-platform-search").send_keys(Email)
        driver.find_element_by_id("input-platform-search").send_keys(Keys.ENTER)
        time.sleep(4)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[7]/div/div[2]/div[6]/div[3]/div/div[1]/div[1]/small[.='"+Email+"']")))
        print "Waiting for the created user to display"
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[7]/div/div[2]/div[6]/div[3]/div/div[1]/div[1]/small[.='"+Email+"']/../../div[2]/div[1]/div[1]/p/a")))
        driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div[2]/div[6]/div[3]/div/div[1]/div[1]/small[.='"+Email+"']/../../div[2]/div[1]/div[1]/p/a").click()
        time.sleep(4)
        print "Clicking on the edit"
        wait.until(EC.visibility_of_element_located((By.XPATH,"//label/input")))
        ele =driver.find_element_by_xpath("//label/input")
        webdriver.ActionChains(driver).move_to_element(ele).click(ele).perform()
        time.sleep(4)
        print "Clicking on the select all"
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[9]/div[3]/div/a[1]")))
        ele =driver.find_element_by_xpath("html/body/div[9]/div[3]/div/a[1]")
        webdriver.ActionChains(driver).move_to_element(ele).click(ele).perform()
        time.sleep(4)
        print "Clicking on the Save button"
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[7]/div/div[2]/div[6]/div[3]/div/div[1]/div[2]/div[2]/div[3]/div[1]/a")))
        driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div[2]/div[6]/div[3]/div/div[1]/div[2]/div[2]/div[3]/div[1]/a").click()
        time.sleep(4)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[7]/div/div[2]/div[6]/div[3]/div/div[1]/div[2]/div[2]/div[3]/div[1]/div[2]/ul/li[2]/a")))
        driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div[2]/div[6]/div[3]/div/div[1]/div[2]/div[2]/div[3]/div[1]/div[2]/ul/li[2]/a").click()
        time.sleep(4)
        print "Selecting Notifying No"
    def createGroup(self,GroupName):
        txpath =TrainingXpath()
        wait =WebDriverWait(driver,80)
        wait.until(EC.visibility_of_element_located((By.XPATH,txpath.learn())))
        wait.until(EC.visibility_of_element_located((By.XPATH,txpath.manage())))
        driver.find_element_by_xpath(txpath.manage()).click()
        print "Clicked on Manage"
        ele =driver.find_element_by_xpath("html/body/div[2]/div[3]/ul/li[6]/a")
        webdriver.ActionChains(driver).move_to_element(ele).click(ele).perform()
        time.sleep(4)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[7]/div[1]/div[2]/div[3]/div/ul/li[4]/a")))
        driver.find_element_by_xpath("html/body/div[2]/div[7]/div[1]/div[2]/div[3]/div/ul/li[4]/a").click()
        time.sleep(4)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[7]/div/div[2]/div[4]/div[1]/div[1]/div[1]/a")))
        driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div[2]/div[4]/div[1]/div[1]/div[1]/a").click()
        time.sleep(4)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[7]/div/div[2]/div[4]/div[1]/div[1]/div[2]/form/table/tbody/tr/td[1]/div/div/input")))
        driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div[2]/div[4]/div[1]/div[1]/div[2]/form/table/tbody/tr/td[1]/div/div/input").send_keys(GroupName)
        time.sleep(4)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[7]/div/div[2]/div[4]/div[1]/div[1]/div[2]/form/table/tbody/tr/td[2]/a")))
        driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div[2]/div[4]/div[1]/div[1]/div[2]/form/table/tbody/tr/td[2]/a").click()
        time.sleep(4)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//ul/li/span[.='"+GroupName+"']")))
        if (driver.find_element_by_xpath("//ul/li/span[.='"+GroupName+"']").is_displayed()):
            print "Created group is displaying"
        else:
            raise Exception
        ele =driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div[2]/div[4]/div[2]/a")
        webdriver.ActionChains(driver).click(ele).perform()
        time.sleep()
    def createUserwithCreatedGroup(self,GroupName,CreateGroupEmail,CreateGroupUserpassword,CreateGroupUserRePassword):
        txpath =TrainingXpath()
        wait =WebDriverWait(driver,80)
        wait.until(EC.visibility_of_element_located((By.XPATH,txpath.learn())))
        wait.until(EC.visibility_of_element_located((By.XPATH,txpath.manage())))
        driver.find_element_by_xpath(txpath.manage()).click()
        print "Clicked on Manage"
        ele =driver.find_element_by_xpath("html/body/div[2]/div[3]/ul/li[2]/a")
        webdriver.ActionChains(driver).move_to_element(ele).click(ele).perform()
        print "Clicking on people"
        driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div[2]/div[1]/div[2]/a[1]").click()
        print "Clicking on Add people"
        time.sleep(4)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[7]/div/div/div[1]/div[1]/div[3]/div/div/form/div[2]/a")))
        driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div/div[1]/div[1]/div[3]/div/div/form/div[2]/a").click()
        time.sleep(4)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[7]/div/div/div[1]/div[1]/div[3]/div/div/form/div[1]/div[1]/a")))
        ele =driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div/div[1]/div[1]/div[3]/div/div/form/div[1]/div[1]/a")
        webdriver.ActionChains(driver).move_to_element(ele).click(ele).perform()
        time.sleep(4)
        ele =driver.find_element_by_xpath("//ul/li/a[.='"+GroupName+"']")
        webdriver.ActionChains(driver).move_to_element(ele).click(ele).perform()
        time.sleep(4)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//form/div/p[.='"+GroupName+"']")))
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[7]/div/div/div[1]/div[1]/div[3]/div/div/form/div[4]/textarea")))
        ele =driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div/div[1]/div[1]/div[3]/div/div/form/div[4]/textarea")
        webdriver.ActionChains(driver).move_to_element(ele).send_keys(CreateGroupEmail).perform()
        time.sleep(4)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[7]/div/div/div[1]/div[2]/div[1]/a")))
        driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div/div[1]/div[2]/div[1]/a").click()
        time.sleep(4)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[7]/div/div/div/div[1]/div[1]/h1")))
        print "Waiting for the page to display"
        ele =driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div/div/div[1]/div[6]/div/ul/li[2]/div/form/div[1]/div[1]/input")
        webdriver.ActionChains(driver).move_to_element(ele).send_keys(Keys.END).perform()
        ele.clear()
        ele.send_keys(CreateGroupUserpassword)
        print "Entering Password"
        time.sleep(4)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[7]/div/div/div/div[1]/div[6]/div/ul/li[2]/div/form/div[1]/div[2]/input")))
        ele = driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div/div/div[1]/div[6]/div/ul/li[2]/div/form/div[1]/div[2]/input")
        webdriver.ActionChains(driver).move_to_element(ele).send_keys(CreateGroupUserRePassword).perform()
        time.sleep(4)
        print "Entering Recurrent Password"
        ele =driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div/div/div[2]/div[1]/a")
        webdriver.ActionChains(driver).move_to_element(ele).click(ele).perform()
        time.sleep(4)
        wait.unti(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[7]/div/div[2]/div[1]/div[1]/h1")))
        ele =driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div[2]/div[3]/div[1]/div[2]/a")
        webdriver.ActionChains(driver).move_to_element(ele).click(ele).perform()
        time.sleep(4)
        wait.unti(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[7]/div/div[2]/div[9]/ul/li[1]/a")))
        ele =driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div[2]/div[9]/ul/li[1]/a")
        webdriver.ActionChains(driver).move_to_element(ele).click(ele).perform()
        time.sleep(4)
        wait.unti(EC.visibility_of_element_located((By.XPATH,"//ul/li/a[.='"+GroupName+"']")))
        ele =driver.find_element_by_xpath("//ul/li/a[.='"+GroupName+"']")
        webdriver.ActionChains(driver).move_to_element(ele).click(ele).perform()
        time.sleep(4)
        if (driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div[2]/div[7]/div[4]/div[1]/div[1]/div[1]/p/a[.='"+CreateGroupEmail+"']").is_displayed()):
            print "Created User is dispalyed"
        else:
            raise Exception
    def saveWithoutDueDateDefault(self):
        wait =WebDriverWait(driver,60)
        time.sleep(4)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[7]/div/div[1]/div[2]/div[1]/a")))
        driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div[1]/div[2]/div[1]/a").click()
        time.sleep(80)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[7]/div/div[1]/div[1]/div/div/div/div[2]/div[1]/div/div[2]/form/div/ul/li[1]/label/input")))
        print "Waiting for the Options page to display"
        ele =driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div[1]/div[1]/div/div/div/div[2]/div[1]/div/div[2]/form/div/ul/li[2]/label/input[@id='qa-training-type-default']")
        webdriver.ActionChains(driver).move_to_element(ele).click(ele).perform()
        time.sleep(4)
        print "Default is clicked"
        if(driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div[1]/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/ul/li[1]/div[1]/div[2]/div/label/input").is_selected):
            print "No due date is selected"
        else:
            driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div[1]/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/ul/li[1]/div[1]/div[2]/div/label/input").click()
            print "No due date is selected"
        time.sleep(4)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[7]/div/div[1]/div[2]/div[1]/a")))
        driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div[1]/div[2]/div[1]/a").click()
        time.sleep(4)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[7]/div/div/div[1]/div/div/div/div[4]/div[1]/div/div[1]/div[1]/div/label/input")))
        driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div/div[1]/div/div/div/div[4]/div[1]/div/div[1]/div[1]/div/label/input").click()
        time.sleep(4)
        print "Clicked on select ALl"
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[7]/div/div/div[2]/div[1]/a")))
        driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div/div[2]/div[1]/a").click()
        time.sleep(4)
    def saveWithDueDateStandrad(self,dateToSelect):
        wait =WebDriverWait(driver,60)
        time.sleep(4)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[7]/div/div[1]/div[2]/div[1]/a")))
        driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div[1]/div[2]/div[1]/a").click()
        time.sleep(80)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[7]/div/div[1]/div[1]/div/div/div/div[2]/div[1]/div/div[2]/form/div/ul/li[1]/label/input")))
        print "Waiting for the page to be displayed"
        if (driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div[1]/div[1]/div/div/div/div[2]/div[1]/div/div[2]/form/div/ul/li[1]/label/input").is_selected):
            print "Standrad Is selected"
        else:
            driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div[1]/div[1]/div/div/div/div[2]/div[1]/div/div[2]/form/div/ul/li[1]/label/input").click()
            print "Clicked on Standrad"
        
        driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div[1]/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/ul/li[1]/div[1]/div[2]/div/label/input").click()
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[7]/div/div[1]/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/ul/li[1]/div[1]/div[1]/a/span")))
        driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div[1]/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/ul/li[1]/div[1]/div[1]/a/span").click()
        time.sleep(4)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[7]/div/div[2]/table/tbody")))
        time.sleep(4)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//table/tbody/tr/td/span[.='"+str(dateToSelect)+"']")))
        driver.find_element_by_xpath("//table/tbody/tr/td/span[.='"+str(dateToSelect)+"']").click()
        time.sleep(6)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[7]/div/div[1]/div[2]/div[1]/a")))
        driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div[1]/div[2]/div[1]/a").click()
        time.sleep(4)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[7]/div/div/div[1]/div/div/div/div[4]/div[1]/div/div[1]/div[1]/div/label/input")))
        driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div/div[1]/div/div/div/div[4]/div[1]/div/div[1]/div[1]/div/label/input").click()
        time.sleep(4)
        print "Clicked on select ALl"
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[7]/div/div/div[2]/div[1]/a")))
        driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div/div[2]/div[1]/a").click()
        time.sleep(4)
    
    def saveWithDueDateDefault(self,dateToSelect):
        wait =WebDriverWait(driver,60)
        time.sleep(4)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[7]/div/div[1]/div[2]/div[1]/a")))
        driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div[1]/div[2]/div[1]/a").click()
        time.sleep(80)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[7]/div/div[1]/div[1]/div/div/div/div[2]/div[1]/div/div[2]/form/div/ul/li[1]/label/input")))
        print "Waiting for the Options page to display"
        ele =driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div[1]/div[1]/div/div/div/div[2]/div[1]/div/div[2]/form/div/ul/li[2]/label/input[@id='qa-training-type-default']")
        webdriver.ActionChains(driver).move_to_element(ele).click(ele).perform()
        time.sleep(6)
        
        driver.find_element_by_xpath('//*[@id="qa-no-auto-due-date"]')
        webdriver.ActionChains(driver).move_to_element(ele).click(ele).perform()
        print "No due date is selected"
        
        time.sleep(4)
        wait.until(EC.visibility_of_element_located((By.ID,"qa-input-due-dates-out")))
        time.sleep(4)
        ele =driver.find_element_by_id("qa-input-due-dates-out")
        webdriver.ActionChains(driver).move_to_element(ele).send_keys(dateToSelect).perform()
        time.sleep(6)
        wait.until(EC.visibility_of_element_located(By.XPATH,"html/body/div[2]/div[7]/div/div[1]/div[2]/div[1]/a"))
        driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div[1]/div[2]/div[1]/a").click()
        time.sleep(4)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[7]/div/div/div[1]/div/div/div/div[4]/div[1]/div/div[1]/div[1]/div/label/input")))
        driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div/div[1]/div/div/div/div[4]/div[1]/div/div[1]/div[1]/div/label/input").click()
        time.sleep(4)
        print "Clicked on select ALl"
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div[7]/div/div/div[2]/div[1]/a")))
        driver.find_element_by_xpath("html/body/div[2]/div[7]/div/div/div[2]/div[1]/a").click()
        time.sleep(4)
        
        
        
        