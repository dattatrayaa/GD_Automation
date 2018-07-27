*** Settings ***
Suite Setup       User Login
Suite Teardown    Close Browser Suite
Force Tags        Admin
Library           ../Master/BaseTestClass.py    #Config
Library           ../TestCases/Admin/Users/UserCreateCreator.py    #Functions for User Creation with standard roles
Library           ../TestCases/Admin/Users/UserCreateLearner.py
Library           ../TestCases/Admin/Users/UserCreateLearnerAdministrator.py
Library           ../TestCases/Admin/Users/UserCreateMasterAdmin.py
Library           ../TestCases/Admin/Users/UpdatingUserDetails.py
Library           ../Master/CloseBrowser.py
Library           ../TestCases/Admin/Users/UserDeactivateCheckForCampaign.py
Library           ../TestCases/Admin/Users/UserDeactivatedCheck.py
Library           ../TestCases/Admin/Users/UserDeactivateFromCampTriggered.py
Library           ../TestCases/Admin/Users/UserDeactivateFromGroup.py
Library           ../TestCases/Admin/Users/UsersPageDefaultActions.py
Library           ../TestCases/Admin/Users/UsersPageDefaultView.py

*** Test Cases ***
TC2- UpdatingUserDetails
    Updation Of Excel Values

TC3 - CreateCreator
    Create Creator User And Validation

TC4 - CreateLearner
    Create Learner User And Validation

TC6 - CreateMasterAdmin
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
