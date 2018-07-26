'''
Created on 09-May-2018

@author: dattatraya
'''
import time

from BaseTestClass import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class UsersPageElements:
    
    def AdminFromSideMenuClick(self):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/a")))
        driver.find_element_by_xpath("html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/a").click()
    
    
    def UsersFromSideMenuClick(self):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/div/ul/li[1]")))
        driver.find_element_by_xpath("html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/div/ul/li[1]").click()

    
    def AddOrEditUserButtonClick(self):
        wait=WebDriverWait(driver, 120)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@class='btn primary-cta-branding']")))
        wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@class='btn primary-cta-branding']")))
        driver.find_element_by_xpath("//a[@class='btn primary-cta-branding']").click()
        
        
    def AddAnIndividualUserButtonClick(self):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/header/div/a")))
        wait.until(EC.element_to_be_clickable((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/header/div/a")))
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[2]/div/header/div/a").click()
        
    
    def AddUserPageHeaderXpath(self):
        return "html/body/div/div/div[3]/div[2]/div/header"
    
    def FirstNameFieldID(self):
        return "create-edit-user-search-firstName" 
    
    def LastNameFieldID(self):
        return "create-edit-user-search-lastName" 
    
    def EmailFieldID(self):
        return "create-edit-user-search-username" 
        
    def EmployeeIDFieldID(self):
        return "create-edit-user-search-employeeId"
    
    def InHeritedRoleFieldXpath(self):
        return "html/body/div/div/div[3]/div[2]/div/div[2]/div/div/div[1]/div[6]/div"
    
    def PassWordFieldID(self):
        return "create-edit-user-search-new-password"



    def AdditionalAttributesViewClick(self):
        wait=WebDriverWait(driver, 60)
        view=wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[2]/div/div[3]/h2/button")))
        view.click()
        
    
    def CityAttributeFieldEnterData(self,cityName):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//label[contains(.,'City')]/../div/div/span/div[1]")))
        city=driver.find_element_by_xpath("//label[contains(.,'City')]/../div/div/span/div[1]")
        webdriver.ActionChains(driver).move_to_element(city).click(city).send_keys(cityName).perform()
        time.sleep(2)
        
    def SelectCreateOption(self,attributeName):
        wait=WebDriverWait(driver, 60)
        ele=wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@role='option']")))
        webdriver.ActionChains(driver).move_to_element(ele).click(ele).perform()
        time.sleep(2)
        
    def CountryAttributeFieldEnterData(self,countryName):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//label[contains(.,'Country')]/../div/div/span/div[1]")))
        country=driver.find_element_by_xpath("//label[contains(.,'Country')]/../div/div/span/div[1]")
        webdriver.ActionChains(driver).move_to_element(country).click(country).send_keys(countryName).perform()
        time.sleep(2)
        
    def DepartmentAttributeFieldEnterData(self,deptName):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//label[contains(.,'Department')]/../div/div/span/div[1]")))
        dept=driver.find_element_by_xpath("//label[contains(.,'Department')]/../div/div/span/div[1]")
        webdriver.ActionChains(driver).move_to_element(dept).click(dept).send_keys(deptName).perform()
        time.sleep(2)
        
    def HireDateAttributeFieldSelectDay(self,dayOfCurrentmonth):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='create-edit-user-search-hireDate']")))
        hiredate=driver.find_element_by_xpath("//input[@id='create-edit-user-search-hireDate']")
        webdriver.ActionChains(driver).move_to_element(hiredate).click(hiredate).perform()
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"(//div[@role='option' and @class='react-datepicker__day' or @class='react-datepicker__day react-datepicker__day--weekend' or @class='react-datepicker__day react-datepicker__day--today'])["+str(dayOfCurrentmonth)+"]")))
        day=driver.find_element_by_xpath("(//div[@role='option' and @class='react-datepicker__day' or @class='react-datepicker__day react-datepicker__day--weekend' or @class='react-datepicker__day react-datepicker__day--today'])["+str(dayOfCurrentmonth)+"]")
        webdriver.ActionChains(driver).move_to_element(day).click(day).perform()
        time.sleep(2)
      
    def selectedDate(self):
        return "//input[@id='create-edit-user-search-hireDate']"
    
    def jobTitleAttributeFieldEnterData(self,jobtitle):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//label[contains(.,'Job Title')]/../div/div/span/div[1]")))
        dept=driver.find_element_by_xpath("//label[contains(.,'Job Title')]/../div/div/span/div[1]")
        webdriver.ActionChains(driver).move_to_element(dept).click(dept).send_keys(jobtitle).perform()
        time.sleep(2)
    
    def LocationAttributeFieldEnterData(self,location):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//label[contains(.,'Location')]/../div/div/span/div[1]")))
        loc=driver.find_element_by_xpath("//label[contains(.,'Location')]/../div/div/span/div[1]")
        webdriver.ActionChains(driver).move_to_element(loc).click(loc).send_keys(location).perform()
        time.sleep(2)  
        
    def RegionAttributeFieldEnterData(self,region):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//label[contains(.,'Region')]/../div/div/span/div[1]")))
        reg=driver.find_element_by_xpath("//label[contains(.,'Region')]/../div/div/span/div[1]")
        webdriver.ActionChains(driver).move_to_element(reg).click(reg).send_keys(region).perform()
        time.sleep(2)  
        
    def StateAttributeFieldEnterData(self,state):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//label[contains(.,'State')]/../div/div/span/div[1]")))
        st=driver.find_element_by_xpath("//label[contains(.,'State')]/../div/div/span/div[1]")
        webdriver.ActionChains(driver).move_to_element(st).click(st).send_keys(state).perform()
        time.sleep(2)  
        
    def ReportsToAttributeFieldEnterData(self,reportsTo):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//label[contains(.,'Reports To')]/../../div[2]/div/span/div[1]")))
        report=driver.find_element_by_xpath("//label[contains(.,'Reports To')]/../../div[2]/div/span/div[1]")
        webdriver.ActionChains(driver).move_to_element(report).click(report).send_keys(reportsTo).perform()
        time.sleep(2)
        
    def AddButtonClick(self):
        wait=WebDriverWait(driver, 60)   
        wait.until(EC.visibility_of_element_located((By.XPATH,"//button[.='Add']")))
        b=wait.until(EC.element_to_be_clickable((By.XPATH,"//button[.='Add']")))
        b.click()
        
    def SaveButtonClick(self):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//button[.='Save']")))
        saveButton=driver.find_element_by_xpath("//button[.='Save']");
        driver.execute_script("arguments[0].click();",saveButton)

    def UsersPageHeader(self):
        return "html/body/div[1]/div/div[3]/div[2]/div/header/h1"
    
    def SearchForUserInGrid(self,FirstName):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.ID,"search-users")))
        driver.find_element_by_id("search-users").clear()
        driver.find_element_by_id("search-users").send_keys(FirstName)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//tbody/tr[1]/td[2]/a")))
        
    def CheckUserDisplayedInGrid(self,FirstName):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//tbody/tr[1]/td[2]/a")))
        ele =driver.find_element_by_xpath("//tbody/tr[1]/td[2]/a").text
        if(ele==FirstName):
            print("Created User Verified")
        else:
            print ""
            raise Exception 
        

    
        
    def checkboxSelectInUsersGrid(self,rownum):
        wait=WebDriverWait(driver, 60)
        row1=wait.until(EC.visibility_of_element_located((By.XPATH,"//tbody/tr["+str(rownum)+"]/td[1]")))
        webdriver.ActionChains(driver).move_to_element(row1).perform()
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"//tbody/tr["+str(rownum)+"]/td[1]/div/label/span")))
        driver.find_element_by_xpath("//tbody/tr["+str(rownum)+"]/td[1]/div/label/span").click()
        
        
        
    def getCountofUserDisplayed(self):
        wait=WebDriverWait(driver, 60)
        row1=wait.until(EC.visibility_of_all_elements_located((By.XPATH,"//tbody/tr/td[1]")))
        co=len(row1)
        return co
        
        
        
    def checkCountDisplayedAtBottomAfterSelection(self):
        
        wait=WebDriverWait(driver, 60)
        bottomCount=wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[1]/div/div[3]/div[3]/div/div/div[2]/div[1]/span")))
        b=bottomCount.text
        return b


    def closeUsersSelectionPopup(self):
        wait=WebDriverWait(driver, 60)
        bottomCount=wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[1]/div/div[3]/div[3]/div/div/div[1]/button")))
        bottomCount.click()



    def checkForCheckboxSelection(self):
        wait=WebDriverWait(driver, 60)
        row1=wait.until(EC.visibility_of_element_located((By.XPATH,"//tbody/tr[1]/td[1]")))
        webdriver.ActionChains(driver).move_to_element(row1).perform()
        if driver.find_element_by_xpath("//tbody/tr[1]/td[1]/div/label/input").is_selected():
            print "Check-box is still selected"
            raise Exception
        else:
            print "Check-box successfully unchecked"
    
    def deactivateLinkAtBottomElement(self):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[1]/div/div[3]/div[3]/div/div/div[2]/div[3]/button")))
        return driver.find_element_by_xpath("html/body/div[1]/div/div[3]/div[3]/div/div/div[2]/div[3]/button")
        
            
    
    def deactivateLinkAtBottom(self):
        wait=WebDriverWait(driver, 60)
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[1]/div/div[3]/div[3]/div/div/div[2]/div[3]/button")))
        except Exception:
            print "Deactivate button not displayed"
            raise Exception
        driver.find_element_by_xpath("html/body/div[1]/div/div[3]/div[3]/div/div/div[2]/div[3]/button").click()
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[4 or 2]/div/div/div[2]/div[2]/button[2]")))
    
    
    def DeactivateUserPopupHeader(self):
        wait=WebDriverWait(driver, 60)
        ele=wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[4 or 2]/div/div/div[1]/h3")))
        return ele
        
        
        
    def deactivateButtonFromPopup(self):
        wait=WebDriverWait(driver, 60)
        deact=wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[4 or 2]/div/div/div[2]/div[2]/button[2]")))
        deact.click()
    def deactivateButtonFromPopupXpath(self):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[4 or 2]/div/div/div[2]/div[2]/button[2]")))
        deact=driver.find_element_by_xpath("html/body/div[4 or 2]/div/div/div[2]/div[2]/button[2]")
        return deact
        
    def CloseButtonDeactivateUserPopup(self):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[4 or 2]/div/div/div[1]/button")))
        close=driver.find_element_by_xpath("html/body/div[4 or 2]/div/div/div[1]/button")
        return close 
    
    def CloseButtonOfPopup(self):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[1]/div/div[3]/div[3]/div/div/div[1]/button")))
        wait.until(EC.element_to_be_clickable((By.XPATH,"html/body/div[1]/div/div[3]/div[3]/div/div/div[1]/button")))
        close=driver.find_element_by_xpath("html/body/div[1]/div/div[3]/div[3]/div/div/div[1]/button")
        return close    
    
        
    def successMessageForDeactivatedUser(self,count):
        wait=WebDriverWait(driver, 60)
        deact=wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[1]/div/div[2]/div/div/span[2]")))
        print "Success  :: "+deact.text
        
        if deact.text==str(count)+" users have been deactivated.":
            print "Success "+deact.text+" message is displayed"
        else:
            print "Success message not displayed properly"
            raise Exception
        
    
    
    def seeDeactivatedUsersLink(self):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//a[.='See deactivated users']")))
        deact=wait.until(EC.element_to_be_clickable((By.XPATH,"//a[.='See deactivated users']")))
        deact.click()
        wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='search-users']")))
        
    def searchDeactivatedUsers(self,LastName):
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='search-users']")))
        driver.find_element_by_id("search-users").send_keys(LastName)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//table/tbody/tr[1]/td[1]")))
        
    def checkDeactivatedUser(self,LastName):
        wait=WebDriverWait(driver, 60)
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,"//table/tbody/tr[1]/td[2][contains(.,'"+LastName+"')]")))
            print "Deactivated users displayed in Grid "
        except Exception:
            print "User not displayed in Deactivated Users list"
            raise Exception
        


    def selectAllUsersCheckboxClickFromGrid(self):
        wait=WebDriverWait(driver, 60)
        row1=wait.until(EC.visibility_of_element_located((By.XPATH,"//table/thead/tr/th[1]")))
        webdriver.ActionChains(driver).move_to_element(row1).perform()
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"//table/thead/tr/th[1]/div/label/span")))
        driver.find_element_by_xpath("//table/thead/tr/th[1]/div/label/span").click()
        
        

    def HeaderTextUsersPageXpath(self):
        return "html/body/div/div/div[3]/div[2]/div/header/h1"
    
    
    
    def AddEditButtonXpath(self):
        return "//a[contains(.,'Add/Edit users')]"
    
    def filterUsersXpath(self):
        return "//button[.='Filter users']"
    
    def seeDeactivatedUsersXpath(self):
        return "//a[.='See deactivated users']"
    
    
    def downLoadUserListLinkXpath(self):
        return "//a[contains(.,'Download active user list')]"
    
    
    def ColumnNameVerifyingOFGrid(self):
        return "//thead/tr/th[contains(.,'First name')]/../th[contains(.,'Email')]/../th[contains(.,'Roles')]/../th[contains(.,'Date added')]/../th[contains(.,'Action')]"
    
    def DeactivateButtonFromGridXpath(self):
        return "//tbody/tr[1]/td[7]/button[.='Deactivate']"
    

    def DeactivateButtonAllLinks(self):
        return "//table/tbody/tr/td[7]/button"
    
    def NoOFrowsDisplayedXpath(self):
        return "//table/tbody/tr"

    def Pagination(self):
        return "//span[.='100']/../span[.='|']/../../../small[contains(.,'per page')]"
        
    def FilterUsersPopUpHeaderText(self):
        wait=WebDriverWait(driver, 60)
        filterText=wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[4 or 2]/div/div/div[1]/h3")))
        return filterText.text
    

    def filterUserPopupCloseButton(self):
        wait=WebDriverWait(driver, 60)
        close=wait.until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[4 or 2]/div/div/div[1]/button/span")))
        close.click()

    def filterUserPopupCancelButton(self):
        wait=WebDriverWait(driver, 60)
        cancel=wait.until(EC.visibility_of_element_located((By.XPATH,"//button[@class='btn btn-transparent-no-border']")))
        cancel.click()
           
    def allcheckboxesSelectedCount(self):
        wait=WebDriverWait(driver, 60)
        count=wait.until(EC.visibility_of_all_elements_located((By.XPATH,"//table/tbody/tr/td[1]/div/label/span/span")))
        return len(count)
           
    def PopupDisplayedAtBottom(self):
        wait=WebDriverWait(driver, 60)
        popup=wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[1]/div/div[3]/div[3]/div/div/div[2]"))) 
        return popup
        
         
    def BulkUncheckedCheckBoxElement(self):
        wait=WebDriverWait(driver, 60)
        row1=wait.until(EC.visibility_of_element_located((By.XPATH,"//table/thead/tr/th[1]")))
        webdriver.ActionChains(driver).move_to_element(row1).perform()
        return driver.find_element_by_xpath("//table/thead/tr/th[1]/div/label/span")
        
        
        
        
        
        
        
        
        
        
        

