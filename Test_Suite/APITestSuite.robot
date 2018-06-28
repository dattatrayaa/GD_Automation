*** Settings ***
Force Tags      API

#Config
Library   ../Master/BaseTestClass.py

#Functions for API
Library   ,,/TestCases/Admin/API/BasicInformationWithDirectRole_28.py
Library   ,,/TestCases/Admin/API/BasicInformationValidData_27.py
Library   ,,/TestCases/Admin/API/BasicInforWithMultipleRoles_33.py
Library   ,,/TestCases/Admin/API/BasicInfoPasswordCreation_35.py
Library   ,,/TestCases/Admin/API/BasicInfoWithDifferentDataType_45.py
Library   ,,/TestCases/Admin/API/AdditionalAttributeWithValidData_48.py
Library   ,,/TestCases/Admin/API/AdditionalAttributeWithBlankValues_49.py
Library   ,,/TestCases/Admin/API/BasicInformationWithoutRole_29.py
Library   ,,/TestCases/Admin/API/BasicInformationInvalidKeyAttriRole_30.py
Library   ,,/TestCases/Admin/API/BasicInformationInvalidValueAttriRole_31.py
Library   ,,/TestCases/Admin/API/BasicInformationInvalidValueAttriRole_32.py
Library   ,,/TestCases/Admin/API/BasicInformationInvalidAttributesRole_34.py
Library   ,,/TestCases/Admin/API/AdditionalAttributeWithInvalidValues_50.py
Library   ,,/TestCases/Admin/API/AdditionalAttriWithoutNodeRegion_53.py
Library   ,,/TestCases/Admin/API/CreateUserWithInvalidDirectRoles_47.py
Library   ,,/TestCases/Admin/API/CustomAttributeWithValidValues_60.py
Library   ,,/TestCases/Admin/API/DirectRoleMasterAdmin_39.py
Library   ,,/TestCases/Admin/API/UserCreationAlreadyExistingEmail_37.py
Library   ,,/TestCases/Admin/API/UserCreationwithBlankEmail_43.py
Library   ,,/TestCases/Admin/API/UserCreationWithBlankHireDate_51.py
Library   ,,/TestCases/Admin/API/UserCreationwithInvalidEmail_44.py
Library   ,,/TestCases/Admin/API/UserCreationWithInvalidEmpId_42.py
Library   ,,/TestCases/Admin/API/UserCreationWithInvalidHireDate_52.py
Library   ,,/TestCases/Admin/API/UserUpdationWithExistingEmp_38.py 
Library   ,,/TestCases/Admin/API/CreateUserBlankFMLN_46.py
Library   ../Master/APIUserDeactivate.py


*** Test Cases ***
TC0 - User Login
    User Login
 
TC01-BasicInformationValidData_27
    BasicInformationValidData_27.User Creation With Valid Data
    BasicInformationValidData_27.Logincreateuser
    BasicInformationValidData_27.Againuser Login

TC02-BasicInformationWithDirectRole_28
    BasicInformationWithDirectRole_28.User Creation With Direct Role
    BasicInformationWithDirectRole_28.Logincreateuser
    BasicInformationWithDirectRole_28.Againuser Login
      
TC03 - BasicInforWithMultipleRoles_33
    BasicInforWithMultipleRoles_33.user Creation With Multiple Roles
    BasicInforWithMultipleRoles_33.Logincreateuser 
    BasicInforWithMultipleRoles_33.Againuser Login

TC04 - BasicInfoPasswordCreation_35
    BasicInfoPasswordCreation_35.test Password Creation For User
    BasicInfoPasswordCreation_35.Logincreateuser
    BasicInfoPasswordCreation_35.Againuser Login    
   
TC05 - BasicInfoWithDifferentDataType_45
    BasicInfoWithDifferentDataType_45.user Creation With Different Data Type 
    BasicInfoWithDifferentDataType_45.Logincreateuser 
    BasicInfoWithDifferentDataType_45.Againuser Login
    
TC06 - AdditionalAttributeWithValidData_48
    AdditionalAttributeWithValidData_48.additional Attribute With Valid Data 
    AdditionalAttributeWithValidData_48.Logincreateuser 
    AdditionalAttributeWithValidData_48.Againuser Login
	
TC07 - AdditionalAttributeWithBlankValues_49
    AdditionalAttributeWithBlankValues_49.additional Attribute With Blank Values 
    AdditionalAttributeWithBlankValues_49.Logincreateuser 
    AdditionalAttributeWithBlankValues_49.Againuser Login
    
 TC08 - BasicInformationWithoutRole_29
    #BasicInformationWithoutRole_29.user Creation Without Role
    #BasicInformationWithoutRole_29.Logincreateuser
    #BasicInformationWithoutRole_29.Againuser Login   
    
 TC09 - BasicInformationInvalidKeyAttriRole_30
    BasicInformationInvalidKeyAttriRole_30.user Creation With Invalid Key Attri Role
    BasicInformationInvalidKeyAttriRole_30.Againuser Login    
 
 TC10 - BasicInformationInvalidValueAttriRole_31
    BasicInformationInvalidValueAttriRole_31.user Creation With Invalid Value Attri Role
    BasicInformationInvalidValueAttriRole_31.Againuser Login
    
 TC11 - BasicInformationInvalidValueAttriRole_32
    BasicInformationInvalidValueAttriRole_32.user Creation With Invalid Value Attri Role
     BasicInformationInvalidValueAttriRole_32.Againuser Login
 
 TC12 - BasicInformationInvalidAttributesRole_34
      BasicInformationInvalidAttributesRole_34.user Creation With Invalid Attributes Role
      BasicInformationInvalidAttributesRole_34.Againuser Login
 
 TC13 - AdditionalAttributeWithInvalidValues_50
      AdditionalAttributeWithInvalidValues_50.additional Attribute With Invalid Values
      AdditionalAttributeWithInvalidValues_50.Logincreateuser
      AdditionalAttributeWithInvalidValues_50.Againuser Login
      
 TC14 - AdditionalAttriWithoutNodeRegion_53
      AdditionalAttriWithoutNodeRegion_53.Additional Attri Without Node Region
      AdditionalAttriWithoutNodeRegion_53.Logincreateuser
      AdditionalAttriWithoutNodeRegion_53.Againuser Login    
      
      
 TC15 - CreateUserWithInvalidDirectRoles_47
      CreateUserWithInvalidDirectRoles_47.create User With Invalid Direct Roles
      CreateUserWithInvalidDirectRoles_47.Againuser Login    
      
 TC16 - CustomAttributeWithValidValues_60
      CustomAttributeWithValidValues_60.custom Attribute With Valid Data
      CustomAttributeWithValidValues_60.Logincreateuser
      CustomAttributeWithValidValues_60.Againuser Login  
      
 TC17 - DirectRoleMasterAdmin_39
      DirectRoleMasterAdmin_39.direct Role Master Admin
      DirectRoleMasterAdmin_39.Logincreateuser
      DirectRoleMasterAdmin_39.Againuser Login 
      
 TC18 - UserCreationAlreadyExistingEmail_37
      UserCreationAlreadyExistingEmail_37.user Creation Already Existing Email
      UserCreationAlreadyExistingEmail_37.Againuser Login 
      
 TC19 - CreateUserBlankFMLN_46
      CreateUserBlankFMLN_46.create User Blank FMLN
      CreateUserBlankFMLN_46.Againuser Login    
        
 TC20 - UserCreationwithBlankEmail_43
      UserCreationwithBlankEmail_43.user Creationwith Blank Email
      UserCreationwithBlankEmail_43.Againuser Login   
      
 TC21 - UserCreationWithBlankHireDate_51
      UserCreationWithBlankHireDate_51.user Creation With Blank Hire Date
      UserCreationWithBlankHireDate_51.Againuser Login 
      
 TC22- UserCreationwithInvalidEmail_44
      UserCreationwithInvalidEmail_44.user Creationwith Invalid Email
      UserCreationwithInvalidEmail_44.Againuser Login    
 
 TC23 - UserCreationWithInvalidEmpId_42
      UserCreationWithInvalidEmpId_42.user Creation With Invalid EmpId
      UserCreationWithInvalidEmpId_42.Logincreateuser
      UserCreationWithInvalidEmpId_42.Againuser Login  
      
      
 TC24 - UserCreationWithInvalidHireDate_52
      UserCreationWithInvalidHireDate_52.user Creation With Invalid Hire Date
      UserCreationWithInvalidHireDate_52.Againuser Login  
    
  TC25 - UserUpdationWithExistingEmp_38
      UserUpdationWithExistingEmp_38.user Updation With Existing Emp
      UserUpdationWithExistingEmp_38.Logincreateuser
      UserUpdationWithExistingEmp_38.Againuser Login   
APIUserDeactivate
    APIUserDeactivate.deactivateuser API
    
    
    
