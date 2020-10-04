import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from Helper import Helper

class EmailInvitation():
  def __init__(self):
    config = Helper().LoadConfigFile()
    self.serverAddress = config['SMTPServerAddress']
    self.portNumber = config['SMTPServerPortNumber']
    self.senderEmail = config['SMTPServerSenderEmail']
    self.senderName = config['SMTPServerSenderName']
    #login, and password

    self.smtpServer = smtplib.SMTP(host = self.serverAddress, port = self.portNumber)


  def __del__(self):
    self.smtpServer.quit()
  

  def Send(self, email, eventName, message):
    try:
      emailMessage = MIMEMultipart()       # create a message

      emailMessage['From'] = "{} <{}>".format(self.senderName, self.senderEmail)
      emailMessage['To'] = email
      emailMessage['Subject'] = "Yay! You are invited to the event '{}'.".format(eventName)
          
      emailMessage.attach(MIMEText(message, 'plain'))          
      self.smtpServer.send_message(emailMessage)
    
    except Exception as ex:
      raise Exception("Error sending email.  Error: " + str(ex))
  
  
  @staticmethod
  def SampleMessage(): 
    return "You are invited!"

