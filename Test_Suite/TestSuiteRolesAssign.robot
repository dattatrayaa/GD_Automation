*** Settings ***

#Config
Library   TestCases/BaseTestClass.py

 
Library  TestCases/AssignReport.py
Library   TestCases/AssignRole.py
Library  TestCases/AdministratorAll.py
Library  TestCases/AssignAdministratorAll.py
Library   TestCases/DeleteRole.py
Library  TestCases/AssignAdministratorBranding.py
Library  TestCases/AssignAdministratorBrandIntegrate.py
Library  TestCases/AssignAdministratorContent.py
Library   TestCases/AssignAdministratorContentRoleTagBrand.py
Library   TestCases/AssignAdministratorContentRoleTagBrandIntegrate.py
Library    TestCases/AssignAdministratorContentTagIntegrate.py
Library    TestCases/AssignAdministratorContentTagBrandIntegrate.py
Library   TestCases/AssignAdministratorIntegrate.py
Library     TestCases/AssignAdministratorRole.py
Library    TestCases/AssignAdministratorRoleTag.py
Library   TestCases/AssignAdministratorRoleTagBrandIntegrate.py
Library   TestCases/AssignAdministratorTag.py
Library   TestCases/AssignAdministratorTagBrandIntegrate.py
Library   TestCases/AssignAdministratorUser.py
Library   TestCases/AssignAdministratorUserBranding.py
Library    TestCases/AssignAdministratorUserContent.py
Library   TestCases/AssignAdministratorUserContentBrandIntegrate.py
Library  TestCases/AssignAdministratorUserContentRole.py
Library  TestCases/AssignAdministratorUserContentRoleBrandIntegrate.py
Library  TestCases/AssignAdministratorUserContentRoleIntegrate.py
Library     TestCases/AssignAdministratorUserContentRoleTag.py
Library  TestCases/AssignAdministratorUserContentRoleTagBranding.py
Library  TestCases/AssignAdministratorUserContentTagBrand.py
Library   TestCases/AssignAdministratorUserContentTagBrandIntegrate.py
Library   TestCases/AssignAdministratorUserIntegrate.py
Library   TestCases/AssignAdministratorUserRole.py
Library    TestCases/AssignAdministratorUserRoleBrand.py
Library   TestCases/AssignAdministratorUserTagBrandIntegrate.py
Library           TestCases/CloseBrowser.py


*** Test Cases ***
TC1 - User Login
    User Login
TC64-AssignReport 
    createAssignReportMain
TC65-AssignRole
    assignRoleMain
TC66- AdministratorAll   
    createAdministratorAllMain
TC67- AssignAdministratorAll 
    Create Assign Administrator All Main   
TC68-AssignAdministratorBranding
    Create Assign Administrator Branding Main
 TC69-AssignAdministratorBrandIntegrate
     Create Assign Administrator Brand Integrate Main
TC70-AssignAdministratorContent
    Create Assign Administrator Content Main
TC71-AssignAdministratorContentRoleTagBrand
    Create Assign Administrator Content Role Tag Brand Main
TC72-AssignAdministratorContentRoleTagBrandIntegrate
    Create Assign Administrator Content Role Tag Brand Integrate Main
TC73-AssignAdministratorContentTagBrandIntegrate
    Create Assign Administrator Content Tag Brand Integrate Main
TC74-AssignAdministratorContentTagIntegrate
    Create Assign Administrator Content Tag Integrate Main
TC75-AssignAdministratorIntegrate
    Create Assign Administrator Integrate Main
TC76-AssignAdministratorRole
    Create Assign Administrator Role Main
TC77-AssignAdministratorRoleTag  
    Create Assign Administrator Role Tag Main
TC78-AssignAdministratorRoleTagBrandIntegrate   
    Create Assign Administrator Role Tag Brand Integrate Main 
TC79-AssignAdministratorTag
    Create Assign Administrator Tag Main
TC80-AssignAdministratorTagBrandIntegrate
    Create Assign Administrator Tag Brand Integrate Main 
TC81-AssignAdministratorUser   
    Create Assign Administrator User Main 
TC82-AssignAdministratorUserBranding    
    Create Assign Administrator User Branding Main   
TC83-AssignAdministratorUserContent
    Create Assign Administrator User Content Main    
TC84-AssignAdministratorUserContentBrandIntegrate   
    Create Assign Administrator User Content Brand Integrate Main 
TC85-AssignAdministratorUserContentRole
    Create Assign Administrator User Content Role Main
TC86-AssignAdministratorUserContentRoleBrandIntegrate
    Create Assign Administrator User Content Role Brand Integrate Main
TC87-AssignAdministratorUserContentRoleIntegrate
    createAssignAdministratorUserContentRoleIntegrateMain
    Create Assign Administrator User Content Role Integrate Main
TC88-AssignAdministratorUserContentRoleTag
    Create Assign Administrator User Content Role Tag Main
Tc89-AssignAdministratorUserContentRoleTagBranding  
    Create Assign Administrator User Content Role Tag Branding Main 
 TC90-AssignAdministratorUserContentTagBrand 
     Maincreate User Content Tag Brand Assign Administrator
 TC-91-AssignAdministratorUserContentTagBrandIntegrate
     Create Assign Administrator User Content Tag Brand Integrate Main
 TC92-AssignAdministratorUserIntegrate
      Create Assign Administrator User Integrate Main
 TC93-AssignAdministratorUserRole
     Create Assign Administrator User Role Main
 TC94-AssignAdministratorUserRoleBrand
     Create Assign Administrator User Role Brand Main
TC95-AssignAdministratorUserTagBrandIntegrate
    Create Assign Administrator User Tag Brand Integrate Main
TC96- ReportAdministratorBranding
    Create Report Administrator Branding Main
Close Browser
    Close Browser Suite


    

    
    
    
    
    
    
    
    
    
    
    
    
