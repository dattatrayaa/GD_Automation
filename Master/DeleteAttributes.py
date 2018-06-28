'''
Created on 26-Mar-2018

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
from BaseTestClass import driver
from BaseTestClass import projectPath
from CreateAttributeXpath import CreateAttributeXpath

class DeleteAttributes:
    def attributeDelete(self,AttributeName):
        try:  
            
            attributedel =CreateAttributeXpath()
                                                              
            wait=WebDriverWait(driver, 60)
            driver.refresh()
            driver.find_element_by_xpath(attributedel.adminSideMenu()).click()
            wait.until(EC.visibility_of_element_located((By.XPATH,attributedel.attributeMenu())))
            driver.find_element_by_xpath(attributedel.attributeMenu()).click()
            wait.until(EC.visibility_of_element_located((By.XPATH,attributedel.attributenameInGrid(AttributeName))))
            driver.find_element_by_xpath(attributedel.attributeDelete(AttributeName)).click()
            wait.until(EC.visibility_of_element_located((By.XPATH,attributedel.popUpDeleteButton())))
            wait.until(EC.element_to_be_clickable((By.XPATH,attributedel.popUpDeleteButton())))
            driver.find_element_by_xpath(attributedel.popUpDeleteButton()).click()
            wait.until(EC.visibility_of_element_located((By.XPATH,attributedel.deleteafterwait())))
        finally:
            book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
            second_sheet = book.sheet_by_name('Login_Credentials')
            cell = second_sheet.cell(1,1)
            url = cell.value
            driver.get(url)    