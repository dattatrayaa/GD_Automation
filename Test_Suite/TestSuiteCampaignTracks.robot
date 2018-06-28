*** Settings ***
Force Tags      Campaign

#Config
Library   ../Master/BaseTestClass.py
#Functions to create CampagnTracks
Library           ../TestCases/Campaign/CampaignCreateTrackWithTextLesson.py
Library           ../TestCases/Campaign/CampaignCreateTrackWithImageLesson.py
Library           ../TestCases/Campaign/CampaignCreateTrackWithVideoLesson.py
Library           ../TestCases/Campaign/CampaignCreateTrackWithDocumentLesson.py
Library           ../TestCases/Campaign/CampaignCreateTrackWithQuestionLesson.py

Library           ../Master/DeleteLesson.py
Library           ../TestCases/Campaign/CampaignTrackAllCardsOnetimeLesson.py
Library           ../TestCases/Campaign/CampaignTrackAllCardsTwoTimeLesson.py
Library           ../TestCases/Campaign/CampaignTrackTxtImgQueLesson.py
Library           ../TestCases/Campaign/CampaignTrackVidDocQueLesson.py
Library           ../TestCases/Campaign/CampaignTrackTxtVidQueLesson.py
Library           ../TestCases/Campaign/CampaignTrackTextLessonImageLesson.py
Library           ../TestCases/Campaign/CampaignTrackImageLessonVideoLesson.py
Library           ../TestCases/Campaign/CampaignTrackVideoDocumentQuestionsLessons.py
Library           ../TestCases/Campaign/CampaignTrackQuesAllCardsOneAllCardsTwoTime.py
Library           ../TestCases/Campaign/CampaignTrackFourLessonsOne.py
Library           ../TestCases/Campaign/CampaignTrackFourLessonsTwo.py
Library           ../TestCases/Campaign/CampaignTrackFourLessonsThree.py
Library           ../Master/CloseBrowser.py

*** Test Cases ***
User Login
    User Login

CreateCampTrackTextLesson
    Campaign For Track With Text Lesson

CreateCampTrackImageLesson
    Campaign For Track With Image Lesson

CreateCampTrackVideo
    Campaign For Track With Video Lesson

CreateCampTrackDocLesson
    Campaign For Track With Document Lesson

CreateCampTrackQuesLesson
    Campaign For Track With Question Lesson

CampaignTrackAllCardsOnetimeLesson
    Campaign For Track With All Cards One Time

CampaignTrackAllCardsTwoTimeLesson
    Campaign For Track With All Cards Two Time

CampaignTrackTxtImgQueLesson
    Campaign For Track With Text Image Question Lesson

CampaignTrackVidDocQueLesson
    Campaign For Track With Video Document Question Lesson

CampaignTrackTxtVidQueLesson
    Campaign For Track With Text Video Question Lesson

CampaignTrackTextLessonImageLesson
    Campaign For Track With Text Lesson Image Lesson

CampaignTrackImageLessonVideoLesson
    Campaign For Track With Image Lesson Video Lesson

CampaignTrackVideoDocumentQuestionsLessons
    Campaign For Track With Video Lesson Document Lesson Question Lesson

CampaignTrackQuesAllCardsOneAllCardsTwoTime
    Campaign For Track With Question Lesson All Cards One All Cards Two Time

CampaignTrackFourLessonsOne
    Campaign For Track With Four Lessons One

CampaignTrackFourLessonsTwo
    Campaign For Track With Four Lessons Two

CampaignTrackFourLessonsThree
    Campaign For Track With Four Lessons Three

Close Browser
    Close Browser Suite
