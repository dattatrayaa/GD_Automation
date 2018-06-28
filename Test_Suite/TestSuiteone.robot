*** Settings ***
Force Tags      Lesson

#Config
Library   TestCases/BaseTestClass.py

#Functions to create Lessons
Library   TestCases/BlankLessonFive.py
Library   TestCases/BlankLessonFiveTwo.py
Library   TestCases/BlankLessonOne.py
Library   TestCases/BlankLessonTen.py
Library   TestCases/BlankLessonTwo.py
Library           TestCases/LessonExplainAConcept.py

Library   TestCases/TeachASkill.py
Library   TestCases/LessonCreateImage.py
Library   TestCases/LessonCreateVideo.py
Library   TestCases/LessonCreateDocument.py
Library   TestCases/LessonCreateQuestion.py
Library   TestCases/LessonCreateText.py
Library           TestCases/DeleteLesson.py
Library           TestCases/CloseBrowser.py


*** Test Cases ***
TC0 - User Login
    User Login
    

#Test cases for Lesson creation
    
TC12 - LessonCreateText
    LessonCreateText.Lesson With Text Card

Close Browser
    Close Browser Suite


