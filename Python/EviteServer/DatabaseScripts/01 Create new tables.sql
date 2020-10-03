DROP TABLE IF EXISTS Events;
DROP TABLE IF EXISTS Attendees;
DROP TABLE IF EXISTS EventsXAttendees;

CREATE TABLE Events (
	EventId INTEGER NOT NULL,
	EventName TEXT NOT NULL,
	StartTime TEXT NOT NULL,
	EndTime TEXT NOT NULL,
	Location TEXT NOT NULL,
	CONSTRAINT Events_PK PRIMARY KEY (EventId)
);

CREATE TABLE Attendees (
	AttendeeId INTEGER NOT NULL,
	AttendeeEmail TEXT NOT NULL UNIQUE,
	CONSTRAINT Attendees_PK PRIMARY KEY (AttendeeId)
);

CREATE TABLE EventsXAttendees (
	EventId INTEGER NOT NULL,
	AttendeeId INTEGER NOT NULL,
	ReceiveEmailNotification INTEGER DEFAULT 0,
	CONSTRAINT EventsXAttendees_FK_EventId FOREIGN KEY (EventId) REFERENCES Events(EventId),
	CONSTRAINT EventsXAttendees_FK_AttendeeId FOREIGN KEY (AttendeeId) REFERENCES Attendees(AttendeeId)
);



-- Insert into Attendees(AttendeeEmail)
-- Values("kelly@abc.com")

-- Insert into Attendees(AttendeeEmail)
-- Values("adam@abc.com")

-- Insert into Attendees(AttendeeEmail)
-- Values("john@abc.com")

-- Insert into Attendees(AttendeeEmail)
-- Values("jeff@abc.com")

-- INSERT INTO Events (EventName, StartTime, EndTime, Location)
-- VALUES ("Test Event 1", datetime('now'), datetime('now', 'start of day', '+1 day'), "Hong Kong")

-- INSERT INTO Events (EventName, StartTime, EndTime, Location)
-- VALUES ("Test Event 2", datetime('now'), datetime('now', 'start of day', '+5 day'), "Hong Kong")

-- INSERT INTO Events (EventName, StartTime, EndTime, Location)
-- VALUES ("Test Event 3", datetime('now'), datetime('now', 'start of month', '+5 day'), "Hong Kong")

-- INSERT INTO EventsXAttendees (EventId, AttendeeId)
-- VALUES (1, 1)

-- INSERT INTO EventsXAttendees (EventId, AttendeeId)
-- VALUES (1, 2)

-- INSERT INTO EventsXAttendees (EventId, AttendeeId)
-- VALUES (2, 3)

-- INSERT INTO EventsXAttendees (EventId, AttendeeId)
-- VALUES (3, 4)


