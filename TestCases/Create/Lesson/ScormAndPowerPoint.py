'''
Created on Mar 8, 2018

@author: Shavinlal E
'''
from os.path import os
import traceback

from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait,expected_conditions as EC
import xlrd
from BaseTestClass import BaseTestClass
from BaseTestClass import WebDriverWait
from BaseTestClass import driver
from BaseTestClass import projectPath

# create a new Firefox session
class ScormAndPowerPoint:
    
    
    def uploadscormAndPowerpoint(self):   
        
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@href='/create/lessons']")))

        print "Clicking on Lessons button from side menu"
        driver.find_element_by_xpath("//a[@href='/create/lessons']").click()
    
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/header/div/button")))  
        print "Clicking on Create Lesson button from lessons page"
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[2]/div/header/div/button").click()
        
        # wait for Power Point icon
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div/div/div[2]/div[7]/div/div/div/span[2]")))
        
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        first_sheet = book.sheet_by_name('MultiCardLesson')
        
        cell1 = first_sheet.cell(56,0)
        ScormOrImageFilePath = cell1.value
  
        print "Going to upload the SCORM or POWER POINT file"
        
        driver.find_element_by_css_selector('input[type="file"]').send_keys(ScormOrImageFilePath)
        
        wait=WebDriverWait(driver, 600)
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[1]/a")))
        
        print "Successfully uploaded the SCORM or POWER POINT file"
        
        
        print "Going to verify the title of Uploaded SCORM or POWER POINT file"
        global actual_titleof_scormlesson
        actual_titleof_scormlesson = driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/h1/textarea").text
        
        cell2 = first_sheet.cell(57,0)
        
        expected_titleof_scormlesson = cell2.value
        
        if(expected_titleof_scormlesson == actual_titleof_scormlesson):
            
            print "Successfully verified the title of Uploaded Scorm or Powerpoint lesson"
            
        
        else:
            
            print "Failed to verify the title of Uploaded Scorm or Powerpoint lesson"
            raise Exception
        

        
    def publishLesson(self): 
        
        
        print "Going to publish the lesson"
        
        wait=WebDriverWait(driver, 60)
        #wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saving...']")))
        #wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saved']"))) 
      
        wait.until(EC.element_to_be_clickable((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/button")))
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/button").click()
        print "Clicking on READY TO PUBLISH button"
         
        
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div/div[1]/section[3]/div/button[1]")))
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div/div[1]/section[3]/div/button[1]").click()
        print "Clicking on PUBLISH button"
        
        '''print "Validating the success message after publish"
        wait=WebDriverWait(driver, 60) 
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[2]/div/div/span[2]"))) 
        actual_success_message= driver.find_element_by_xpath(".//*[@id='content']/div/div/div[2]/div/div/span[2]").text
        expected_success_message= "You have successfully published \"" + actual_titleof_scormlesson + "\""; 
        
        
        if(expected_success_message==actual_success_message):
            
            print "The success message is displaying as"+ " "+expected_success_message
            
        else:
            
            print "The success message is not displaying as expected"
           '''
            
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[1]/a").click()
        print "Clicking on EXIT button"
        
             
        print "Verifying lesson displayed in Grid"
        wait.until(EC.visibility_of_element_located((By.XPATH,"(//tbody/tr/td[2]/a[.='"+actual_titleof_scormlesson+"'])[1]")))

        if driver.find_element_by_xpath("(//tbody/tr/td[2]/a[.='"+actual_titleof_scormlesson+"'])[1]").is_displayed():
            
            print "Lesson is displayed in Grid ::"+actual_titleof_scormlesson
            
        else:
            print "Lesson not displaying in grid"
       
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[1]/div/nav/div/div[4]").click()    
        
        
    
    def uploadscormAndPowerpointMain(self): 
        
        try: 
            obj1 = ScormAndPowerPoint()
            obj1.uploadscormAndPowerpoint()
            obj1.publishLesson()
        except Exception as e:
            traceback.print_exc()
            print (e)
            raise Exception
      
        finally:    
            
            book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
            first_sheet = book.sheet_by_name('Login_Credentials')
            #print("Fetching the Attribute Name from Excel Sheet\n")
            
            # read a cell
            cell = first_sheet.cell(1,1)
            HomeURL = cell.value
            #print HomeURL
            driver.get(HomeURL)
            #print "Home Page Loaded"


if __name__ == '__main__':
    
    obj11= ScormAndPowerPoint()
    obj12= BaseTestClass()
    obj12.UserLogin()
    obj11.uploadscormAndPowerpointMain()
  
    print "Test executed successfully"
           
        
        
        
        
        
        
        
        
   
        