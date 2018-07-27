*** Settings ***
Suite Setup       User Login
Suite Teardown    Close Browser Suite
Force Tags        Admin
Library           ../Master/BaseTestClass.py    
Library           ../TestCases/Admin/Users/UserCreateCreator.py    
Library           ../TestCases/Admin/Users/UserCreateLearner.py
Library           ../TestCases/Admin/Users/UserCreateLearnerAdministrator.py
Library           ../TestCases/Admin/Users/UserCreateMasterAdmin.py
Library           ../TestCases/Admin/Users/UpdatingUserDetails.py
Library           ../Master/CloseBrowser.py
Library           C:/Python27/Lib/site-packages/GrovoTC/UserDeactivateCheckForCampaign.py
Library           C:/Python27/Lib/site-packages/GrovoTC/UserDeactivatedCheck.py
Library           C:/Python27/Lib/site-packages/GrovoTC/UserDeactivateFromCampTriggered.py
Library           C:/Python27/Lib/site-packages/GrovoTC/UserDeactivateFromGroup.py
Library           C:/Python27/Lib/site-packages/GrovoTC/UsersPageDefaultActions.py
Library           C:/Python27/Lib/site-packages/GrovoTC/UsersPageDefaultView.py

*** Test Cases ***
TC1- UpdatingUserDetails
    Updation Of Excel Values

TC2 - CreateCreator
    Create Creator User And Validation

TC3 - CreateLearner
    Create Learner User And Validation

TC4 - CreateMasterAdmin
    Create Master Admin User And Validation

TC5 - CreateLearnerAdministrator
    Create Learner Admin User And Validation

TC6 - UserDeactivateCheckForCampaign
    User Deactivated Available For Campaign Main

TC7 - UserDeactivatedCheck
    User Deactivate Main

TC8 - UserDeactivateFromCampTriggered
    User Deactivated From Triggered Campaign

TC9 - UserDeactivateFromGroup
    User Deactivate From Group Main

TC10 - UsersPageDefaultActions
    User Page Default Actions Main

TC11 - UsersPageDefaultView
    Users Default View Main
