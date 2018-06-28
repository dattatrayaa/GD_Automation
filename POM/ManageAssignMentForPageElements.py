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

class ManageAssignMentForPageElements:
    
    def HeaderTextManageAssign(self):
        return ".//*[@id='content']/div/div[3]/div[2]/div/header/div[1]/h1[contains(.,'Manage')]"
    
    def campaignButtonFromBreadcrumb(self):
        return ".//*[@id='content']/div/div[3]/div[2]/div/div[1]/a[1]"
    
    def cancelAssignMentClick(self):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//header/div[2]/button[contains(.,'Cancel')]")))
        driver.find_element_by_xpath("//header/div[2]/button").click()
        
    def cancelAssignmentButtonFromPopup(self):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[4]/div/div/div[2]/div[2]/button[2]")))
        driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div[2]/button[2]").click()
        wait.until(EC.invisibility_of_element_located((By.XPATH,"/html/body/div[4]/div/div/div[2]/div[2]/button[2]")))
        
    def getLink(self):
        wait=WebDriverWait(driver, 60)
        getlink=wait.until(EC.visibility_of_element_located((By.XPATH,"//button[@class='get-link-button btn btn-secondary btn-responsive u-mr8']//div")))
        getlink.click()  
        
        
    def getLinkCopyButtonCampaignDetailsPage(self):
        
        wait=WebDriverWait(driver, 60)
        copy=wait.until(EC.visibility_of_element_located((By.XPATH,"//button[@class='btn primary-cta-branding btn-cta']")))
        linkName=driver.find_element_by_xpath("//div[@class='get-link-popover-input-wrapper']//div//input[@type='text']").get_attribute("value")
        copy.click()
        return linkName
    
    
    
    
    
    
    
    
    
    
        
        