*** Settings ***

#Config
Library  TestCases/G1BaseTestClass.py

#Functions for User Creation with standard roles
Library  TestCases/WithDueDefaultAllGroup.py
Library  TestCases/WithDueStandardAllgroup.py
Library  TestCases/WithoutDueDefaultAllgroup.py
Library  TestCases/WithoutDueStandardAllgroup.py
Library  TestCases/CloseBrowser.py
*** Test Cases ***
TC0 - G1 User Login
    User Login G1
   
#Test cases for User Creation with standard roles
TC01 - WithDueDefaultAllGroup
    Training Main With Due Default All Group
 TC02 -WithDueStandardAllgroup
     Training Main With Due Standard Allgroup
 TC03-WithoutDueDefaultAllgroup
     Training Main Without Due Default Allgroup
 TC04-WithoutDueStandardAllgroup
     Training Main Without Due Standard Allgroup

Close Browser
    Close Browser Suite
