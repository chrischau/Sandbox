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


if __name__ == '__main__':
     app.run(port='5002')
     