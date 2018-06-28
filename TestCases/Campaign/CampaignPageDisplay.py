'''
Created on 27-Feb-2018

@author: dattatraya
'''
import os

from BaseTestClass import BaseTestClass
from BaseTestClass import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xlrd
from BaseTestClass import projectPath
class CampaignPageDisplay:
    
    
    def campaignPage(self,actualPageHeaderText,actualTextBelowHeader,actualCreateCampaignButtonText,actualGridText,actualTitleCol,actualDurationCol,actualupdatedByCol,
                       actualactionsCol,actualEditLinkText,actualduplicateLinkText,actualassignLinkText):
        print "\n----Campaign page display----"
        
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@href='/plan/campaigns'][1]")))
        
        print "Clicking on Campaigns button from side menu"
        driver.find_element_by_xpath("//a[@href='/plan/campaigns'][1]").click()
        wait.until(EC.visibility_of_element_located((By.XPATH,"//tbody/tr[1]/td[1]/a")))
     
        print "Checking all the UI elements in Campaigns home page"
        
        print "\nVerifying Header Text"
        
        pageHeaderText=driver.find_element_by_xpath("//header/h1").text
        
        if pageHeaderText==actualPageHeaderText:
            print "Campaigns page displayed with Header text ::"+pageHeaderText
        else:
            print "Header text is not displayed"
            raise Exception
        
        
        print "\nChecking for text below Header text is displaying"
        
        textBelowHeader=driver.find_element_by_xpath("//header/div/p").text
        
        if textBelowHeader==actualTextBelowHeader:
            print "Text displayed below header text ::"+textBelowHeader
        else:
            print "Text displayed below header text is not correct"
            raise Exception
        
        print "\nChecking Create campaign button is displayed"
            
        createCampaignButton=driver.find_element_by_xpath("//header/div/div/a")
        createCampaignButtonText=driver.find_element_by_xpath("//header/div/div/a").text
        
        if createCampaignButton.is_displayed():
            print "Create Campaign button is displayed"
            
        else :
            print "Create Campaign button is not displayed"
            raise Exception
        
        
        
        if createCampaignButtonText==actualCreateCampaignButtonText:
            print "Create Campaign button is displayed with Text ::"+createCampaignButtonText
            
        else:
            print "Create Campaign button text displayed is invalid"
            raise Exception
        
        print "\nChecking Campaigns Grid header text"
        
        
        gridText=driver.find_element_by_xpath("//div/div/h3").text
        
        if actualGridText in gridText:
            print "Grid header Text displayed as ::"+gridText
            
        else:
            print "Grid Header Text is not displayed properly"
            raise Exception
        
        
        
        print "\nChecking all the Table column header text"
        
        titleCol=driver.find_element_by_xpath("//table/thead/tr/th[1]").text
        if titleCol == actualTitleCol:
            print "Column 1 text ::"+titleCol
            
        else:
            print "Column 1 text is not displayed"
            raise Exception
        
        
        '''durationCol=driver.find_element_by_xpath("//thead/tr/th[2]").text
        if durationCol == actualDurationCol:
            print "Column 2 text ::"+durationCol
            
        else:
            print "Column 2 text is not displayed"
            raise Exception'''
        
        
        updatedByCol=driver.find_element_by_xpath("//thead/tr/th[3]").text
        if updatedByCol == actualupdatedByCol:
            print "Column 3 text ::"+updatedByCol
            
        else:
            print "Column 3 text is not displayed"
            raise Exception
        
        actionsCol=driver.find_element_by_xpath("//thead/tr/th[4]").text
        if actionsCol == actualactionsCol:
            print "Column 4 text ::"+actionsCol
            
        else:
            print "Column 4 text is not displayed"
            raise Exception
        
        
        
        
        print "\nChecking for different links displaying in Actions column"
        
        editLink=driver.find_element_by_xpath("//tr[1]/td[4]/a[1]")
        editLinkText=editLink.text
        if editLink.is_displayed() and editLinkText==actualEditLinkText:
            print "Edit link is displayed with text ::"+editLinkText
            
        else:
            print "Invalid Edit link is displayed"
            raise Exception
        
        
        duplicateLink=driver.find_element_by_xpath("//tr[1]/td[4]/a[2]")
        duplicateLinkText=duplicateLink.text
        if duplicateLink.is_displayed() and duplicateLinkText==actualduplicateLinkText:
            print "Duplicate link is displayed with text ::"+duplicateLinkText
            
        else:
            print "Invalid Duplicate link is displayed"
            raise Exception
        
        
        assignLink=driver.find_element_by_xpath("//tr[1]/td[4]/a[3]")
        assignLinkText=assignLink.text
        if assignLink.is_displayed() and assignLinkText==actualassignLinkText:
            print "Assign link is displayed with text ::"+assignLinkText
            
        else:
            print "Invalid Assign link is displayed"
            raise Exception
        
        
        
        print "\nAll UI elements in Campaigns page displayed properly"
        
        
    def campaignsPageDisplayMain(self):
        
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        first_sheet = book.sheet_by_name('CreateCampaigns')
        
        cell1 = first_sheet.cell(1,1)
        actualPageHeaderText = cell1.value
        
        cell2 = first_sheet.cell(2,1)
        actualTextBelowHeader = cell2.value
        
        cell3 = first_sheet.cell(3,1)
        actualCreateCampaignButtonText = cell3.value
        
        cell3 = first_sheet.cell(4,1)
        actualGridText = cell3.value
        
        cell3 = first_sheet.cell(5,1)
        actualTitleCol = cell3.value
        
        cell3 = first_sheet.cell(6,1)
        actualDurationCol = cell3.value
        
        cell3 = first_sheet.cell(7,1)
        actualupdatedByCol = cell3.value
        
        cell3 = first_sheet.cell(8,1)
        actualactionsCol = cell3.value
        
        cell3 = first_sheet.cell(9,1)
        actualEditLinkText = cell3.value
        
        cell3 = first_sheet.cell(10,1)
        actualduplicateLinkText = cell3.value
        
        cell3 = first_sheet.cell(11,1)
        actualassignLinkText = cell3.value
        
        try:
            camp=CampaignPageDisplay()
            camp.campaignPage(actualPageHeaderText, actualTextBelowHeader, actualCreateCampaignButtonText, actualGridText, actualTitleCol, actualDurationCol, actualupdatedByCol, actualactionsCol, actualEditLinkText, actualduplicateLinkText, actualassignLinkText)
            print "\n----Execution Completed----\n"
        finally:
            second_sheet = book.sheet_by_name('Login_Credentials')
            cell = second_sheet.cell(1,1)
            url = cell.value
            driver.get(url)
            
            
if __name__ == '__main__':
    btc=BaseTestClass()
    btc.UserLogin()
    
    c=CampaignPageDisplay()
    c.campaignsPageDisplayMain()
          
        
