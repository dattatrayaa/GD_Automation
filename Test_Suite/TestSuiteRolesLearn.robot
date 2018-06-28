*** Settings ***

#Config
Library   TestCases/BaseTestClass.py
 Library   TestCases/LearnAdministratorBranding.py
 Library   TestCases/LearnAdministratorBrandIntegrate.py
 Library   TestCases/LearnAdministratorContenRoleTagBrand.py
 Library     TestCases/LearnAdministratorContent.py
 Library    TestCases/LearnAdministratorContentRoleTagBrandIntegrate.py
 Library   TestCases/LearnAdministratorContentTagBrandIntegrate.py
 Library   TestCases/LearnAdministratorContentTagIntegrate.py
 Library   TestCases/LearnAdministratorIntegrate.py
 Library   TestCases/LearnAdministratorRole.py
 Library   TestCases/LearnAdministratorRoleTag.py
 Library    TestCases/LearnAdministratorRoleTagBrandIntegrate.py
Library      TestCases/LearnAdministratorTag.py
 Library   TestCases/LearnAdministratorTagBrandIntegrate.py
 Library    TestCases/LearnAdministratorUser.py
Library    TestCases/LearnAdministratorUserBranding.py
Library    TestCases/LearnAdministratorUserContent.py
Library    TestCases/LearnAdministratorUserContentBrandIntegrate.py
Library     TestCases/LearnAdministratorUserContentRole.py
Library   TestCases/LearnAdministratorUserContentRoleBrandIntegrate.py
Library    TestCases/LearnAdministratorUserContentRoleIntegrate.py
Library     TestCases/LearnAdministratorUserContentRoleTag.py
Library   TestCases/LearnAdministratorUserContentRoleTagBrand.py
Library    TestCases/LearnAdministratorUserContentTagBrand.py
Library    TestCases/LearnAdministratorUserContentTagBrandIntegrate.py
Library    TestCases/LearnAdministratorUserIntegrate.py
Library     TestCases/LearnAdministratorUserRole.py
Library   TestCases/LearnAdministratorUserRoleBrand.py
Library    TestCases/LearnAdministratorUserTagBrandIntegrate.py
Library    TestCases/LearnCreateRole.py
Library    TestCases/LearnRole.py
Library   TestCases/ReportAdministratorAll.py
Library    TestCases/ReportRole.py
Library   TestCases/LearnAssignCreateReportAdministratorAllRole.py
Library   TestCases/LearnAssignCreateReportAdministratorAllRole.py
Library   TestCases/LearnAssignCreateReportAdministratorBranding.py
Library   TestCases/LearnAssignCreateReportAdministratorBrandIntegrate.py
Library   TestCases/LearnAssignCreateReportAdministratorContent.py
Library   TestCases/LearnAssignCreateReportAdministratorContentRoleTagBrand.py
Library   TestCases/LearnAssignCreateReportAdministratorContentRoleTagBrandIntegrate.py
Library   TestCases/LearnAssignCreateReportAdministratorContentTagBrandIntegrate.py
Library    TestCases/LearnAssignCreateReportAdministratorContentTagIntegrate.py
Library   TestCases/LearnAssignCreateReportAdministratorIntegrate.py
Library   TestCases/LearnAssignCreateReportAdministratorRole.py
Library     TestCases/LearnAssignCreateReportAdministratorRoleTag.py
Library   TestCases/LearnAssignCreateReportAdministratorRoleTagBrandIntegrate.py
Library    TestCases/LearnAssignCreateReportAdministratorTag.py
Library    TestCases/LearnAssignCreateReportAdministratorTagBrandIntegrate.py
Library   TestCases/LearnAssignCreateReportAdministratorUser.py
Library   TestCases/LearnAssignCreateReportAdministratorUserBranding.py
Library    TestCases/LearnAssignCreateReportAdministratorUserContent.py
Library  TestCases/LearnAssignCreateReportAdministratorUserContentBrandIntegrate.py
Library    TestCases/LearnAssignCreateReportAdministratorUserContentRole.py
Library    TestCases/LearnAssignCreateReportAdministratorUserContentRoleBrandIntegrate.py
Library     TestCases/LearnAssignCreateReportAdministratorUserContentRoleIntegrate.py
Library    TestCases/LearnAssignCreateReportAdministratorUserContentRoleTag.py
Library      TestCases/LearnAssignCreateReportAdministratorUserContentRoleTagBrand.py
Library    TestCases/LearnAssignCreateReportAdministratorUserContentTagBrand.py
Library      TestCases/LearnAssignCreateReportAdministratorUserContentTagBrandIntegrate.py
Library    TestCases/LearnAssignCreateReportAdministratorUserIntegrate.py
Library    TestCases/LearnAssignCreateReportAdministratorUserRole.py
Library   TestCases/LearnAssignCreateReportAdministratorUserRoleBrand.py
Library    TestCases/LearnAssignCreateReportAdministratorUserTagBrandIntegrate.py
Library           TestCases/CloseBrowser.py


*** Test Cases ***
TC1 - User Login
    User Login
 TC32-LearnAdministratorBranding
     Create Create Administrator Branding Main
TC33-LearnAdministratorBrandIntegrate
    Create Create Administrator Brand Integrate Main
TC34-LearnAdministratorContenRoleTagBrand
    Create Learn Administrator Conten Role Tag Brand Main
TC35-LearnAdministratorContent
    Create Learn Administrator Content Main
 TC36-LearnAdministratorContentRoleTagBrandIntegrate
     Create Learn Administrator Content Role Tag Brand Integrate Main    
TC37-LearnAdministratorContentTagBrandIntegrate
    Create Learn Administrator Content Tag Brand Integrate Main
TC38-LearnAdministratorContentTagIntegrate
    Create Learn Administrator Content Tag Integrate Main
TC39- LearnAdministratorIntegrate
    Create Learn Administrator Integrate Main
TC40-LearnAdministratorRole
    Create Learn Administrator Role Main
TC41- LearnAdministratorRoleTag
    Create Learn Administrator Role Tag Main
TC42-LearnAdministratorRoleTagBrandIntegrate
    Create Learn Administrator Role Tag Brand Integrate Main
 TC43-LearnAdministratorTag
    Create Learn Administrator Tag Main
 TC44-LearnAdministratorTagBrandIntegrate
     Create Learn Administrator Tag Brand Integrate Main
 TC45-LearnAdministratorUser
     Create Learn Administrator User Main
 TC46-LearnAdministratorUserBranding
     Create Learn Administrator User Branding Main
 TC47-LearnAdministratorUserContent
     Create Learn Administrator User Content Main
 TC48-LearnAdministratorUserContentBrandIntegrate
     Create Learn Administrator User Content Brand Integrate Main
TC49-LearnAdministratorUserContentRole
    Create Learn Administrator User Content Role Main
TC50-LearnAdministratorUserContentRoleBrandIntegrate
    Create Learn Administrator User Content Role Brand Integrate Main
 TC51-LearnAdministratorUserContentRoleIntegrate
     Create Learn Administrator User Content Role Integrate Main
 TC52-LearnAdministratorUserContentRoleTag
     Create Learn Administrator User Content Role Tag Main
 TC53-LearnAdministratorUserContentRoleTagBrand
     Create Learn Administrator User Content Role Tag Brand Main
 TC54-LearnAdministratorUserContentTagBrand  
     Create Learn Administrator User Content Tag Brand Main
 TC55-LearnAdministratorUserContentTagBrandIntegrate
     Create Learn Administrator User Content Tag Brand Integrate Main
 TC56-LearnAdministratorUserIntegrate
     Create Learn Administrator User Integrate Main
 TC57-LearnAdministratorUserRole
     Create Learn Administrator User Role Main   
TC58-LearnAdministratorUserRoleBrand    
    Create Learn Administrator User Role Brand Main
 TC59-LearnAdministratorUserTagBrandIntegrate
    Create Learn Administrator User Tag Brand Integrate Main
 TC60-LearnCreateRole
     Create Learn Create Main
 TC61-LearnRole  
     Learn Role Main
 TC62-ReportAdministratorAll   
    Create Report Administrator All Main    
TC63-ReportRole    
    Report Role Main    
TC123-LearnAssignCreateReportAdministratorAllRole
    Create Learn Assign Create Report Administrator All Main
TC124- LearnAssignCreateReportAdministratorBranding
    Create Learn Assign Create Report Administrator Branding Main
TC125-LearnAssignCreateReportAdministratorBrandIntegrate
    Create Learn Assign Create Report Administrator Brand Integrate Main
TC126-LearnAssignCreateReportAdministratorContent
    Create Learn Assign Create Report Administrator Content Main
TC127-LearnAssignCreateReportAdministratorContentRoleTagBrand
    Create Learn Assign Create Report Administrator Content Role Tag Brand Main
TC128-LearnAssignCreateReportAdministratorContentRoleTagBrandIntegrate
        Create Learn Assign Create Report Administrator Content Role Tag Brand Integrate Main
TC129-LearnAssignCreateReportAdministratorContentTagBrandIntegrate
    Create Learn Assign Create Report Administrator Content Tag Brand Integrate Main
TC130-LearnAssignCreateReportAdministratorContentTagIntegrate
    Create Learn Assign Create Report Administrator Content Tag Integrate Main
TC131-LearnAssignCreateReportAdministratorIntegrate
    Create Learn Assign Create Report Administrator Integrate Main
TC132-LearnAssignCreateReportAdministratorRole
    Create Learn Assign Create Report Administrator Role Main
TC133-LearnAssignCreateReportAdministratorRoleTag
    Main Learn Assign Create Report Administrator Role Tag
TC134-LearnAssignCreateReportAdministratorRoleTagBrandIntegrate
    Create Learn Assign Create Report Administrator Role Tag Brand Integrate Main
TC135-LearnAssignCreateReportAdministratorTag
    Create Learn Assign Create Report Administrator Tag Main
TC136-LearnAssignCreateReportAdministratorTagBrandIntegrate
    Create Learn Assign Create Report Administrator Tag Brand Integrate Main
TC137-LearnAssignCreateReportAdministratorUser
    Create Learn Assign Create Report Administrator User Main
TC138-LearnAssignCreateReportAdministratorUserBranding
    Create Learn Assign Create Report Administrator User Branding Main
TC139-LearnAssignCreateReportAdministratorUserContent
    Create Learn Assign Create Report Administrator User Content Main
TC140-LearnAssignCreateReportAdministratorUserContentBrandIntegrate
    Create Learn Assign Create Report Administrator User Content Brand Integrate Main
TC141-LearnAssignCreateReportAdministratorUserContentRole
    Create Learn Assign Create Report Administrator User Content Role Main
TC142-LearnAssignCreateReportAdministratorUserContentRoleBrandIntegrate
    Create Learn Assign Create Report Administrator User Content Role Brand Integrate Main
TC143-LearnAssignCreateReportAdministratorUserContentRoleIntegrate
    Create Learn Assign Create Report Administrator User Content Role Integrate Main
TC144-LearnAssignCreateReportAdministratorUserContentRoleTag
    Create Learn Assign Create Report Administrator User Content Role Tag Main
TC145-LearnAssignCreateReportAdministratorUserContentRoleTagBrand
    Create Learn Assign Create Report Administrator User Content Role Tag Brand Main
TC146-LearnAssignCreateReportAdministratorUserContentTagBrand
    Main Learn Assign Create Report Administrator User Content Tag Brand
TC147-LearnAssignCreateReportAdministratorUserContentTagBrandIntegrate
    Create Learn Assign Create Report Administrator User Content Tag Brand Integrate Main
TC148-LearnAssignCreateReportAdministratorUserIntegrate
    Create Learn Assign Create Report Administrator User Integrate Main
TC149-LearnAssignCreateReportAdministratorUserRole
    Create Learn Assign Create Report Administrator User Role Main
TC150-LearnAssignCreateReportAdministratorUserRoleBrand
    Create Learn Assign Create Report Administrator User Role Brand Main
TC151-LearnAssignCreateReportAdministratorUserTagBrandIntegrate
    Create Learn Assign Create Report Administrator User Tag Brand Integrate Main

Close Browser
    Close Browser Suite


    

    
    
    
    
    
    
    
    
    
    
    
    
