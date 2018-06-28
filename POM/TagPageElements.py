'''
Created on 11-Jun-2018

@author: Sheethu C
'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from BaseTestClass import driver


class TagPageElements:
    
        
    def tagCreation(self,tagName):
        wait=WebDriverWait(driver, 80)
        driver.refresh()
        wait.until(EC.visibility_of_element_located((By.XPATH,("(//a[@href='/admin/users'])[1]"))))
        driver.find_element_by_xpath("(//a[@href='/admin/users'])[1]").click()
        print "Clicked on admin icon"
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[1]/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/div/ul/li[5]/a")))
        driver.find_element_by_xpath("html/body/div[1]/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/div/ul/li[5]/a").click()
        print "Clicked on Admin"
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[1]/div/div[3]/div[2]/div/header/div/div/button")))
        wait.until(EC.element_to_be_clickable((By.XPATH,"html/body/div[1]/div/div[3]/div[2]/div/header/div/div/button")))
        driver.find_element_by_xpath("html/body/div[1]/div/div[3]/div[2]/div/header/div/div/button").click()
        print "Clicked on Create Tag Button"
        wait.until(EC.visibility_of_element_located((By.ID,"add-tag-input")))
        print "Verifying Create Tag Name field "
        time.sleep(4)
        if driver.find_element_by_id("add-tag-input").is_displayed():
            print("Enter Tag name field is displayed")
        else:
            print ""
            raise Exception
        print "Verified Tag Name field"
        ele = driver.find_element_by_id("add-tag-input")
        webdriver.ActionChains(driver).move_to_element(ele).send_keys(tagName).perform()
        print "Entered Tag Name :"+tagName
        time.sleep(3)
        button=wait.until(EC.element_to_be_clickable((By.XPATH,"html/body/div[1]/div/div[3]/div[2]/div/div/section[1]/div[1]/div/div[2]/button[1]")))
        button.click()
        time.sleep(4)
        print "Searching for the created Tag"
        wait.until(EC.visibility_of_element_located((By.ID,"tag-index-search")))
        time.sleep(6)
        element =driver.find_element_by_id("tag-index-search")
        element.send_keys(tagName)
        driver.find_element_by_id("tag-index-search").send_keys(Keys.ENTER)
        time.sleep(6)
        print "Entered Tag Name for Search"
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[2]/div/div/section[2]/div/ul/li[.='"+tagName+"']/a")))
        print "Verifying the created Tag in the list"
        ele =driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/div/section[2]/div/ul/li[.='"+tagName+"']/a")
        print ele.text
        time.sleep(4)
        if driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/div/section[2]/div/ul/li[.='"+tagName+"']/a").is_displayed():
            print("Created Tag in the list")
        else:
            print ""
            raise Exception
        driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/div/section[2]/div/ul/li[.='"+tagName+"']/a").click()
        time.sleep(4)
    def addlesson(self,lessonname):
        wait=WebDriverWait(driver, 80)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[1]/div/div[3]/div[2]/div/ul/li[1]/a")))
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[1]/div/div[3]/div[2]/div/div[2]/button")))
        driver.find_element_by_xpath("html/body/div[1]/div/div[3]/div[2]/div/div[2]/button").click()
        wait.until(EC.visibility_of_element_located((By.ID,"search-lessons-in-modal")))
        SearchElement =driver.find_element_by_id("search-lessons-in-modal")
        SearchElement.send_keys(lessonname)
        SearchElement.send_keys(Keys.ENTER) 
        wait.until(EC.visibility_of_element_located((By.XPATH,"//li/div[2]/h4[.='"+lessonname+"']/../../div[1]/div")))   
        driver.find_element_by_xpath("//li/div[2]/h4[.='"+lessonname+"']/../../div[1]/div").click()   
        time.sleep(6)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[4]/div/div/div[2]/div[3]/button[1]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,"html/body/div[4]/div/div/div[2]/div[3]/button[1]")))
        driver.find_element_by_xpath("html/body/div[4]/div/div/div[2]/div[3]/button[1]").click()   
        wait.until(EC.visibility_of_element_located((By.XPATH,"//table/tbody/tr/td[.='"+lessonname+"']/a"))) 
        searchinList =driver.find_element_by_xpath("//table/tbody/tr/td[.='"+lessonname+"']/a").text          
        if searchinList==lessonname:
            print "selected lesson is in the list"
        else:
            print "selected lesson is not in the list"
            raise Exception           
                   
                                        
        
    def addTrack(self,Trackname):  
        
        wait=WebDriverWait(driver, 80)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[1]/div/div[3]/div[2]/div/ul/li[2]/a")))
        driver.find_element_by_xpath("html/body/div[1]/div/div[3]/div[2]/div/ul/li[2]/a").click()
        time.sleep(4)   
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[1]/div/div[3]/div[2]/div/div[2]/button")))
        driver.find_element_by_xpath("html/body/div[1]/div/div[3]/div[2]/div/div[2]/button").click()
        wait.until(EC.visibility_of_element_located((By.ID,"search-objectives-in-modal")))
        SearchElement =driver.find_element_by_id("search-objectives-in-modal")
        SearchElement.send_keys(Trackname)
        SearchElement.send_keys(Keys.ENTER) 
        wait.until(EC.visibility_of_element_located((By.XPATH,"(html/body/div[4]/div/div/div[2]/div[2]/div/ul/li[1]/div[2]/h4[.='"+Trackname+"']/../../div[1])[1]")))
        driver.find_element_by_xpath("(html/body/div[4]/div/div/div[2]/div[2]/div/ul/li[1]/div[2]/h4[.='"+Trackname+"']/../../div[1])[1]").click()  
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[4]/div/div/div[2]/div[3]/button[1]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,"html/body/div[4]/div/div/div[2]/div[3]/button[1]")))
        driver.find_element_by_xpath("html/body/div[4]/div/div/div[2]/div[3]/button[1]").click()   
        
        wait.until(EC.element_to_be_clickable((By.XPATH,"//table/tbody/tr/td[.='"+Trackname+"']/a")))
        searchinList =driver.find_element_by_xpath("//table/tbody/tr/td[.='"+Trackname+"']/a").text          
        if searchinList==Trackname:
            print "selected Track is in the list"
        else:
            print "selected Track is not in the list"
            raise Exception           
        driver.find_element_by_xpath("html/body/div[1]/div/div[3]/div[2]/div/div[1]/a").click()   
        
    def library(self,TagName): 
        wait=WebDriverWait(driver, 80)  
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[1]/div/div[3]/div[1]/div/nav/div/div[2]/div[2]"))) 
        driver.find_element_by_xpath("html/body/div[1]/div/div[3]/div[1]/div/nav/div/div[2]/div[2]").click()
        time.sleep(4)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[1]/div/div[3]/div[2]/div/div/div[1]/div/header/h1")))
        if driver.find_element_by_xpath("html/body/div[1]/div/div[3]/div[2]/div/div/div[2]/div/div/h2"):
            print("Filter By Tag is Displayed,")
        else:
            print "Filter By Tag is not displayed,"
            raise Exception
        if driver.find_element_by_xpath("//ul/li/button[.='"+TagName+"']").is_displayed():
            print("Created Tag is found in Libarray Page")
        else:
            print "Created Tag is not found in Libarray Page,"
            raise Exception
        driver.find_element_by_xpath("//ul/li/button[.='"+TagName+"']").click()
        
    def trackLibray(self,TrackName): 
        wait=WebDriverWait(driver, 80)  
        driver.refresh()
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[1]/div/div[3]/div[2]/div/div/div[3]/div/h2"))) 
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[1]/div/div[3]/div[2]/div/div/div[3]/div/ul/li[1]")))
        driver.find_element_by_xpath("html/body/div[1]/div/div[3]/div[2]/div/div/div[3]/div/ul/li[1]").click()
        wait.until(EC.visibility_of_element_located((By.XPATH,"//div/a/div[2]/span[contains(.,'"+TrackName+"')]")))
        trk=driver.find_element_by_xpath("//div/a/div[2]/span[contains(.,'"+TrackName+"')]")
        webdriver.ActionChains(driver).move_to_element(trk).perform()
        Name = trk.text
        NameTrack =Name.strip()
        
        time.sleep(3)
        if TrackName == NameTrack:
            print("Track Verified")
        else:
            print "Track is not Verified"
            raise Exception
        
    def lessonLibrary(self,lessonName):   
        wait=WebDriverWait(driver, 80)  
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[1]/div/div[3]/div[2]/div/div/div[3]/div/h2"))) 
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[1]/div/div[3]/div[2]/div/div/div[3]/div/ul/li[2]")))
        driver.find_element_by_xpath("html/body/div[1]/div/div[3]/div[2]/div/div/div[3]/div/ul/li[2]").click()
        wait.until(EC.visibility_of_element_located((By.XPATH,"//div/a/div[2]/span[contains(.,'"+lessonName+"')]")))
        lsn=driver.find_element_by_xpath("//div/a/div[2]/span[contains(.,'"+lessonName+"')]")
        webdriver.ActionChains(driver).move_to_element(lsn).perform()
        Name = lsn.text
        NameLesson =Name.strip()
        
        time.sleep(3)
        if lessonName == NameLesson:
            print("Lesson Verified")
        else:
            print "Lesson is not Verified"
            raise Exception
        
        
        
        
        
        