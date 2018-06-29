*** Settings ***
Force Tags      Admin

#Config
Library   ../Master/BaseTestClass.py

Library   ../TestCases/Admin/Roles/RoleCreateAdministratorAll.py
Library   ../TestCases/Admin/Roles/RoleCreateAdministratorBranding.py
Library   ../TestCases/Admin/Roles/RoleCreateAdministratorBrandIntegrate.py
Library   ../TestCases/Admin/Roles/RoleCreateAdministratorContent.py
Library   ../TestCases/Admin/Roles/RoleCreateAdministratorContentRoleTagBrand.py
Library   ../TestCases/Admin/Roles/RoleCreateAdministratorContentRoleTagBrandIntegrate.py

Library      ../TestCases/Admin/Roles/RoleCreateAdministratorContentTagBrandIntegrate.py
Library       ../TestCases/Admin/Roles/RoleCreateAdministratorContentTagIntegrate.py
Library      ../TestCases/Admin/Roles/RoleCreateAdministratorIntegrate.py
Library     ../TestCases/Admin/Roles/RoleCreateAdministratorRole.py
Library    ../TestCases/Admin/Roles/RoleCreateAdministratorRoleTag.py
Library   ../TestCases/Admin/Roles/RoleCreateAdministratorRoleTagBrandIntegrate.py
Library    ../TestCases/Admin/Roles/RoleCreateAdministratorTag.py
Library   ../TestCases/Admin/Roles/RoleCreateAdministratorTagBrandIntegrate.py
Library     ../TestCases/Admin/Roles/RoleCreateAdministratorUser.py
 Library  ../TestCases/Admin/Roles/RoleCreateAdministratorUserBranding.py
 Library  ../TestCases/Admin/Roles/RoleCreateAdministratorUserContent.py
 Library  ../TestCases/Admin/Roles/RoleCreateAdministratorUserContentBrandIntegrate.py
 Library  ../TestCases/Admin/Roles/RoleCreateAdministratorUserContentRole.py
 Library   ../TestCases/Admin/Roles/RoleCreateAdministratorUserContentRoleBrandIntegrate.py
 Library   ../TestCases/Admin/Roles/RoleCreateAdministratorUserContentRoleIntegrate.py
 Library   ../TestCases/Admin/Roles/RoleCreateAdministratorUserContentRoleTag.py
 Library  ../TestCases/Admin/Roles/RoleCreateAdministratorUserContentRoleTagBranding.py
 Library    ../TestCases/Admin/Roles/RoleCreateAdministratorUserContentTagBrand.py
 Library   ../TestCases/Admin/Roles/RoleCreateAdministratorUserContentTagBrandIntegrate.py
 Library    ../TestCases/Admin/Roles/RoleCreateAdministratorUserIntegrate.py
 Library   ../TestCases/Admin/Roles/RoleCreateAdministratorUserRole.py
 Library    ../TestCases/Admin/Roles/RoleCreateAdministratorUserRoleBrand.py
 Library    ../TestCases/Admin/Roles/RoleCreateAdministratorUserTagBrandIntegrate.py
 Library     ../TestCases/Admin/Roles/RoleCreateReporterRole.py
 Library    ../TestCases/Admin/Roles/RoleCreateRole.py
 Library   ../TestCases/Admin/Roles/RoleLearnAdministratorBranding.py
 Library   ../TestCases/Admin/Roles/RoleLearnAdministratorBrandIntegrate.py
 Library   ../TestCases/Admin/Roles/RoleLearnAdministratorContenRoleTagBrand.py
 Library     ../TestCases/Admin/Roles/RoleLearnAdministratorContent.py
 Library    ../TestCases/Admin/Roles/RoleLearnAdministratorContentRoleTagBrandIntegrate.py
 Library   ../TestCases/Admin/Roles/RoleLearnAdministratorContentTagBrandIntegrate.py
 Library   ../TestCases/Admin/Roles/RoleLearnAdministratorContentTagIntegrate.py
 Library   ../TestCases/Admin/Roles/RoleLearnAdministratorIntegrate.py
 Library   ../TestCases/Admin/Roles/RoleLearnAdministratorRole.py
 Library   ../TestCases/Admin/Roles/RoleLearnAdministratorRoleTag.py
 Library    ../TestCases/Admin/Roles/RoleLearnAdministratorRoleTagBrandIntegrate.py
Library      ../TestCases/Admin/Roles/RoleLearnAdministratorTag.py
 Library   ../TestCases/Admin/Roles/RoleLearnAdministratorTagBrandIntegrate.py
 Library    ../TestCases/Admin/Roles/RoleLearnAdministratorUser.py
Library    ../TestCases/Admin/Roles/RoleLearnAdministratorUserBranding.py
Library    ../TestCases/Admin/Roles/RoleLearnAdministratorUserContent.py
Library    ../TestCases/Admin/Roles/RoleLearnAdministratorUserContentBrandIntegrate.py
Library     ../TestCases/Admin/Roles/RoleLearnAdministratorUserContentRole.py
Library   ../TestCases/Admin/Roles/RoleLearnAdministratorUserContentRoleBrandIntegrate.py
Library    ../TestCases/Admin/Roles/RoleLearnAdministratorUserContentRoleIntegrate.py
Library     ../TestCases/Admin/Roles/RoleLearnAdministratorUserContentRoleTag.py
Library   ../TestCases/Admin/Roles/RoleLearnAdministratorUserContentRoleTagBrand.py
Library    ../TestCases/Admin/Roles/RoleLearnAdministratorUserContentTagBrand.py
Library    ../TestCases/Admin/Roles/RoleLearnAdministratorUserContentTagBrandIntegrate.py
Library    ../TestCases/Admin/Roles/RoleLearnAdministratorUserIntegrate.py
Library     ../TestCases/Admin/Roles/RoleLearnAdministratorUserRole.py
Library   ../TestCases/Admin/Roles/RoleLearnAdministratorUserRoleBrand.py
Library    ../TestCases/Admin/Roles/RoleLearnAdministratorUserTagBrandIntegrate.py
Library    ../TestCases/Admin/Roles/RoleLearnCreateRole.py
Library    ../TestCases/Admin/Roles/RoleLearnRole.py
Library   ../TestCases/Admin/Roles/RoleReportAdministratorAll.py
Library    ../TestCases/Admin/Roles/RoleReportRole.py
Library  ../TestCases/Admin/Roles/RoleAssignReport.py
Library   ../TestCases/Admin/Roles/RoleAssignRole.py
Library  ../TestCases/Admin/Roles/RoleAdministratorAll.py
Library  ../TestCases/Admin/Roles/RoleAssignAdministratorAll.py
Library   ../TestCases/Admin/Roles/DeleteRole.py
Library  ../TestCases/Admin/Roles/RoleAssignAdministratorBranding.py
Library  ../TestCases/Admin/Roles/RoleAssignAdministratorBrandIntegrate.py
Library  ../TestCases/Admin/Roles/RoleAssignAdministratorContent.py
Library   ../TestCases/Admin/Roles/RoleAssignAdministratorContentRoleTagBrand.py
Library   ../TestCases/Admin/Roles/RoleAssignAdministratorContentRoleTagBrandIntegrate.py
Library    ../TestCases/Admin/Roles/RoleAssignAdministratorContentTagIntegrate.py
Library    ../TestCases/Admin/Roles/RoleAssignAdministratorContentTagBrandIntegrate.py
Library   ../TestCases/Admin/Roles/RoleAssignAdministratorIntegrate.py
Library     ../TestCases/Admin/Roles/RoleAssignAdministratorRole.py
Library    ../TestCases/Admin/Roles/RoleAssignAdministratorRoleTag.py
Library   ../TestCases/Admin/Roles/RoleAssignAdministratorRoleTagBrandIntegrate.py
Library   ../TestCases/Admin/Roles/RoleAssignAdministratorTag.py
Library   ../TestCases/Admin/Roles/RoleAssignAdministratorTagBrandIntegrate.py
Library   ../TestCases/Admin/Roles/RoleAssignAdministratorUser.py
Library   ../TestCases/Admin/Roles/RoleAssignAdministratorUserBranding.py
Library    ../TestCases/Admin/Roles/RoleAssignAdministratorUserContent.py
Library   ../TestCases/Admin/Roles/RoleAssignAdministratorUserContentBrandIntegrate.py
Library  ../TestCases/Admin/Roles/RoleAssignAdministratorUserContentRole.py
Library  ../TestCases/Admin/Roles/RoleAssignAdministratorUserContentRoleBrandIntegrate.py
Library  ../TestCases/Admin/Roles/RoleAssignAdministratorUserContentRoleIntegrate.py
Library     ../TestCases/Admin/Roles/RoleAssignAdministratorUserContentRoleTag.py
Library  ../TestCases/Admin/Roles/RoleAssignAdministratorUserContentRoleTagBranding.py
Library  ../TestCases/Admin/Roles/RoleAssignAdministratorUserContentTagBrand.py
Library   ../TestCases/Admin/Roles/RoleAssignAdministratorUserContentTagBrandIntegrate.py
Library   ../TestCases/Admin/Roles/RoleAssignAdministratorUserIntegrate.py
Library   ../TestCases/Admin/Roles/RoleAssignAdministratorUserRole.py
Library    ../TestCases/Admin/Roles/RoleAssignAdministratorUserRoleBrand.py
Library   ../TestCases/Admin/Roles/RoleAssignAdministratorUserTagBrandIntegrate.py
Library  ../TestCases/Admin/Roles/RoleReportAdministratorBranding.py
Library   ../TestCases/Admin/Roles/RoleReportAdministratorBrandIntegrate.py
Library   ../TestCases/Admin/Roles/RoleReportAdministratorContent.py
Library   ../TestCases/Admin/Roles/RoleReportAdministratorContentRoleTagBrand.py
Library  ../TestCases/Admin/Roles/RoleReportAdministratorContentRoleTagBrandIntegrate.py
Library   ../TestCases/Admin/Roles/RoleReportAdministratorContentTagIntegrate.py
Library   ../TestCases/Admin/Roles/RoleReportAdministratorIntegrate.py
Library   ../TestCases/Admin/Roles/RoleReportAdministratorRole.py
Library   ../TestCases/Admin/Roles/RoleReportAdministratorRoleTag.py
Library   ../TestCases/Admin/Roles/RoleReportAdministratorRoleTagBrandIntegrate.py
Library    ../TestCases/Admin/Roles/RoleReportAdministratorTag.py
Library    ../TestCases/Admin/Roles/RoleReportAdministratorTagBrandIntegrate.py
Library  ../TestCases/Admin/Roles/RoleReportAdministratorUser.py
Library   ../TestCases/Admin/Roles/RoleReportAdministratorUserBranding.py
Library   ../TestCases/Admin/Roles/RoleReportAdministratorUserContent.py
Library   ../TestCases/Admin/Roles/RoleReportAdministratorUserContentBrandIntegrate.py
Library     ../TestCases/Admin/Roles/RoleReportAdministratorUserContentRole.py
Library    ../TestCases/Admin/Roles/RoleReportAdministratorUserContentRoleIntegrate.py
Library   ../TestCases/Admin/Roles/RoleReportAdministratorUserContentRoleBrandIntegrate.py
Library   ../TestCases/Admin/Roles/RoleReportAdministratorUserContentRoleTag.py
Library   ../TestCases/Admin/Roles/RoleReportAdministratorUserContentRoleTagBranding.py
Library    ../TestCases/Admin/Roles/RoleReportAdministratorUserContentTagBrand.py
Library   ../TestCases/Admin/Roles/RoleReportAdministratorUserContentTagBrandIntegrate.py
Library     ../TestCases/Admin/Roles/RoleReportAdministratorUserIntegrate.py
Library     ../TestCases/Admin/Roles/RoleReportAdministratorUserRole.py
Library    ../TestCases/Admin/Roles/RoleReportAdministratorUserRoleBrand.py
Library    ../TestCases/Admin/Roles/RoleReportAdministratorUserTagBrandIntegrate.py
Library   ../TestCases/Admin/Roles/RoleLearnAssignCreateReportAdministratorAllRole.py
Library   ../TestCases/Admin/Roles/RoleLearnAssignCreateReportAdministratorAllRole.py
Library   ../TestCases/Admin/Roles/RoleLearnAssignCreateReportAdministratorBranding.py
Library   ../TestCases/Admin/Roles/RoleLearnAssignCreateReportAdministratorBrandIntegrate.py
Library   ../TestCases/Admin/Roles/RoleLearnAssignCreateReportAdministratorContent.py
Library   ../TestCases/Admin/Roles/RoleLearnAssignCreateReportAdministratorContentRoleTagBrand.py
Library   ../TestCases/Admin/Roles/RoleLearnAssignCreateReportAdministratorContentRoleTagBrandIntegrate.py
Library   ../TestCases/Admin/Roles/RoleLearnAssignCreateReportAdministratorContentTagBrandIntegrate.py
Library    ../TestCases/Admin/Roles/RoleLearnAssignCreateReportAdministratorContentTagIntegrate.py
Library   ../TestCases/Admin/Roles/RoleLearnAssignCreateReportAdministratorIntegrate.py
Library   ../TestCases/Admin/Roles/RoleLearnAssignCreateReportAdministratorRole.py
Library     ../TestCases/Admin/Roles/RoleLearnAssignCreateReportAdministratorRoleTag.py
Library   ../TestCases/Admin/Roles/RoleLearnAssignCreateReportAdministratorRoleTagBrandIntegrate.py
Library    ../TestCases/Admin/Roles/RoleLearnAssignCreateReportAdministratorTag.py
Library    ../TestCases/Admin/Roles/RoleLearnAssignCreateReportAdministratorTagBrandIntegrate.py
Library   ../TestCases/Admin/Roles/RoleLearnAssignCreateReportAdministratorUser.py
Library   ../TestCases/Admin/Roles/RoleLearnAssignCreateReportAdministratorUserBranding.py
Library    ../TestCases/Admin/Roles/RoleLearnAssignCreateReportAdministratorUserContent.py
Library  ../TestCases/Admin/Roles/RoleLearnAssignCreateReportAdministratorUserContentBrandIntegrate.py
Library    ../TestCases/Admin/Roles/RoleLearnAssignCreateReportAdministratorUserContentRole.py
Library    ../TestCases/Admin/Roles/RoleLearnAssignCreateReportAdministratorUserContentRoleBrandIntegrate.py
Library     ../TestCases/Admin/Roles/RoleLearnAssignCreateReportAdministratorUserContentRoleIntegrate.py
Library    ../TestCases/Admin/Roles/RoleLearnAssignCreateReportAdministratorUserContentRoleTag.py
Library      ../TestCases/Admin/Roles/RoleLearnAssignCreateReportAdministratorUserContentRoleTagBrand.py
Library    ../TestCases/Admin/Roles/RoleLearnAssignCreateReportAdministratorUserContentTagBrand.py
Library      ../TestCases/Admin/Roles/RoleLearnAssignCreateReportAdministratorUserContentTagBrandIntegrate.py
Library    ../TestCases/Admin/Roles/RoleLearnAssignCreateReportAdministratorUserIntegrate.py
Library    ../TestCases/Admin/Roles/RoleLearnAssignCreateReportAdministratorUserRole.py
Library   ../TestCases/Admin/Roles/RoleLearnAssignCreateReportAdministratorUserRoleBrand.py
Library    ../TestCases/Admin/Roles/RoleLearnAssignCreateReportAdministratorUserTagBrandIntegrate.py
Library          ../Master/CloseBrowser.py


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
TC64-AssignReport 
    createAssignReportMain
TC65-AssignRole
    assignRoleMain
TC66- AdministratorAll   
    createAdministratorAllMain
TC67- AssignAdministratorAll    
    Create Create Administrator All Main
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
    Main Create Assign Administrator Role Tag 
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


    

    
    
    
    
    
    
    
    
    
    
    
    
