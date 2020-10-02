# Data Layer class to return reults from database interaction
# This is for code separation and ease of change
from flask import Flask, json
import datetime
import sqlite3


class DataLayer:  
  databaseName = "Database\EventServer.db"
  findAllEventsSQL = "SELECT EventId, EventName, Location, StartTime, EndTime FROM Events"
  createEventSQL = "INSERT INTO Events(EventName, Location, StartTime, EndTime) VALUES ('{}', '{}', '{}', '{}')"

  def __init__(self):
    ## TODO add logging
    self.sqliteConnection = sqlite3.connect(self.databaseName)
    self.cursor = self.sqliteConnection.cursor()
    print("Database created and Successfully Connected to SQLite")

    self.cursor.execute("select sqlite_version();")
    print("SQLite Database Version is: ", self.cursor.fetchall())


  def FindAllEvents(self):
    #self.logger.info("Inside Users get function")

    self.cursor.execute(self.findAllEventsSQL)
    results = self.cursor.fetchall()        

    return results

  
  def FindEvent(self, eventId, eventName):
    #self.logger.info("Inside Users get function")

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

  def ValidateTimeFormat(self, timeStamp):
    try:
      datetime.datetime.strptime(timeStamp, '%Y-%m-%d %H:%M:%S')
    except ValueError:
      return False
    
    return True
    

  def CreateEvent(self, eventName, location, startTime, endTime):
    #TODO test, assume time format are set correct when passed in
    if self.ValidateTimeFormat(startTime) and self.ValidateTimeFormat(endTime):
      insertStatement = self.createEventSQL.format(eventName, location, startTime, endTime)
    else:
      raise ValueError("Incorrect datetime format.  It should be YYYY-MM-DD HH:MM:SS")

    count = self.cursor.execute(insertStatement)
    self.sqliteConnection.commit()

    return count



# data = DataLayer()
# print(data.FindEvent(1, None))

# data = EventsData()
# print(data.FindAllEvents())

# print(data.CreateEvent("Tokyo Midnight Outing", "Tokyo", "2020-10-02 20:00:00", "2020-10-03 02:00:00"))
