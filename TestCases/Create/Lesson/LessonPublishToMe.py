'''
Created on 13-Jul-2018

@author: OptisLabs
'''
import traceback
import os
import time

from BaseTestClass import driver
from openpyxl.reader.excel import load_workbook
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xlrd

from CreateLessonDifferentCards import CreateLessonDifferentCards
from CreateUserWithRole import CreateUserWithRole
from LessonsPageElements import LessonsPageElements
from DeleteLesson import DeleteLesson
from BaseTestClass import BaseTestClass


class LessonPublishToMe:
    
    def lessonForPublishToMeLesson(self,lessonName,textCard):
        print "\nCreating lesson with one card"
        wait=WebDriverWait(driver, 60)
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
        
        
        
        e=CreateLessonDifferentCards()
        e.textCard(textCard)
        
        
        
        time.sleep(2)
        print "Publishing lesson"
        lessons.readyToPublishButtonClick()
        
        print "Clicking on 'Everyone' toggle button"
        lessons.everyoneToggle()
        print "Clicked on 'Everyone' toggle button"
    
        
        
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
    
    
    def CheckingLessonInBuiltByEnterpriseTab(self,lessonName,Email,Password):
        
        wait=WebDriverWait(driver, 60)
        
        driver.refresh()
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[1]/div[1]/nav/div[2]/a/span[3]")))
        
        
        print "Logging out"
        print "Clicking on Username Dropdown"
        ele =driver.find_element_by_xpath(".//*[@id='content']/div/div[1]/div[1]/nav/div[2]/a/span[3]")
        driver.execute_script('arguments[0].click()',ele)
        elem=driver.find_element_by_xpath("html/body/div/div/div[1]/div[2]/div[2]/a")
        driver.execute_script('arguments[0].click()',elem)
        
        print "Clicked on Sign Out option"
        
        
        element=wait.until(EC.presence_of_element_located((By.ID, "password")))
        
        if driver.title == "Grovo":
            print("Grovo Application URL Opened")
        else:
            raise Exception.message

        print "Grovo Sign-In page is displayed"
        
        print "Entering User name"
        driver.find_element_by_xpath(".//*[@id='username']").send_keys(Email)
       
        print "Entering Password"
        element.send_keys(Password)
        
        element.send_keys(Keys.TAB)
        print "Clicking on Sign_In button"
        driver.find_element_by_xpath("//*[@id='submitButton']").click()
        
        print "Successfully Logged Into Users account"  
        
        
        
        driver.refresh()
        print "Clicking on Lessons button from side menu"
        
        lessons=LessonsPageElements()
        lessons.lessonsButtonSideMenuUnexpanded()
     
        print "Clicking on 'Built by enterprise' tab"
        tr=lessons.BuiltByEnterpriseTab()
        print "Clicked on '"+tr+"' tab"
        
        print "Searching lesson :"+lessonName
        try:
            lessons.SearchLessonTextField(lessonName)
        except Exception as e:
            print e
            traceback.print_exc()
            raise Exception("Failed to search Lesson")
        print "Waiting for lessons to be displayed"
        try:
            noresult=lessons.noresultFound()
            print "Validation message '"+noresult.text+"' displayed"
            print "Hence no lesson displayed"
        except Exception:
            traceback.print_exc()
            raise Exception("Lesson displayed")
        
        time.sleep(6)
        
        
    
    def LessonPublishToMeCheckInForOtherUserMain(self):
        
        book=xlrd.open_workbook(os.path.abspath(os.path.join(os.path.dirname(__file__),'TestData.xlsx')))
        first_sheet = book.sheet_by_name('LessonCreate')
        
        cell1 = first_sheet.cell(86,1)
        lessonName = cell1.value
        
        cell2 = first_sheet.cell(87,1)
        textCard= cell2.value
        
        
        #Creator 1
        cell = first_sheet.cell(88,1)
        FirstName = cell.value
        
        FirstNameId = FirstName.split("_")
        emp = FirstNameId[0]+"_"
        ids = FirstNameId[1]
        empId = int(ids)+1
        FirstNameUpdated= emp+str(empId)
        
        cell = first_sheet.cell(89,1)
        LastName = cell.value
        
        LastNameID = LastName.split("_")
        emp = LastNameID[0]+"_"
        ids = LastNameID[1]
        empId = int(ids)+1
        LastNameUpdated= emp+str(empId)
        
        
        
        cell = first_sheet.cell(90,1)
        Email = cell.value
        
        EmailId = Email.split("_")
        emp = EmailId[0]+"_"
        ids = EmailId[1]
        remaining="_"+EmailId[2]
        empId = int(ids)+1
        EmailIdUpdated= emp+str(empId)+remaining
        
        cell = first_sheet.cell(91,1)
        EmployeeId = cell.value
        
        Employee = EmployeeId.split("_")
        emp = Employee[0]+"_"
        ids = Employee[1]
        empId = int(ids)+1
        EmployeeIdUpdated= emp+str(empId)
        
        cell = first_sheet.cell(92,1)
        Password = cell.value
        
        cell = first_sheet.cell(92,1)
        NewPassword = cell.value
        
        cell = first_sheet.cell(93,1)
        role = cell.value
        
        
        #For Original User
        book=xlrd.open_workbook(os.path.join('TestData.xlsx'))
        s_sheet = book.sheet_by_name('Login_Credentials')
        
        cell = s_sheet.cell(1,1)
        url = cell.value
        
        cell = s_sheet.cell(3,1)
        username = cell.value
        
        cell = s_sheet.cell(3,2)
        password = cell.value
        
            
        
        
        #updating user values
        wb = load_workbook(os.path.abspath(os.path.join(os.path.dirname(__file__),'TestData.xlsx')))
            #print (wb.sheetnames)
        
        sheet = wb['LessonCreate']
        
        sheet.cell(row=89, column=2).value = FirstNameUpdated
        sheet.cell(row=90, column=2).value = LastNameUpdated
        sheet.cell(row=91, column=2).value = EmailIdUpdated
        sheet.cell(row=92, column=2).value = EmployeeIdUpdated
        
        
        wb.save(os.path.abspath(os.path.join(os.path.dirname(__file__),'TestData.xlsx')))
            
        print "All User Data Updated in Excel"
        
        
        
        
        try:
            print "\nCreating a New Creator\n"
            lt=CreateUserWithRole()
            lt.createUserWithRoleMain(FirstName, LastName, Email, EmployeeId, Password, role, NewPassword, url, username, password)
            
            print "\nCreating a lesson with coping get link\n"
            un=LessonPublishToMe()
            un.lessonForPublishToMeLesson(lessonName, textCard)
            
            print "\nChecking for other user lesson displayed in Built by enterprise Tab\n"
            
            un.CheckingLessonInBuiltByEnterpriseTab(lessonName, Email, Password)
            print "\n----Test Execution Completed----\n"
            
            
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
            
            wait=WebDriverWait(driver, 60)
            unDropDown=wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[1]/div[1]/nav/div[2]/a/span[3]")))
            driver.execute_script('arguments[0].click()',unDropDown)
            
            signOut=driver.find_element_by_xpath("html/body/div/div/div[1]/div[2]/div[2]/a")
            driver.execute_script('arguments[0].click()',signOut)
            
            
            
            element = wait.until(EC.presence_of_element_located((By.ID, "password")))
            
            
            time.sleep(3)
            if driver.title == "Grovo":
                print("Grovo Application URL Opened")
            else:
                raise Exception.message
    
            print "Grovo Sign-In page is displayed"
            
            print "Entering User name"
            driver.find_element_by_xpath(".//*[@id='username']").send_keys(username)
           
            print "Entering Password"
            element.send_keys(password)
            
            element.send_keys(Keys.TAB)
            print "Clicking on Sign_In button"
            driver.find_element_by_xpath("//*[@id='submitButton']").click()
            
            print "Successfully Logged Into Users account"
            time.sleep(3)
            
            try:
                d=DeleteLesson()
                d.lessonDelete(lessonName)
            except Exception:
                driver.get(url)
            
            
            
            
if __name__ == '__main__':
    
    btc=BaseTestClass()
    btc.UserLogin()
    
    les=LessonPublishToMe()
    les.LessonPublishToMeCheckInForOtherUserMain()
        
        
        
        
    
    
    