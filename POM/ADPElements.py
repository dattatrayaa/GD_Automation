'''
Created on 02-Jul-2018

@author: geethukn
'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xlrd

from BaseTestClass import driver

class ADPXpath:
    def adminMenu(self):
        time.sleep(2)
        return "(//a[@href='/admin/users'])[1]"
    
    def integrationMenu(self):
        time.sleep(2)
        return ".//*[@id='content']/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/div/ul/li[7]/a"
    
    def adpConfigure_Button(self):
        time.sleep(2)
        return ".//*[@id='content']/div/div[3]/div[2]/div/div/section[1]/div/div[1]/div[1]/button"
    
    def goToADP(self):
        time.sleep(2)
        return "html/body/div[4]/div/div/div[2]/div/div/button"
    
    def adpBuyNow(self):
        time.sleep(2)
        return ".//*[@id='main']/div/section/div/div[1]/div/div[2]/div[2]/div/div[2]/menu/button"
    
    def adpLoginusename(self):
        time.sleep(2)
        return "//*[@id='user_id']"
    def adpLoginpassword(self):
        time.sleep(2)
        return "//*[@id='password']"
    def adpsigninbutton(self):
        time.sleep(2)
        return "html/body/div[2]/div[1]/div[1]/div[2]/div/form/div[4]/button/span"
    
    def discountCode(self):
        time.sleep(2)
        return "//*[@id='id2c']"
    
    def apply(self):
        time.sleep(2)
        return "//*[@id='id9']/span"
    
    def continuebutton(self):
        time.sleep(2)
        return "//*[@id='id19']/span"
    
    def grovoidcopy(self):
        time.sleep(2)
        return"html/body/div[4]/div/div/div[2]/div/div/div[1]/div/button[1]"
    
    def grovoorganizationidcopy(self):
        time.sleep(2)
        return"html/body/div[4]/div/div/div[2]/div/div/div[1]/div/button[2]"
    
    def adpuserid(self):
        time.sleep(2)
        return"//*[@id='id58']"
    
    def enterpriseid(self):
        time.sleep(2)
        return"//*[@id='id57']"
    
    def continuebuttonafteradding(self):
        time.sleep(2)
        return"//*[@id='id50']/span"
    
    def agreeToTermsCheckbox(self):
        time.sleep(2)
        return"//*[@id='agreeToTermsCheckbox']"
    
    def placeOrder(self):
        time.sleep(2)
        return"//*[@id='placeOrder']/span"
    
    def gotomyapps(self):
        time.sleep(2)
        return"//*[@id='return']/span"
    
    def connectbutton(self):
        time.sleep(2)
        return"html/body/div[4]/div/div/div[2]/div/div/button"
    
    def consenturl(self):
        time.sleep(2)
        return"html/body/div[4]/div/div/div[2]/div/div[2]/div/a"
    
    def managebutton(self):
        time.sleep(2)
        return"//*[@id='app']/div/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div[2]/table/tbody/tr[1]/td[5]/div/button/span"
    
    def allowbutton(self):
        time.sleep(2)
        return"html/body/div[2]/div/div[2]/div/div/div/div/div[3]/div[2]/div/button[1]/span"
    
    def continuefromconsent(self):
        time.sleep(2)
        return"html/body/div[2]/div/div[2]/div/div/div/div/div[3]/div[1]/div/div/div[3]/button/span"
    
    def search(self):
        time.sleep(2)
        return "//*[@id='attributes-search']"
    
    
    def userfield_checkbox(self):
        
        userfield_checkbox = "html/body/div[4]/div/div/div[2]/div/div[1]/table/thead/tr/th[1]/div/label/span[2]"
        return userfield_checkbox
    
    def nextbutton_selectscreen(self):
        
        nextbutton_selectscreen= "html/body/div[4]/div/div/div[2]/div/div[3]/button[1]"
        return nextbutton_selectscreen
    
    def syncbutton_confirmscreen(self):
        
        syncbutton_confirmscreen= "html/body/div[4]/div/div/div[2]/div/div[2]/button"
        return syncbutton_confirmscreen
    
    def checknow_link(self):
        
        checknow_link= "//*[@id='content']/div/div[2]/div/div/a"
        return checknow_link
    
    def connected_status(self):
        
        connected_status= "//*[@id='content']/div/div[3]/div[2]/div/div/section[1]/div/div[1]/div[1]/h3"
        return connected_status
      
    def users_tab(self):
        
        users_tab= ".//*[@id='content']/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/div/ul/li[1]/a"
        return users_tab   
    
    def search_users_field(self):
        
        search_users_field= ".//*[@id='search-users']"
        return search_users_field  
    
    def user_attributes_tab(self):
        
        user_attributes_tab = ".//*[@id='content']/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/div/ul/li[4]/a"
        return user_attributes_tab 
    
    def grovo_attributres_subtab(self):
        
        grovo_attributres_subtab = ".//*[@id='content']/div/div[3]/div[2]/div/div/ul/li[2]"
        return grovo_attributres_subtab
    
    
    def loginurladp(self):
        time.sleep(2)
        return "//*[@id='adminLogin']"
    
    def adpusername(self):
        time.sleep(2)
        return"//*[@id='USER']"
    
    
    def adpsubmit(self):
        time.sleep(2)
        return"//*[@id='registrationForm']/div[3]/div[2]"
        
    
    def adppassword(self):
        time.sleep(2)
        return"//*[@id='passwordForm:password']"
    
    
    def passwordsubmit(self):
        time.sleep(2)
        return"//*[@id='passwordForm']/div[1]/div[3]/div[2]"
    
    def adpprocess(self):
        time.sleep(2)
        return"//*[@id='Process_navItem_label']"
    
    def adphr(self):
        time.sleep(2)
        return"//*[@id='revit_layout_TabContainer_4_tablist_dijit_layout_ContentPane_25']/span[2]/span"
    
    def hireandrehire(self):
        time.sleep(2)
        return"//*[@id='Process_ttd_ProcessTabHRCategoryHireRehire']/span[2]"
    
    def quickhire(self):
        time.sleep(2)
        return"//*[@id='HireRehireIntermediatary_HireRehireTemplates_HireRehireTemplateEntryWrapper_HireRehireTemplateEntry_0.TemplateName.Value']/span"
    
    def firstnameadp(self):
        time.sleep(2)
        return"//*[@id='QuickHireReact.QuickHirePersonalInformation_0.Name.first']"
    
    def lastnameadp(self):
        time.sleep(2)
        return"//*[@id='QuickHireReact.QuickHirePersonalInformation_0.Name.last']"
    
    def hiredateadp(self):
        time.sleep(2)
        return"//*[@id='QuickHireReact.QuickHirePersonalInformation_0.HireDate']"
    
    def reasonforhire(self):
        time.sleep(2)
        return"//*[@id='QuickHireReact.QuickHirePersonalInformation_0.ReasonForHire.input']"
    
    def companycode(self):
        time.sleep(2)
        return"//*[@id='QuickHireReact.QuickHirePersonalInformation_0.CompanyCode.input']"
    
    def taxidtype(self):
        time.sleep(2)
        return"//*[@id='QuickHireReact.QuickHirePersonalInformation_0.taxId.type.input']"
    
    def taxidtypearrow(self):
        time.sleep(2)
        return"//*[@id='QuickHireReact.QuickHirePersonalInformation_0.taxId.type.button']"
    
    
    
    
    def taxidappliedfor(self):
        time.sleep(2)
        return "//*[@id='QuickHireReact.QuickHirePersonalInformation_0.taxId.appliedFor.icon']"
    
    def gender(self):
        time.sleep(2)
        return "//*[@id='QuickHireReact.QuickHirePersonalInformation_0.Gender.input']"
    
    def dob(self):
        time.sleep(2)
        return"//*[@id='QuickHireReact.QuickHirePersonalInformation_0.BirthDate']"
    
    def addressline(self):
        time.sleep(2)
        return"//*[@id='QuickHireReact.QuickHirePersonalInformation_0.QuickHireAddressaddressLine1']"
    
    
    def city(self):
        time.sleep(2)
        return"//*[@id='QuickHireReact.QuickHirePersonalInformation_0.QuickHireAddresscity']"
    
    def state(self):
        time.sleep(2)
        return"//*[@id='QuickHireReact.QuickHirePersonalInformation_0.QuickHireAddressstate.input']"
    
    
    def zipcode(self):
        time.sleep(2)
        return"//*[@id='QuickHireReact.QuickHirePersonalInformation_0.QuickHireAddresspostalCode']"
    
    def filenumber(self):
        time.sleep(2)
        return"//*[@id='QuickHireReact.QuickHireEmployment_0.QuickHireEmploymentView_0.FileNumber']"
    
    def regularpayrate(self):
        time.sleep(2)
        return"//*[@id='QuickHireReact.QuickHireEmployment_0.QuickHireEmploymentView_0.RegularPayRate']"
    
    def doneadp(self):
        time.sleep(2)
        return"//*[@id='QuickHireReact.Done.label']"
    
    def donepopup(self):
        time.sleep(2)
        return"//*[@id='medicalAutoEnrollmentDialog.Done']"
    
    def federal(self):
        time.sleep(2)
        return"//*[@id='QuickHireReact.QuickHireTax_0.FederalExemptions']"
    
    def searchadp(self):
        time.sleep(2)
        return"//*[@id='toolbarQuickSearch']"
    
    def clicksearckfn(self):
        time.sleep(2)
        return"//*[@id='enterpriseSearchSkinnyList']/div[1]/div[1]/div/div/div[1]/div[1]/a/span"
    
    def clickonname(self):
        time.sleep(2)
        return"//*[@id='wfnForm1']/table/tbody/tr[1]/td[2]/div/span[2]/a/i"
    
    def personaldetails(self):
        time.sleep(2)
        return"//*[@id='revit_layout_ContentPane_4']/table/tbody/tr[1]/td[1]/span/a/span"
    
    def waitcontacts(self):
        time.sleep(2)
        return"//*[@id='PersonalProfile20.Contact.header.Text']"
    
    def clickoncontacts(self):
        time.sleep(2)
        return"//*[@id='PersonalProfile20.Contact.header.ActionIconInner']"
    
   
    
    def enteremail(self):
        time.sleep(2)
        return"//*[@id='ContactInfo20.WorkContact_0.WorkEmail']"
    
    def doneemail(self):
        time.sleep(2)
        return"//*[@id='ContactInfo20.Save.icon']"
    

    
    def editsetting(self):
        time.sleep(2)
        return"//*[@id='content']/div/div[3]/div[2]/div/div/section[1]/div/div[1]/div[3]/div/span/button"
    
    
    def disconnectlink(self):
        time.sleep(2)
        return"html/body/div[4]/div/div/div[2]/div/div[1]/div[2]/div/span[1]"
    
    def disconnectbutton(self):
        time.sleep(2)
        return"html/body/div[4]/div/div/div[2]/div/div/button[1]"
    
    def updatesubscription(self):
        time.sleep(2)
        return"//*[@id='idf']"
    
    def cancelsubscription(self):
        time.sleep(2)
        return"//*[@id='cancel']/span"
    
    def donecancelsubscription(self):
        time.sleep(2)
        return"//*[@id='posLabel']/span"
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    

    
    

    
    
    
      
    
    
    
    
    
   
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
        
    
    
    
    
        
        
        
    
    
    
        
    
    
    
    
    
    