'''
Created on 06-Jun-2018

@author: dattatraya
'''

import traceback

from BaseTestClass import BaseTestClass
from BaseTestClass import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from UsersPageElements import UsersPageElements
from ExcelFunctions import ExcelFunctions
from selenium import webdriver


class UsersPageDefaultActions:
    
    
    def UsersDefaultActionsONUI(self,FilterUsersHeaderTextExpected):
        
        user=UsersPageElements()
        wait=WebDriverWait(driver, 60)
        driver.refresh()
        
        user.AdminFromSideMenuClick()
        print "CLicked on Admin Menu"
        
        user.UsersFromSideMenuClick()
        print "Clicked On Users from Side Menu"
        
        wait.until(EC.visibility_of_element_located((By.XPATH,user.HeaderTextUsersPageXpath())))
        
        print "Check Filter Users Default Action"
        
        filterUsers=wait.until(EC.visibility_of_element_located((By.XPATH,user.filterUsersXpath())))
        filterUsers.click()
        print "Clicked on filter Users"
        
        print "Check for Filter Users pop up is displayed"
        
        if FilterUsersHeaderTextExpected==user.FilterUsersPopUpHeaderText():
            print "Filter user popup header text displayed as ::"+user.FilterUsersPopUpHeaderText()
        
        else:
            raise Exception('Filter users pop up text not displayed properly')
        
        print "Check pop up getting closed After click on Close and Cancel buttons"
        
        user.filterUserPopupCloseButton()
        print "Clicked on Close button"
        
        
        filterUsers=wait.until(EC.visibility_of_element_located((By.XPATH,user.filterUsersXpath())))
        filterUsers.click()
        print "Again Clicked on Filter Users button"
        
        user.filterUserPopupCancelButton()
        print "Click on Cancel  button"
        
        
        print "Verifying Checkbox displayed for every user in grid"
        countOfUsersDisplayed =user.getCountofUserDisplayed()
        print "Users displayed in Grid ::"+str(countOfUsersDisplayed)
        
        user.selectAllUsersCheckboxClickFromGrid()
        print "All checkboxes selected"
        
        print "Checking for number of users, checkboxes displayed"
        countOfCheckboxesDisplayed = user.allcheckboxesSelectedCount()
        
        if str(countOfUsersDisplayed)==str(countOfCheckboxesDisplayed):
            print "Checkboxes displayed for all the users"
            
        else:
            raise Exception('Checkbox not displayed for all the users in Grid')
        
        
        print "Checking pop up displayed after selecting users"
        if user.PopupDisplayedAtBottom().is_displayed():
            print "Popup Displayed at  bottom after checkbox selection"
        else:
            raise Exception("Popup not displayed after selecting Checkbox")
        
        if user.getCountofUserDisplayed()==countOfCheckboxesDisplayed:
            print "Count of checkbox selected is matching with count displayed in Popup"
        else:
            raise Exception("Count not matching of checkbox selection")
                
        print "Checking Deactivate button is displayed"
        if user.deactivateLinkAtBottomElement().is_displayed():
            print "Deactivate button is displayed"
        else:
            raise Exception("Deactivate button is not displayed")
        
        user.deactivateLinkAtBottom()
        print "Clicked on Deactivate button"
        
        
        print "Check pop up is displayed"
        if user.DeactivateUserPopupHeader().text=="Deactivate User":
            print "Deactivate user pop up is displayed"
        else:
            raise Exception('Deactivate pop up is not displayed')
        
        
        print "Checking Deactivate button is displayed"
        try:
            user.deactivateButtonFromPopupXpath()
            print "Deactivate button is displayed"
        except Exception:
            raise Exception('Deactivate button is not displayed in Deactivate user pop up')
        
        user.CloseButtonDeactivateUserPopup().click()
        print "Clicked on Close button of pop up"
        
        try:
            user.CloseButtonOfPopup().click()
            print "Clicked on Close pop up button"
        except Exception:
            raise Exception('Not able to click on Close popup button')
        
        print "Verifying Checkbox is unchecked"
        if user.BulkUncheckedCheckBoxElement().is_selected():
            raise Exception('Checkboox still selected')
        else:
            print "All check box unchecked Successfully"
        
        
        
        
        
        
    def UserPageDefaultActionsMain(self):
        exc=ExcelFunctions()
        exc.OpenExcelFile("TestData.xlsx")
        exc.OpenSheet("UsersPage")
                
        
        FilterUsersHeaderTextExpected=exc.getCellData(14, 1)
            
            
            
            
        try:
            print "\nVerifying All UI elements present in Users page\n"
            t=UsersPageDefaultActions()
            t.UsersDefaultActionsONUI(FilterUsersHeaderTextExpected)
                
                
        except Exception as e:
            traceback.print_exc()
            print(e)
            raise Exception
            
        finally:  
            exc.OpenSheet("Login_Credentials")
            url=exc.getCellData(1, 1)
            
            driver.get(url)
            try:
                WebDriverWait(driver, 5).until(EC.alert_is_present())
    
                alert = driver.switch_to.alert
                alert.accept()
                print("alert accepted")
            except Exception:
                print("no alert")
        
        
        
        
        
if __name__=='__main__':
    
    btc=BaseTestClass()
    btc.UserLogin()    
    
    ct=UsersPageDefaultActions()
    ct.UserPageDefaultActionsMain()    
        
        
    
