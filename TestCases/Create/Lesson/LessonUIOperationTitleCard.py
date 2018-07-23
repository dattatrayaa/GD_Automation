'''
Created on 05-Jul-2018

@author: Optislabs
'''
import os
import time

from BaseTestClass import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xlrd

from CreateLessonDifferentCards import CreateLessonDifferentCards
from LessonsPageElements import LessonsPageElements
from DeleteLesson import DeleteLesson
from BaseTestClass import BaseTestClass


class LessonUIOperationTitleCard:
    
    def lessonUiOperation(self,lessonName,textCard,setcolorInHexForm,Imagefilepath1):
        
        print "\nCreating lesson with one card"
        wait=WebDriverWait(driver, 120)
        driver.refresh()
        print "Clicking on Lessons button from side menu"
        
        lessons=LessonsPageElements()
        lessons.lessonsButtonSideMenuUnexpanded()
     
        print "Click on Create lesson button"
        lessons.createLessonButton()
        
        print "Verifying Create new lesson tab is displayed"
        
        
        if lessons.createANewLessonPopupHeader()== "Create a new lesson":
            print("Create a new lesson tab is displayed")
        else:
            print ""
            raise Exception
        
               
        
        lessons.clickOnBlankLesson()
        print "Clicked on Blank lesson"
        
        print "Creating New lesson"
        
        lessons.settingLessonName(lessonName)
        print "Entered lesson name ::"+lessonName
        
        
        print "Setting background color"
        bgcolor=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.titlebackgroundColor())))
        bgcolor.click()
        print "Clicked on Background color button"
        
        print "Setting color"
        wait.until(EC.visibility_of_element_located((By.XPATH,lessons.colorpickerHex())))
        hexcolor=driver.find_element_by_xpath(lessons.colorpickerHex())
        hexcolor.clear()
        #time.sleep(4)
        
        hexcolor.send_keys(setcolorInHexForm)
        time.sleep(2)
        print "New BG color set as :"+hexcolor.get_attribute("value")
        
        print "Changing background image for title card"
        
        lessons.imageUploadInImageCard(Imagefilepath1)
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,lessons.BgImgdeletebuttonTitlecard())))
            print "Image uploaded successfully in background"
        except Exception:
            raise Exception("Background image is not displayed for Title card")
        
        bgImage=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.BgImgdeletebuttonTitlecard())))
        
        bgImage.click()
        print "Clicked on delete image button"
        
        print "Adding GIF to background"
        giphy=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.giphyButton())))
        giphy.click()
        print "Clicked on Giphy button"
        
        print "Checking Pop up is displayed"
        try:
            giphyHeader=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.giphypopupHeader())))
            print "'"+giphyHeader.text+"' is displayed"
        except Exception:
            raise Exception('Giphy pop up is not displayed')
        
        print "Checking Cancel button"
        cancel=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.CancelButtonGIF)))
        cancel.click()
        print "Clicked on Cancel button"
        
        print "Clicking Giphy button again"
        giphy=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.giphyButton())))
        giphy.click()
        
        print "Selecting first Giphy displayed in Popup"
        
        firstGif=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.selectFirstGiphy())))
        firstGif.click()
        print "First GIF selected"
        
        savebutton=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.saveButtonGIF())))
        savebutton.click()
        print "Clicked on Save button"
        
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,lessons.BgImgdeletebuttonTitlecard())))
            print "GIF displayed in Background"
        except Exception:
            raise Exception('GIF not displayed in Background')
        
        
        
        e=CreateLessonDifferentCards()
        e.textCard(textCard)
        
        
        
        time.sleep(2)
        print "Publishing lesson"
        lessons.readyToPublishButtonClick()
        
        print "Clicked on publish button"
        lessons.publishButtonClick()

        print "Lesson published"
        
        
        lessons.backButton()
        
        #Verifying created lesson is displayed in list
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"(//tbody/tr/td[2]/a[.='"+lessonName+"'])[1]")))

        if driver.find_element_by_xpath("(//tbody/tr/td[2]/a[.='"+lessonName+"'])[1]").is_displayed():
            
            print "\nLesson is displayed in Grid ::"+lessonName
            
        else:
            print "Lesson not displaying in grid"
            raise Exception
        
        
        lessons.expandSideMenu()


    def lessonUiOpearationOnTitleCardMain(self):
        
        book=xlrd.open_workbook(os.path.join('TestData.xlsx'))
        first_sheet = book.sheet_by_name('LessonCreate')
        
        cell1 = first_sheet.cell(32,1)
        lessonName = cell1.value
        
        cell2 = first_sheet.cell(33,1)
        textCard = cell2.value
        
        cell2 = first_sheet.cell(34,1)
        setcolorInHexForm = cell2.value
        
        cell2 = first_sheet.cell(35,1)
        Imagefilepath1 = cell2.value
        
        try:
            img=LessonUIOperationTitleCard()
            img.lessonUiOperation(lessonName, textCard, setcolorInHexForm, Imagefilepath1)
            
        finally:  
            second_sheet = book.sheet_by_name('Login_Credentials')
            cell = second_sheet.cell(1,1)
            url = cell.value
            driver.get(url)
            
            try:
                delLesson=DeleteLesson()
                delLesson.lessonDelete(lessonName)
            except Exception:
                driver.get(url)



if __name__ == '__main__':
    
    b=BaseTestClass()
    b.UserLogin()
    
    ui=LessonUIOperationTitleCard()
    ui.lessonUiOpearationOnTitleCardMain()
    
    
    
    