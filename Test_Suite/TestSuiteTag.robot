*** Settings ***
Force Tags      Admin

#Config
Library   ../Master/BaseTestClass.py

#Functions to create Tags
Library   ../TestCases/Admin/Tag/Delete_Tags.py
Library   ../TestCases/Admin/Tag/CreateTag.py

Library   ../Master/CloseBrowser.py
*** Test Cases ***
TC0 - User Login
    User Login

TC01 - Delete Tag

	Main DeleteAll

TC02 - Create Tag

	CreateTag And Search In List

Close Browser
    Close Browser Suite

    
    
    
    
    
    
    
    
    
    
    
    
