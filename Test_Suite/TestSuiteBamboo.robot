*** Settings ***
#Force Tags      Bamboo

#Config
Library   ../Master/BaseTestClass.py

#Functions to create Lessons
Library   ../TestCases/Integration/Bamboo/BambooHRISIntegration.py
Library           ../Master/CloseBrowser.py



*** Test Cases ***
TC0 - User Login
    User Login
    

#Test cases for Bamboo  
TC12 -BambooHRISIntegration
   Updating The Employee Values And Startmain

Close Browser
    Close Browser Suite


