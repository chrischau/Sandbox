from flask import Flask, request, jsonify
import sys
import traceback
import logging
from DataLayer import DataLayer

app = Flask(__name__)

@app.route('/', methods=['GET'])
def HomePageInstruction():
  return "<h1>Insert documentation later.</h1>"


@app.route('/events', methods=['GET'])
def FindEvents():
  try:
    dataLayer = DataLayer()
    
    if 'id' in request.args:
      id = int(request.args['id'])
      results = dataLayer.FindEvent(id, None)
      return jsonify(results), 200
    if 'name' in request.args:
      name = request.args['name']
      results = dataLayer.FindEvent(None, name)
      return jsonify(results), 200      
    else:
      results = dataLayer.FindAllEvents()
      return jsonify(results), 200

  except Exception as ex:
    return str(ex), 404


@app.route('/events', methods=['POST'])
def CreateEvent():
  try:
    if 'name' not in request.args:
      raise ValueError("Event is not created.  Event Name is not provided.  Please resubmit with the correct parameters.")
    if 'starttime' not in request.args:
      raise ValueError("Event is not created.  Event Start Time is not provided.  Please resubmit with the correct parameters.")
    if 'endtime' not in request.args:
      raise ValueError("Event is not created.  Event End Time is not provided.  Please resubmit with the correct parameters.")
    if 'location' not in request.args:
      raise ValueError("Event is not created.  Event Location is not provided.  Please resubmit with the correct parameters.")

    name = request.args['name']
    startTime = request.args['starttime']
    endTime = request.args['endtime']
    location = request.args['location']
    
    dataLayer = DataLayer()
    dataLayer.CreateEvent(name, location, startTime, endTime)

    return "Event '{}' has been created successful.".format(name), 200
  
  except Exception as ex:
    return str(ex), 404


@app.route('/attendees', methods=['GET'])
def FindAttendees():
  try:
    dataLayer = DataLayer()
    
    if 'email' in request.args:
      email = request.args['email']
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
    if 'email' not in request.args:
      raise ValueError("Attendee is not created.  Attendee email is not provided.  Please resubmit with the correct parameters.")

    email = request.args['email']

    dataLayer = DataLayer()
    dataLayer.CreateAttendee(email)

    return "Attendee '{}' has been created successful.".format(email), 200
  
  except Exception as ex:
    return str(ex), 404


@app.route('/invites', methods=['GET'])
def FindConfirmedInvitations():
  try:
    dataLayer = DataLayer()
    
    email, location, eventName, startTime, endTime = None, None, None, None, None
    emailKeyWord, locationKeyWord, eventNameKeyWord, startTimeKeyWord, endTimeKeyWord = "email", "location", "eventname", "starttime", "endtime"

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



if __name__ == '__main__':
     app.run(port='5002')
     