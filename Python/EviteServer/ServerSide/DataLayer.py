# Data Layer class to return reults from database interaction
# This is for code separation and ease of change
from flask import Flask, json
import datetime
import sqlite3
import re
import json


class DataLayer:
  # Event related SQLs
  selectAllEventsSQL = "SELECT EventId, EventName, Location, StartTime, EndTime FROM Events"
  insertEventSQL = "INSERT INTO Events(EventName, Location, StartTime, EndTime) VALUES ('{}', '{}', '{}', '{}')"
    
  # Attendee related SQLs
  selectAllAttendeeSQL = "SELECT AttendeeId, AttendeeEmail FROM Attendees"
  insertAttendeeSQL = "INSERT INTO Attendees(AttendeeEmail) VALUES ('{}')"

  # EventsXAttendees related SQLs
  findAllEXASQL = "SELECT E.EventId, E.EventName, E.Location, E.StartTime, E.EndTime, A.AttendeeId, A.AttendeeEmail FROM Events AS E \
  JOIN EventsXAttendees AS EXA ON EXA.EventId = E.EventId \
  JOIN Attendees AS A ON EXA.AttendeeId = A.AttendeeId"

  insertEXASQL = "INSERT INTO EventsXAttendees(EventId, AttendeeId) VALUES ('{}', '{}')"
  selectEXASQL = "SELECT EventId, AttendeeId FROM EventsXAttendees"
  deleteEXASQL = "DELETE FROM EventsXAttendees WHERE EventId = {} AND AttendeeId = {}"


  def __LoadConfigFile(self):
    with open("ServerSide\\config.json") as json_data_file:
      configFile = json.load(json_data_file)
    
    return configFile

  
  def __init__(self):
    ## TODO add logging
    configFile = self.__LoadConfigFile();
    databaseName = configFile['DatabasePath']

    self.sqliteConnection = sqlite3.connect(databaseName)
    self.cursor = self.sqliteConnection.cursor()
    #print("Database created and Successfully Connected to SQLite") #TODO logging


  def FindAllEvents(self):
    self.cursor.execute(self.selectAllEventsSQL)
    results = self.cursor.fetchall()        

    return results

  
  def FindEvent(self, eventId, eventName):
    #TODO paging data if too many data at once
    if (eventId != None):
      whereClause = " WHERE EventId = {}".format(eventId)
      self.cursor.execute(self.selectAllEventsSQL + whereClause)
      results = self.cursor.fetchall()        

      return results
    
    if (eventName != None and eventName != ''):
      whereClause = " WHERE EventName = '{}'".format(eventName)
      self.cursor.execute(self.selectAllEventsSQL + whereClause)
      results = self.cursor.fetchall()        
      
      return results

    else:
      return None


  def __ValidateTimeFormat(self, timeStamp, errorMessage):
    try:
      datetime.datetime.strptime(timeStamp, '%Y-%m-%d %H:%M:%S')
    except ValueError:
      raise ValueError("Incorrect datetime format.  It should be YYYY-MM-DD HH:MM:SS")
    

  def CreateEvent(self, eventName, location, startTime, endTime):
    sqlStatement = self.selectAllEventsSQL + " WHERE EventName = '{}'".format(eventName)
    
    self.__ValidateRecordDoesNotExist(sqlStatement, "Event with the same name '{}' already exist.  Please choose another name.".format(eventName))
    self.__ValidateTimeFormat(startTime, "Incorrect Start Time datetime format.  It should be YYYY-MM-DD HH:MM:SS")
    self.__ValidateTimeFormat(endTime, "Incorrect End Time datetime format.  It should be YYYY-MM-DD HH:MM:SS")

    insertStatement = self.insertEventSQL.format(eventName, location, startTime, endTime)

    try:
      self.cursor.execute(insertStatement)
      self.sqliteConnection.commit()

    except Exception as ex:
      self.sqliteConnection.rollback()
      raise ValueError("An error has occurred on the database interaction.  Changes have been rolled back.  \nError Message:" + str(ex))


  def CreateAttendee(self, email):
    sqlStatement = self.selectAllAttendeeSQL + " WHERE AttendeeEmail = '{}'".format(email)
    
    self.__ValidateRecordDoesNotExist(sqlStatement, "Attendee with the same email '{}' already exist.  Please verify and adjust accordingly.".format(email))
    self.__ValidateEmailStructure(email)    

    insertStatement = self.insertAttendeeSQL.format(email)

    try:
      self.cursor.execute(insertStatement)
      self.sqliteConnection.commit()

    except Exception as ex:
      self.sqliteConnection.rollback()
      raise ValueError("An error has occurred on the database interaction.  Changes have been rolled back.  \nError Message:" + str(ex))


  def FindAllAttendees(self):
    self.cursor.execute(self.selectAllAttendeeSQL)
    results = self.cursor.fetchall()        
    
    return results

  
  def FindAttendee(self, email):
    #TODO paging data if too many data at once
    if (email != None and email != ''):
      whereClause = " WHERE AttendeeEmail = '{}'".format(email)
      self.cursor.execute(self.selectAllAttendeeSQL + whereClause)
      results = self.cursor.fetchall()        

      return results

    else:
      return None


  def __ValidateEmailStructure(self, email):
    emailRegex = "[^@]+@[^@]+\.[^@]+"

    if (not re.match(emailRegex, email)):  
      raise ValueError("Email provided '{}' is not a valid structured email.", email)     
        

  def __ValidateRecordDoesNotExist(self, sqlStatement, errorMessage):
    self.cursor.execute(sqlStatement)
    row = self.cursor.fetchone()
    if (row is not None):
      raise ValueError(errorMessage)

  
  def FindAllConfirmedInvitations(self):
    self.cursor.execute(self.findAllEXASQL)
    results = self.cursor.fetchall()        
    
    return results


  def FindConfirmedInvitations(self, email, location, eventName, startTime, endTime):
    whereClause = " WHERE 1 = 1"  #this is created to allow additional where clause to be added below

    if (startTime is not None and startTime != '') and (endTime is not None and endTime != ''):
      if (startTime > endTime):
        raise ValueError("Start Time cannot be later than End Time")
    
    if (email is not None and email != ''):
      whereClause += " AND A.AttendeeEmail = '{}'".format(email)
    if (location is not None and location != ''):
      whereClause += " AND E.Location = '{}'".format(location)
    if (eventName is not None and eventName != ''):
      whereClause += " AND E.EventName = '{}'".format(eventName)
    if (startTime is not None and startTime != ''):
      whereClause += " AND E.StartTime >= '{}'".format(startTime)
    if (endTime is not None and endTime != ''):
      whereClause += " AND E.EndTime <= '{}'".format(endTime)
    
    self.cursor.execute(self.findAllEXASQL + whereClause + " ORDER BY StartTime ASC")
    results = self.cursor.fetchall()        
    
    return results

  def __ValidateIfNullOrEmpty(self, element, errorObject):
    if (element is None or str(element) == ''):
      raise ValueError("'{}' is not provided.".format(errorObject))


  def __FindFirstElement(self, sqlStatement, whereClause, errorObject, element):
    self.cursor.execute(sqlStatement + whereClause.format(element))
    result = self.cursor.fetchone()

    if (result is None):
      raise ValueError("{} '{}' does not exist".format(errorObject, element))

    return result

  def __ValidateIfDoesntExist(self, sqlStatement, whereClause, eventId, eventName, attendeeId, email):
    self.cursor.execute(sqlStatement + whereClause.format(eventId, attendeeId))
    result = self.cursor.fetchone()

    if (result is not None):
      raise ValueError("Email '{}' has already been added to event '{}'.".format(email, eventName))

  
  def __ValidateIfExist(self, sqlStatement, whereClause, eventId, eventName, attendeeId, email):
    self.cursor.execute(sqlStatement + whereClause.format(eventId, attendeeId))
    result = self.cursor.fetchone()

    if (result is None):
      raise ValueError("Email '{}' has not been added to event '{}'.".format(email, eventName))


  def __FindEventIdAttendeeId(self, eventName, email):
    self.__ValidateIfNullOrEmpty(eventName, "Event name")
    self.__ValidateIfNullOrEmpty(email, "Attendee email")
    
    result = self.__FindFirstElement(self.selectAllEventsSQL, " WHERE EventName = '{}'", "Event name", eventName)
    eventId = result[0]

    result = self.__FindFirstElement(self.selectAllAttendeeSQL, " WHERE AttendeeEmail = '{}'", "Attendee email", email)
    attendeeId = result[0]

    return eventId, attendeeId


  def UpdateAttendanceInvitation(self, eventName, email):
    eventId, attendeeId = self.__FindEventIdAttendeeId(eventName, email)

    self.__ValidateIfDoesntExist(self.selectEXASQL, " WHERE EventId = {} AND AttendeeId = {}", eventId, eventName, attendeeId, email)

    try:
      self.cursor.execute(self.insertEXASQL.format(eventId, attendeeId))
      self.sqliteConnection.commit()

    except Exception as ex:
      self.sqliteConnection.rollback()
      raise ValueError("An error has occurred on the database interaction.  Changes have been rolled back.  \nError Message:" + str(ex))


  def RemoveAttendanceInvitation(self, eventName, email):
    eventId, attendeeId = self.__FindEventIdAttendeeId(eventName, email)

    self.__ValidateIfExist(self.selectEXASQL, " WHERE EventId = {} AND AttendeeId = {}", eventId, eventName, attendeeId, email)

    try:
      self.cursor.execute(self.deleteEXASQL.format(eventId, attendeeId))
      self.sqliteConnection.commit()

    except Exception as ex:
      self.sqliteConnection.rollback()
      raise ValueError("An error has occurred on the database interaction.  Changes have been rolled back.  \nError Message:" + str(ex))

 

data = DataLayer()
print(data.FindAllAttendees())
# data.RemoveAttendanceInvitation("Test Event 1", "adam@abc.com")

