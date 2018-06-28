*** Settings ***
Force Tags      Admin

#Config
Library   ../Master/BaseTestClass.py

#Functions to create Tags
Library   ../TestCases/Admin/Tag/CreateTag.py
Library   ../Master/CloseBrowser.py
*** Test Cases ***
TC0 - User Login
    User Login

TC01 - Create Tag

	CreateTag And Search In List

Close Browser
    Close Browser Suite

    
    
    
    
    
    
    
    
    
    
    
    
