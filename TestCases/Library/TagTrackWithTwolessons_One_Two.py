'''
Created on 26-Feb-2018

@author: Sheethu C
'''
from operator import contains
import os.path
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.support.ui import WebDriverWait
import xlrd
from BaseTestClass import driver
from DeleteLesson import DeleteLesson

class TagTrackWithTwolessons_One_Two():
    
    
    def taglessonWithText(self,lessonName,textCard):
        
        wait=WebDriverWait(driver, 60)
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

        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/h1/textarea").send_keys(lessonName)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saving...']")))
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saved']")))
        
        print "Entered lesson name ::"+lessonName
        
        print "Click on (+) icon"
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div/span").click()

        driver.find_element_by_xpath("html/body/div/div/div/div[3]/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]").click()
        
        textCardelement=driver.find_element_by_xpath("//div[@class='text']/div/div[1]/div")
        
        #Entering Text in Text card 
        
        webdriver.ActionChains(driver).move_to_element(textCardelement).click().send_keys(textCard).perform()
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saving...']")))
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saved']")))
        
        #Verifying entered text is displaying text card
        print "Verifying entered text is displaying text card"
        
        textAfterEntering=driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/span/span").text
        
        if textAfterEntering==textCard:
            print "Verified Text '"+textCard+"' is displayed in Text Card"
        else:
            print "Text not displayed in Text card"
            raise Exception
        
        time.sleep(4)
       

        publishButton=wait.until(EC.element_to_be_clickable((By.XPATH,"html/body/div/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/button")))

        publishButton.click()

        wait.until(EC.element_to_be_clickable((By.XPATH,"html/body/div/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div/div[1]/section[3]/div/button[1]")))

        driver.find_element_by_xpath("html/body/div/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div/div[1]/section[3]/div/button[1]").click()
        print "Clicked on publish button"
        
        
        
        # verifying success message
        
        
        
        print "Verifying Success message"
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[2]/div/div/span[2]")))

        headerText=driver.find_element_by_xpath(".//*[@id='content']/div/div/div[2]/div/div/span[2]").text
        print "Message '"+headerText+"' is displayed"
        
        if "You have successfully published" in headerText:
            print("Create a new lesson tab is displayed")
        else:
            print "Success message is not displayed"
            raise Exception

        print "Lesson published"
        
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[1]/a").click()
        time.sleep(5)
        
        #Verifying created lesson is displayed in list
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"(//tbody/tr/td[2]/a[.='"+lessonName+"'])[1]")))

        if driver.find_element_by_xpath("(//tbody/tr/td[2]/a[.='"+lessonName+"'])[1]").is_displayed():
            
            print "Lesson is displayed in Grid ::"+lessonName
            
        else:
            print "Lesson not displaying in grid"
            raise Exception
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[1]/div/nav/div/div[4]").click()
        
    def taglessonWithImage(self,lessonName,Imagefilepath1):
        
        wait=WebDriverWait(driver, 60)
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

        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/h1/textarea").send_keys(lessonName)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saving...']")))
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saved']")))
        
        print "Entered lesson name ::"+lessonName
        
        print "Click on (+) icon"
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div/span").click()
        
        #Clicking on Image card
        driver.find_element_by_xpath("html/body/div/div/div/div[3]/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[1]").click()
        
        #Uploading image
        driver.find_element_by_css_selector('input[type="file"]').send_keys(Imagefilepath1)
        
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[1]/img")))
        
        imageContainerlocator_after1upload= driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[1]/img")
        
        if(imageContainerlocator_after1upload.is_displayed()):
            
            print 'Successfully uploaded the image1 file'
            
        else:
            print "Failed to upload the image1 file"
            raise Exception
        
        
        time.sleep(4)
        
        publishButton=wait.until(EC.element_to_be_clickable((By.XPATH,"html/body/div/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/button")))

        publishButton.click()

        wait.until(EC.element_to_be_clickable((By.XPATH,"html/body/div/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div/div[1]/section[3]/div/button[1]")))

        driver.find_element_by_xpath("html/body/div/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div/div[1]/section[3]/div/button[1]").click()
        print "Clicked on publish button"
        
        
        
        # verifying success message
        
        
        
        print "Verifying Success message"
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[2]/div/div/span[2]")))

        headerText=driver.find_element_by_xpath(".//*[@id='content']/div/div/div[2]/div/div/span[2]").text
        print "Message '"+headerText+"' is displayed"
        
        if "You have successfully published" in headerText:
            print("Create a new lesson tab is displayed")
        else:
            print "Success message is not displayed"
            raise Exception

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
        
        
    def tagcreateTrackwithTxtAndImgLesson(self,titleOfTrack,Imagefilepath,description,tagName,lessonNameforTextcard,lessonNameforImgcard,expectedSuccessText):
        print "\nCreating track with one lesson contains Text Card"
        
        wait=WebDriverWait(driver, 120)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@href='/create/lessons']")))
        
        print "Clicking on Lessons button from side menu"
        driver.find_element_by_xpath("//a[@href='/create/lessons']").click()
        
        print "Clicking on Track button from side menu"
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
        
        
        print "Adding created two lessons"
        
        print "Clicking on Add lessons button"
       
        driver.execute_script("window.scrollTo(0, 0);")
        addlessonbutton=driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div/button")
        addlessonbutton.click()
        
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div/div/div[2]/div[2]/div/ul/li[1]/div[1]/div")))
        
        print "Searching for first lesson in Add lessons pop up"
        driver.find_element_by_xpath(".//*[@id='search-lessons-in-modal']").send_keys(lessonNameforTextcard)
        searchedLesson=wait.until(EC.visibility_of_element_located((By.XPATH,"//li/div[2]/h4[.='"+lessonNameforTextcard+"']/../../div[1]/div")))
        searchedLesson.click()
        print "Lesson '"+lessonNameforTextcard+"' selected"
        
        
        print "Searching for Second lesson in Add lessons pop up"
        driver.find_element_by_xpath(".//*[@id='search-lessons-in-modal']").clear()
        driver.find_element_by_xpath(".//*[@id='search-lessons-in-modal']").send_keys(lessonNameforImgcard)
        searchedLesson=wait.until(EC.visibility_of_element_located((By.XPATH,"//li/div[2]/h4[.='"+lessonNameforImgcard+"']/../../div[1]/div")))
        searchedLesson.click()
        print "Lesson '"+lessonNameforImgcard+"' selected"
        
        
        
     
        print "Adding to Track"
        driver.find_element_by_xpath("html/body/div[2]/div/div/div[2]/div[3]/button[1]").click()
        
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/div/div[2]/div[2]/div[1]/div/ul/li/div[2]/div/h4/div")))
        
        print "Checking added lesson is selected lesson from Pop up"
        
        
        lessonTextAddedToGrid=driver.find_element_by_xpath("//li[1]/div[2]/div/h4/div").text
        if lessonTextAddedToGrid==lessonNameforTextcard:
            print "Selected Lesson '"+lessonNameforTextcard+"' is displayed in grid of tracks page"
        
        else:
            print "Lesson is not displayed"
            raise Exception
        
        lessonTextAddedToGrid1=driver.find_element_by_xpath("//li[2]/div[2]/div/h4/div").text
        if lessonTextAddedToGrid1==lessonNameforImgcard:
            print "Selected Lesson '"+lessonNameforImgcard+"' is displayed in grid of tracks page"
        
        else:
            print "Lesson is not displayed"
            raise Exception
        
        #Publishing Track
        print "Clicking on Publish Track button"
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[2]/div/div/div[2]/div[2]/div[3]/button").click()
        
        print "\nVerifying Success message is displaying"
        
        
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[2]/div/div/span")))
        actualSuccessText=driver.find_element_by_xpath(".//*[@id='content']/div/div[2]/div/div/span").text
        
        if actualSuccessText==expectedSuccessText:
            print "Success message '"+actualSuccessText+"' is displayed"
        else:
            print "failed to display expected success message"
            raise Exception
        
        
        print "\nVerifying Creates track '"+titleOfTrack+"' is displayed in Tracks grid"
        
        
      
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[1]/div/nav/div/div[2]/div[3]/div/ul/li[2]/a").click()
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"//tbody/tr/td[2]/a[.='"+titleOfTrack+"']")))
        
        trackInGrid=driver.find_element_by_xpath("//tbody/tr/td[2]/a[.='"+titleOfTrack+"']").text
        
        if trackInGrid==titleOfTrack:
            print "Track '"+trackInGrid+"' is displayed in grid"
        else:
            print "Track is not displayed in grid"
            raise Exception
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[1]/div/nav/div/div[4]").click()
    
    
    
    
    def createTrackWithTwolessons_one_twotag(self,TagName,ExpectedSuccessMessage,ExpectedAddLessonMessage,TrackName,ExpectedTrackMessage,lessonNameforTextcard,lessonNameforImgcard):
      
        
        
        wait=WebDriverWait(driver, 80)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/a")))
        driver.find_element_by_xpath("html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/a").click()
        print "Clicked on admin icon"
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]")))
        driver.find_element_by_xpath("html/body/div/div/div[3]/div[1]/div/nav/div/div[2]/div[6]").click()
        print "Clicked on Admin"
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
        ExpectedMessage =  TagName+" "+ExpectedSuccessMessage
        time.sleep(3)
        
        #if ExpectedMessage in ActualMessage:
           #print("Expected Success Message and Actual Success Message is Matching,Success Message Verified")
        #else:
           # print "Success message is not displayed"
            #raise Exception
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
        SearchElement.send_keys(lessonNameforImgcard)
        SearchElement.send_keys(Keys.ENTER)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//li/div[2]/h4[.='"+lessonNameforTextcard+"']/../../div[1]/div")))
        time.sleep(4)
        driver.find_element_by_xpath("//li/div[2]/h4[.='"+lessonNameforTextcard+"']/../../div[1]/div").click()
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
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"//tbody/tr/td[1]/a[.='"+lessonNameforTextcard+"']")))
        print "Clicking on Track Tab"
       # driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/ul/li[2]/a").click()
        time.sleep(2)
        
        print "clicking on Tag lessons"
        driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/div[2]/button").click()
        wait.until(EC.visibility_of_element_located((By.ID,"search-lessons-in-modal")))
        SearchElement =driver.find_element_by_id("search-lessons-in-modal")
        SearchElement.send_keys(lessonNameforVidcard)
        SearchElement.send_keys(Keys.ENTER)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//li/div[2]/h4[.='"+lessonNameforImgcard+"']/../../div[1]/div")))
        time.sleep(4)
        driver.find_element_by_xpath("//li/div[2]/h4[.='"+lessonNameforImgcard+"']/../../div[1]/div").click()
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
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"//tbody/tr/td[1]/a[.='"+lessonNameforImgcard+"']")))
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
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[2]/div/div[3]/table/tbody/tr/td[1]")))
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
        
    def  searchInLibraryTrackWithTwoLessons_One_Two(self,lessonNameforTextcard,lessonNameforImgcard,TrackName,TagName): 
         
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
        driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/div/div[3]/div/ul/li[1]").click()
        time.sleep(3)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[2]/div/div/div[4]/div/div/div/a/div[2]/span")))
        Name =driver.find_element_by_xpath("//div/a/div[2]/span[contains(.,'"+lessonNameforTextcard+"')]").text
        NameLesson =Name.strip()
        print NameLesson
        print lessonNameforTextcard
        time.sleep(3)
        if lessonNameforTextcard == NameLesson:
           print("Lesson Verified")
        else:
            print "Lesson is not Verified"
            raise Exception
        
        print "Clicked on Lessons Tab"
        driver.find_element_by_xpath("html/body/div/div/div[3]/div[2]/div/div/div[3]/div/ul/li[1]").click()
        time.sleep(3)
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div[3]/div[2]/div/div/div[4]/div/div/div/a/div[2]/span")))
        Name =driver.find_element_by_xpath("//div/a/div[2]/span[contains(.,'"+lessonNameforImgcard+"')]").text
        NameLesson =Name.strip()
        print NameLesson
        print lessonNameforImgcard
        time.sleep(3)
        if lessonNameforImgcard == NameLesson:
           print("Lesson Verified")
        else:
            print "Lesson is not Verified"
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
        

    def tagtrackWithTwoLessonsTxtandImg(self):
        
        book=xlrd.open_workbook(os.path.join('TestData.xlsx'))
        first_sheet = book.sheet_by_name('TagTrackLesson')
        
        #Track Data
        cell1 = first_sheet.cell(70,1)
        titleOfTrack = cell1.value
        
        cell1 = first_sheet.cell(70,1)
        TrackName = cell1.value
        
        cell2 = first_sheet.cell(71,1)
        Imagefilepath = cell2.value
        
        cell2 = first_sheet.cell(72,1)
        description = cell2.value
        
        cell2 = first_sheet.cell(73,1)
        tagName = cell2.value
        
      
        cell2 = first_sheet.cell(74,1)
        expectedSuccessText= cell2.value
        
        # Lesson Data
        cell2 = first_sheet.cell(70,3)
        lessonNameforTextcard= cell2.value
        
        cell2 = first_sheet.cell(71,3)
        textCard= cell2.value
        
        cell2 = first_sheet.cell(73,3)
        lessonNameforImgcard = cell2.value
        cell2 = first_sheet.cell(73,3)
        lessonname = cell2.value
        
        
        cell2 = first_sheet.cell(74,3)
        Imagefilepath1= cell2.value
        
        first_sheet = book.sheet_by_name('AssignCreateTag')
        print("Fetching the Attribute Name from Excel Sheet\n")
        # read a cell
        cell = first_sheet.cell(11,2)
        TagName = cell.value
        print TagName
        
        cell = first_sheet.cell(11,3)
        ExpectedSuccessMessage = cell.value
        print ExpectedSuccessMessage
        
        cell = first_sheet.cell(11,4)
        ExpectedTrackMessage = cell.value
       
        cell = first_sheet.cell(11,5)
        ExpectedAddLessonMessage = cell.value
        
        print "Setting Pre-requisite"
        print "Creating Two lessons\n"
     
        try:
            tr1=TagTrackWithTwolessons_One_Two()
            tr1.taglessonWithText(lessonNameforTextcard, textCard)
            tr1.taglessonWithImage(lessonNameforImgcard, Imagefilepath1)
            tr1.tagcreateTrackwithTxtAndImgLesson(titleOfTrack,Imagefilepath,description,tagName,lessonNameforTextcard,lessonNameforImgcard,expectedSuccessText)
            tr1.createTrackWithTwolessons_one_twotag(TagName,ExpectedSuccessMessage,ExpectedAddLessonMessage,TrackName,ExpectedTrackMessage,lessonNameforTextcard,lessonNameforImgcard)
            tr1.searchInLibraryTrackWithTwoLessons_One_Two(lessonNameforTextcard,TrackName,TagName)
            tr1.searchInLibraryTrackWithTwoLessons_One_Two(lessonNameforImgcard,TrackName,TagName)
            lesdel= DeleteLesson()
            lesdel.lessonDelete(lessonNameforTextcard)
             lesdel.lessonDelete(lessonNameforImgcard)
        finally:
            second_sheet = book.sheet_by_name('Login_Credentials')
            cell = second_sheet.cell(1,1)
            url = cell.value
            driver.get(url)
    
    
#if __name__ == '__main__':
    
   # btc=BaseTestClass()
   # btc.UserLogin()
  #  m1=TagTrackWithTwolessons_One_Two()
  #  m1.tagtrackWithTwoLessonsTxtandImg()
