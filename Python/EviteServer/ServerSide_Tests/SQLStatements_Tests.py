import unittest
import sys
sys.path.insert(1, 'C:\Development\GitHub\Sandbox\Python\EviteServer\ServerSide')

from SQLStatements import SQLStatements


#sanity checks for all the SQLs
class SQLStatements_Tests(unittest.TestCase):
  
  def test_SelectAllEventsSQL(self):
    sql = SQLStatements()
    self.assertEqual(sql.SelectAllEventsSQL, "SELECT EventId, EventName, Location, StartTime, EndTime FROM Events")

  def test_InsertEventSQL(self):
    sql = SQLStatements()
    self.assertEqual(sql.InsertEventSQL, "INSERT INTO Events(EventName, Location, StartTime, EndTime) VALUES ('{}', '{}', '{}', '{}')")
  
  def test_DeleteEventSQL(self):
    sql = SQLStatements()
    self.assertEqual(sql.DeleteEventSQL,  "DELETE FROM Events")

  def test_UpdateEventSQL(self):
    sql = SQLStatements()
    self.assertEqual(sql.UpdateEventSQL, "UPDATE Events SET")
  
  def test_SelectAllAttendeeSQL(self):
    sql = SQLStatements()
    self.assertEqual(sql.SelectAllAttendeeSQL, "SELECT AttendeeId, AttendeeEmail FROM Attendees")

  def test_InsertAttendeeSQL(self):
    sql = SQLStatements()
    self.assertEqual(sql.InsertAttendeeSQL, "INSERT INTO Attendees(AttendeeEmail) VALUES ('{}')")
    
  def test_DeleteAttendeeSQL(self):
    sql = SQLStatements()
    self.assertEqual(sql.DeleteAttendeeSQL, "DELETE FROM Attendees")
  
  def test_UpdateAttendeeSQL(self):
    sql = SQLStatements()
    self.assertEqual(sql.UpdateAttendeeSQL, "Update Attendees SET")

  def test_SelectAllEXASQL(self):
    sql = SQLStatements()
    self.assertEqual(sql.SelectAllEXASQL, "SELECT E.EventId, E.EventName, E.Location, E.StartTime, E.EndTime, A.AttendeeId, A.AttendeeEmail FROM Events AS E \
  JOIN EventsXAttendees AS EXA ON EXA.EventId = E.EventId \
  JOIN Attendees AS A ON EXA.AttendeeId = A.AttendeeId")

  def test_InsertEXASQL(self):
    sql = SQLStatements()
    self.assertEqual(sql.InsertEXASQL, "INSERT INTO EventsXAttendees(EventId, AttendeeId) VALUES ('{}', '{}')")

  def test_SelectEXASQL(self):
    sql = SQLStatements()
    self.assertEqual(sql.SelectEXASQL, "SELECT EventId, AttendeeId FROM EventsXAttendees")

  def test_DeleteEXASQL(self):
    sql = SQLStatements()
    self.assertEqual(sql.DeleteEXASQL, "DELETE FROM EventsXAttendees")
  


if __name__ == '__main__':
    unittest.main()
