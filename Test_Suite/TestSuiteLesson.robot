*** Settings ***
Force Tags        Lesson
Library           ../Master/BaseTestClass.py    #Config
Library           ../TestCases/Create/Lesson/LessonTextQueVidTenTime.py    #Functions to create Lessons
Library           ../TestCases/Create/Lesson/LessonTextQueImgFiveTime.py
Library           ../TestCases/Create/Lesson/LessonTextDocQueImgVidTwoTime.py
Library           ../TestCases/Create/Lesson/LessonTextDocQueImgVid.py
Library           ../TestCases/Create/Lesson/LessonQueVidDocFiveTime.py
Library           ../TestCases/Create/Lesson/LessonExplainAConcept.py
Library           ../TestCases/Create/Lesson/TeachASkill.py
Library           ../TestCases/Create/Lesson/LessonCreateImage.py
Library           ../TestCases/Create/Lesson/LessonCreateVideo.py
Library           ../TestCases/Create/Lesson/LessonCreateDocument.py
Library           ../TestCases/Create/Lesson/LessonCreateQuestion.py
Library           ../TestCases/Create/Lesson/LessonCreateText.py
Library           ../TestCases/Create/Lesson/LessonCreateText.py
Library           ../TestCases/Create/Lesson/LessonsUIOperationVideoCard.py
Library           ../TestCases/Create/Lesson/LessonUIOperationImageCard.py
Library           ../TestCases/Create/Lesson/LessonUIOperationTextCard.py
Library           ../TestCases/Create/Lesson/LessonUIOperationTitleCard.py
Library           ../TestCases/Create/Lesson/LessonDuplicateForPublish.py
Library           ../TestCases/Create/Lesson/LessonGetLinkBuilderToCreator.py
Library           ../TestCases/Create/Lesson/LessonGetLinkBuilderToLearner.py
Library           ../TestCases/Create/Lesson/LessonGetLinkBuilderToLearningAdmin.py
Library           ../TestCases/Create/Lesson/LessonGetLinkDraftCreator.py
Library           ../TestCases/Create/Lesson/LessonGetLinkDraftLearner.py
Library           ../TestCases/Create/Lesson/LessonGetLinkDraftLearningAdmin.py
Library           ../TestCases/Create/Lesson/LessonPublishToMe.py
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

TC13 - LessonsUIOperationVideoCard
    Lesson Ui Opearation On Video Card Main

TC14 - LessonUIOperationImageCard
    Lesson Ui Opearation On Image Card Main

TC15 - LessonUIOperationTextCard
    Lesson Ui Opearation On Text Card Main

TC16 - LessonUIOperationTitleCard
    Lesson Ui Opearation On Title Card Main

TC17 - LessonDuplicateForPublish
    Lesson Duplicate For Draft Status Main

TC18 - LessonGetLinkBuilderToCreator
    Lesson Getlink Lesson Builder For Creator Main

TC19 - LessonGetLinkBuilderToLearner
    Lesson Getlink Lesson Builder For Learner Main

TC20 - LessonGetLinkBuilderToLearningAdmin
    Lesson Getlink Lesson Builder For Learning Admin Main

TC21 - LessonGetLinkDraftCreator
    Lesson Getlink Unpublished Draft Main Creator

TC22 - LessonGetLinkDraftLearner
    Lesson Getlink Unpublished Draft Learner Main

TC23 - LessonGetLinkDraftLearningAdmin
    Lesson Getlink Unpublished Draft Learning Admin Main

TC24 - LessonPublishToMe
    Lesson Publish To Me Check In For Other User Main


