'''
Created on 05-Jul-2018

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


class LessonUIOperationTextCard:
    
    def lessonUiOperationTextcard(self,lessonName,textCard1,textCard2,linkForText,fontcolorHex,Imagefilepath1):
        
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
        
        
        print "Text card"
        print "Click on (+) icon"
        lessons.addCardPlusiCon()
    
        lessons.textCardClick()
        print "Clicked on Text Card"
            
        print "Entering Text in Text card" 
        lessons.textCardEnteringText(textCard1)
        
        lessons.waitTillLessonSaved()
            
        #Verifying entered text is displaying text card
        print "Verifying entered text is displaying text card"
            
        textAfterEntering=driver.find_element_by_xpath(lessons.textCardVerifyTextEnteredXpath()).text
            
        if textAfterEntering==textCard1:
            print "Verified Text '"+textCard1+"' is displayed in Text Card"
        else:
            print "Text not displayed in Text card"
            raise Exception
        
        
        print "Selecting all Text by entering more Text"
        lessons.textCardEnteringText(textCard2)
        
        textCardelement=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.selectingText())))
        webdriver.ActionChains(driver).move_to_element(textCardelement).click().send_keys(Keys.CONTROL,'a').perform()
        
        print "Text has been selected"
        time.sleep(4)
        #setting up link for Text
        '''textLink=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.textUrlLink())))
        textLink.click()
        time.sleep(4)
        print "Setting up link for the Text"
        wait.until(EC.visibility_of_element_located((By.XPATH,lessons.linkTextBox())))
        driver.find_element_by_xpath(lessons.linkTextBox()).click()
        driver.find_element_by_xpath(lessons.linkTextBox()).send_keys(linkForText)
        
        #webdriver.ActionChains(driver).move_to_element(link).send_keys(linkForText).perform()
        time.sleep(4)
        print "Link entered"
        driver.find_element_by_xpath(lessons.linkTickmark()).click()
        print "Link '"+linkForText+"' is set for text :"+textCard1+textCard2
        time.sleep(4)
        
        print "Checking Link is working properly"
        print "Clicking on Preview button"
        lessons.previewButton()
        
        mainwindow=driver.current_window_handle
        
        print "Clicking on Text to check link"
        textLink=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.linkInPreviewofTextCard())))
        textLink.click()
        driver.switch_to.window(driver.window_handles[1]) 
        
        titleOfNewPage=driver.title()
        if titleOfNewPage=="Google":
            print "Link entered is correct"
        else:
            print "Link is incorrect for Text card"
            raise Exception
        
        driver.switch_to.window(mainwindow)
        
        print "Closing preview"
        close=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.closePreview())))
        close.click()'''
        
        
        print "Moving text Middle, right"
        
        mid=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.TextSettingsMovingToMid())))
        mid.click()
        print "Text box moved to mid"
        
        right=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.TextSettingsMovingToRight())))
        right.click()
        print "Text box moved to Right position"
        
        print "Checking font size toggle displayed"
        time.sleep(2)
        font=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.fontSizeToggle())))
        font.click()
        print "Clicked on toggle font size"
        
        print "Checking four font size displayed"
        
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,lessons.fontSizeToggleOption())))
            print "Font size Small, Normal, Large, Huge is displayed"
        except Exception:
            print "Font size not displayed"
            raise Exception
        
        print "Making font size as Huge"
        driver.find_element_by_xpath(lessons.fontSizeToggleHuge()).click()
        
        fontsize=lessons.checkFontSizeHuge().get_attribute("style")
        
        if "2em" in fontsize:
            print "Font size changed to huge"
        else :
            print "Font size didn't changed"
            raise Exception
        
        print "Adding bullet to text"
        bullet=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.bulletTOText())))
        bullet.click()
        print "Checking bullet added to text"
        bulletText=bullet.get_attribute("class")
        if "is-active" in bulletText:
            print "Bullet displayed"
        else :
            print "Bullet not displayed"
            raise Exception
        
        print "Adding number bullet to text"
        bullet=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.NumberBulletTOText())))
        bullet.click()
        print "Checking Number bullet added to text"
        bulletText=bullet.get_attribute("class")
        if "is-active" in bulletText:
            print "Number Bullet displayed"
        else :
            print "Number Bullet not displayed"
            raise Exception
        
        
        
        print "-Making Text As Bold"
        
        bold=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.boldText())))
        bold.click()
        print "Checking Bold font added to text"
        bulletText=bold.get_attribute("class")
        if "is-active" in bulletText:
            print "Bold font added to text"
        else :
            print "failed to add bold font to text"
            raise Exception
        
        
        
        print "-Making Text As Italic"
        
        talik=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.ItalicText())))
        talik.click()
        print "Checking italic font added to text"
        bulletText=talik.get_attribute("class")
        if "is-active" in bulletText:
            print "Italic font added to text"
        else :
            print "failed to add Italic font to text"
            raise Exception
        
        
        print "-Making Text Underlined"
        
        unline=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.underline())))
        unline.click()
        print "Checking underline added to text"
        bulletText=unline.get_attribute("class")
        if "is-active" in bulletText:
            print "Underline added to text"
        else :
            print "failed to underline text"
            raise Exception
        
        
        print "Changing Font color from black to "+fontcolorHex
        color=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.fontColor())))
        color.click()
        print "Clicked on Font Color picker"
        wait.until(EC.visibility_of_element_located((By.XPATH,lessons.colorpickerHex())))
        hexcolor=driver.find_element_by_xpath(lessons.colorpickerHex())
        hexcolor.clear()
        #time.sleep(4)
        
        hexcolor.send_keys(fontcolorHex)
        time.sleep(2)
        print "New font color set as :"+hexcolor.get_attribute("value")
        
        
        print "Uploading Background Image"
        lessons.imageUploadInBgTextCard(Imagefilepath1)
        
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,lessons.textCardDeleteBgImageButton())))
            print "Image is displayed in Background"
        except Exception:
            print "Image not displayed in Background"
            raise Exception
        
        
        print "Creating New Text Card"
        print "Click on (+) icon"
        lessons.addCardPlusiCon()
    
        lessons.textCardClick()
        print "Clicked on Text Card"
            
        print "Entering Text in Text card" 
        lessons.textCardEnteringText(textCard2)
        
        lessons.waitTillLessonSaved()
        
        print "Un-checking 'Show white box behind text'"
        
        try:
            whiteBox=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.showWhiteBox())))  
            whiteBox.click()      
            print "Clicked on White box"
        except Exception:
            print "Failed to click on white box"
            raise Exception
        
        
        ele=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.checkWhiteBoxdisabled())))
        whiteBox=ele.get_attribute("class")
        
        if "has-white-box" in whiteBox:
            print "White box displayed after unchecking show white box"
            raise Exception
        else :
            print "White box disabled from Text Card"
            
        
        print "Adding White box again"
        
        try:
            whiteBox=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.showWhiteBoxUnchecked())))  
            whiteBox.click()      
            print "Clicked on White box"
        except Exception:
            print "Failed to click on white box"
            raise Exception
        
        whiteBox=ele.get_attribute("class")
        if "has-white-box" in whiteBox:
            print "White box Enabled"
        else :
            print "White box failed to enable"
            raise Exception
        
        print "Adding in-line Image"
        
        try:
            whiteBox=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.addInlineImageCheckBox())))  
            whiteBox.click()      
            print "Clicked on inline image checkbox"
        except Exception:
            print "Failed to click on add inline image box"
            raise Exception
        
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,lessons.inlineImageBox())))  
            print "In-line Image box is displayed"
        except Exception:
            print "In-line image box is not displayed"
            raise Exception
        
        print "Uploading image"
        
        lessons.addingInlineImage(Imagefilepath1)
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,lessons.inlineImageDisplayed())))  
            print "In-line Image successfully displayed"
        except Exception:
            print "In-line image not displayed"
            raise Exception
        
        print "Checking, Change and Delete button is displayed"
        lessons.changeImageButtonInlineBox()
        lessons.DeleteImageButtonInlineBox()
        
        print "Deleting image"
        lessons.DeleteImageButtonInlineBox().click()
        
        print "Checking Image is deleted"
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,lessons.inlineImageBox())))  
            print "empty image box displayed"
        except Exception:
            print "Empty Image box not displayed"
            raise Exception
        
        
        print "Unchecking Add In-line image checkbox"
        whiteBox=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.addInlineImageCheckBox())))  
        whiteBox.click() 
        
        print "Checking Inline image box disabled from card"
        try:
            wait.until(EC.invisibility_of_element_located((By.XPATH,lessons.inlineImageBox())))  
            print "Empty image box disabled"
        except Exception:
            print "Empty Image box not disabled"
            raise Exception
        
        
        
        print "Adding New card"
        print "Click on (+) icon"
        lessons.addCardPlusiCon()
    
        lessons.textCardClick()
        print "Clicked on Text Card"
            
        print "Entering Text in Text card" 
        lessons.textCardEnteringText(textCard1)
        
        lessons.waitTillLessonSaved()
        
        try:
            adjust=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.adjustTextBoxLayOut())))  
            adjust.click()      
            print "Clicked on adjust text box layout"
        except Exception:
            print "Failed to adjust text box layout"
            raise Exception
       
       
        print "Moving to Top left corner"
        try:
            topleft=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.topLeftLayOut()))) 
            topleft.click()
            
        except Exception:
            print "Not able to click on  topleft layout"
            raise Exception
        print "Checking textbox moved to top left corner"
        topleftclass=topleft.get_attribute("class")
        if "is-selected" in topleftclass:
            print "Textbox moved to top left corner"
        else:
            print "Textbox falied to move top left corner"
            raise Exception
            
        
        
        
        print "Moving to Top right corner"
        try:
            topRight=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.topRightLayOut()))) 
            topRight.click()
            
        except Exception:
            print "Not able to click on  topRight layout"
            raise Exception
        print "Checking textbox moved to top right corner"
        topRightclass=topRight.get_attribute("class")
        if "is-selected" in topRightclass:
            print "Textbox moved to top Right corner"
        else:
            print "Textbox falied to move top Right corner"
            raise Exception
        
        
        
        print "Moving to Bottom left corner"
        try:
            Bottomleft=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.bottomLeftLayOut()))) 
            Bottomleft.click()
            
        except Exception:
            print "Not able to click on  Bottom left layout"
            raise Exception
        print "Checking textbox moved to Bottom left corner"
        Bottomleftclass=Bottomleft.get_attribute("class")
        if "is-selected" in Bottomleftclass:
            print "Textbox moved to Bottom left corner"
        else:
            print "Textbox falied to move Bottom left corner"
            raise Exception
        
        
        
        print "Moving to Bottom right corner"
        try:
            BottomRight=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.bottomRightLayOut()))) 
            BottomRight.click()
            
        except Exception:
            print "Not able to click on  Bottom right layout"
            raise Exception
        print "Checking textbox moved to Bottom right corner"
        BottomRightclass=BottomRight.get_attribute("class")
        if "is-selected" in BottomRightclass:
            print "Textbox moved to bottom Right corner"
        else:
            print "Textbox falied to move bottom Right corner"
            raise Exception
        
        
        print "Hiding Text box layout"
        try:
            adjust=wait.until(EC.visibility_of_element_located((By.XPATH,lessons.adjustTextBoxLayOut()))) 
            adjust.click()
            print "Clicked on text box layout"
        except Exception:
            print "Failed to click on Hide text-box layout"
            
        
        print "Checking text box is hidden"
        lessons.checkingTextBoxHidden()
            
        
        
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


    def lessonUiOpearationOnTextCardMain(self):
        
        book=xlrd.open_workbook(os.path.join('TestData.xlsx'))
        first_sheet = book.sheet_by_name('LessonCreate')
        
        cell1 = first_sheet.cell(39,1)
        lessonName = cell1.value
        
        cell2 = first_sheet.cell(40,1)
        textCard1 = cell2.value
        
        cell2 = first_sheet.cell(41,1)
        textCard2 = cell2.value
        
        cell2 = first_sheet.cell(42,1)
        linkForText = cell2.value
        
        cell2 = first_sheet.cell(43,1)
        fontcolorHex = cell2.value
        
        cell2 = first_sheet.cell(44,1)
        Imagefilepath1 = cell2.value
        
        try:
            li=LessonUIOperationTextCard()
            li.lessonUiOperationTextcard(lessonName, textCard1, textCard2, linkForText, fontcolorHex, Imagefilepath1)
        finally:  
            '''second_sheet = book.sheet_by_name('Login_Credentials')
            cell = second_sheet.cell(1,1)
            url = cell.value
            driver.get(url)
            
            try:
                delLesson=DeleteLesson()
                delLesson.lessonDelete(lessonName)
            except Exception:
                driver.get(url)'''



if __name__ == '__main__':
    
    b=BaseTestClass()
    b.UserLogin()
    
    text=LessonUIOperationTextCard()
    text.lessonUiOpearationOnTextCardMain()
    
    
    

    
