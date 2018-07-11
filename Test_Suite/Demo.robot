*** Settings ***

Library           ../Master/BaseTestClass.py
Library           ../TestCases/Create/Tracks/TrackWithTextLesson.py
Library           ../TestCases/Create/Lesson/LessonCreateQuestion.py
Library           ../TestCases/Campaign/CreateCampaignForImageLesson.py
Library           ../TestCases/Admin/Users/UserCreateCreator.py
Library           ../Master/CloseBrowser.py

#Suite setup for setting up login environment 
#Suite teardown to close the browser after executing all the Test cases

Suite Setup       User Login
Suite Teardown	  Close Browser Suite

*** Test Cases ***
    
TC - LessonCreateQuestion
    [Documentation]    This test validates Question card in lesson and publish it
    [Tags]    Create
    LessonCreateQuestion.Lesson With Question Answer Card
    
TC- TrackWithTextLesson
    [Documentation]    This test validates the creation of track with one lesson
    [Tags]    Create
    Track With Lesson Contains Text Card

TC - CreateCampaignForImageLesson
    [Documentation]    This test validates creation of campaign
    [Tags]    Campaign
    Create Campaign Image Lesson 
 
#TC - CreateCreator
    #[Documentation]    This test validates creation of user with Creator permission
    #[Tags]    Admin
    #Create Creator User And Validation 



    



