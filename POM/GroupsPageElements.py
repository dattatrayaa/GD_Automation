'''
Created on 24-Apr-2018

@author: dattatraya
'''
import os
import time

from BaseTestClass import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xlrd


class GroupsPageElements:
    def adminSideMenuUnexpanded(self):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/a")))
        driver.find_element_by_xpath("html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/a").click()
    
    
    def groupSideMenuExpanded(self):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/div/ul/li[2]/a")))
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/div/ul/li[2]/a").click() 
        
    def groupDetailPageHeader(self):
        return ".//*[@id='content']/div/div[3]/div[2]/div/header/div[1]/h1/div"
        

    def groupPageHeader(self):
        return ".//*[@id='content']/div/div[3]/div[2]/div/header/h1"
    
    def createGroupButton(self):
        wait=WebDriverWait(driver, 60)
        createGroup=wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/header/div/button")))
        createGroup.click()
    def enteringGroupname(self,groupName):
        wait=WebDriverWait(driver, 60)
        grpName=wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='create-group']")))
        grpName.send_keys(groupName)
        
    def nextButton(self):
        wait=WebDriverWait(driver, 60)
        nextButton=wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[4 or 2]/div/div/div[2]/div/div[2]/button[1]")))
        driver.execute_script('arguments[0].click()',nextButton)


    def addByNameButton(self):
        wait=WebDriverWait(driver, 60)
        addByName=wait.until(EC.element_to_be_clickable((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/div[2]/div/div/div[1]/div/div/div[2]/div/button")))
        addByName.click()
        wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@class='Select-placeholder']")))
        
    def addByName(self,FirstName):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@class='Select-placeholder']")))
        names=driver.find_element_by_xpath("//div[@class='Select-placeholder']")
        time.sleep(2)
        webdriver.ActionChains(driver).move_to_element(names).click()
        webdriver.ActionChains(driver).move_to_element(names).send_keys(FirstName).perform()
        userDisplayed=wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@role='option']/span[contains(.,'"+FirstName+"')]")))
        webdriver.ActionChains(driver).move_to_element(userDisplayed).click().perform()
        print "User selected and added to group"
        time.sleep(2)
        wait.until(EC.invisibility_of_element_located((By.XPATH,"html/body/div[4]/div/div/div/div")))
    
    def closeAddByNameTextField(self):
        wait=WebDriverWait(driver, 60)
        close=wait.until(EC.visibility_of_element_located((By.XPATH,"//button[@class='u-center-v-abs']")))
        close.click()
        
    def usersInGridOFUserDetails(self):
        return "//table/tbody/tr/td[2]"  
    
    
    def groupAddedInList(self,FirstName):
        wait=WebDriverWait(driver, 60)
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,"//table/tbody/tr/td[.='"+FirstName+"']")))
            print "User is displayed in grid ::"+FirstName
        except:
            print "User is not displayed in grid"
      
      
    def saveButton(self):
        wait=WebDriverWait(driver, 60)
        saveButton=wait.until(EC.element_to_be_clickable((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/header/div[2]/button[2]")))
        saveButton.click()   
        
        
    def saveButtonPopup(self):
        wait=WebDriverWait(driver, 60)
        saveFrompopup=wait.until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[4]/div/div/div[2]/div/button[2]")))
        saveFrompopup.click() 
        time.sleep(4)
        wait.until(EC.invisibility_of_element_located((By.XPATH,"html/body/div[4]/div/div/div/div")))
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/header/div[2]/button"))) 
        
    def createdGroupDisplayedInGrid(self,groupName):
        wait=WebDriverWait(driver, 60)
        driver.find_element_by_xpath(".//*[@id='search-groups']").send_keys(groupName)
        ele=wait.until(EC.visibility_of_element_located((By.XPATH,"//table/tbody/tr/td[2]/a[.='"+groupName+"']")))
        
        if ele.text==groupName:
            print "Group is displayed in grid"
        else:
            print "Group is not displayed in grid"
            raise Exception
      
    def groupsLinkFromBreadCrumb(self):
        wait=WebDriverWait(driver, 60)
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        first_sheet = book.sheet_by_name('Login_Credentials')
        print("Fetching the Attribute Name from Excel Sheet\n")
            # read a cell
        cell = first_sheet.cell(1,1)
        URL = cell.value
        driver.get(URL+"admin/groups")
        time.sleep(4)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//table/tbody/tr[1]/td[2]/a")))  
        
        
    def groupInGrid(self,groupName):
        return "//table/tbody/tr/td[2]/a[.='"+groupName+"']"
    
    def searchGroupTextFieldXpath(self):
        return ".//*[@id='search-groups']"
        
    
    def AddByAttributes(self):    
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"(//button[.='Add by attribute'])[2]")))
        addByName=driver.find_element_by_xpath("(//button[.='Add by attribute'])[2]")
        addByName.click()
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2 or 4]/div/div/div[2]/div[1]/div[1]")))
        
    def AllOptionSelected(self):
        wait=WebDriverWait(driver, 60)
        all1=wait.until(EC.element_to_be_clickable((By.XPATH,"html/body/div[2 or 4]/div/div/div[2]/div[1]/div[1]/div/div/span[1]/div[1]/span")))
        return all1.text
    
    def AttributeNameEnter(self,attributeName):
        wait=WebDriverWait(driver, 60)
        attr=wait.until(EC.element_to_be_clickable((By.XPATH,"(//div[.='Select...'])[1]")))
        webdriver.ActionChains(driver).move_to_element(attr).click(attr).send_keys(attributeName).perform()
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@role='option']")))
        lio=driver.find_element_by_xpath("//div[@role='option']")
        webdriver.ActionChains(driver).move_to_element(lio).click(lio).perform()
        time.sleep(2)
        
    def ValueSelect(self,valueName):
        wait=WebDriverWait(driver, 60)
        attr=wait.until(EC.element_to_be_clickable((By.XPATH,"(//div[.='Select...' or .='Start typing...'])[1]")))
        webdriver.ActionChains(driver).move_to_element(attr).click(attr).send_keys(valueName).perform()
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@role='option' and contains(.,'"+valueName+"')]")))
        lio=driver.find_element_by_xpath("//div[@role='option' and contains(.,'"+valueName+"')]")
        webdriver.ActionChains(driver).move_to_element(lio).click(lio).perform()
        time.sleep(2)
        
    def DateSelect(self,dayOfCurrentmonth):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@placeholder='Select date']")))
        hiredate=driver.find_element_by_xpath("//input[@placeholder='Select date']")
        webdriver.ActionChains(driver).move_to_element(hiredate).click(hiredate).perform()
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"(//div[@role='option' and @class='react-datepicker__day' or @class='react-datepicker__day react-datepicker__day--weekend' or @class='react-datepicker__day react-datepicker__day--today'])["+str(dayOfCurrentmonth)+"]")))
        day=driver.find_element_by_xpath("(//div[@role='option' and @class='react-datepicker__day' or @class='react-datepicker__day react-datepicker__day--weekend' or @class='react-datepicker__day react-datepicker__day--today'])["+str(dayOfCurrentmonth)+"]")
        webdriver.ActionChains(driver).move_to_element(day).click(day).perform()
        time.sleep(2)
    
    
    def PreviewGroupButtonClick(self):
        wait=WebDriverWait(driver, 60)
        pre=wait.until(EC.element_to_be_clickable((By.XPATH,"html/body/div[2 or 4]/div/div/div[2]/div[2]/button[2]")))
        pre.click()
        time.sleep(3)
        wait.until(EC.invisibility_of_element_located((By.XPATH,"html/body/div[2 or 4]/div/div/div/div")))
        
        
    
    def OverViewContainer(self,valueName):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//div[1]/small/div[1]/span")))
        filter1=driver.find_element_by_xpath("//div[1]/small/div[1]/span")
        if valueName in filter1.text:
            print "Filter applied properly"
        else:
            print "Filter is not applied properly"
            raise Exception
        
    
    
    
    def addAttributePopupButtonClick(self):
        wait=WebDriverWait(driver, 60)
        add=wait.until(EC.element_to_be_clickable((By.XPATH,"html/body/div[4 or 2]/div/div/div[2]/div[1]/div/button")))
        add.click()
        wait.until(EC.visibility_of_element_located((By.XPATH,"(//div[.='Select...'])[1]")))
        
        

    def SelectAnyOFTheFollowingOption(self):
        wait=WebDriverWait(driver, 60)   
        b=wait.until(EC.visibility_of_element_located((By.XPATH,"(//div[@class='Select-value'])[1]")))
        b.click()
        
        an=wait.until(EC.visibility_of_element_located((By.XPATH,'html/body/div[4]/div/div/div[2]/div[1]/div[1]/div/div[2]/div/div[2]')))
        an.click()



