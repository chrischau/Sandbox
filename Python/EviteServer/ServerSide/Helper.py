import datetime
import re
import json

class Helper:
  @staticmethod
  def ValidateTimeFormat(timeStamp, errorMessage = "Incorrect datetime format.  It should be YYYY-MM-DD HH:MM:SS"):
    try:
      datetime.datetime.strptime(timeStamp, '%Y-%m-%d %H:%M:%S')
    except ValueError:
      raise ValueError(errorMessage)
  
  
  @staticmethod
  def ValidateEmailStructure(email):
    emailRegex = "[^@]+@[^@]+\.[^@]+"

    if (not re.match(emailRegex, email)):  
      raise ValueError("Email provided '{}' is not a valid structured email.", email)     
        

  @staticmethod
  def ValidateIfNullOrEmpty(element, errorObject):
    if (element is None or str(element) == ''):
      raise ValueError("'{}' is not provided.".format(errorObject))

  
  @staticmethod
  def LoadConfigFile():
    with open("ServerSide\\config.json") as json_data_file:
      configFile = json.load(json_data_file)
    
    return configFile

  @staticmethod
  def ValidateEndTimeIsAfterStartTime(startTime, endTime):
    if (endTime < startTime):
      raise ValueError("EndTime cannot be earlier than StartTime")
    
  
  