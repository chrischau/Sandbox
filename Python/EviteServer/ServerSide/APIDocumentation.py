class APIDocumentation:
  APIDocumentation = '''  
<!DOCTYPE html>
<html lang=en-us>
<head>
<meta charset=utf-8>
<title>EviteServer API Documentation</title>
<meta name=description content="EviteServer API Documentation">
<meta name=viewport content="width=device-width, initial-scale=1">
<link rel=stylesheet href=apidocs.css>
<body>
<h1>EviteServer API Documentation</h1>

<p>The EviteServer Api consists of eleven RESTful endpoints.  These operations should be sufficient to allow user to manipulate Events, Attendance, and Attendance Invitations.</p>
<p>version 0.1</p>
<br>
<h2 id="table-of-contents">Table of Contents</h2>

<h3 id="restful-endpointsdef"><a href="#restfulEndDef">RESTful Endpoints</a></h3>

<ul>
  <li>
    <p><b><a href="#eventsDef">Events</a></p></b>

    <ul>
      <li>
        <p><b><a href="#getEvents">GET events</a></p></b>
        <ul>
        <li>
          <p><b>Parameters</b><p>
          <ul>
          <li>
            <p>EventId as an integer, optional</p>            
          </li>
          <li>
            <p>EventName as string, optional</p>
          </li>
          </ul>
        </li>
        <li>
          <p><b>Response</b><p>
          <ul>
          <li>
            <p>EventId</p>            
          </li>
          <li>
            <p>EventName</p>
          </li>
          <li>
            <p>Location</p>
          </li>
          <li>
            <p>Starttime</p>
          </li>
          <li>
            <p>EndTime</p>
          </li>
          </ul>
        </li>
        </ul>
      </li>
      <li>
        <p><b><a href="#postEvents">POST events</a></p></b>
        <ul>
        <li>
          <p><b>Parameters</b><p>
          <ul>
          <li>
            <p>EventName as string, mandatory</p>            
          </li>
          <li>
            <p>StartTime as string, mandatory</p>
          </li>
          <li>
            <p>EndTime as string, mandatory</p>            
          </li>
          <li>
            <p>Location as string, mandatory</p>
          </li>
          </ul>
        </li>
        <li>
          <p><b>Response</b><p>
          <ul>
          <li>
            <p>success or failed message</p>            
          </li>
          </ul>
        </li>
        </ul>
      </li>
      <li>
        <p><b><a href="#putEvents">PUT events</a></p></b>
        <ul>
        <li>
          <p><b>Parameters</b><p>
          <ul>
          <li>
            <p>EventId as string, mandatory</p>            
          </li>
          <li>
            <p>EventName as string, optional</p>            
          </li>
          <li>
            <p>StartTime as string, optional</p>
          </li>
          <li>
            <p>EndTime as string, optional</p>            
          </li>
          <li>
            <p>Location as string, optional</p>
          </li>
          </ul>
        </li>
        <li>
          <p><b>Response</b><p>
          <ul>
          <li>
            <p>success or failed message</p>            
          </li>
          </ul>
        </li>
        </ul>
      </li>
      <li>
        <p><b><a href="#deleteEvents">DELETE events</a></p></b>
        <ul>
        <li>
          <p><b>Parameters</b><p>
          <ul>
          <li>
            <p>EventId as string, mandatory</p>            
          </li>
          </ul>
        </li>
        <li>
          <p><b>Response</b><p>
          <ul>
          <li>
            <p>success or failed message</p>            
          </li>
          </ul>
        </li>
        </ul>
      </li>
    </ul>
  </li>
  <li>
    <p><b><a href="#attendeeDef">Attendees</a></p></b>

    <ul>
      <li>
        <p><b><a href="#getAttendees">GET attendees</a></p></b>
        <ul>
        <li>
          <p><b>Parameters</b><p>
          <ul>
          <li>
            <p>AttendeeEmail as string, optional</p>            
          </li>
          </ul>
        </li>
        <li>
          <p><b>Response</b><p>
          <ul>
          <li>
            <p>AttendeeId</p>            
          </li>
          <li>
            <p>AttendeeEmail</p>            
          </li>
          </ul>
        </li>
        </ul>
      </li>
      <li>
        <p><b><a href="#postAttendees">POST attendees</a></p></b>
        <ul>
        <li>
          <p><b>Parameters</b><p>
          <ul>
          <li>
            <p>AttendeeEmail as string, mandatory</p>            
          </li>
          </ul>
        </li>
        <li>
          <p><b>Response</b><p>
          <ul>
          <li>
            <p>success or failed message</p>            
          </li>
          </ul>
        </li>
        </ul>
      </li>
      <li>
        <p><b><a href="#putAttendees">PUT attendees</a></p></b>
        <ul>
        <li>
          <p><b>Parameters</b><p>
          <ul>
          <li>
            <p>AttendeeId as string, mandatory</p>            
          </li>
          <li>
            <p>AttendeeEmail as string, mandatory</p>            
          </li>
          </ul>
        </li>
        <li>
          <p><b>Response</b><p>
          <ul>
          <li>
            <p>success or failed message</p>            
          </li>
          </ul>
        </li>
        </ul>
      </li>
      <li>
        <p><b><a href="#deleteAttendees">DELETE attendees</a></p></b>
        <ul>
        <li>
          <p><b>Parameters</b><p>
          <ul>
          <li>
            <p>AttendeeEmail as string, mandatory</p>            
          </li>
          </ul>
        </li>
        <li>
          <p><b>Response</b><p>
          <ul>
          <li>
            <p>success or failed message</p>            
          </li>
          </ul>
        </li>
        </ul>
      </li>
    </ul>
  </li>
  <li>
    <p><b><a href="#invitationAttendanceDef">Invitation Attendance</a></p></b>

    <ul>
      <li>
        <p><b><a href="#getInvites">Get invites</a></p></b>
        <ul>
        <li>
          <p><b>Parameters</b><p>
          <ul>
          <li>
            <p>AttendeeEmail as string, optional</p>            
          </li>
          <li>
            <p>EventName as string, optional</p>            
          </li>
          <li>
            <p>StartTime as string, optional</p>            
          </li>
          <li>
            <p>EndTime as string, optional</p>            
          </li>
          <li>
            <p>Location as string, optional</p>            
          </li>          
          </ul>
        </li>
        <li>
          <p><b>Response</b><p>
          <ul>
          <li>
            <p>EventId</p>            
          </li>
          <li>
            <p>EventName</p>            
          </li>
          <li>
            <p>Location</p>            
          </li>
          <li>
            <p>StartTime</p>            
          </li>
          <li>
            <p>EndTime</p>            
          </li>
          <li>
            <p>AttendeeId</p>            
          </li>
          <li>
            <p>AttendeeEmail</p>            
          </li>
          </ul>
        </li>
        </ul>
      </li>
      <li>
        <p><b><a href="#putInvites">POST invites</a></p></b>
        <ul>
        <li>
          <p><b>Parameters</b><p>
          <ul>
          <li>
            <p>EventName as integer, mandatory</p>
          </li>
          <li>
            <p>AttendeeEmail as string, mandatory</p>            
          </li>
          </ul>
        </li>
        <li>
          <p><b>Response</b><p>
          <ul>
          <li>
            <p>success or failed message</p>            
          </li>
          </ul>
        </li>
        </ul>
      </li>
      <li>
        <p><b><a href="#deleteInvites">DELETE invites</a></p></b>
        <ul>
        <li>
          <p><b>Parameters</b><p>
          <ul>
          <li>
            <p>EventName as integer, mandatory</p>
          </li>
          <li>
            <p>AttendeeEmail as string, mandatory</p>            
          </li>
          </ul>
        </li>
        <li>
          <p><b>Response</b><p>
          <ul>
          <li>
            <p>success or failed message</p>            
          </li>
          </ul>
        </li>
        </ul>
      </li>      
    </ul>
  </li>
  
</ul>

</body>
</html>

'''