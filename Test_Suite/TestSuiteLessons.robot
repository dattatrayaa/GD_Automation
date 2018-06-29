*** Settings ***
Force Tags      Lesson

#Config
Library   ../Master/BaseTestClass.py

#Functions to create Lessons
Library   ../TestCases/Create/Lesson/LessonCreateText.py
Library           ../Master/DeleteLesson.py
Library           ../Master/CloseBrowser.py



*** Test Cases ***
TC0 - User Login
    User Login
    

#Test cases for Lesson creation    
TC12 - LessonCreateText
    LessonCreateText.Lesson With Text Card

Close Browser
    Close Browser Suite


