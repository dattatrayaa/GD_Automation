*** Settings ***
Force Tags      Campaign

#Config
Library   ../Master/BaseTestClass.py
#Functions to create Campaign
Library   ../TestCases/Campaign/CreateCampaignForTextLesson.py
Library   ../TestCases/Campaign/CreateCampaignForImageLesson.py
Library   ../TestCases/Campaign/CreateCampaignForVideoLesson.py
Library   ../TestCases/Campaign/CreateCampaignForDocumentLesson.py
Library   ../TestCases/Campaign/CreateCampaignForQuestionLesson.py
Library   ../TestCases/Campaign/CreateCampaignForAllCardsOneTime.py
Library   ../TestCases/Campaign/CreateCampaignForTxtImgQueLesson.py
Library   ../TestCases/Campaign/CreateCampaignForAllCardsTwoTime.py
Library   ../TestCases/Campaign/CreateCampaignForTxtVidQuesLesson.py
Library   ../TestCases/Campaign/CreateCampaignForVidDocQueLesson.py
Library   ../TestCases/Campaign/CreateCampaignForFourLessonsOne.py
Library   ../TestCases/Campaign/CreateCampaignForFourLessonsTwo.py
Library   ../TestCases/Campaign/CreateCampaignForFourLessonsThree.py
Library   ../TestCases/Campaign/CreateCampaignForTextAndImageLesson.py
Library   ../TestCases/Campaign/CreateCampaignForImageAndVideoLesson.py
Library   ../TestCases/Campaign/CreateCampaignForQuesLesssonAllCards1timeAllCards2TimeLessons.py
Library   ../TestCases/Campaign/CreateCampaignForVideoLsnDocLsQuestionLes.py
Library   ../TestCases/Campaign/CampaignPageDisplay.py
Library          ../Master/DeleteLesson.py
Library           ../Master/CloseBrowser.py


*** Test Cases ***
TC0 - User Login
    User Login
    


#Test cases for Campaign creation   
TC1 - CreateCampaignForTextLesson
    Create Campaign Text Lesson

TC2 - CreateCampaignForImageLesson
    Create Campaign Image Lesson

TC3 - CreateCampaignForVideoLesson
    Create Campaign Video Lesson

TC4 - CreateCampaignForDocumentLesson
    Create Campaign Document Lesson

TC5 - CreateCampaignForQuestionLesson
    Create Campaign Question Lesson

TC6 - CreateCampaignForTxtImgQueLesson
    Create Campaign Text Image Ques Lesson

TC7 - CreateCampaignForAllCardsOneTime
    Create Campaign All Cards One Time Lesson

TC8 - CreateCampaignForAllCardsTwoTime
    Create Campaign With All Cards Two Time Lesson

TC9 - CreateCampaignForTxtVidQuesLesson
    Create Campaign With Lesson Text Video Question

TC10 - CreateCampaignForVidDocQueLesson
    Create Campaign With Lesson Video Document Question

#TC11 - CreateCampaignForFourLessonsOne
    #Create Campaign With Four Lessons One

#TC12 - CreateCampaignForFourLessonsTwo
    #Create Campaign With Four Lessons Two

#TC13 - CreateCampaignForFourLessonsThree
    #Create Campaign With Four Lessons Three

TC14 - CreateCampaignForTextAndImageLesson
    Create Campaign With Text Lesson Image Lesson

TC15 - CreateCampaignForImageAndVideoLesson
    Create Campaign With Image Lesson Video Lesson

TC16 - CreateCampaignForQuesLesssonAllCards1timeAllCards2TimeLessons
    Create Campaign With Three Lessons

TC17 - CreateCampaignForVideoLsnDocLsQuestionLes
    Create Campaign With Video Lesson Document Lesson Question Lesson  
    
TC18 - CampaignPageDisplay
    Campaigns Page Display Main

Close Browser
    Close Browser Suite
