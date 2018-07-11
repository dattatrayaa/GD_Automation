'''
Created on 07-Mar-2018

@author: dattatraya
'''

import os

from BaseTestClass import BaseTestClass
from BaseTestClass import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xlrd
from BaseTestClass import projectPath
class CreateCampaignsPageDisplay:
    
    def createCampaignsPage(self,actualHeaderText):
        
        print "\n----Create Campaigns page display----\n"
        
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@href='/plan/campaigns'][1]")))
        
        print "Clicking on Campaigns button from side menu"
        driver.find_element_by_xpath("//a[@href='/plan/campaigns'][1]").click()
        createCampaignButton=wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@href='/plan/campaigns/new/edit']")))
        createCampaignButton.click()
        print "Clicked on Create Campaign button"
        
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/header/div/h1")))
        
        print "\nVerifying Create Campaign page is displayed"
        
        headerText=driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[2]/div/header/div/h1").text
        
        
        
        if headerText==actualHeaderText:
            print "Create Campaign page is dispalyed with Header Text '"+headerText+"'"
        else:
            print "Create Campaign page is not displayed"
            raise Exception
        
        
        print "\nChecking breadcrumb is displayed"
        
        breadcrumbText=driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[2]/div/div[1]/span[2]").text
        if headerText==breadcrumbText:
            print "Breadcrumb is displayed"
        else:
            print "Error in BreadCrumb"
            raise Exception
        
        
        
        
        
        
        
        
        
        
        
        
if __name__ == '__main__':
    btc=BaseTestClass()
    btc.UserLogin()
    
    c=CreateCampaignsPageDisplay()
    
               
        
        
        
        
        
