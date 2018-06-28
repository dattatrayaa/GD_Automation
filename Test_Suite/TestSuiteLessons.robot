*** Settings ***
Force Tags      Lesson

#Config
Library   ../Master/BaseTestClass.py

#Functions to create Lessons
Library   ../TestCases/Create/Lesson/BlankLessonFive.py
Library   ../TestCases/Create/Lesson/BlankLessonFiveTwo.py
Library   ../TestCases/Create/Lesson/BlankLessonOne.py
Library   ../TestCases/Create/Lesson/BlankLessonTen.py
Library   ../TestCases/Create/Lesson/BlankLessonTwo.py
Library    ../TestCases/Create/Lesson/LessonExplainAConcept.py

Library   ../TestCases/Create/Lesson/TeachASkill.py
Library   ../TestCases/Create/Lesson/LessonCreateImage.py
Library   ../TestCases/Create/Lesson/LessonCreateVideo.py
Library   ../TestCases/Create/Lesson/LessonCreateDocument.py
Library   ../TestCases/Create/Lesson/LessonCreateQuestion.py
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


