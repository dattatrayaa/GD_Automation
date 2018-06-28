'''
Created on 05-Apr-2018

@author: dattatraya
'''


from BaseTestClass import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class PlanAssignmentForPageElements:
    
    def headerTextPlanAssignment(self):
        return ".//*[@id='content']/div/div[3]/div[2]/div/header/h1"
    
    def triggredRadioButton(self):
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[2]/div/section/div/div[2]/label/span[2]").click()
    
    
    def NewHireOnBoarding(self):
        return ".//*[@id='content']/div/div[3]/div[2]/div/div[2]/section[1]/div/div[1]/label/span[2]"
    
    def NewtoGroup(self):
        return ".//*[@id='content']/div/div[3]/div[2]/div/div[2]/section[1]/div/div[2]/label/span[2]"
    
    def AddGroupTextField(self):
        return "//div[@class='Select-placeholder']"
    
    def CheckBoxCurrentUserMatching(self):
        return ".//*[@id='content']/div/div[3]/div[2]/div/div[2]/section[1]/div/div[3]/div[2]/label/span[2]"
    
    def YourCriteriaMatchesBox(self):
        return ".//*[@id='content']/div/div[3]/div[2]/div/div[2]/section[1]/div/div[3]/div[3]"
    
    def YourCriteriaMatchesLearnerLink(self):
        return ".//*[@id='content']/div/div[3]/div[2]/div/div[2]/section[1]/div/div[3]/div[3]/button"
    
    
    
    
    
    def saveTrigger(self):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/div[2]/section[2]/div/div[2]/button")))
        save=wait.until(EC.element_to_be_clickable((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/div[2]/section[2]/div/div[2]/button")))
        save.click()
        
    def confirmPopupYesSaveButton(self):
        return "html/body/div[4]/div/div/div[2]/div[2]/button[1]"
    
    
    def confirmPopupCancelButton(self):
        return "html/body/div[2]/div/div/div[2]/div[2]/button[2]"
    
    def confirmPopupCloseIcon(self):
        return "html/body/div[2]/div/div/div[1]/button"
    def confirmPopupHeaderText(self):
        return "html/body/div[2]/div/div/div[1]/h3"
    
     
    def sendAssignmentButtonPopup(self):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[4]/div/div/div[2]/div[2]/button[1]")))
        yesSend=wait.until(EC.element_to_be_clickable((By.XPATH,"html/body/div[4]/div/div/div[2]/div[2]/button[1]")))
        yesSend.click()
         
        
    def planAssignmentHeader(self):
        wait=WebDriverWait(driver, 60)
        h=wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[1]/div/div[3]/div[2]/div/header/h1")))
        return h.text 
    
    def sendAssignmentButton(self):
        return "html/body/div/div/div[3]/div[2]/div/div[2]/section[2]/div/div[2]/button"
    
    def assignButton(self):
        return "html/body/div/div/div[3]/div[2]/div/section[2]/div/div[4]/div[2]/button"
        
    
    
        
        
        
        