DROP TABLE IF EXISTS Events;
DROP TABLE IF EXISTS Attendees;
DROP TABLE IF EXISTS EventsXAttendees;

CREATE TABLE Events (
	EventId INTEGER NOT NULL,
	EventName TEXT NOT NULL UNIQUE,
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



INSERT INTO Events (EventName, StartTime, EndTime, Location)
VALUES ("Test Event 3", datetime('now'), datetime('now', 'start of month', '+5 day'), "Hong Kong")

