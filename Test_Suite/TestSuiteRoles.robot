*** Settings ***
Force Tags      Admin

#Config
Library   ../Master/BaseTestClass.py

Library   ../TestCases/Admin/Roles/CreateAdministratorAll.py
Library   ../TestCases/Admin/Roles/CreateAdministratorBranding.py
Library   ../TestCases/Admin/Roles/CreateAdministratorBrandIntegrate.py
Library   ../TestCases/Admin/Roles/CreateAdministratorContent.py
Library   ../TestCases/Admin/Roles/CreateAdministratorContentRoleTagBrand.py
Library   ../TestCases/Admin/Roles/CreateAdministratorContentRoleTagBrandIntegrate.py

Library      ../TestCases/Admin/Roles/CreateAdministratorContentTagBrandIntegrate.py
Library       ../TestCases/Admin/Roles/CreateAdministratorContentTagIntegrate.py
Library      ../TestCases/Admin/Roles/CreateAdministratorIntegrate.py
Library     ../TestCases/Admin/Roles/CreateAdministratorRole.py
Library    ../TestCases/Admin/Roles/CreateAdministratorRoleTag.py
Library   ../TestCases/Admin/Roles/CreateAdministratorRoleTagBrandIntegrate.py
Library    ../TestCases/Admin/Roles/CreateAdministratorTag.py
Library   ../TestCases/Admin/Roles/CreateAdministratorTagBrandIntegrate.py
Library     ../TestCases/Admin/Roles/CreateAdministratorUser.py
 Library  ../TestCases/Admin/Roles/CreateAdministratorUserBranding.py
 Library  ../TestCases/Admin/Roles/CreateAdministratorUserContent.py
 Library  ../TestCases/Admin/Roles/CreateAdministratorUserContentBrandIntegrate.py
 Library  ../TestCases/Admin/Roles/CreateAdministratorUserContentRole.py
 Library   ../TestCases/Admin/Roles/CreateAdministratorUserContentRoleBrandIntegrate.py
 Library   ../TestCases/Admin/Roles/CreateAdministratorUserContentRoleIntegrate.py
 Library   ../TestCases/Admin/Roles/CreateAdministratorUserContentRoleTag.py
 Library  ../TestCases/Admin/Roles/CreateAdministratorUserContentRoleTagBranding.py
 Library    ../TestCases/Admin/Roles/CreateAdministratorUserContentTagBrand.py
 Library   ../TestCases/Admin/Roles/CreateAdministratorUserContentTagBrandIntegrate.py
 Library    ../TestCases/Admin/Roles/CreateAdministratorUserIntegrate.py
 Library   ../TestCases/Admin/Roles/CreateAdministratorUserRole.py
 Library    ../TestCases/Admin/Roles/CreateAdministratorUserRoleBrand.py
 Library    ../TestCases/Admin/Roles/CreateAdministratorUserTagBrandIntegrate.py
 Library     ../TestCases/Admin/Roles/CreateReporterRole.py
 Library    ../TestCases/Admin/Roles/CreateRole.py
 Library   ../TestCases/Admin/Roles/LearnAdministratorBranding.py
 Library   ../TestCases/Admin/Roles/LearnAdministratorBrandIntegrate.py
 Library   ../TestCases/Admin/Roles/LearnAdministratorContenRoleTagBrand.py
 Library     ../TestCases/Admin/Roles/LearnAdministratorContent.py
 Library    ../TestCases/Admin/Roles/LearnAdministratorContentRoleTagBrandIntegrate.py
 Library   ../TestCases/Admin/Roles/LearnAdministratorContentTagBrandIntegrate.py
 Library   ../TestCases/Admin/Roles/LearnAdministratorContentTagIntegrate.py
 Library   ../TestCases/Admin/Roles/LearnAdministratorIntegrate.py
 Library   ../TestCases/Admin/Roles/LearnAdministratorRole.py
 Library   ../TestCases/Admin/Roles/LearnAdministratorRoleTag.py
 Library    ../TestCases/Admin/Roles/LearnAdministratorRoleTagBrandIntegrate.py
Library      ../TestCases/Admin/Roles/LearnAdministratorTag.py
 Library   ../TestCases/Admin/Roles/LearnAdministratorTagBrandIntegrate.py
 Library    ../TestCases/Admin/Roles/LearnAdministratorUser.py
Library    ../TestCases/Admin/Roles/LearnAdministratorUserBranding.py
Library    ../TestCases/Admin/Roles/LearnAdministratorUserContent.py
Library    ../TestCases/Admin/Roles/LearnAdministratorUserContentBrandIntegrate.py
Library     ../TestCases/Admin/Roles/LearnAdministratorUserContentRole.py
Library   ../TestCases/Admin/Roles/LearnAdministratorUserContentRoleBrandIntegrate.py
Library    ../TestCases/Admin/Roles/LearnAdministratorUserContentRoleIntegrate.py
Library     ../TestCases/Admin/Roles/LearnAdministratorUserContentRoleTag.py
Library   ../TestCases/Admin/Roles/LearnAdministratorUserContentRoleTagBrand.py
Library    ../TestCases/Admin/Roles/LearnAdministratorUserContentTagBrand.py
Library    ../TestCases/Admin/Roles/LearnAdministratorUserContentTagBrandIntegrate.py
Library    ../TestCases/Admin/Roles/LearnAdministratorUserIntegrate.py
Library     ../TestCases/Admin/Roles/LearnAdministratorUserRole.py
Library   ../TestCases/Admin/Roles/LearnAdministratorUserRoleBrand.py
Library    ../TestCases/Admin/Roles/LearnAdministratorUserTagBrandIntegrate.py
Library    ../TestCases/Admin/Roles/LearnCreateRole.py
Library    ../TestCases/Admin/Roles/LearnRole.py
Library   ../TestCases/Admin/Roles/ReportAdministratorAll.py
Library    ../TestCases/Admin/Roles/ReportRole.py
Library  ../TestCases/Admin/Roles/AssignReport.py
Library   ../TestCases/Admin/Roles/AssignRole.py
Library  ../TestCases/Admin/Roles/AdministratorAll.py
Library  ../TestCases/Admin/Roles/AssignAdministratorAll.py
Library   ../TestCases/Admin/Roles/DeleteRole.py
Library  ../TestCases/Admin/Roles/AssignAdministratorBranding.py
Library  ../TestCases/Admin/Roles/AssignAdministratorBrandIntegrate.py
Library  ../TestCases/Admin/Roles/AssignAdministratorContent.py
Library   ../TestCases/Admin/Roles/AssignAdministratorContentRoleTagBrand.py
Library   ../TestCases/Admin/Roles/AssignAdministratorContentRoleTagBrandIntegrate.py
Library    ../TestCases/Admin/Roles/AssignAdministratorContentTagIntegrate.py
Library    ../TestCases/Admin/Roles/AssignAdministratorContentTagBrandIntegrate.py
Library   ../TestCases/Admin/Roles/AssignAdministratorIntegrate.py
Library     ../TestCases/Admin/Roles/AssignAdministratorRole.py
Library    ../TestCases/Admin/Roles/AssignAdministratorRoleTag.py
Library   ../TestCases/Admin/Roles/AssignAdministratorRoleTagBrandIntegrate.py
Library   ../TestCases/Admin/Roles/AssignAdministratorTag.py
Library   ../TestCases/Admin/Roles/AssignAdministratorTagBrandIntegrate.py
Library   ../TestCases/Admin/Roles/AssignAdministratorUser.py
Library   ../TestCases/Admin/Roles/AssignAdministratorUserBranding.py
Library    ../TestCases/Admin/Roles/AssignAdministratorUserContent.py
Library   ../TestCases/Admin/Roles/AssignAdministratorUserContentBrandIntegrate.py
Library  ../TestCases/Admin/Roles/AssignAdministratorUserContentRole.py
Library  ../TestCases/Admin/Roles/AssignAdministratorUserContentRoleBrandIntegrate.py
Library  ../TestCases/Admin/Roles/AssignAdministratorUserContentRoleIntegrate.py
Library     ../TestCases/Admin/Roles/AssignAdministratorUserContentRoleTag.py
Library  ../TestCases/Admin/Roles/AssignAdministratorUserContentRoleTagBranding.py
Library  ../TestCases/Admin/Roles/AssignAdministratorUserContentTagBrand.py
Library   ../TestCases/Admin/Roles/AssignAdministratorUserContentTagBrandIntegrate.py
Library   ../TestCases/Admin/Roles/AssignAdministratorUserIntegrate.py
Library   ../TestCases/Admin/Roles/AssignAdministratorUserRole.py
Library    ../TestCases/Admin/Roles/AssignAdministratorUserRoleBrand.py
Library   ../TestCases/Admin/Roles/AssignAdministratorUserTagBrandIntegrate.py
Library  ../TestCases/Admin/Roles/ReportAdministratorBranding.py
Library   ../TestCases/Admin/Roles/ReportAdministratorBrandIntegrate.py
Library   ../TestCases/Admin/Roles/ReportAdministratorContent.py
Library   ../TestCases/Admin/Roles/ReportAdministratorContentRoleTagBrand.py
Library  ../TestCases/Admin/Roles/ReportAdministratorContentRoleTagBrandIntegrate.py
Library   ../TestCases/Admin/Roles/ReportAdministratorContentTagIntegrate.py
Library   ../TestCases/Admin/Roles/ReportAdministratorIntegrate.py
Library   ../TestCases/Admin/Roles/ReportAdministratorRole.py
Library   ../TestCases/Admin/Roles/ReportAdministratorRoleTag.py
Library   ../TestCases/Admin/Roles/ReportAdministratorRoleTagBrandIntegrate.py
Library    ../TestCases/Admin/Roles/ReportAdministratorTag.py
Library    ../TestCases/Admin/Roles/ReportAdministratorTagBrandIntegrate.py
Library  ../TestCases/Admin/Roles/ReportAdministratorUser.py
Library   ../TestCases/Admin/Roles/ReportAdministratorUserBranding.py
Library   ../TestCases/Admin/Roles/ReportAdministratorUserContent.py
Library   ../TestCases/Admin/Roles/ReportAdministratorUserContentBrandIntegrate.py
Library     ../TestCases/Admin/Roles/ReportAdministratorUserContentRole.py
Library    ../TestCases/Admin/Roles/ReportAdministratorUserContentRoleIntegrate.py
Library   ../TestCases/Admin/Roles/ReportAdministratorUserContentRoleBrandIntegrate.py
Library   ../TestCases/Admin/Roles/ReportAdministratorUserContentRoleTag.py
Library   ../TestCases/Admin/Roles/ReportAdministratorUserContentRoleTagBranding.py
Library    ../TestCases/Admin/Roles/ReportAdministratorUserContentTagBrand.py
Library   ../TestCases/Admin/Roles/ReportAdministratorUserContentTagBrandIntegrate.py
Library     ../TestCases/Admin/Roles/ReportAdministratorUserIntegrate.py
Library     ../TestCases/Admin/Roles/ReportAdministratorUserRole.py
Library    ../TestCases/Admin/Roles/ReportAdministratorUserRoleBrand.py
Library    ../TestCases/Admin/Roles/ReportAdministratorUserTagBrandIntegrate.py
Library   ../TestCases/Admin/Roles/LearnAssignCreateReportAdministratorAllRole.py
Library   ../TestCases/Admin/Roles/LearnAssignCreateReportAdministratorAllRole.py
Library   ../TestCases/Admin/Roles/LearnAssignCreateReportAdministratorBranding.py
Library   ../TestCases/Admin/Roles/LearnAssignCreateReportAdministratorBrandIntegrate.py
Library   ../TestCases/Admin/Roles/LearnAssignCreateReportAdministratorContent.py
Library   ../TestCases/Admin/Roles/LearnAssignCreateReportAdministratorContentRoleTagBrand.py
Library   ../TestCases/Admin/Roles/LearnAssignCreateReportAdministratorContentRoleTagBrandIntegrate.py
Library   ../TestCases/Admin/Roles/LearnAssignCreateReportAdministratorContentTagBrandIntegrate.py
Library    ../TestCases/Admin/Roles/LearnAssignCreateReportAdministratorContentTagIntegrate.py
Library   ../TestCases/Admin/Roles/LearnAssignCreateReportAdministratorIntegrate.py
Library   ../TestCases/Admin/Roles/LearnAssignCreateReportAdministratorRole.py
Library     ../TestCases/Admin/Roles/LearnAssignCreateReportAdministratorRoleTag.py
Library   ../TestCases/Admin/Roles/LearnAssignCreateReportAdministratorRoleTagBrandIntegrate.py
Library    ../TestCases/Admin/Roles/LearnAssignCreateReportAdministratorTag.py
Library    ../TestCases/Admin/Roles/LearnAssignCreateReportAdministratorTagBrandIntegrate.py
Library   ../TestCases/Admin/Roles/LearnAssignCreateReportAdministratorUser.py
Library   ../TestCases/Admin/Roles/LearnAssignCreateReportAdministratorUserBranding.py
Library    ../TestCases/Admin/Roles/LearnAssignCreateReportAdministratorUserContent.py
Library  ../TestCases/Admin/Roles/LearnAssignCreateReportAdministratorUserContentBrandIntegrate.py
Library    ../TestCases/Admin/Roles/LearnAssignCreateReportAdministratorUserContentRole.py
Library    ../TestCases/Admin/Roles/LearnAssignCreateReportAdministratorUserContentRoleBrandIntegrate.py
Library     ../TestCases/Admin/Roles/LearnAssignCreateReportAdministratorUserContentRoleIntegrate.py
Library    ../TestCases/Admin/Roles/LearnAssignCreateReportAdministratorUserContentRoleTag.py
Library      ../TestCases/Admin/Roles/LearnAssignCreateReportAdministratorUserContentRoleTagBrand.py
Library    ../TestCases/Admin/Roles/LearnAssignCreateReportAdministratorUserContentTagBrand.py
Library      ../TestCases/Admin/Roles/LearnAssignCreateReportAdministratorUserContentTagBrandIntegrate.py
Library    ../TestCases/Admin/Roles/LearnAssignCreateReportAdministratorUserIntegrate.py
Library    ../TestCases/Admin/Roles/LearnAssignCreateReportAdministratorUserRole.py
Library   ../TestCases/Admin/Roles/LearnAssignCreateReportAdministratorUserRoleBrand.py
Library    ../TestCases/Admin/Roles/LearnAssignCreateReportAdministratorUserTagBrandIntegrate.py
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


    

    
    
    
    
    
    
    
    
    
    
    
    
