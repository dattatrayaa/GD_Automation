*** Settings ***
Force Tags      Lesson

#Config
Library   ../Master/BaseTestClass.py

#Functions to create Lessons
Library   ../TestCases/Create/Lesson/LessonTextQueVidTenTime.py
Library   ../TestCases/Create/Lesson/LessonTextQueImgFiveTime.py
Library   ../TestCases/Create/Lesson/LessonTextDocQueImgVidTwoTime.py
Library   ../TestCases/Create/Lesson/LessonTextDocQueImgVid.py
Library   ../TestCases/Create/Lesson/LessonQueVidDocFiveTime.py
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
TC1 - BlankLessonFive
    Blank Lesson Five Main   

#TC2 - BlankLessonFiveTwo
    #Blank Lesson Five Two Main
    
TC3 - BlankLessonOne
    Blank Lesson One Main
    
TC4 - BlankLessonTen
    Blank Lesson Ten Main
    
TC5 - BlankLessonTwo
    Blank Lesson Two Main  
    
TC6 - LessonExplainAConcept
    Lesson Explain A Concept Main

TC7 - TeachASkill
    Teach A Skill Main

TC9 - LessonCreateVideo
    Lesson With Video Upload Card

TC10 - LessonCreateDocument 
    Lesson With Document Upload Card
       
TC11 - LessonCreateQuestion
    LessonCreateQuestion.Lesson With Question Answer Card
    
TC12 - LessonCreateText
    LessonCreateText.Lesson With Text Card

Close Browser
    Close Browser Suite


