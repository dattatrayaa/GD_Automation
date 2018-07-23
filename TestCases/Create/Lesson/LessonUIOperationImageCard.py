'''
Created on 09-Jul-2018

@author: OptisLabs
'''
import os
import time

from BaseTestClass import BaseTestClass
from BaseTestClass import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xlrd

from DeleteLesson import DeleteLesson
from LessonsPageElements import LessonsPageElements

class LessonUIOperationImageCard:
    
    def lessonUiOperationImageCard(self,lessonName,Imagefilepath1,r, g, b,ImagefilepathPNG,ImagefilepathBMP,ImagefilepathTIFF,ImagefilepathGIF):
                
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
        
        print "\nUploading Image"
        print "Click on (+) icon"
        
        lessons.addCardPlusiCon()
        
        print "Clicking on Image card"
        lessons.imageCardClick()
        
        print "Uploading image"
        lessons.imageUploadInImageCard(Imagefilepath1)
        
        print "Verifying Image is uploaded"
        imageContainerlocator_after1upload=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.waitTillImageDisplayedXpath())))
        
        
        if(imageContainerlocator_after1upload.is_displayed()):
            
            print 'Successfully uploaded the image1 file'
            
        else:
            print "Failed to upload the image1 file"
            raise Exception
        
        
        e=driver.find_element_by_xpath(lessons.waitTillImageDisplayedXpath())
        currentSize= e.size
        print "Current Size =="
        print currentSize["width"]
        print "Disable Enlarge to fit toggle button"
        lessons.enalargeToFitToggle()
        print "Clicked on Enlarge to fit toggle button"
        
        sizeAfterToggleClick=e.size
        print "Checking enlarge to fit is enabled"
        
        if sizeAfterToggleClick["width"]!=currentSize["width"]:
            print "Size after clicking on Enlarge to fit toggle =="
            print sizeAfterToggleClick["width"]
        else :
            print "Image size didn't change after click the enlarge to fit icon"
            raise Exception
        
        print "Setting Background color for Image"
        bg=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.ImageCardBGColor())))        
        bg.click()
        print "Setting RGB color"
        lessons.settingRGBcolor(r, g, b)
        print "RGB color has been set to Image BG color"
        
        print "Verifying RGB color has been set to Image card"
        lessons.checkingRGBColorImgCardBG(r, g, b)
        
        print "Adding new Image card"
        print "Click on (+) icon"
        
        lessons.addCardPlusiCon()
        
        print "Clicking on Image card"
        lessons.imageCardClick()
        
        print "Uploading image"
        lessons.imageUploadInImageCard(Imagefilepath1)
        
        print "Verifying Image is uploaded"
        imageContainerlocator_after1upload=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.waitTillImageDisplayedXpath())))
        
        
        if(imageContainerlocator_after1upload.is_displayed()):
            
            print 'Successfully uploaded the image1 file'
            
        else:
            print "Failed to upload the image1 file"
            raise Exception
        
        
        print "Deleting Image"
        lessons.deleteImageImgCard()
        print "Clicked on Delete image button"
        
        print "Verifying image is deleted"
        lessons.ImgCardImgDeleteCheck()
        
        
        
        print "Checking card is deleted after clicking on Delete card"
        print "Taking Current count of Cards"
        count=str(lessons.CountOfAllCardDisplayed())
        print "Total number of cards displayed as ::"+count
        time.sleep(2)
        d=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.deleteCardLink())))        
        d.click()
        print "Clicked on Delete Card"
        countafterDelete=str(lessons.CountOfAllCardDisplayed())
        print countafterDelete
        print "Verifying Card is deleted"
        if count!=countafterDelete:
            print "Verified, card is deleted successfully ::"+countafterDelete
        else:
            print "Card is not deleted"
            raise Exception
        
        
        print "Adding New Image Card"
        print "Click on (+) icon"
        
        lessons.addCardPlusiCon()
        lessons.imageCardClick()
        lessons.imageUploadInImageCard(Imagefilepath1)
        
        print "Verifying Image is uploaded"
        imageContainerlocator_after1upload=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.waitTillImageDisplayedXpath())))
        if(imageContainerlocator_after1upload.is_displayed()):
            print 'Successfully uploaded the image1 file'
        else:
            print "Failed to upload the image1 file"
            raise Exception
        
        print "Checking in Preview link image is displayed"
        try:
            lessons.previewButton()
            print "Clicked on Preview button"
        except Exception:
            print "Failed to click on Preview Button"
            raise Exception
        
        lessons.DesktopPreviewOfImageCard()
        
        lessons.mobilePreviewButton()
        print "Clicked on Mobile preview button"
        
        lessons.MobilePreviewOfImageCard()
        
        print "Clicking on Close Preview button"
        close=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.closePreview())))
        close.click()
        print "Clicked on Close Button"
        wait.until(EC.visibility_of_element_located((By.XPATH,lessons.waitTillImageDisplayedXpath())))
        
        
        print "Verifying Upload of different formats of Images"
        print "Adding New Image Card"
        print "Click on (+) icon"
        lessons.addCardPlusiCon()
        lessons.imageCardClick()
        lessons.imageUploadInImageCard(ImagefilepathPNG)
        print "Verifying Image is uploaded"
        imageContainerlocator_after1upload=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.waitTillImageDisplayedXpath())))
        if(imageContainerlocator_after1upload.is_displayed()):
            print 'Successfully uploaded the PNG image file'
        else:
            print "Failed to upload the PNG image file"
            raise Exception
        
        lessons.addCardPlusiCon()
        lessons.imageCardClick()
        lessons.imageUploadInImageCard(ImagefilepathBMP)
        print "Verifying Image is uploaded" 
        imageContainerlocator_after1upload=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.waitTillImageDisplayedXpath())))
        if(imageContainerlocator_after1upload.is_displayed()):
            print 'Successfully uploaded the BMP image file'
        else:
            print "Failed to upload the BMP image file"
            raise Exception
        
        lessons.addCardPlusiCon()
        lessons.imageCardClick()
        lessons.imageUploadInImageCard(ImagefilepathTIFF)
        print "Verifying Image is uploaded"
        imageContainerlocator_after1upload=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.waitTillImageDisplayedXpath())))
        if(imageContainerlocator_after1upload.is_displayed()):
            print 'Successfully uploaded the TIF image file'
        else:
            print "Failed to upload the TIFF image file"
            raise Exception
        
        
        lessons.addCardPlusiCon()
        lessons.imageCardClick()
        lessons.imageUploadInImageCard(ImagefilepathGIF)
        print "Verifying Image is uploaded"
        imageContainerlocator_after1upload=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.waitTillImageDisplayedXpath())))
        if(imageContainerlocator_after1upload.is_displayed()):
            print 'Successfully uploaded the GIF image file'
        else:
            print "Failed to upload the GIF image file"
            raise Exception
        
        
        
        
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
        
        
        
        
    
    
    def lessonUiOpearationOnImageCardMain(self):
        
        book=xlrd.open_workbook(os.path.join('TestData.xlsx'))
        first_sheet = book.sheet_by_name('LessonCreate')
        
        cell1 = first_sheet.cell(47,1)
        lessonName = cell1.value
        
        cell2 = first_sheet.cell(48,1)
        Imagefilepath1 = cell2.value
        
        cell2 = first_sheet.cell(49,1)
        r = cell2.value
        
        cell2 = first_sheet.cell(50,1)
        g = cell2.value
        
        cell2 = first_sheet.cell(51,1)
        b = cell2.value
        
        cell2 = first_sheet.cell(52,1)
        ImagefilepathPNG = cell2.value
        
        cell2 = first_sheet.cell(53,1)
        ImagefilepathBMP = cell2.value
        
        cell2 = first_sheet.cell(54,1)
        ImagefilepathTIFF = cell2.value
        
        cell2 = first_sheet.cell(55,1)
        ImagefilepathGIF = cell2.value
        
        
        
        try:
            print "\nThis Test case Tests the UI operations and functionality of Image Card\n"
            li=LessonUIOperationImageCard()
            li.lessonUiOperationImageCard(lessonName, Imagefilepath1, r, g, b, ImagefilepathPNG, ImagefilepathBMP, ImagefilepathTIFF, ImagefilepathGIF)
            print "\n Test Execution completed\n"
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
    
    text=LessonUIOperationImageCard()
    text.lessonUiOpearationOnImageCardMain()
    
    
    

