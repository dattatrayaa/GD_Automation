*** Settings ***

Library           ../Master/BaseTestClass.py
Library           ../TestCases/Create/Tracks/TrackWithTextLesson.py
Library           ../TestCases/Create/Lesson/LessonCreateQuestion.py
Library           ../TestCases/Campaign/CreateCampaignForImageLesson.py
Library       ../TestCases/Integration/Bamboo/BambooHRISIntegration.py
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
 
TC -BambooHRISIntegration
    [Documentation]    This test will integrate BambooHRIS to Grovo and validates in employees from BambooHR SandBox Account
    [Tags]    Admin
   Updating The Employee Values And Startmain


    



