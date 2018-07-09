*** Settings ***
Force Tags      Lesson

#Config
Library   /Users/automation/Downloads/TeamCity/buildAgent/work/764a857d3ed1a731/Master/BaseTestClass.py

#Functions to create Lessons
Library   /Users/automation/Downloads/TeamCity/buildAgent/work/764a857d3ed1a731/TestCases/Create/Lesson/LessonCreateText.py
Library           /Users/automation/Downloads/TeamCity/buildAgent/work/764a857d3ed1a731/Master/DeleteLesson.py
Library           /Users/automation/Downloads/TeamCity/buildAgent/work/764a857d3ed1a731/Master/CloseBrowser.py



*** Test Cases ***
TC0 - User Login
    User Login
    

#Test cases for Lesson creation    
TC12 - LessonCreateText
    LessonCreateText.Lesson With Text Card

Close Browser
    Close Browser Suite


