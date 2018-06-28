*** Settings ***

#Config
Library   TestCases/BaseTestClass.py
Library  TestCases/ReportAdministratorBranding.py
Library   TestCases/ReportAdministratorBrandIntegrate.py
Library   TestCases/ReportAdministratorContent.py
Library   TestCases/ReportAdministratorContentRoleTagBrand.py
Library  TestCases/ReportAdministratorContentRoleTagBrandIntegrate.py
Library   TestCases/ReportAdministratorContentTagIntegrate.py
Library   TestCases/ReportAdministratorIntegrate.py
Library   TestCases/ReportAdministratorRole.py
Library   TestCases/ReportAdministratorRoleTag.py
Library   TestCases/ReportAdministratorRoleTagBrandIntegrate.py
Library    TestCases/ReportAdministratorTag.py
Library    TestCases/ReportAdministratorTagBrandIntegrate.py
Library  TestCases/ReportAdministratorUser.py
Library   TestCases/ReportAdministratorUserBranding.py
Library   TestCases/ReportAdministratorUserContent.py
Library   TestCases/ReportAdministratorUserContentBrandIntegrate.py
Library     TestCases/ReportAdministratorUserContentRole.py
Library    TestCases/ReportAdministratorUserContentRoleIntegrate.py
Library   TestCases/ReportAdministratorUserContentRoleBrandIntegrate.py
Library   TestCases/ReportAdministratorUserContentRoleTag.py
Library   TestCases/ReportAdministratorUserContentRoleTagBranding.py
Library    TestCases/ReportAdministratorUserContentTagBrand.py
Library   TestCases/ReportAdministratorUserContentTagBrandIntegrate.py
Library     TestCases/ReportAdministratorUserIntegrate.py
Library     TestCases/ReportAdministratorUserRole.py
Library    TestCases/ReportAdministratorUserRoleBrand.py
Library    TestCases/ReportAdministratorUserTagBrandIntegrate.py
Library           TestCases/CloseBrowser.py


*** Test Cases ***
TC1 - User Login
    User Login
TC96- ReportAdministratorBranding
    Create Report Administrator Branding Main
TC97-ReportAdministratorBrandIntegrate
    Create Report Administrator Brand Integrate Main
TC98-ReportAdministratorContent 
    Create Report Administrator Content Main
 TC99-ReportAdministratorContentRoleTagBrand
     Create Report Administrator Content Role Tag Brand Main
 TC100-ReportAdministratorContentRoleTagBrandIntegrate
     Create Report Administrator Content Role Tag Brand Integrate Main
TC101-ReportAdministratorContentTagIntegrate
    Maincreate Report Administrator Content Tag Integrate
 TC102-ReportAdministratorIntegrate
      Create Report Administrator Integrate Main  
TC103-ReportAdministratorRole
    Create Report Administrator Role Main
TC104-ReportAdministratorRoleTag    
    Maincreate Report Admin Role Tag
 TC105-ReportAdministratorRoleTagBrandIntegrate
    Create Report Administrator Role Tag Brand Integrate Main
 TC106-ReportAdministratorTag
     Create Report Administrator Tag Main
 TC107-ReportAdministratorTagBrandIntegrate
     Create Report Administrator Tag Brand Integrate Main
 TC108-ReportAdministratorUser
     Create Report Administrator User Main
TC109-ReportAdministratorUserBranding   
    Create Report Administrator User Branding Main 
TC110-ReportAdministratorUserContent    
    Create Report Administrator User Content Main
TC111-ReportAdministratorUserContentBrandIntegrate    
    Create Report Administrator User Content Brand Integrate Main
Tc112-ReportAdministratorUserContentRole    
    Create Report Administrator User Content Role Main
 TC113-ReportAdministratorUserContentRoleBrandIntegrate
    Create Report Administrator User Content Role Brand Integrate Main
 TC114-ReportAdministratorUserContentRoleIntegrate
     Create Report Administrator User Content Role Integrate Main
TC115-ReportAdministratorUserContentRoleTag 
     Create Report Administrator User Content Role Tag Main
Tc116-ReportAdministratorUserContentRoleTagBranding
     Create Report Administrator User Content Role Tag Branding Main
 TC117-ReportAdministratorUserContentTagBrand
     Create Report Administrator User Content Tag Brand Main
TC118-ReportAdministratorUserContentTagBrandIntegrate
        Create Report Administrator User Content Tag Brand Integrate Main
TC119-ReportAdministratorUserIntegrate 
     Create Report Administrator User Integrate Main
TC120-ReportAdministratorUserRole 
     Create Report Administrator User Role Main
TC121-ReportAdministratorUserRoleBrand     
     Create Report Administrator User Role Brand Main
TC122- ReportAdministratorUserTagBrandIntegrate
	Maincreate Report Admini User Tag Brand Integrate    
Close Browser
    Close Browser Suite


    

    
    
    
    
    
    
    
    
    
    
    
    
