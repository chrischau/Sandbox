class SQLStatements:
  # Event related SQLs
  SelectAllEventsSQL = "SELECT EventId, EventName, Location, StartTime, EndTime FROM Events"
  InsertEventSQL = "INSERT INTO Events(EventName, Location, StartTime, EndTime) VALUES ('{}', '{}', '{}', '{}')"
  DeleteEventSQL = "DELETE FROM Events"
  UpdateEventSQL = "UPDATE Events SET"
  
  # Attendee related SQLs
  SelectAllAttendeeSQL = "SELECT AttendeeId, AttendeeEmail FROM Attendees"
  InsertAttendeeSQL = "INSERT INTO Attendees(AttendeeEmail) VALUES ('{}')"
  DeleteAttendeeSQL = "DELETE FROM Attendees"
  UpdateAttendeeSQL = "Update Attendees SET"

  # EventsXAttendees related SQLs
  SelectAllEXASQL = "SELECT E.EventId, E.EventName, E.Location, E.StartTime, E.EndTime, A.AttendeeId, A.AttendeeEmail FROM Events AS E \
  JOIN EventsXAttendees AS EXA ON EXA.EventId = E.EventId \
  JOIN Attendees AS A ON EXA.AttendeeId = A.AttendeeId"

  InsertEXASQL = "INSERT INTO EventsXAttendees(EventId, AttendeeId) VALUES ('{}', '{}')"
  SelectEXASQL = "SELECT EventId, AttendeeId FROM EventsXAttendees"
  DeleteEXASQL = "DELETE FROM EventsXAttendees"