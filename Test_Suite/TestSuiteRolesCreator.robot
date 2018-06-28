*** Settings ***

#Config
Library   TestCases/BaseTestClass.py

Library   TestCases/CreateAdministratorAll.py
Library   TestCases/CreateAdministratorBranding.py
Library   TestCases/CreateAdministratorBrandIntegrate.py
Library   TestCases/CreateAdministratorContent.py
Library   TestCases/CreateAdministratorContentRoleTagBrand.py
Library   TestCases/CreateAdministratorContentRoleTagBrandIntegrate.py

Library      TestCases/CreateAdministratorContentTagBrandIntegrate.py
Library       TestCases/CreateAdministratorContentTagIntegrate.py
Library      TestCases/CreateAdministratorIntegrate.py
Library     TestCases/CreateAdministratorRole.py
Library    TestCases/CreateAdministratorRoleTag.py
Library   TestCases/CreateAdministratorRoleTagBrandIntegrate.py
Library    TestCases/CreateAdministratorTag.py
Library   TestCases/CreateAdministratorTagBrandIntegrate.py
Library     TestCases/CreateAdministratorUser.py
 Library  TestCases/CreateAdministratorUserBranding.py
 Library  TestCases/CreateAdministratorUserContent.py
 Library  TestCases/CreateAdministratorUserContentBrandIntegrate.py
 Library  TestCases/CreateAdministratorUserContentRole.py
 Library   TestCases/CreateAdministratorUserContentRoleBrandIntegrate.py
 Library   TestCases/CreateAdministratorUserContentRoleIntegrate.py
 Library   TestCases/CreateAdministratorUserContentRoleTag.py
 Library  TestCases/CreateAdministratorUserContentRoleTagBranding.py
 Library    TestCases/CreateAdministratorUserContentTagBrand.py
 Library   TestCases/CreateAdministratorUserContentTagBrandIntegrate.py
 Library    TestCases/CreateAdministratorUserIntegrate.py
 Library   TestCases/CreateAdministratorUserRole.py
 Library    TestCases/CreateAdministratorUserRoleBrand.py
 Library    TestCases/CreateAdministratorUserTagBrandIntegrate.py
 Library     TestCases/CreateReporterRole.py
 Library    TestCases/CreateRole.py
Library           TestCases/CloseBrowser.py


*** Test Cases ***
TC1 - User Login
    User Login

TC1 -CreateAdministratorAll
    
    Create Create Administrator All Main
    

TC2 -CreateAdministratorBranding
    
    Create Create Administrator Branding Main
    
TC3- CreateAdministratorBrandIntegrate
 
     Create Create Administrator Brand Integrate Main
     
TC4- CreateAdministratorContent
    
    Create Create Administrator Content Main
TC5 -CreateAdministratorContentRoleTagBrand
    Create Create Administrator Content Role Tag Brand Main
 TC6- CreateAdministratorContentRoleTagBrandIntegrate
     Create Create Administrator Content Role Tag Brand Integrate Main

TC7- CreateAdministratorContentTagBrandIntegrate
    
    Create Create Administrator Content Tag Brand Integrate Main
    
 TC8 -CreateAdministratorContentTagIntegrate
 
     Create Create Administrator Content Tag Integrate Main

TC 9- CreateAdministratorIntegrate
    Create Create Administrator Integrate Main
    
TC10- CreateAdministratorRole   
       
        Create Create Administrator Role Main
 TC11- CreateAdministratorRoleTag
     
     Main Crte Admin Role Tag
    
 TC12- CreateAdministratorRoleTagBrandIntegrate
     Create Create Administrator Role Tag Brand Integrate Main
     
 TC13- CreateAdministratorTag
     Create Create Administrator Tag Main
     
 TC14-CreateAdministratorTagBrandIntegrate
     Create Create Administrator Tag Brand Integrate Main
 TC15-CreateAdministratorUser
     Create Create Administrator User Main
     
 TC16- CreateAdministratorUserBranding
   Create Create Administrator User Branding Main
 TC17- CreateAdministratorUserContent
     Create Create Administrator User Content Main
 TC18- CreateAdministratorUserContentBrandIntegrate
     Create Create Administrator User Content Brand Integrate Main
 TC19- CreateAdministratorUserContentRole
     Create Create Administrator User Content Role Main
 TC20- CreateAdministratorUserContentRoleBrandIntegrate
     Create Create Administrator User Content Role Brand Integrate Main
TC21- CreateAdministratorUserContentRoleIntegrate
    Create Create Administrator User Content Role Integrate Main
TC22-CreateAdministratorUserContentRoleTag
     Create Create Administrator User Content Role Tag Main
TC23-CreateAdministratorUserContentRoleTagBranding
    Create Create Administrator User Content Role Tag Branding Main
 TC24- CreateAdministratorUserContentTagBrand
     Create Create Administrator User Content Tag Brand Main
 TC25- CreateAdministratorUserContentTagBrandIntegrate
     Create Create Administrator User Content Tag Brand Integrate Main
 TC26-CreateAdministratorUserIntegrate
     Create Create Administrator User Integrate Main 
 TC27-CreateAdministratorUserRole
     Create Create Administrator User Role Main
 TC28-CreateAdministratorUserRoleBrand
     Create Create Administrator User Role Brand Main
 TC29-CreateAdministratorUserTagBrandIntegrate
     Create Create Administrator User Tag Brand Integrate Main
 TC30-CreateReporterRole
     Create Create Report Role Main
 TC31-CreateRole
     Create Role Main
 TC32-LearnAdministratorBranding
     Create Create Administrator Branding Main
Close Browser
    Close Browser Suite


    

    
    
    
    
    
    
    
    
    
    
    
    
