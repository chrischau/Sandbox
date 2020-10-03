Evite Server API Server
 - Author: Chris Chau
 - Last Modified Date: Oct 4, 2020
 - Version: 0.1

Description
  The EviteServer API Server provides a gateway for users to create and manage events.  
  The operations are based on RESTful GET, POST, PUT, and DELETE operations.
  
  A user can -
  - find events                      : GET /events 
  - create an events                 : POST /events
  - update an event                  : PUT /events
  - delete an event                  : DELETE /events
  - find attendees                   : GET /attendees
  - create an attendee               : POST /attendees
  - update an attendee               : PUT /attendees
  - delete an attendee               : DELETE /attendees
  - find all events with attendees   : GET /invites
  - assign an attendee to an event   : PUT /invites
  - remove attendee to an event      : DELETE /invites

  For additional information about each operation, please start the API server and find more information at this link.
  http://127.0.0.1:5002/

  
Pre-requisite
  - python 3
  - SQLite database
  - Microsoft Windows (optional)
  

Deployment
  1. Unzip the file and deploy all the content in your desired directory.
  
  2. If you prefer to create your SQL database, a script has been provided under DatabaseScript folder.
     Run the SQL script "01 Create new tables.sql" in your desired SQLite database.
  
  3. If you don't have access to SQLite database, or you prefer to use the sample database provided.
      You can find a sample database file has been provided in the Database folder, named "EventServer.db".
  
  4. Locate the file "config.json" in ServerSide folder.  
     Open it and confirm the correct location of the "DatabasePath" value.
  
  5. Kick off the "StartServer.bat".  Your EventServer API server is ready to use.
     If you are not using Windows, you will need to kick off the Server.py file in your environment.

  6. The base web address is http://127.0.0.1:5002/

  7. For more information, please consult the API documentation page at http://127.0.0.1:5002/