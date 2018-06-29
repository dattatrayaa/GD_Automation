'''
Created on 05-Apr-2018

@author: Sheethu C
'''

import os
import time
import traceback

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xlrd

from BaseTestClass import driver
from BaseTestClass import projectPath
from BaseTestClass import excelPath

class DeleteRole:
    def roleDelete(self,RoleName):  
        try:                                                       
            wait=WebDriverWait(driver, 60)
            driver.refresh()
            wait.until(EC.visibility_of_element_located((By.XPATH,"(//a[@href='/admin/users'])[1]")))
            driver.find_element_by_xpath("(//a[@href='/admin/users'])[1]").click()
            print "clicking Admin menu in the side menu"
            wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/div/ul/li[3]/a")))
            driver.find_element_by_xpath("html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/div/ul/li[3]/a").click()
            wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[2]/div/header/h1")))
            time.sleep(4)
            wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[2]/div/div/ul/li[2]/a")))
            driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/div/ul/li[2]/a").click()
            wait.until(EC.visibility_of_element_located((By.XPATH,"//tbody/tr[1]/td[4]/button")))
            time.sleep(4)
            wait.until(EC.visibility_of_element_located((By.ID,"search-roles")))
            driver.find_element_by_id("search-roles").send_keys(RoleName)
            wait.until(EC.visibility_of_element_located((By.XPATH,"//tbody/tr/td[.='"+RoleName+"']/span/a/../../../td[4]/button")))
            time.sleep(4)
            driver.find_element_by_xpath("//tbody/tr/td[.='"+RoleName+"']/span/a/../../../td[4]/button").click()
            wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[4]/div/div/div[2]/div[2]/button[1]")))
            wait.until(EC.element_to_be_clickable((By.XPATH,"html/body/div[4]/div/div/div[2]/div[2]/button[1]")))
            driver.find_element_by_xpath("html/body/div[4]/div/div/div[2]/div[2]/button[1]").click()
            time.sleep(4)
        finally:
            book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
            second_sheet = book.sheet_by_name('Login_Credentials')
            cell = second_sheet.cell(1,1)
            url = cell.value
            driver.get(url)       
    
              
            
            
            
            
            
            