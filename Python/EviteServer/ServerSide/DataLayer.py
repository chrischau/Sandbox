# Data Layer class to return reults from database interaction
# This is for code separation and ease of change
from flask import Flask, json
import sqlite3
from SQLStatements import SQLStatements
from Helper import Helper
from EmailInvitation import EmailInvitation


class DataLayer:
  
  def __init__(self):
    ## TODO add logging
    self.sql = SQLStatements()
    self.helper = Helper()

    configFile = self.helper.LoadConfigFile();
    databaseName = configFile['DatabasePath']
    
    if (configFile['SMTPServerSenderEmail'] == ''):
      self.ShouldSendEmail = False
    else:
      self.ShouldSendEmail = True
    
    self.sqliteConnection = sqlite3.connect(databaseName)
    self.cursor = self.sqliteConnection.cursor()
    #print("Database created and Successfully Connected to SQLite") #TODO logging    


  def __del__ (self):
    self.cursor.close()
    self.sqliteConnection.close()


  def FindAllEvents(self):
    self.cursor.execute(self.sql.SelectAllEventsSQL)
    results = self.__AggregateData(self.cursor.description, self.cursor.fetchall())

    return results

  
  def FindEvent(self, eventId, eventName):
    if (eventId != None):
      whereClause = " WHERE EventId = {}".format(eventId)
      self.cursor.execute(self.sql.SelectAllEventsSQL + whereClause)
      results = self.__AggregateData(self.cursor.description, self.cursor.fetchall())
      
      return results
    
    if (eventName != None and eventName != ''):
      whereClause = " WHERE EventName = '{}'".format(eventName)
      self.cursor.execute(self.sql.SelectAllEventsSQL + whereClause)
      results = self.__AggregateData(self.cursor.description, self.cursor.fetchall())

      return results

    else:
      return None


  def CreateEvent(self, eventName, location, startTime, endTime):
    sqlStatement = self.sql.SelectAllEventsSQL + " WHERE EventName = '{}'".format(eventName)
    
    #self.__ValidateRecordDoesNotExist(sqlStatement, "Event with the same name '{}' already exist.  Please choose another name.".format(eventName))
    self.helper.ValidateTimeFormat(startTime, "Incorrect Start Time datetime format.  It should be YYYY-MM-DD HH:MM:SS")
    self.helper.ValidateTimeFormat(endTime, "Incorrect End Time datetime format.  It should be YYYY-MM-DD HH:MM:SS")
    self.helper.ValidateEndTimeIsAfterStartTime(startTime, endTime)
    
    insertStatement = self.sql.InsertEventSQL.format(eventName, location, startTime, endTime)

    try:
      self.cursor.execute(insertStatement)
      self.sqliteConnection.commit()

    except Exception as ex:
      self.sqliteConnection.rollback()
      raise ValueError("An error has occurred on the database interaction.  Changes have been rolled back.  \nError Message:" + str(ex))

  
  def DeleteEvent(self, eventId):
    event = self.FindEvent(eventId, None)
    if (event is None or len(event) == 0):
      raise ValueError("Event Id '{}' is not found, or does not exist.".format(eventId))

    try:
      whereClause = " WHERE EventId = {}".format(eventId)      
      self.cursor.execute(self.sql.DeleteEXASQL + whereClause) # TODO maybe it is a good idea to report how many were deleted
      self.cursor.execute(self.sql.DeleteEventSQL + whereClause)
      self.sqliteConnection.commit()
      
    except Exception as ex:
      self.sqliteConnection.rollback()
      raise ValueError("An error has occurred on the database interaction.  Changes have been rolled back.  \nError Message:" + str(ex))

  
  def UpdateEvent(self, eventId, eventName, location, startTime, endTime):
    whereClause = " WHERE EventId = {}".format(eventId)
    errorMessage = "Event Id '{}' does not exist.".format(eventId)
    self.__ValidateIfExist(self.sql.SelectAllEventsSQL, whereClause, errorMessage)

    if ((eventName is None or len(eventName) == 0)
        and (location is None or len(location) == 0)
        and (startTime is None or len(startTime) == 0)
        and (endTime is None or len(endTime) == 0)):
      raise ValueError("No update values have been provided.  Event is not updated.")
    
    event = self.FindEvent(eventId, None)
    newStartTime = event[0]["StartTime"]
    newEndTime = event[0]["EndTime"]

    updateSQL = self.sql.UpdateEventSQL

    if (eventName is not None and len(eventName) > 0):
      updateSQL += " EventName = '{}',".format(eventName)
    
    if (location is not None and len(location) > 0):
      updateSQL += " Location = '{}',".format(location)

    if (startTime is not None and len(startTime) > 0):
      self.helper.ValidateTimeFormat(startTime)
      updateSQL += " StartTime = '{}',".format(startTime)
      newStartTime = startTime
    
    if (endTime is not None and len(endTime) > 0):
      self.helper.ValidateTimeFormat(endTime)
      updateSQL += " EndTime = '{}',".format(endTime)
      newEndTime = endTime
    
    updateSQL = updateSQL[:-1] + " WHERE EventId = {}".format(eventId)
    
    self.helper.ValidateEndTimeIsAfterStartTime(newStartTime, newEndTime)
    
    try:
      self.cursor.execute(updateSQL)
      self.sqliteConnection.commit()

    except Exception as ex:
      self.sqliteConnection.rollback()
      raise ValueError("An error has occurred on the database interaction.  Changes have been rolled back.  \nError Message:" + str(ex))


  def CreateAttendee(self, email):
    self.helper.ValidateEmailStructure(email)    
    
    sqlStatement = self.sql.SelectAllAttendeeSQL + " WHERE AttendeeEmail = '{}'".format(email)
    self.__ValidateRecordDoesNotExist(sqlStatement, "Attendee with the same email '{}' already exist.  Please verify and adjust accordingly.".format(email))
    
    
    insertStatement = self.sql.InsertAttendeeSQL.format(email)

    try:
      self.cursor.execute(insertStatement)
      self.sqliteConnection.commit()

    except Exception as ex:
      self.sqliteConnection.rollback()
      raise ValueError("An error has occurred on the database interaction.  Changes have been rolled back.  \nError Message:" + str(ex))


  def FindAllAttendees(self):
    self.cursor.execute(self.sql.SelectAllAttendeeSQL)
    results = self.__AggregateData(self.cursor.description, self.cursor.fetchall())
    
    return results

  
  def FindAttendee(self, email):
    if (email != None and email != ''):
      whereClause = " WHERE AttendeeEmail = '{}'".format(email)
      self.cursor.execute(self.sql.SelectAllAttendeeSQL + whereClause)
      results = self.__AggregateData(self.cursor.description, self.cursor.fetchall())

      return results

    else:
      return None

  
  def DeleteAttendee(self, email):
    attendee = self.FindAttendee(email)
    if (attendee is None or len(attendee) == 0):
      raise ValueError("Attendee with email '{}' is not found, or does not exist.".format(email))

    try:
      attendeeId = attendee[0]['AttendeeId']
      whereClause = " WHERE AttendeeId = {}".format(attendeeId)      
      self.cursor.execute(self.sql.DeleteEXASQL + whereClause) # TODO maybe it is a good idea to report how many were deleted
      self.cursor.execute(self.sql.DeleteAttendeeSQL + whereClause)
      self.sqliteConnection.commit()
      
    except Exception as ex:
      self.sqliteConnection.rollback()
      raise ValueError("An error has occurred on the database interaction.  Changes have been rolled back.  \nError Message:" + str(ex))


  def UpdateAttendee(self, attendeeId, email):
    whereClause = " WHERE AttendeeId = {}".format(attendeeId)
    errorMessage = "Attendee Id '{}' does not exist.".format(attendeeId)
    self.__ValidateIfExist(self.sql.SelectAllAttendeeSQL, whereClause, errorMessage)
    self.helper.ValidateEmailStructure(email)
    
    updateSQL = self.sql.UpdateAttendeeSQL + " AttendeeEmail = '{}'".format(email) + " WHERE AttendeeId = {}".format(attendeeId)
    
    try:
      self.cursor.execute(updateSQL)
      self.sqliteConnection.commit()

    except Exception as ex:
      self.sqliteConnection.rollback()
      raise ValueError("An error has occurred on the database interaction.  Changes have been rolled back.  \nError Message:" + str(ex))


  def __ValidateRecordDoesNotExist(self, sqlStatement, errorMessage):
    self.cursor.execute(sqlStatement)
    row = self.cursor.fetchone()
    if (row is not None):
      raise ValueError(errorMessage)

  
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
    
    self.cursor.execute(self.sql.SelectAllEXASQL + whereClause + " ORDER BY StartTime ASC")
    results = self.__AggregateData(self.cursor.description, self.cursor.fetchall())
    
    return results


  @staticmethod
  def __AggregateData(columnsDescription, data):
    columns = [column[0] for column in columnsDescription]
    results = []
    for row in data:
      results.append(dict(zip(columns, row)))

    return results
  

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
      raise ValueError("Email '{}' has already been added to event '{}'.  Invitation Attendance is not added.".format(email, eventName))

  
  def __ValidateIfExist(self, sqlStatement, whereClause, errorMessage):
    self.cursor.execute(sqlStatement + whereClause)
    result = self.cursor.fetchone()

    if (result is None):
      raise ValueError(errorMessage)


  def __FindEventIdAttendeeId(self, eventName, email):
    self.helper.ValidateIfNullOrEmpty(eventName, "Event name")
    self.helper.ValidateIfNullOrEmpty(email, "Attendee email")
    
    result = self.__FindFirstElement(self.sql.SelectAllEventsSQL, " WHERE EventName = '{}'", "Event name", eventName)
    eventId = result[0]

    result = self.__FindFirstElement(self.sql.SelectAllAttendeeSQL, " WHERE AttendeeEmail = '{}'", "Attendee email", email)
    attendeeId = result[0]

    return eventId, attendeeId


  def AddAttendanceInvitation(self, eventName, email):
    eventId, attendeeId = self.__FindEventIdAttendeeId(eventName, email)

    whereClause = " WHERE EventId = {} AND AttendeeId = {}"
    self.__ValidateIfDoesntExist(self.sql.SelectEXASQL, whereClause, eventId, eventName, attendeeId, email)

    try:
      self.cursor.execute(self.sql.InsertEXASQL.format(eventId, attendeeId))
      
      if (self.ShouldSendEmail):
        emailInvitation = EmailInvitation()
        emailInvitation.Send(email, eventName, EmailInvitation.SampleMessage())
      
      self.sqliteConnection.commit()
    except Exception as ex:
      self.sqliteConnection.rollback()
      raise ValueError("An error has occurred on the database interaction.  Changes have been rolled back.  \nError Message:" + str(ex))


  def RemoveAttendanceInvitation(self, eventName, email):
    eventId, attendeeId = self.__FindEventIdAttendeeId(eventName, email)

    whereClause = " WHERE EventId = {} AND AttendeeId = {}".format(eventId, attendeeId)
    errorMessage = "Email '{}' was not added to event '{}'.  Invitation Attendance is not deleted.".format(email, eventName)
    self.__ValidateIfExist(self.sql.SelectEXASQL, whereClause, errorMessage)

    try:
      self.cursor.execute(self.sql.DeleteEXASQL + whereClause)
      self.sqliteConnection.commit()

    except Exception as ex:
      self.sqliteConnection.rollback()
      raise ValueError("An error has occurred on the database interaction.  Changes have been rolled back.  \nError Message:" + str(ex))
