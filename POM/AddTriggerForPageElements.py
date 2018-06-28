'''
Created on 05-Apr-2018

@author: dattatraya
'''
import time

from BaseTestClass import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class AddTriggerPage:
    
    
    def HeaderTextAddTrigger(self):
        return ".//*[@id='content']/div/div[3]/div[2]/div/div[2]/header/h1"
    
    def newToGroupRadio(self):
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[2]/div/div[2]/section[1]/div/div[2]/label/span[2]").click()
    
    def SelectGroupTextBoxTriggerPage(self):
        return "//div[@class='Select-placeholder']"
    
    def AlsoAssignToCurrentUserCheckbox(self):
        return ".//*[@id='content']/div/div[3]/div[2]/div/div[2]/section[1]/div/div[3]/div[2]/div/label/span[2]"
    
    def YourCriteriaMatchesBox(self):
        return ".//*[@id='content']/div/div[3]/div[2]/div/div[2]/section[1]/div/div[3]/div[2]/div[2]"
    
    def YourCriteriaMatchesBoxLearnersButton(self):
        return ".//*[@id='content']/div/div[3]/div[2]/div/div[2]/section[1]/div/div[3]/div[2]/div[2]/button"
    
    def NewTriggerHire(self):
        return "//input[@id='trigger-new-hire']"
    
    
    def saveTriggerButton(self):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/div[2]/section[2]/div[2]/button")))
        newToGrp=wait.until(EC.element_to_be_clickable((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/div[2]/section[2]/div[2]/button")))
        newToGrp.click()
    
    def deleteTriggerButtonEditTriggerPage(self):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/div[2]/header/div/button[1]")))
        deleteTrigger=wait.until(EC.element_to_be_clickable((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/div[2]/header/div/button[1]")))
        deleteTrigger.click()
    def deleteTriggerFromPopup(self):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[4]/div/div/div[2]/div[2]/button[1]")))
        deleteTrigger=wait.until(EC.element_to_be_clickable((By.XPATH,"html/body/div[4]/div/div/div[2]/div[2]/button[1]")))
        deleteTrigger.click()
        
        
        
        
        
        
    