from datetime import date, datetime
import os
import sys
import smtplib
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Importing Connection String Parameters
try:
  load_dotenv('.env')
except:
  sys.exit('Environmental File not loaded.')
SERVICE_USER = os.getenv('SERVICE_USER')
SERVICE_PASSWORD = os.getenv('SERVICE_PASSWORD')
SERVICE_HOST = os.getenv('SERVICE_HOST')
SERVICE_PORT = os.getenv('SERVICE_PORT')

class Message:
   
    """
    Designed to allow you to create and send emails

    Args:
        emailto: Intended recipient list; emails separated by comma
        emailsubject: Subject of your email
        emailbody: The body of your email 
        mail_attachment: The file that you are attaching (optional)
        mail_attachment_name: The name of the file that you are attaching (optional)
        emaillcc: Intended cc recipient list; emails separated by comma (optional)
        mimemsg: The actual message. email method cares for creation of this object
        success: P / F . P indicates a Pass, F a Failure. Intended for auto generated emails
                 Failure will provide a date time stamp with an attachment. (optional)

    Usage:
        Instantiate the message object, then email() it.
    
    Example:
        message_example = Message('John.Doe@Example.com','Test','This is a test email.')
        message_example.email()
    """

    def __init__(self,emailto,emailsubject,emailbody,mail_attachment=None,mail_attachment_name=None,emailcc=None,mimemsg=None,success=None):
        self.emailto = emailto
        self.emailsubject = emailsubject
        self.emailbody = emailbody
        self.mail_attachment = mail_attachment
        self.mail_attachment_name = mail_attachment_name
        self.emailcc = emailcc
        self.mimemsg = mimemsg
        self.success = success

    def email(self):
        # Compostion of the email message and sending
        go_time = (datetime.now()).strftime('%d/%m/%Y %H:%M')
        main_file = os.path.basename(sys.argv[0])[:-3]
        mimemsg = MIMEMultipart()
        mimemsg['From']= SERVICE_USER
        mimemsg['To']= self.emailto
        if self.emailcc is not None:
            mimemsg['CC'] = self.emailcc
        # Coding in automated completion verbiage
        if self.success in ('p','P'):
            self.emailsubject = f'{main_file}  Completion'
            self.emailbody = f'''
            Greetings, Script ran and completed at: 
            {go_time} 
            with no issues at all.
            '''
        elif self.success in ('f','F'):
            self.emailsubject = f'{main_file} - Failure'
            self.emailbody = f'''Script failed at:
             {go_time}.
            Attached is the current log file.'''

        mimemsg['Subject'] = self.emailsubject
        mimemsg.attach(MIMEText(self.emailbody, 'plain'))
        if self.mail_attachment is not None and self.mail_attachment_name is not None:
            with open(self.mail_attachment, "rb") as attachment:
                mimefile = MIMEBase('application', 'octet-stream')
                mimefile.set_payload((attachment).read())
                encoders.encode_base64(mimefile)
                mimefile.add_header('Content-Disposition', "attachment; filename= %s" % self.mail_attachment_name)
                mimemsg.attach(mimefile)
                self.mimemsg = mimemsg
                self.send_it()
        else:
            self.mimemsg = mimemsg
            self.send_it()

    def send_it(self):
        # Mechanics to send the email
        username = SERVICE_USER
        password = SERVICE_PASSWORD
        connection = smtplib.SMTP(host=SERVICE_HOST, port=SERVICE_PORT)
        connection.starttls()
        connection.login(username,password)
        connection.send_message(self.mimemsg)
        connection.quit()


if __name__ == '__main__':

print('Though you can use this as a stand alone script, it is better to import it!')
