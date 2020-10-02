# Data Layer class to return reults from database interaction
# This is for code separation and ease of change
from flask import Flask, json
import datetime
import sqlite3
import re


class DataLayer:  
  databaseName = "Database\EventServer.db"

  # Event related SQLs
  findAllEventsSQL = "SELECT EventId, EventName, Location, StartTime, EndTime FROM Events"
  createEventSQL = "INSERT INTO Events(EventName, Location, StartTime, EndTime) VALUES ('{}', '{}', '{}', '{}')"
    
  # Attendee related SQLs
  findAllAttendeeSQL = "SELECT AttendeeId, AttendeeEmail FROM Attendees"
  createAttendeeSQL = "INSERT INTO Attendees(AttendeeEmail) VALUES ('{}')"

  # EventsXAttendees related SQLs
  findAllEXASQL = "SELECT E.EventId, E.EventName, E.Location, E.StartTime, E.EndTime, A.AttendeeId, A.AttendeeEmail FROM Events AS E \
  JOIN EventsXAttendees AS EXA ON EXA.EventId = E.EventId \
  JOIN Attendees AS A ON EXA.AttendeeId = A.AttendeeId"

  createEXASQL = "INSERT INTO EventsXAttendee(EventId, AttendeeId) VALUES ('{}', '{}')"

  
  def __init__(self):
    ## TODO add logging
    self.sqliteConnection = sqlite3.connect(self.databaseName)
    self.cursor = self.sqliteConnection.cursor()
    #print("Database created and Successfully Connected to SQLite") #TODO logging


  def FindAllEvents(self):
    #self.logger.info("Inside Users get function")

    self.cursor.execute(self.findAllEventsSQL)
    results = self.cursor.fetchall()        

    return results

  
  def FindEvent(self, eventId, eventName):
    #self.logger.info("Inside Users get function")

    #TODO paging data if too many data at once
    if (eventId != None):
      whereClause = " WHERE EventId = {}".format(eventId)
      self.cursor.execute(self.findAllEventsSQL + whereClause)
      results = self.cursor.fetchall()        

      return results
    
    if (eventName != None):
      whereClause = " WHERE EventName = '{}'".format(eventName)
      self.cursor.execute(self.findAllEventsSQL + whereClause)
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
    sqlStatement = self.findAllEventsSQL + " WHERE EventName = '{}'".format(eventName)
    
    self.__ValidateRecordDoesNotExist(sqlStatement, "Event with the same name '{}' already exist.  Please choose another name.".format(eventName))
    self.__ValidateTimeFormat(startTime, "Incorrect Start Time datetime format.  It should be YYYY-MM-DD HH:MM:SS")
    self.__ValidateTimeFormat(endTime, "Incorrect End Time datetime format.  It should be YYYY-MM-DD HH:MM:SS")

    insertStatement = self.createEventSQL.format(eventName, location, startTime, endTime)

    try:
      self.cursor.execute(insertStatement)
      self.sqliteConnection.commit()

    except Exception as ex:
      self.sqliteConnection.rollback()
      raise ValueError("An error has occurred on the database interaction.  Changes have been rolled back.  \nError Message:" + str(ex))


  def CreateAttendee(self, email):
    sqlStatement = self.findAllAttendeeSQL + " WHERE AttendeeEmail = '{}'".format(email)
    
    self.__ValidateRecordDoesNotExist(sqlStatement, "Attendee with the same email '{}' already exist.  Please verify and adjust accordingly.".format(email))
    self.__ValidateEmailStructure(email)    

    insertStatement = self.createAttendeeSQL.format(email)

    try:
      self.cursor.execute(insertStatement)
      self.sqliteConnection.commit()

    except Exception as ex:
      self.sqliteConnection.rollback()
      raise ValueError("An error has occurred on the database interaction.  Changes have been rolled back.  \nError Message:" + str(ex))


  def FindAllAttendees(self):
    self.cursor.execute(self.findAllAttendeeSQL)
    results = self.cursor.fetchall()        
    
    return results

  
  def FindAttendee(self, email):
    #TODO paging data if too many data at once
    if (email != None):
      whereClause = " WHERE AttendeeEmail = '{}'".format(email)
      self.cursor.execute(self.findAllAttendeeSQL + whereClause)
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
    whereClause = " WHERE 1=1"

    if (email is not None):
      whereClause += " AND A.AttendeeEmail = '{}'".format(email)
    if (location is not None):
      whereClause += " AND E.Location = '{}'".format(location)
    if (eventName is not None):
      whereClause += " AND E.EventName = '{}'".format(evenName)
    if (startTime is not None):
      whereClause += " AND E.StartTime >= '{}'".format(startTime)
    if (endTime is not None):
      whereClause += " AND E.EndTime <= '{}'".format(endTime)
    
    self.cursor.execute(self.findAllEXASQL + whereClause + " ORDER BY StartTime ASC")
    results = self.cursor.fetchall()        
    
    return results



# # print(data.FindEvent(1, None))

# # print(data.FindAllEvents())
# data = DataLayer()
# # #print(data.CreateEvent("American Social Meeting 2", "Tokyo", "2020-10-02 20:00:00", "2020-10-03 02:00:00"))
# # data.CreateAttendee("joseph@abc.com")

# print(data.FindConfirmedInvitations(None, None, None, None, "2020-11-20 00:00:00"))
