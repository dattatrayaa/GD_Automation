*** Settings ***
Force Tags      API

#Config
Library   ../Master/BaseTestClass.py

#Functions for API
Library   ,,/TestCases/Admin/API/APIBasicInformationWithDirectRole.py
Library   ,,/TestCases/Admin/API/APIBasicInformationValidData.py
Library   ,,/TestCases/Admin/API/APIBasicInforWithMultipleRoles.py
Library   ,,/TestCases/Admin/API/APIBasicInfoPasswordCreation.py
Library   ,,/TestCases/Admin/API/APIBasicInfoWithDifferentDataType.py
Library   ,,/TestCases/Admin/API/APIAdditionalAttributeWithValidData.py
Library   ,,/TestCases/Admin/API/APIAdditionalAttributeWithBlankValues.py
Library   ,,/TestCases/Admin/API/APIBasicInformationWithoutRole.py
Library   ,,/TestCases/Admin/API/APIBasicInformationInvalidKeyAttriRole.py
Library   ,,/TestCases/Admin/API/APIBasicInformationInvalidValueAttriRole.py
Library   ,,/TestCases/Admin/API/APIBasicInformationInvalidValueAttriRole.py
Library   ,,/TestCases/Admin/API/APIBasicInformationInvalidAttributesRole.py
Library   ,,/TestCases/Admin/API/APIAdditionalAttributeWithInvalidValues.py
Library   ,,/TestCases/Admin/API/APIAdditionalAttriWithoutNodeRegion.py
Library   ,,/TestCases/Admin/API/APICreateUserWithInvalidDirectRoles.py
Library   ,,/TestCases/Admin/API/APICustomAttributeWithValidValues.py
Library   ,,/TestCases/Admin/API/APIDirectRoleMasterAdmin.py
Library   ,,/TestCases/Admin/API/APIUserCreationAlreadyExistingEmail.py
Library   ,,/TestCases/Admin/API/APIUserCreationwithBlankEmail.py
Library   ,,/TestCases/Admin/API/APIUserCreationWithBlankHireDate.py
Library   ,,/TestCases/Admin/API/APIUserCreationwithInvalidEmail.py
Library   ,,/TestCases/Admin/API/APIUserCreationWithInvalidEmpId.py
Library   ,,/TestCases/Admin/API/APIUserCreationWithInvalidHireDate.py
Library   ,,/TestCases/Admin/API/APIUserUpdationWithExistingEmp.py 
Library   ,,/TestCases/Admin/API/APICreateUserBlankFMLN.py
Library   ../Master/APIUserDeactivate.py


*** Test Cases ***
TC0 - User Login
    User Login
 
TC01-BasicInformationValidData_27
    APIBasicInformationValidData.User Creation With Valid Data
    APIBasicInformationValidData.Logincreateuser
    APIBasicInformationValidData.Againuser Login

TC02-BasicInformationWithDirectRole_28
    APIBasicInformationWithDirectRole.User Creation With Direct Role
    APIBasicInformationWithDirectRole.Logincreateuser
    APIBasicInformationWithDirectRole.Againuser Login
      
TC03 - BasicInforWithMultipleRoles_33
    APIBasicInforWithMultipleRoles.user Creation With Multiple Roles
    APIBasicInforWithMultipleRoles.Logincreateuser 
    APIBasicInforWithMultipleRoles.Againuser Login

TC04 - BasicInfoPasswordCreation_35
    APIBasicInfoPasswordCreation.test Password Creation For User
    APIBasicInfoPasswordCreation.Logincreateuser
    APIBasicInfoPasswordCreation.Againuser Login    
   
TC05 - BasicInfoWithDifferentDataType_45
    APIBasicInfoWithDifferentDataType.user Creation With Different Data Type 
    APIBasicInfoWithDifferentDataType.Logincreateuser 
    APIBasicInfoWithDifferentDataType.Againuser Login
    
TC06 - AdditionalAttributeWithValidData_48
    APIAdditionalAttributeWithValidData.additional Attribute With Valid Data 
    APIAdditionalAttributeWithValidData.Logincreateuser 
    APIAdditionalAttributeWithValidData.Againuser Login
	
TC07 - AdditionalAttributeWithBlankValues_49
    APIAdditionalAttributeWithBlankValues.additional Attribute With Blank Values 
    APIAdditionalAttributeWithBlankValues.Logincreateuser 
    APIAdditionalAttributeWithBlankValues.Againuser Login
    
 TC08 - BasicInformationWithoutRole_29
    APIBasicInformationWithoutRole.user Creation Without Role
    APIBasicInformationWithoutRole.Logincreateuser
    APIBasicInformationWithoutRole.Againuser Login   
    
 TC09 - BasicInformationInvalidKeyAttriRole_30
    APIBasicInformationInvalidKeyAttriRole.user Creation With Invalid Key Attri Role
    APIBasicInformationInvalidKeyAttriRole.Againuser Login    
 
 TC10 - BasicInformationInvalidValueAttriRole_31
    APIBasicInformationInvalidValueAttriRole.user Creation With Invalid Value Attri Role
    APIBasicInformationInvalidValueAttriRole.Againuser Login
    
 TC11 - BasicInformationInvalidValueAttriRole_32
    APIBasicInformationInvalidValueAttriRole.user Creation With Invalid Value Attri Role
     APIBasicInformationInvalidValueAttriRole.Againuser Login
 
 TC12 - BasicInformationInvalidAttributesRole_34
      APIBasicInformationInvalidAttributesRole.user Creation With Invalid Attributes Role
      APIBasicInformationInvalidAttributesRole.Againuser Login
 
 TC13 - AdditionalAttributeWithInvalidValues_50
      APIAdditionalAttributeWithInvalidValues.additional Attribute With Invalid Values
      APIAdditionalAttributeWithInvalidValues.Logincreateuser
      APIAdditionalAttributeWithInvalidValues.Againuser Login
      
 TC14 - AdditionalAttriWithoutNodeRegion_53
      APIAdditionalAttriWithoutNodeRegion.Additional Attri Without Node Region
      APIAdditionalAttriWithoutNodeRegion.Logincreateuser
      APIAdditionalAttriWithoutNodeRegion.Againuser Login    
      
      
 TC15 - CreateUserWithInvalidDirectRoles_47
      APICreateUserWithInvalidDirectRoles.create User With Invalid Direct Roles
      APICreateUserWithInvalidDirectRoles.Againuser Login    
      
 TC16 - CustomAttributeWithValidValues_60
      APICustomAttributeWithValidValues.custom Attribute With Valid Data
      APICustomAttributeWithValidValues.Logincreateuser
      APICustomAttributeWithValidValues.Againuser Login  
      
 TC17 - DirectRoleMasterAdmin_39
      APIDirectRoleMasterAdmin.direct Role Master Admin
      APIDirectRoleMasterAdmin.Logincreateuser
      APIDirectRoleMasterAdmin.Againuser Login 
      
 TC18 - UserCreationAlreadyExistingEmail_37
      APIUserCreationAlreadyExistingEmail.user Creation Already Existing Email
      APIUserCreationAlreadyExistingEmail.Againuser Login 
      
 TC19 - CreateUserBlankFMLN_46
      APICreateUserBlankFMLN.create User Blank FMLN
      APICreateUserBlankFMLN.Againuser Login    
        
 TC20 - UserCreationwithBlankEmail_43
      APIUserCreationwithBlankEmail.user Creationwith Blank Email
      APIUserCreationwithBlankEmail.Againuser Login   
      
 TC21 - UserCreationWithBlankHireDate_51
      APIUserCreationWithBlankHireDate.user Creation With Blank Hire Date
      APIUserCreationWithBlankHireDate.Againuser Login 
      
 TC22- UserCreationwithInvalidEmail_44
      APIUserCreationwithInvalidEmail.user Creationwith Invalid Email
      APIUserCreationwithInvalidEmail.Againuser Login    
 
 TC23 - UserCreationWithInvalidEmpId_42
      APIUserCreationWithInvalidEmpId.user Creation With Invalid EmpId
      APIUserCreationWithInvalidEmpId.Logincreateuser
      APIUserCreationWithInvalidEmpId.Againuser Login  
      
      
 TC24 - UserCreationWithInvalidHireDate_52
      APIUserCreationWithInvalidHireDate.user Creation With Invalid Hire Date
      APIUserCreationWithInvalidHireDate.Againuser Login  
    
  TC25 - UserUpdationWithExistingEmp_38
      APIUserUpdationWithExistingEmp.user Updation With Existing Emp
      APIUserUpdationWithExistingEmp.Logincreateuser
      APIUserUpdationWithExistingEmp.Againuser Login   
APIUserDeactivate
    APIUserDeactivate.deactivateuser API
    
    
    
