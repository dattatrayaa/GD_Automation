*** Settings ***
Force Tags      Admin

#Config
Library   ../Master/BaseTestClass.py

#Functions to create User Attribute

Library   ../TestCases/Admin/UserAttributes/UserAttributeCheckboxWithReq.py
Library   ../TestCases/Admin/UserAttributes/UserAttributeWithoutCheckbox.py
Library   ../TestCases/Admin/UserAttributes/UserAttributeDateWithReq.py
Library   ../TestCases/Admin/UserAttributes/UserAttributeDateWithoutReq.py
Library   ../TestCases/Admin/UserAttributes/UserAttributeListWithReq.py
Library   ../TestCases/Admin/UserAttributes/UserAttributeListWithoutReq.py
Library   ../TestCases/Admin/UserAttributes/UserAttributeNumWithReq.py
Library   ../TestCases/Admin/UserAttributes/UserAttributeNumWithoutReq.py
Library   ../TestCases/Admin/UserAttributes/UserAttributeTextWithReq.py
Library   ../TestCases/Admin/UserAttributes/UserAttributeTextWithoutReq.py
Library   ../TestCases/Admin/UserAttributes/UserAttributeUserReferenceWithReq.py
Library   ../TestCases/Admin/UserAttributes/UserAttributeUserReferenceWithoutReq.py
Library   ../TestCases/Admin/UserAttributes/UserAttributeWithEmail.py
Library   ../TestCases/Admin/UserAttributes/UserAttributeWithoutEmail.py



*** Test Cases ***
TC1 - User Login
    User Login

TC2 - UserAttributeListWithReq
    Create List Attribute With Required Field
    
TC3 - UserAttributeListWithoutReq
    Create List Attribute Without Required Field
           
TC4 - UserAttributeNumWithReq
    Create Number Attribute With Req
    
TC5 - UserAttributeNumWithoutReq
    Create Number Attribute Without Req
    
TC6 - UserAttributeTextWithReq
    Create Text Attribute With Req
    
TC7 - UserAttributeTextWithoutReq
    Create Text Attribute Without Req
    
TC8 - UserAttributeCheckboxWithReq
    Create Check Box Attribute With Req
    
TC9 - UserAttributeWithoutCheckbox
    Create Check Box Attribute Without Req
    
TC10 - UserAttributeDateWithReq
    Create Date Attribute With Req
    
TC11 - UserAttributeDateWithoutReq
    Create Date Attribute Without Req
    
TC12 - UserAttributeWithEmail
    Create Email Attribute With Req
    
TC13 - UserAttributeWithoutEmail
    Create Email Attribute Without Req
    
TC14 - UserAttributeUserReferenceWithReq
    Create User Reference Attribute With Required Field
    
TC15 - UserAttributeUserReferenceWithoutReq
    Create User Reference Attribute Without Required Field

    

    
    
    
    
    
    
    
    
    
    
    
    
