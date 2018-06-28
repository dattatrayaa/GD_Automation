*** Settings ***
Force Tags      Admin
#Config
Library   ../Master/BaseTestClass.py
#Functions to create Group
Library           ../TestCases/Admin/Groups/GroupWithAttributesCity.py
Library           ../TestCases/Admin/Groups/GroupWithAttributesCountry.py
Library           ../TestCases/Admin/Groups/GroupWithAttributesDepartment.py
Library           ../TestCases/Admin/Groups/GroupWithAttributesHireDate.py
Library           ../TestCases/Admin/Groups/GroupWithAttributesJobTitle.py
Library           ../TestCases/Admin/Groups/GroupWithAttributesLocation.py
Library           ../TestCases/Admin/Groups/GroupWithAttributesRegion.py
Library           ../TestCases/Admin/Groups/GroupWithAttributesReportsTo.py
Library           ../TestCases/Admin/Groups/GroupWithAttributesState.py
Library           ../TestCases/Admin/Groups/GroupWithAllAttributes.py
Library           ../TestCases/Admin/Groups/GroupWithAnyAttribute.py
Library           ../TestCases/Admin/Groups/GroupWithAnyAttributesTwo.py
Library           ../TestCases/Admin/Groups/GroupWithAnyAttributesThree.py

Library           ../Master/CloseBrowser.py

*** Test Cases ***
TC00 - Login
    User Login

TC01 - GroupWithAttributesCity
    Create Group With Attribute City

TC02 - GroupWithAttributesCountry
    Create Group With Attribute Country

TC03 - GroupWithAttributesDepartment
    Create Group With Attribute Department

TC04 - GroupWithAttributesHireDate
    Create Group With Attribute Hiredate

TC05 - GroupWithAttributesJobTitle
    Create Group With Attribute Job Title

TC06 - GroupWithAttributesLocation
    Create Group With Attribute Location

TC07 - GroupWithAttributesRegion
    Create Group With Attribute Region

TC08 - GroupWithAttributesReportsTo
    Create Group With Attribute Reports To

TC09 - GroupWithAttributesState
    Create Group With Attribute State

TC10 - GroupWithAllAttributes
    Create Group With All Attributes

TC11 - GroupWithAnyAttribute
    Create Group With Any Attribute

TC12 - GroupWithAnyAttributesTwo
    Create Group With Any Attribute Two

TC13 - GroupWithAnyAttributesThree
    Create Group With Any Attribute Three

TC Close Browser
    Close Browser Suite
