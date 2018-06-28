'''
Created on 26-Feb-2018

@author: Sheethu C
'''
import os.path
import time
import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xlrd
from BaseTestClass import driver
from DeleteLesson import DeleteLesson
from BaseTestClass import projectPath
class TagTrackWiththreelessons_Three_Four_Five():
    
    
    def taglessonWithVideo(self,lessonName,videoPath,timeToUploadVideo):
        
        wait=WebDriverWait(driver, timeToUploadVideo)
        driver.refresh()
        wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@href='/create/lessons']")))
        
        print "Clicking on Lessons button from side menu"
        driver.find_element_by_xpath("//a[@href='/create/lessons']").click()
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/header/div/button")))
     
        print "Click on Create lesson button"
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[2]/div/header/div/button").click()
        
        print "Verifying Create new lesson tab is displayed"
        
        #assert "Create a new lesson"==driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/h3").text
        if driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/h3").text == "Create a new lesson":
            print("Create a new lesson tab is displayed")
        else:
            print ""
            raise Exception
        
        # self.assertEqual("Create a new lesson", driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/h3").text)

        
               
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div/div/div[2]/div[2]/div")))

        
        print "Clicked on Blank lesson"
        driver.find_element_by_xpath("html/body/div[2]/div/div/div[2]/div[2]/div").click()
        
        print "Creating New lesson With one Video card"
        
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/h1/textarea")))

        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/h1/textarea").send_keys(lessonName)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saving...']")))
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saved']")))
        
        print "Entered lesson name ::"+lessonName
        
        print "Click on (+) icon"
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div/span").click()
        
        #Clicking on Video card
        driver.find_element_by_xpath("html/body/div/div/div/div[3]/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[1]").click()
        
        #Uploading Video
        print "Uploading Video"
        driver.find_element_by_css_selector('input[type="file"]').send_keys(videoPath)
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[1]/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div[1]/button")))
        
        videoContainerlocator_afterupload= driver.find_element_by_xpath("html/body/div[1]/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div[1]/button")
        
        if(videoContainerlocator_afterupload.is_displayed()):
            
            print "Successfully uploaded the Video file"
            
        else:
            print "Failed to upload the Video file"
            raise Exception
        
        time.sleep(4)
        print "Publishing lesson"
        
        publishButton=wait.until(EC.element_to_be_clickable((By.XPATH,"html/body/div/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/button")))

        publishButton.click()

        wait.until(EC.element_to_be_clickable((By.XPATH,"html/body/div/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div/div[1]/section[3]/div/button[1]")))

        driver.find_element_by_xpath("html/body/div/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div/div[1]/section[3]/div/button[1]").click()
        print "Clicked on publish button"
        
        
       

        print "Lesson published"
        
        
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[1]/a").click()

        
        #Verifying created lesson is displayed in list
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"(//tbody/tr/td[2]/a[.='"+lessonName+"'])[1]")))

        if driver.find_element_by_xpath("(//tbody/tr/td[2]/a[.='"+lessonName+"'])[1]").is_displayed():
            
            print "Lesson is displayed in Grid ::"+lessonName
            
        else:
            print "Lesson not displaying in grid"
            raise Exception
        
        
            
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[1]/div/nav/div/div[4]").click()
       
        
    def taglessonWithDocument(self,lessonname,documentPath,timeToUploaddocument):
        print "This is lesson with document"
        
        wait=WebDriverWait(driver, timeToUploaddocument)
        driver.refresh()
        wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@href='/create/lessons']")))
        
        print "Clicking on Lessons button from side menu"
        driver.find_element_by_xpath("//a[@href='/create/lessons']").click()
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/header/div/button")))
     
        print "Click on Create lesson button"
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[2]/div/header/div/button").click()
        
        print "Verifying Create new lesson tab is displayed"
        
        #assert "Create a new lesson"==driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/h3").text
        if driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/h3").text == "Create a new lesson":
            print("Create a new lesson tab is displayed")
        else:
            print ""
            raise Exception
        
        # self.assertEqual("Create a new lesson", driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/h3").text)

        
               
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div/div/div[2]/div[2]/div")))

        
        print "Clicked on Blank lesson"
        driver.find_element_by_xpath("html/body/div[2]/div/div/div[2]/div[2]/div").click()
        
        print "Creating New lesson With one Text card"
        
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/h1/textarea")))

        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/h1/textarea").send_keys(lessonname)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saving...']")))
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saved']")))
        
        print "Entered lesson name ::"+lessonname
        
        print "Click on (+) icon"
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div/span").click()
        
        #Clicking on Document card
        driver.find_element_by_xpath("html/body/div/div/div/div[3]/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[4]/div[1]/div").click()
        
        time.sleep(6)
        
        #Uploading Document
        print "Uploading Document"
        driver.find_element_by_css_selector('input[type="file"]').send_keys(documentPath)
        
        
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[2]/div/div/div[1]/div/a")))
        
        documentContainerlocator_afterupload= driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[2]/div/div/div[1]/div/a")
        
        if(documentContainerlocator_afterupload.is_displayed()):
            
            print "Successfully uploaded the Document file"
            
        else:
            print "Failed to upload the Document file"
            raise Exception
        
        
        
        print "Publishing lesson"
        
        time.sleep(4)
        
        publishButton=wait.until(EC.element_to_be_clickable((By.XPATH,"html/body/div/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/button")))

        publishButton.click()

        wait.until(EC.element_to_be_clickable((By.XPATH,"html/body/div/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div/div[1]/section[3]/div/button[1]")))

        driver.find_element_by_xpath("html/body/div/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div/div[1]/section[3]/div/button[1]").click()
        print "Clicked on publish button"
        
        
        

        print "Lesson published"
        
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[1]/a").click()
        
        #Verifying created lesson is displayed in list
        
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"(//tbody/tr/td[2]/a[.='"+lessonname+"'])[1]")))

        if driver.find_element_by_xpath("(//tbody/tr/td[2]/a[.='"+lessonname+"'])[1]").is_displayed():
            
            print "Lesson is displayed in Grid ::"+lessonname
            
        else:
            print "Lesson not displaying in grid"
            raise Exception
        
        
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[1]/div/nav/div/div[4]").click()  



    def taglessonWithQuestion(self,lessonNameforQuescard,questionCard,ans1,ans2):
        wait=WebDriverWait(driver, 60)
        driver.refresh()
        wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@href='/create/lessons']")))

        print "Clicking on Lessons button from side menu"
        driver.find_element_by_xpath("//a[@href='/create/lessons']").click()
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/header/div/button")))
     
        print "Click on Create lesson button"
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[2]/div/header/div/button").click()
        
        print "Verifying Create new lesson tab is displayed"
        
        #assert "Create a new lesson"==driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/h3").text
        if driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/h3").text == "Create a new lesson":
            print("Create a new lesson tab is displayed")
        else:
            print ""
            raise Exception
        
        # self.assertEqual("Create a new lesson", driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/h3").text)

        
               
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div/div/div[2]/div[2]/div")))

        
        
        print "Clicked on Blank lesson"
        driver.find_element_by_xpath("html/body/div[2]/div/div/div[2]/div[2]/div").click()
        
        print "Creating New lesson With one question card"
        
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/h1/textarea")))

        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/h1/textarea").send_keys(lessonNameforQuescard)
        
        print "Entered lesson name ::"+lessonNameforQuescard
        
        print "Click on (+) icon"
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div/span").click()
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[5]/div[1]/div").click()
        
        print "Question card selected"
        
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='question-answer-input-0']")))
        print "Entering question"
        questionArea=driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/p/textarea")
        questionArea.send_keys(questionCard)
        print "Question entered ::"
        
        print "Entering first answer"
        driver.find_element_by_xpath(".//*[@id='question-answer-input-0']").send_keys(ans1)
        print "First Answer entered "
        print "Entering Second answer"
        driver.find_element_by_xpath(".//*[@id='question-answer-input-1']").send_keys(ans2)
        print "Second Answer entered "
        
        

         
        
        print "\nVerifying All the data entered is displaying in fields"
        
        if questionArea.text==questionCard:
            print "Question ::"+questionCard
        else:
            print "Question is not displayed"
            raise Exception
        
        
        if driver.find_element_by_xpath(".//*[@id='question-answer-input-0']").text==ans1:
            print "Answer 1 ::"+ans1
        else:
            print "Answer 1 is not displayed"
            raise Exception
        
        if driver.find_element_by_xpath(".//*[@id='question-answer-input-1']").text==ans2:
            print "Answer 2 ::"+ans2
        else:
            print "Answer 2 is not displayed"
            raise Exception
      
        #Verifying Correct answer displayed
        print "\nVerifying by default correct answer selected as A"
        
        if driver.find_element_by_xpath("//input[@id='question-answer-correct-0']").is_selected():
            print "Verified Radio button for Correct answer A is selected"
        else:
            print "Radio button is not selected"
            raise Exception
        

        time.sleep(2)
        
        publishButton=wait.until(EC.element_to_be_clickable((By.XPATH,"html/body/div/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/button")))

        publishButton.click()

        wait.until(EC.element_to_be_clickable((By.XPATH,"html/body/div/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div/div[1]/section[3]/div/button[1]")))

        driver.find_element_by_xpath("html/body/div/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div/div[1]/section[3]/div/button[1]").click()
        print "Clicked on publish button"
        

        print "Lesson published"
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[1]/a").click()
        
        
        print "\nVerifying lesson displayed in Grid"
        wait.until(EC.visibility_of_element_located((By.XPATH,"(//tbody/tr/td[2]/a[.='"+lessonNameforQuescard+"'])[1]")))

        if driver.find_element_by_xpath("(//tbody/tr/td[2]/a[.='"+lessonNameforQuescard+"'])[1]").is_displayed():
            
            print "Lesson is displayed in Grid ::"+lessonNameforQuescard
            
        else:
            print "Lesson not displaying in grid"
            raise Exception
        
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[1]/div/nav/div/div[4]").click()
        
     
    def tagcreateTrackwithVidDocAndQuesLesson(self,titleOfTrack,Imagefilepath,description,tagName,lessonNameforVidcard,lessonNameforDoccard,lessonNameforQuescard,expectedSuccessText):
        print "\nCreating track with one lesson contains Text Card"
        driver.refresh()
        wait=WebDriverWait(driver, 120)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@href='/create/lessons']")))
        
        print "Clicking on Lessons button from side menu"
        driver.find_element_by_xpath("//a[@href='/create/lessons']").click()
        
        print "Clicking on Track button from side menu"
        wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@href='/create/tracks']")))
        driver.find_element_by_xpath("//a[@href='/create/tracks']").click()
        
        createTrackbutton=wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/header/div/a")))
        
        createTrackbutton.click()
        
        print "Entering title"
        titlefield=wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='title']")))
        titlefield.send_keys(titleOfTrack)
        print "Title entered ::"+titleOfTrack
        
        driver.find_element_by_css_selector('input[type="file"]').send_keys(Imagefilepath)
        print "waiting to upload image"
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/div/div[2]/div[1]/div[2]/div/div/div/div/div[1]/img")))
        print "Image uploaded"
        
        print "Entering Description"
        driver.find_element_by_xpath(".//*[@id='description']").send_keys(description)
        print "Description entered ::"+description 
        
        
        print "Adding tag"
        addTags=driver.find_element_by_xpath("//div[@class='Select-placeholder']")
        webdriver.ActionChains(driver).move_to_element(addTags).click().send_keys(tagName).perform()
        
        option=wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='react-select-2--option-0']")))
        webdriver.ActionChains(driver).move_to_element(option).click(option).perform()
        
        driver.find_element_by_xpath(".//*[@id='description']").send_keys(" ")
        
        
        print "\nAdding created two lessons"
        
        print "Clicking on Add lessons button"
       
        driver.execute_script("window.scrollTo(0, 0);")
        addlessonbutton=driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div/button")
        addlessonbutton.click()
        
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div/div/div[2]/div[2]/div/ul/li[1]/div[1]/div")))
        
        print "Searching for first lesson in Add lessons pop up"
        driver.find_element_by_xpath(".//*[@id='search-lessons-in-modal']").send_keys(lessonNameforVidcard)
        searchedLesson=wait.until(EC.visibility_of_element_located((By.XPATH,"//li/div[2]/h4[.='"+lessonNameforVidcard+"']/../../div[1]/div")))
        searchedLesson.click()
        print "Lesson '"+lessonNameforVidcard+"' selected"
        
        
        print "Searching for Second lesson in Add lessons pop up"
        driver.find_element_by_xpath(".//*[@id='search-lessons-in-modal']").clear()
        driver.find_element_by_xpath(".//*[@id='search-lessons-in-modal']").send_keys(lessonNameforDoccard)
        searchedLesson=wait.until(EC.visibility_of_element_located((By.XPATH,"//li/div[2]/h4[.='"+lessonNameforDoccard+"']/../../div[1]/div")))
        searchedLesson.click()
        print "Lesson '"+lessonNameforDoccard+"' selected"
        
        
        print "Searching for Third lesson in Add lessons pop up"
        driver.find_element_by_xpath(".//*[@id='search-lessons-in-modal']").clear()
        driver.find_element_by_xpath(".//*[@id='search-lessons-in-modal']").send_keys(lessonNameforQuescard)
        searchedLesson=wait.until(EC.visibility_of_element_located((By.XPATH,"//li/div[2]/h4[.='"+lessonNameforQuescard+"']/../../div[1]/div")))
        searchedLesson.click()
        print "Lesson '"+lessonNameforQuescard+"' selected"
        
        
        
     
        print "Adding to Track"
        driver.find_element_by_xpath("html/body/div[2]/div/div/div[2]/div[3]/button[1]").click()
        
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/div/div[2]/div[2]/div[1]/div/ul/li/div[2]/div/h4/div")))
        
        print "\nChecking added lesson is selected lesson from Pop up"
        
        
        lessonTextAddedToGrid=driver.find_element_by_xpath("//li[1]/div[2]/div/h4/div").text
        if lessonTextAddedToGrid==lessonNameforVidcard:
            print "Selected Lesson '"+lessonNameforVidcard+"' is displayed in grid of tracks page"
        
        else:
            print "Lesson is not displayed"
            raise Exception
        
        lessonTextAddedToGrid1=driver.find_element_by_xpath("//li[2]/div[2]/div/h4/div").text
        if lessonTextAddedToGrid1==lessonNameforDoccard:
            print "Selected Lesson '"+lessonNameforDoccard+"' is displayed in grid of tracks page"
        
        else:
            print "Lesson is not displayed"
            raise Exception
        
        lessonTextAddedToGrid2=driver.find_element_by_xpath("//li[3]/div[2]/div/h4/div").text
        if lessonTextAddedToGrid2==lessonNameforQuescard:
            print "Selected Lesson '"+lessonNameforQuescard+"' is displayed in grid of tracks page"
        
        else:
            print "Lesson is not displayed"
            raise Exception
        
        
        #Publishing Track
        print "Clicking on Publish Track button"
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[2]/div/div/div[2]/div[2]/div[3]/button").click()
        time.sleep(2)
        
        
        print "\nVerifying Creates track '"+titleOfTrack+"' is displayed in Tracks grid"
        
        
      
        
        driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/div/div[1]/a").click()
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"(//tbody/tr/td[2]/a[.='"+titleOfTrack+"'])[1]")))
        
        trackInGrid=driver.find_element_by_xpath("(//tbody/tr/td[2]/a[.='"+titleOfTrack+"'])[1]").text
        
        if trackInGrid==titleOfTrack:
            print "Track '"+trackInGrid+"' is displayed in grid"
        else:
            print "Track is not displayed in grid"
            raise Exception
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[1]/div/nav/div/div[4]").click()
    
    
    
    def createTrackWiththreelessons_Three_Four_Five_Tag(self,TagName,ExpectedSuccessMessage,ExpectedAddLessonMessage,lessonNameforVidcard,lessonNameforDoccard,lessonNameforQuescard,TrackName,ExpectedTrackMessage):
        wait=WebDriverWait(driver, 80)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/a")))
        driver.find_element_by_xpath("html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/a").click()
        print "Clicked on admin icon"
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]")))
        driver.find_element_by_xpath("html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]").click()
        print "Clicked on Admin"
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/div/ul/li[5]")))
        driver.find_element_by_xpath("html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/div/ul/li[5]").click()
        print "Clicked on Tag"
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[2]/div/header/h1")))
        print "Tag Page Loaded"
        driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/header/div/div/button").click()
        print "Clicked on Create Tag Button"
        wait.until(EC.visibility_of_element_located((By.ID,"add-tag-input")))
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
        time.sleep(3)
        button=wait.until(EC.element_to_be_clickable((By.XPATH,"html/body/div/div/div[3]/div[2]/div/div/section[1]/div[1]/div/div[2]/button[1]")))
        button.click()
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[2]/div/div/section[1]/div[1]/div")))
        ActualMessage = driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/div/section[1]/div[1]/div").text
        print "Actual message "+ActualMessage
        time.sleep(3)
        
        print "Searching for the created Tag"
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[2]/div/div/section[1]/div[2]/div/div/input")))
        time.sleep(6)
      
        element =driver.find_element_by_name("tag-index-search")
        element.send_keys(TagName)
        driver.find_element_by_name("tag-index-search").send_keys(Keys.ENTER)
        time.sleep(6)
        print "Entered Tag Name for Search"
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[2]/div/div/section[2]/div/ul/li[1]")))
        print "Verifying the created Tag in the list"
        ele =driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/div/section[2]/div/ul/li[1]")
        print ele.text
        time.sleep(4)
        if driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/div/section[2]/div/ul/li[1]").is_displayed():
            print("Created Tag in the list")
        else:
            print ""
            raise Exception
        print "Clicking on "+TagName
        driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/div/section[2]/div/ul/li[1]").click()
        time.sleep(4)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[2]/div/ul/li[1]/a")))
        print "Verifying the "+TagName+"Page"
        ExpectedPageName =driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/header/h1").text
        time.sleep(4)
        if ExpectedPageName in TagName:
            print("Verified the "+TagName+"Page")
        else:
            print TagName+"Page is not displayed"
            raise Exception
        
        print "Clicking on Lesson tab"
        driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/ul/li[1]/a").click()
        time.sleep(2)
        print "clicking on Tag lessons"
        driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/div[2]/button").click()
        wait.until(EC.visibility_of_element_located((By.ID,"search-lessons-in-modal")))
        SearchElement =driver.find_element_by_id("search-lessons-in-modal")
        SearchElement.send_keys(lessonNameforVidcard)
        SearchElement.send_keys(Keys.ENTER)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//li/div[2]/h4[.='"+lessonNameforVidcard+"']/../../div[1]/div")))
        time.sleep(4)
        driver.find_element_by_xpath("//li/div[2]/h4[.='"+lessonNameforVidcard+"']/../../div[1]/div").click()
        time.sleep(6)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div/div/div[2]/div[3]/button[1]")))
        driver.find_element_by_xpath("html/body/div[2]/div/div/div[2]/div[3]/button[1]").click()
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[2]/div/div")))
        ActualAddLessonMessage =driver.find_element_by_xpath("html/body/div/div/div[2]/div/div").text
        print "ActualAddedMessage :" +ActualAddLessonMessage
        
        if ActualAddLessonMessage in ExpectedAddLessonMessage:
            print("Expected Success Message and Actual Success Message is Matching,Success Message Verified")
        else:
            print "Success message is not displayed"
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"//tbody/tr/td[1]/a[.='"+lessonNameforVidcard+"']")))
        
        print "Clicking on Lesson tab"
        driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/ul/li[1]/a").click()
        time.sleep(2)
        
        print "clicking on Tag lessons"
        driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/div[2]/button").click()
        wait.until(EC.visibility_of_element_located((By.ID,"search-lessons-in-modal")))
        SearchElement =driver.find_element_by_id("search-lessons-in-modal")
        SearchElement.send_keys(lessonNameforDoccard)
        SearchElement.send_keys(Keys.ENTER)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//li/div[2]/h4[.='"+lessonNameforDoccard+"']/../../div[1]/div")))
        time.sleep(4)
        driver.find_element_by_xpath("//li/div[2]/h4[.='"+lessonNameforDoccard+"']/../../div[1]/div").click()
        time.sleep(6)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div/div/div[2]/div[3]/button[1]")))
        driver.find_element_by_xpath("html/body/div[2]/div/div/div[2]/div[3]/button[1]").click()
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[2]/div/div")))
        ActualAddLessonMessage1 =driver.find_element_by_xpath("html/body/div/div/div[2]/div/div").text
        print "ActualAddedMessage1 :" +ActualAddLessonMessage1
        
        if ActualAddLessonMessage1 in ExpectedAddLessonMessage:
            print("Expected Success Message and Actual Success Message is Matching,Success Message Verified")
        else:
            print "Success message is not displayed"
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"//tbody/tr/td[1]/a[.='"+lessonNameforDoccard+"']")))
        
        print "Clicking on Lesson tab"
        driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/ul/li[1]/a").click()
        time.sleep(2)
        
        print "clicking on Tag lessons"
        driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/div[2]/button").click()
        wait.until(EC.visibility_of_element_located((By.ID,"search-lessons-in-modal")))
        SearchElement =driver.find_element_by_id("search-lessons-in-modal")
        SearchElement.send_keys(lessonNameforQuescard)
        SearchElement.send_keys(Keys.ENTER)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//li/div[2]/h4[.='"+lessonNameforQuescard+"']/../../div[1]/div")))
        time.sleep(4)
        driver.find_element_by_xpath("//li/div[2]/h4[.='"+lessonNameforQuescard+"']/../../div[1]/div").click()
        time.sleep(6)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div/div/div[2]/div[3]/button[1]")))
        driver.find_element_by_xpath("html/body/div[2]/div/div/div[2]/div[3]/button[1]").click()
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[2]/div/div")))
        ActualAddLessonMessage1 =driver.find_element_by_xpath("html/body/div/div/div[2]/div/div").text
        print "ActualAddedMessage1 :" +ActualAddLessonMessage1
        
        if ActualAddLessonMessage1 in ExpectedAddLessonMessage:
            print("Expected Success Message and Actual Success Message is Matching,Success Message Verified")
        else:
            print "Success message is not displayed"
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"//tbody/tr/td[1]/a[.='"+lessonNameforQuescard+"']")))
        print "Clicking on Track Tab"
        driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/ul/li[2]/a").click()
        time.sleep(2)
        
        
        
        print "clicking on Tag Tracks"
        driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/div[2]/button").click()
        wait.until(EC.visibility_of_element_located((By.ID,"search-objectives-in-modal")))
        SearchElement =driver.find_element_by_id("search-objectives-in-modal")
        SearchElement.send_keys(TrackName)
        SearchElement.send_keys(Keys.ENTER)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div/div/div[2]/div[2]/div/ul/li[1]/div[1]")))
        time.sleep(4)
        driver.find_element_by_xpath("html/body/div[2]/div/div/div[2]/div[2]/div/ul/li[1]/div[1]").click()
        time.sleep(6)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div/div/div[2]/div[3]/button[1]")))
        driver.find_element_by_xpath("html/body/div[2]/div/div/div[2]/div[3]/button[1]").click()
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[2]/div/div")))
        ActualAddTrackMessage =driver.find_element_by_xpath("html/body/div/div/div[2]/div/div").text
        print "ActualAddTrackMessage :" +ActualAddTrackMessage
        print "ExpectedTrackMessage :" +ExpectedTrackMessage
        if ActualAddTrackMessage in ExpectedTrackMessage:
            print("Expected Success Message and Actual Success Message is Matching,Success Message Verified")
        else:
            print "Success message is not displayed"
            raise Exception
        wait.until(EC.visibility_of_element_located((By.XPATH,"//tbody/tr/td[1]/a[.='"+TrackName+"']")))
        #wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[2]/div/header/h1")))
        print "Clicking on Tracks"
        driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/ul/li[2]/a").click()
        time.sleep(4)
        AddedTrackname =driver.find_element_by_xpath("//tbody/tr/td[1]/a[.='"+TrackName+"']").text
        print "Verifying addede Track in the List"
        if AddedTrackname in TrackName:
            print("Added Track in the List,")
        else:
            print "Added Track is not in the List,"
            raise Exception
        
    def  searchInLibraryTrackWithTwoLessons_Three_Four_Five(self,lessonNameforVidcard,lessonNameforDoccard,lessonNameforQuescard,TrackName,TagName): 
         
        wait=WebDriverWait(driver, 80)
        
       
        print "Clicking On Library"
        driver.find_element_by_xpath("html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[2]").click()
        time.sleep(10)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[2]/div/div/div[1]/div/header/h1")))
        print "Library page Loaded"
        print "verifying Filter By tag"
        if driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/div/div[2]/div/div/h2"):
            print("Filter By Tag is Displayed,")
        else:
            print "Filter By Tag is not displayed,"
            raise Exception
        print "Searching for the Created Tag"
        if driver.find_element_by_xpath("//ul/li/button[.='"+TagName+"']").is_displayed():
            print("Created Tag is found in Libarray Page")
        else:
            print "Created Tag is not found in Libarray Page,"
            raise Exception
        
        driver.find_element_by_xpath("//ul/li/button[.='"+TagName+"']").click()
        print "Clicked on The Tag"
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[2]/div/div/div[3]/div/ul/li[1]")))
        time.sleep(4)
        print "Clicked on Lessons Tab"
        #driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/div/div[3]/div/ul/li[1]").click()
        time.sleep(3)
        elem =driver.find_element_by_xpath("//div/a/div[2]/span[contains(.,'"+lessonNameforVidcard+"')]")
        driver.execute_script("arguments[0].scrollIntoView()", elem)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//div/a/div[2]/span[contains(.,'"+lessonNameforVidcard+"')]")))
        Name =driver.find_element_by_xpath("//div/a/div[2]/span[contains(.,'"+lessonNameforVidcard+"')]").text
        NameLesson =Name.strip()
        print NameLesson
        print lessonNameforVidcard
        time.sleep(3)
        if lessonNameforVidcard == NameLesson:
            print("first Lesson Verified")
        else:
            print "first Lesson is not Verified"
            raise Exception
        
        
        print "Clicked on Lessons Tab"
        driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/div/div[3]/div/ul/li[1]").click()
        time.sleep(3)
        elem =driver.find_element_by_xpath("//div/a/div[2]/span[contains(.,'"+lessonNameforDoccard+"')]")
        driver.execute_script("arguments[0].scrollIntoView()", elem)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//div/a/div[2]/span[contains(.,'"+lessonNameforDoccard+"')]")))
        Name2 =driver.find_element_by_xpath("//div/a/div[2]/span[contains(.,'"+lessonNameforDoccard+"')]").text
        NameLesson2 =Name2.strip()
        print NameLesson2
        print lessonNameforDoccard
        time.sleep(3)
        if lessonNameforDoccard == NameLesson2:
            print("second Lesson Verified")
        else:
            print "second Lesson is not Verified"
            raise Exception
        
        print "Clicked on Lessons Tab"
        driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/div/div[3]/div/ul/li[1]").click()
        time.sleep(3)
        elem =driver.find_element_by_xpath("//div/a/div[2]/span[contains(.,'"+lessonNameforQuescard+"')]")
        driver.execute_script("arguments[0].scrollIntoView()", elem)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//div/a/div[2]/span[contains(.,'"+lessonNameforQuescard+"')]")))
        Name2 =driver.find_element_by_xpath("//div/a/div[2]/span[contains(.,'"+lessonNameforQuescard+"')]").text
        NameLesson2 =Name2.strip()
        print NameLesson2
        print lessonNameforQuescard
        time.sleep(3)
        if lessonNameforQuescard == NameLesson2:
            print("Third Lesson Verified")
        else:
            print "Third Lesson is not Verified"
            raise Exception
        
        print "Clicking On Track Tab"
        driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/div/div[3]/div/ul/li[2]").click()
        time.sleep(3)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[2]/div/div/div[4]/div/div/div[1]/a/div[1]")))
        Track = driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/div/div[4]/div/div/div[1]/a/div[2]/span[1]").text
        NameTrack =Track.strip()
        if TrackName == NameTrack:
            print("Track Verified")
        else:
            print "Track is not Verified"
            
            
            
    def tagtrackWithTwoLessonsVidDocQues(self):
        
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        first_sheet = book.sheet_by_name('TagTrackLesson')
        
        #Track Data
        cell1 = first_sheet.cell(88,1)
        titleOfTrack = cell1.value
        cell1 = first_sheet.cell(88,1)
        TrackName = cell1.value
        
        
        cell2 = first_sheet.cell(89,1)
        Imagefilepath = cell2.value
        
        cell2 = first_sheet.cell(90,1)
        description = cell2.value
        
        cell2 = first_sheet.cell(91,1)
        tagName = cell2.value
        
      
        cell2 = first_sheet.cell(92,1)
        expectedSuccessText= cell2.value
        
        # Lesson Data
        
        cell2 = first_sheet.cell(88,3)
        lessonNameforVidcard= cell2.value
        
        cell2 = first_sheet.cell(89,3)
        videoPath = cell2.value
        
        cell2 = first_sheet.cell(90,3)
        timeToUploadVideo = cell2.value
        
        cell2 = first_sheet.cell(92,3)
        lessonNameforDoccard = cell2.value
        
        cell2 = first_sheet.cell(93,3)
        documentPath= cell2.value
        
        cell2 = first_sheet.cell(94,3)
        timeToUploaddocument = cell2.value
        
        cell2 = first_sheet.cell(96,3)
        lessonNameforQuescard = cell2.value
        
        cell2 = first_sheet.cell(97,3)
        questionCard = cell2.value
        
        cell3 = first_sheet.cell(98,3)
        ans1 = cell3.value
        
        cell4 = first_sheet.cell(99,3)
        ans2 = cell4.value
     
       
        
        print "\n\nSetting Pre-requisite"
        print "Creating Two lessons\n"
     
     
     
        first_sheet = book.sheet_by_name('AssignCreateTag')
      
        cell = first_sheet.cell(13,2)
        TagName = cell.value
        print TagName
        
        cell = first_sheet.cell(13,3)
        ExpectedSuccessMessage = cell.value
        print ExpectedSuccessMessage
        
        cell = first_sheet.cell(13,4)
        ExpectedTrackMessage = cell.value
       
        cell = first_sheet.cell(13,5)
        ExpectedAddLessonMessage = cell.value
        
        try:     
            tr1=TagTrackWiththreelessons_Three_Four_Five()
            tr1.taglessonWithVideo(lessonNameforVidcard, videoPath, timeToUploadVideo)
            tr1.taglessonWithDocument(lessonNameforDoccard, documentPath, timeToUploaddocument)
           
            tr1.taglessonWithQuestion(lessonNameforQuescard, questionCard, ans1, ans2)
            tr1.tagcreateTrackwithVidDocAndQuesLesson(titleOfTrack,Imagefilepath,description,tagName,lessonNameforVidcard,lessonNameforDoccard,lessonNameforQuescard,expectedSuccessText)
            tr1.createTrackWiththreelessons_Three_Four_Five_Tag(TagName, ExpectedSuccessMessage, ExpectedAddLessonMessage, lessonNameforVidcard, lessonNameforDoccard, lessonNameforQuescard, TrackName, ExpectedTrackMessage)
            tr1.searchInLibraryTrackWithTwoLessons_Three_Four_Five(lessonNameforVidcard, lessonNameforDoccard, lessonNameforQuescard, TrackName, TagName)
            lesdel= DeleteLesson()
            lesdel.lessonDelete(lessonNameforVidcard)
            lesdel.lessonDelete(lessonNameforDoccard)
            lesdel.lessonDelete(lessonNameforQuescard)
        except Exception as e:
            traceback.print_exc()
            print (e)
            raise Exception
        finally:  
            second_sheet = book.sheet_by_name('Login_Credentials')
            cell = second_sheet.cell(1,1)
            url = cell.value
            driver.get(url)
            try:
                WebDriverWait(driver, 5).until(EC.alert_is_present())

                alert = driver.switch_to.alert
                alert.accept()
                print("alert accepted")
            except Exception:
                print("no alert")

#if __name__ == '__main__':
    
  #  btc=BaseTestClass()
   # btc.UserLogin()
   # m1=TagTrackWiththreelessons_Three_Four_Five()
  #  m1.tagtrackWithTwoLessonsVidDocQues()
       
        