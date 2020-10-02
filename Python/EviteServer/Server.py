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
  dataLayer = DataLayer()
  
  if 'id' in request.args:
    id = int(request.args['id'])
    results = dataLayer.FindEvent(id, None)
    return jsonify(results)

  if 'name' in request.args:
    name = request.args['name']
    results = dataLayer.FindEvent(None, name)
    return jsonify(results)
    
  else:
    results = dataLayer.FindAllEvents()
    return jsonify(results)



if __name__ == '__main__':
     app.run(port='5002')
     