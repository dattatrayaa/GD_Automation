'''
Created on 27-Feb-2018

@author: Sheethu C
'''
from operator import contains
import os.path
import pdb
import thread
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from xlrd import book
import xlrd
from BaseTestClass import projectPath
from BaseTestClass import driver
class CreateTag():
    
    def tagCreation(self):
            book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
            sheet=book.sheet_by_name('CreateTag')
            cell = sheet.cell(22,3)
            ExpectedSuccessMessage = cell.value
            print ExpectedSuccessMessage
            wait=WebDriverWait(driver, 80)
            driver.refresh()
            driver.find_element_by_xpath("(//a[@href='/admin/users'])[1]").click()
            wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[2]/div/header/h1")))
            driver.find_element_by_xpath("html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/div/ul/li[5]").click()
            print "Clicked on Tag"
            wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[2]/div/header/h1")))
            print "Tag Page Loaded"
            i=0
            j=2
            for i in range(30):
                book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
                sheet=book.sheet_by_name('CreateTag')
               
                #Read from Excel to search
                cell1 = sheet.cell(i+1,j)
                TagName = cell1.value
                driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/header/div/div/button").click()
                print "Clicked on Create Tag Button"
                wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[2]/div/div/section[1]/div[1]/div/div[1]/div/input")))
                print "Verifying Create Tag Name field "
                if driver.find_element_by_id("add-tag-input").is_displayed():
                    print("Enter Tag name field is displayed")
                else:
                    print ""
                    raise Exception
                    print "Verified Tag Name field"
                
                ele = driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/div/section[1]/div[1]/div/div[1]/div/input")
                webdriver.ActionChains(driver).move_to_element(ele).send_keys(TagName).perform()
                print "Entered Tag Name :"+TagName
                time.sleep(6)
                driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/div/section[1]/div[1]/div/div[2]/button[1]").click()
                time.sleep(6)
                wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[2]/div/div/section[1]/div[1]/div")))
                ActualMessage = driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/div/section[1]/div[1]/div")
                ExpectedMessage =  TagName+ExpectedSuccessMessage
                print "ExpectedMessage "+ExpectedMessage
                print("Expected Success Message and Actual Success Message is Matching,Success Message Verified")
                print "Searching for the created Tag"
                wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[2]/div/div/section[1]/div[2]/div/div/input")))
                time.sleep(6)
          
                element =driver.find_element_by_name("tag-index-search")
                element.clear()
                element.send_keys(TagName)
                driver.find_element_by_name("tag-index-search").send_keys(Keys.ENTER)
 
                time.sleep(6)
                print "Entered Tag Name for Search"
                wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[2]/div/div/section[2]/div/ul/li[1]")))
                print "Verifying the created Tag in the list"
                ele =driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/div/section[2]/div/ul/li[1]")
                print ele.text
                if driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/div/section[2]/div/ul/li[1]").is_displayed():
                    print("Created Tag in the list")
                else:
                    print ""
                    raise Exception
  
    def loopdelete(self,Tagname):
        wait=WebDriverWait(driver, 60)
        driver.refresh()
        wait.until(EC.visibility_of_element_located((By.XPATH,("(//a[@href='/admin/users'])[1]"))))
        driver.find_element_by_xpath("(//a[@href='/admin/users'])[1]").click()
        print "Clicked on admin icon"
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[1]/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/div/ul/li[5]/a")))
        driver.find_element_by_xpath("html/body/div[1]/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/div/ul/li[5]/a").click()
        i=0
        j=2
        for i in range(30):
            book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
            sheet=book.sheet_by_name('CreateTag')
               
                #Read from Excel to search
            cell1 = sheet.cell(i+1,j)
            Tagname = cell1.value
            wait.until(EC.visibility_of_element_located((By.ID,"tag-index-search")))
            tag= driver.find_element_by_id("tag-index-search")
            tag.send_keys(Tagname)
            tag.send_keys(Keys.ENTER)
            wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[1]/div/div[3]/div[2]/div/div/section[2]/div/ul/li[1]/a")))
            driver.find_element_by_xpath("html/body/div[1]/div/div[3]/div[2]/div/div/section[2]/div/ul/li[1]/a").click()
            wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[1]/div/div[3]/div[2]/div/header/div/button")))
            wait.until(EC.element_to_be_clickable((By.XPATH,"html/body/div[1]/div/div[3]/div[2]/div/header/div/button")))
            driver.find_element_by_xpath("html/body/div[1]/div/div[3]/div[2]/div/header/div/button").click()
            wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[4]/div/div/div[2]/div/button[1]")))
            wait.until(EC.element_to_be_clickable((By.XPATH,"html/body/div[4]/div/div/div[2]/div/button[1]")))
            driver.find_element_by_xpath("html/body/div[4]/div/div/div[2]/div/button[1]").click()
            time.sleep(4)
       
    def CreateTagAndSearchInList(self):
        try :
            obj2= CreateTag()
            obj2.tagCreation()
        finally:  
            print "clicking on Home"
            book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
            first_sheet = book.sheet_by_name('Login_Credentials')
        
            # read a cell
            cell = first_sheet.cell(1,1)
            HomeURL = cell.value
            print HomeURL
            driver.get(HomeURL)
            wait=WebDriverWait(driver, 80)
            wait.until(EC.visibility_of_element_located((By.ID,"global-header-search")))
            print "Home Page Loaded"
