from email import Encoders
from email.MIMEBase import MIMEBase
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
import glob
import os
import smtplib
from time import strftime
#from BaseTestClass import emailPath
from BaseTestClass import driver

class SendEmailWithAttachment:

        
    def send_mail_with_attachment(self,from_user,from_password,to, subject, text,attach,attach1):
        
        msg = MIMEMultipart()
    
        msg['From'] = from_user
        msg['To'] = to
        msg['Subject'] = subject

        msg.attach(MIMEText(text))


        part = MIMEBase('application', 'octet-stream')
        part.set_payload(open(attach, 'rb').read())
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition',
               'attachment; filename="%s"' % os.path.basename(attach))
        
        msg.attach(part)
        

        part = MIMEBase('application', 'octet-stream')
        part.set_payload(open(attach1, 'rb').read())
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition',
               'attachment; filename="%s"' % os.path.basename(attach1))
        msg.attach(part)
        
        
        
        

        mailServer = smtplib.SMTP("smtp.gmail.com", 587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(from_user, from_password)
        mailServer.sendmail(from_user, to, msg.as_string())
        # Should be mailServer.quit(), but that crashes...
        mailServer.close()
        print "Mail successfully sent"

   
        
    def sendMail(self,reportfile,logfile):
        #sf=strftime("%Y%m%d-%H%M")
        #print sf
        

 
        emailBody="Please find the Automation test execution results in the attached file. Download the file and open to view the attachment."
        subject="Robot Results - Test summary as on "+strftime("%d"+'/'+"%m"+'/'+"%Y")
        g=glob.glob(r'/Users/automation/Downloads/TeamCity/buildAgent/work/a27c680be862cb8f/Test_Results/'+reportfile+'.html') 
        g1=glob.glob(r'/Users/automation/Downloads/TeamCity/buildAgent/work/a27c680be862cb8f/Test_Results/'+logfile+'.html') 
        s=SendEmailWithAttachment()
        s.send_mail_with_attachment("gdtestautomation@gmail.com","Grovo123!", "gdtestautomation@gmail.com", subject,
                            emailBody, g[0],g1[0])

if __name__ == '__main__':
    
    sf=strftime("%Y%m%d-%H%M")
    print sf
    g=glob.glob(r'../RobotSuite/report-'+sf+ '*.html') 
    #s=SendEmailUtility()
    #s.send_mail_with_attachment("dattatrayaa@datatemplate.in", "password", "sheethuc@datatemplate.in", 
                            #"Robot results trial", "This is Sample attachment", g[0])
        
        
        
        
        
        
