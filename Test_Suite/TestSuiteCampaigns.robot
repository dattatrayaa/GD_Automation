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


