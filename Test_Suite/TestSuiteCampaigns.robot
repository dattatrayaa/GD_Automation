*** Settings ***
Force Tags      Campaign

#Config
Library   ../Master/BaseTestClass.py
#Functions to create Campaign
Library   ../TestCases/Campaign/CreateCampaignForTextLesson.py
Library          ../Master/DeleteLesson.py
Library           ../Master/CloseBrowser.py


*** Test Cases ***
TC0 - User Login
    User Login
    


#Test cases for Campaign creation   
TC1 - CreateCampaignForTextLesson
    Create Campaign Text Lesson


