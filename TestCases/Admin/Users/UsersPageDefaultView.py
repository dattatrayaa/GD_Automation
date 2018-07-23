'''
Created on 05-Jun-2018

@author: dattatraya
'''
import os.path
import traceback

from BaseTestClass import BaseTestClass
from BaseTestClass import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xlrd

from ExcelFunctions import ExcelFunctions
from UsersPageElements import UsersPageElements


class UsersPageDefaultView:
    
        
    
    def checkUsersPageUi(self,expctedHeaderText):
        user=UsersPageElements()
        wait=WebDriverWait(driver, 60)
        driver.refresh()
        
        user.AdminFromSideMenuClick()
        print "CLicked on Admin Menu"
        
        user.UsersFromSideMenuClick()
        print "Clicked On Users from Side Menu"
        
        headerActual=wait.until(EC.visibility_of_element_located((By.XPATH,user.HeaderTextUsersPageXpath())))
    
        if expctedHeaderText==headerActual.text:
            print "Header Text Is displayed"
        else:
            raise Exception('Header Text of users page is not correct')
        
        
        print "Verifying Add/Edit button is displayed"
        
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,user.AddEditButtonXpath())))
            print "Add/Edit is displayed"
        except Exception:
            raise Exception('Add/Edit button not displayed')
        
        
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,user.filterUsersXpath())))
            print "Filter button is displayed"
        except Exception:
            raise Exception('Filter button not displayed')
        
        
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,user.seeDeactivatedUsersXpath())))
            print "See Deactivated Users link is displayed"
        except Exception:
            raise Exception('See Deactivated Users link is not displayed')
        
        
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,user.downLoadUserListLinkXpath())))
            print "Download active user list link is displayed"
        except Exception:
            raise Exception('Download active user list link is not displayed')
        
        
        print "Verifying Column Names"
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,user.ColumnNameVerifyingOFGrid())))
            print "Column Names "
        except Exception:
            raise Exception('Column Names not displayed properly')
        
        
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,user.ColumnNameVerifyingOFGrid())))
            print "All columns displayed properly"
        except Exception:
            raise Exception('Column Names not displayed properly')
        
        print "Checking Deactivate Link is displayed for all Users"
        
        rowsIngrid=wait.until(EC.visibility_of_all_elements_located((By.XPATH,user.NoOFrowsDisplayedXpath())))
        count=len(rowsIngrid)
        print "Number of users displayed in grid ::"+str(count)
        
        
        deactLinks=wait.until(EC.visibility_of_all_elements_located((By.XPATH,user.DeactivateButtonAllLinks())))
        count2=len(deactLinks)
        
        if count==count2:
            print "Deactivate links are displayed for every user in list i.e. =="+str(count2)
        else:
            raise Exception('Deactivate Links are not matching with the number of users displayed')
        
        try:
            wait.until(EC.visibility_of_all_elements_located((By.XPATH,user.Pagination())))
            print "Proper pagination displayed"
            
        except Exception:
            raise Exception('Pagination not displayed properly')
        
        
        
        
        
        
        
    def UsersDefaultViewMain(self):
        exc=ExcelFunctions()
        exc.OpenExcelFile("TestData.xlsx")
        exc.OpenSheet("UsersPage")
                
        
        expctedHeaderText=exc.getCellData(11, 1)
            
            
            
            
        try:
            print "\nVerifying All UI elements present in Users page\n"
            t=UsersPageDefaultView()
            t.checkUsersPageUi(expctedHeaderText)
                
                
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
    
    bulk=UsersPageDefaultView()
    bulk.UsersDefaultViewMain()
        
        
        


