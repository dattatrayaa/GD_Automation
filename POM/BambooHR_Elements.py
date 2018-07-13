'''
Created on Jul 2, 2018

@author: Shavinlal E
'''
import os

import xlrd


class BambooHR_Elements:
    
    def admin_tab(self):
        
        admin_link= ".//*[@id='content']/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/a"
        return  admin_link
    
    def integrations_subtab(self):
        
        integrations_link = ".//*[@id='content']/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/div/ul/li[7]/a"
        return  integrations_link
    
    def configure_button(self):
        
        congigure_link = '//*[@id="content"]/div/div[3]/div[2]/div/div/section[1]/div/div[2]/div[1]/button'
        return congigure_link
     
    def subdomain_field(self):
        
        subdomain_field = ".//*[@id='provider-subdomain']"
        return subdomain_field
           
    def apikey_field(self):
        
        api_field = ".//*[@id='api-key']"
        return api_field
           
    def connect_button(self):
        
        connect_button = "html/body/div[4]/div/div/div[2]/div/div[1]/button"
        return connect_button
    
    def select_scree_summary(self):
        
        select_screen_summary = "html/body/div[4]/div/div/div[2]/div/div[2]/small"
        return select_screen_summary
    
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
        
        checknow_link= ".//*[@id='content']/div/div[2]/div/div/a"
        return checknow_link
    
    def connected_status(self):
        
        connected_status= ".//*[@id='content']/div/div[3]/div[2]/div/div/section[1]/div/div[2]/div[1]/h3"
        return connected_status
      
    def users_tab(self):
        
        users_tab= ".//*[@id='content']/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/div/ul/li[1]/a"
        return users_tab   
    
    def search_users_field(self):
        
        search_users_field= ".//*[@id='search-users']"
        return search_users_field   
    
    def sandbox_username(self):
        
        sandbox_username = ".//*[@id='lemail']"
        return sandbox_username
    
    def sandbox_password(self):
        
        sandbox_password = ".//*[@id='password']"
        return sandbox_password    
    
    def sandbox_login(self):
        
        sandbox_login = ".//*[@id='passwordFields']/div[3]/button"
        return sandbox_login
    
    def sandbox_dashboard(self):
        
        sandbox_dashboard = ".//*[@id='nav-tabs']/li[1]/a"
        return sandbox_dashboard
    
    
    def sandbox_accounticon(self):
        
        sandbox_accounticon = ".//*[@id='utilAccount']"
        return sandbox_accounticon    
    
    def api_key_link(self):
        
        api_key_link = "//*[@id='infoLinks']/li[4]/a"
        return api_key_link 
    
    
    def add_new_apikey(self):
        
        add_new_apikey = ".//*[@id='inside-content']/div/div/a"
        return add_new_apikey 
    
    def api_key_name(self):
        
        api_key_name = "//*[@id='name']"
        return api_key_name 
    
    def generate_key_button(self):
        
        generate_key_button = "/html/body/div[7]/div[3]/div[3]/div/button[1]"
        return generate_key_button 
    
    
        
    def copy_key_link(self):
        
        copy_key_link = "/html/body/div[7]/div[3]/div[2]/form/div[2]/div/label/span"
        return copy_key_link 
    
    def apikey_done_button(self):
        
        apikey_done_button = "/html/body/div[7]/div[3]/div[3]/div/button[1]"
        return apikey_done_button 
    
    def employees_link(self):
        
        employees_link = ".//*[@id='employeeTab']/a"
        return employees_link
    
        
    def add_employee_button(self):
        
        add_employee_button = ".//*[@id='contentTop']/div[1]/a"
        return add_employee_button
    
    def employee_number_field(self):
        
        employee_number_field = ".//*[@id='field_636-0']"
        return employee_number_field
    
    def employee_firstname_field(self):
        
        employee_firstname_field = ".//*[@id='field_1-0']"
        return employee_firstname_field
    
    def employee_lastname_field(self):
        
        employee_lastname_field = ".//*[@id='field_2-0']"
        return employee_lastname_field
    
    
    def employee_workemail_field(self):
        
        employee_workemail_field = ".//*[@id='field_15-0']"
        return employee_workemail_field
    
        
    def employee_form_save(self):
        
        employee_form_save = "//*[@id='footer-buttons']/a[1]"
        return employee_form_save   
        
    def employee_personal_tab(self):
        
        employee_personal_tab = ".//*[@id='tab_1']/a"
        return employee_personal_tab
                         
    def user_attributes_tab(self):
        
        user_attributes_tab = ".//*[@id='content']/div/div[3]/div[1]/div/nav/div/div[2]/div[6]/div/ul/li[4]/a"
        return user_attributes_tab              

    def grovo_attributres_subtab(self):
        
        grovo_attributres_subtab = ".//*[@id='content']/div/div[3]/div[2]/div/div/ul/li[2]"
        return grovo_attributres_subtab  
    
    def view_instructions_link(self):
        
        view_instructions_link = ".//*[@id='content']/div/div[3]/div[2]/div/div/section[1]/div/div[2]/div[3]/div/a"
        return view_instructions_link 
    
    def authentication_errormessage(self):
        
        authentication_errormessage = "html/body/div[4]/div/div/div[2]/div/div[2]/div[1]"
        return authentication_errormessage 
    
        
    def search_attributes_field(self):
        
        search_attributes_field = ".//*[@id='attributes-search']"
        return search_attributes_field 
    
            
    def search_attributes_field_checkbox(self):
        
        book=xlrd.open_workbook(os.path.join('Test_Data/TestData.xlsx'))
        first_sheet = book.sheet_by_name('BambooHR')
        cell1= first_sheet.cell(4,3)
        suggested_attribute_name = cell1.value
        print "Suggested attribute name is"+suggested_attribute_name
        
        search_attributes_field_checkbox = "//table/tbody/tr/td[1]/div/label/span[.='"+suggested_attribute_name+"']/../../../div/label/span[2]"
        return search_attributes_field_checkbox 
        
    def confirm_attributes_count(self):
        
        confirm_attributes_count = "html/body/div[4]/div/div/div[2]/div/h3"
        return confirm_attributes_count 
    
    def edit_button_in_confirm_screen(self):
        
        edit_button_in_confirm_screen = "html/body/div[4]/div/div/div[2]/div/h3/button"
        return edit_button_in_confirm_screen
    
    def edit_settings_link(self):
        
        edit_settings_link = ".//*[@id='content']/div/div[3]/div[2]/div/div/section[1]/div/div[2]/div[3]/div/span/button"
        return edit_settings_link 
    
        
    def disconnect_link(self):
        
        disconnect_link = "html/body/div[4]/div/div/div[2]/div/div[1]/div[2]/div[2]/span[1]"
        return disconnect_link 
    
    def disconnect_button(self):
        
        disconnect_button = "html/body/div[4]/div/div/div[2]/div/div/button[1]"
        return disconnect_button
    
    
     
     
     
    
    
    
    
