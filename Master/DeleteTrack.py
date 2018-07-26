'''
Created on 13-Mar-2018

@author: Sheethu C
'''
import os
import traceback

from BaseTestClass import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xlrd

from BaseTestClass import BaseTestClass


class DeleteTrack:
    def deleteIt(self,titleOfTrack):    
        wait=WebDriverWait(driver, 120)
        #wait.until(EC.visibility_of_element_located((By.XPATH,"//tr[1]/td[4]/button[.='Delete']")))
        
        driver.refresh()
        wait.until(EC.visibility_of_element_located((By.XPATH,"//tbody/tr/td[2]/a[.='"+titleOfTrack+"']/../../td[4]/button[.='Delete']")))
        wait.until(EC.element_to_be_clickable((By.XPATH,"//tbody/tr/td[2]/a[.='"+titleOfTrack+"']/../../td[4]/button[.='Delete']")))
        driver.find_element_by_xpath("//tbody/tr/td[2]/a[.='"+titleOfTrack+"']/../../td[4]/button[.='Delete']").click()
        wait.until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2 or 4]/div/div/div[2]/div[2]/button[1]")))
        driver.find_element_by_xpath("/html/body/div[2 or 4]/div/div/div[2]/div[2]/button[1]").click()
        wait.until(EC.invisibility_of_element_located((By.XPATH,"/html/body/div[2 or 4]/div/div/div[2]/div[2]/button[1]")))
        
        
    def mainDelete(self,titleOfTrack):
        try:
            d=DeleteTrack()
            print "\n\nDeleting Track.........."
            wait=WebDriverWait(driver, 60)
            wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@href='/create/lessons']")))
        
            driver.find_element_by_xpath("//a[@href='/create/lessons']").click()
            wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@href='/create/tracks']")))
        
            driver.find_element_by_xpath("//a[@href='/create/tracks']").click()
            
            wait=WebDriverWait(driver, 60)
            search=wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='search-objectives']")))
            search.send_keys(titleOfTrack)
            wait.until(EC.visibility_of_all_elements_located((By.XPATH,"//tbody/tr/td[2]/a[.='"+titleOfTrack+"']")))
            ele=driver.find_elements_by_xpath("//tbody/tr/td[2]/a[.='"+titleOfTrack+"']")
            print "Deleting Track"
            count=len(ele)
            
            for count in range (0,count):
                d.deleteIt(titleOfTrack)
            
            print "All Elements are deleted"
            
        finally:
            book=xlrd.open_workbook(os.path.join('TestData.xlsx'))
            second_sheet = book.sheet_by_name('Login_Credentials')
            cell = second_sheet.cell(1,1)
            url = cell.value
            driver.get(url)

        
if __name__ == '__main__':
    btc=BaseTestClass()
    btc.UserLogin()
       
    d=DeleteTrack()
    d.mainDelete("Track_first_with_TextLesson1")
        
        
        
        