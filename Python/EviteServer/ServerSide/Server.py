from flask import Flask, request, jsonify
import sys
import traceback
import logging
import DataLayer


app = Flask(__name__)

endTimeKeyWord, eventIdKeyWord, locationKeyWord, eventNameKeyWord, startTimeKeyWord = "endtime", "eventid", "location", "eventname", "starttime"
emailKeyWord,attendeeIdKeyWord = "email","attendeeId"


@app.route('/', methods=['GET'])
def HomePageInstruction():
  webpageHelpDoc = "<h1>Evite Server API</h1>"

  return webpageHelpDoc


@app.route('/events', methods=['GET'])
def FindEvents():
  try:
    dataLayer = DataLayer()
    
    if eventIdKeyWord in request.args:
      eventId = int(request.args[eventIdKeyWord])
      results = dataLayer.FindEvent(eventId, None)
      return jsonify(results), 200
    if eventNameKeyWord in request.args:
      eventName = request.args[eventNameKeyWord]
      results = dataLayer.FindEvent(None, eventName)
      return jsonify(results), 200      
    else:
      results = dataLayer.FindAllEvents()
      return jsonify(results), 200

  except Exception as ex:
    return str(ex), 404


@app.route('/events', methods=['POST'])
def CreateEvent():
  try:
    if eventNameKeyWord not in request.args:
      raise ValueError("Event is not created.  Event Name is not provided.  Please resubmit with the correct parameters.")
    if startTimeKeyWord not in request.args:
      raise ValueError("Event is not created.  Event Start Time is not provided.  Please resubmit with the correct parameters.")
    if endTimeKeyWord not in request.args:
      raise ValueError("Event is not created.  Event End Time is not provided.  Please resubmit with the correct parameters.")
    if locationKeyWord not in request.args:
      raise ValueError("Event is not created.  Event Location is not provided.  Please resubmit with the correct parameters.")

    name = request.args[eventNameKeyWord]
    startTime = request.args[startTimeKeyWord]
    endTime = request.args[endTimeKeyWord]
    location = request.args[locationKeyWord]
    
    dataLayer = DataLayer()
    dataLayer.CreateEvent(name, location, startTime, endTime)

    return "Event '{}' has been created successful.".format(name), 200
  
  except Exception as ex:
    return str(ex), 404


@app.route('/events', methods=['PUT'])
def UpdateEvent():
  try:
    if eventIdKeyWord not in request.args:
      raise ValueError("Event is not updated.  Event Id is not provided.  Please resubmit with the correct parameters.")
    
    if eventIdKeyWord in request.args:
      eventName = request.args[eventNameKeyWord]
    if startTimeKeyWord in request.args:
      startTime = request.args[startTimeKeyWord]
    if endTimeKeyWord in request.args:
      endTime = request.args[endTimeKeyWord]
    if locationKeyWord in request.args:
      location = request.args[locationKeyWord]

    eventId = request.args[eventIdKeyWord]

    dataLayer = DataLayer()
    dataLayer.UpdateEvent(eventId, eventName, location, startTime, endTime)    

    return "Event '{}' has been updated successful.".format(eventName), 200
  
  except Exception as ex:
    return str(ex), 404


@app.route('/events', methods=['DELETE'])
def DeleteEvent():
  try:
    if eventNameKeyWord not in request.args:
      raise ValueError("Event is not deleted.  Event Name is not provided.  Please resubmit with the correct parameters.")
    
    eventName = request.args[eventNameKeyWord]
    
    dataLayer = DataLayer()
    dataLayer.DeleteEvent(None, eventName)    

    return "Event '{}' and the confirmed attendees have been deleted successful.".format(eventName), 200
  
  except Exception as ex:
    return str(ex), 404


@app.route('/attendees', methods=['GET'])
def FindAttendees():
  try:
    dataLayer = DataLayer()
    
    if emailKeyWord in request.args:
      email = request.args[emailKeyWord]
      results = dataLayer.FindAttendee(email)
      return jsonify(results), 200
    else:
      results = dataLayer.FindAllAttendees()
      return jsonify(results), 200

  except Exception as ex:
    return str(ex), 404


@app.route('/attendees', methods=['POST'])
def CreateAttendee():
  try:
    if emailKeyWord not in request.args:
      raise ValueError("Attendee is not created.  Attendee email is not provided.  Please resubmit with the correct parameters.")

    email = request.args[emailKeyWord]

    dataLayer = DataLayer()
    dataLayer.CreateAttendee(email)

    return "Attendee '{}' has been created successful.".format(email), 200
  
  except Exception as ex:
    return str(ex), 404


@app.route('/attendees', methods=['DELETE'])
def DeleteAttendee():
  try:
    if emailKeyWord not in request.args:
      raise ValueError("Attendee is not deleted.  Attendee email is not provided.  Please resubmit with the correct parameters.")

    email = request.args[emailKeyWord]

    dataLayer = DataLayer()
    dataLayer.DeleteAttendee(email)

    return "Attendee '{}' has been deleted successful.".format(email), 200
  
  except Exception as ex:
    return str(ex), 404


@app.route('/attendees', methods=['PUT'])
def DeleteAttendee():
  try:
    if attendeeIdKeyWord not in request.args:
      raise ValueError("Attendee is not deleted.  Attendee Id is not provided.  Please resubmit with the correct parameters.")

    attendeeId = request.args[eventIdKeyWord]

    if emailKeyWord in request.args:
      email = request.args[emailKeyWord]

    dataLayer = DataLayer()
    dataLayer.UpdateAttendee(attendeeId, email)

    return "Attendee '{}' has been updated successful.".format(email), 200
  
  except Exception as ex:
    return str(ex), 404


@app.route('/invites', methods=['GET'])
def FindConfirmedInvitations():
  try:
    dataLayer = DataLayer()
    
    email, location, eventName, startTime, endTime = None, None, None, None, None

    if emailKeyWord in request.args:
      email = request.args[emailKeyWord]
    if locationKeyWord in request.args:
      location = request.args[locationKeyWord]
    if eventNameKeyWord in request.args:
      eventName = request.args[eventNameKeyWord]
    if startTimeKeyWord in request.args:
      startTime = request.args[startTimeKeyWord]
    if endTimeKeyWord in request.args:
      endTime = request.args[endTimeKeyWord]

    results = dataLayer.FindConfirmedInvitations(email, location, eventName, startTime, endTime)
    return jsonify(results), 200

  except Exception as ex:
    return str(ex), 404


@app.route('/invites', methods=['PUT'])
def UpdateInvitationAttendance():
  try:
    dataLayer = DataLayer()
    eventName, attendeeName = None, None

    if eventNameKeyWord in request.args:
      eventName = request.args[eventNameKeyWord]
    if emailKeyWord in request.args:
      email = request.args[emailKeyWord]
        
    results = dataLayer.UpdateAttendanceInvitation(eventName, email)
    return "Attendee '{}' has been added to event '{}'.".format(email, eventName), 200

  except Exception as ex:
    return str(ex), 404


@app.route('/invites', methods=['DELETE'])
def RemoveInvitationAttendance():
  try:
    dataLayer = DataLayer()
    eventName, attendeeName = None, None

    if eventNameKeyWord in request.args:
      eventName = request.args[eventNameKeyWord]
    if emailKeyWord in request.args:
      email = request.args[emailKeyWord]
        
    results = dataLayer.UpdateAttendanceInvitation(eventName, email)
    return "Attendee '{}' has been remove from event '{}'.".format(email, eventName), 200

  except Exception as ex:
    return str(ex), 404


if __name__ == '__main__':
     app.run(port='5002')
