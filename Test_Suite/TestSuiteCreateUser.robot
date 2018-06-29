*** Settings ***
Force Tags      Admin
#Config
Library   ../Master/BaseTestClass.py

#Functions for User Creation with standard roles
Library   ../TestCases/Admin/Users/UserCreateCreator.py
Library   ../TestCases/Admin/Users/UserCreateLearner.py
Library   ../TestCases/Admin/Users/UserCreateLearnerAdministrator.py
Library   ../TestCases/Admin/Users/UserCreateMasterAdmin.py

Library   ../TestCases/Admin/Users/UpdatingUserDetails.py

Library     ../Master/CloseBrowser.py
*** Test Cases ***
TC0 - User Login
    User Login
   
#Test cases for User Creation with standard roles
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
Close Browser
    Close Browser Suite
