from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from sqlalchemy import create_engine
from flask_jsonpify import jsonify
import json
import sys
import traceback
import logging
import pyodbc
from DataLayer import UserData

app = Flask(__name__)
api = Api(app)
connectionString = "Driver={SQL Server};Server=SINWS0127;Database=EscrowService;UID=sa;PWD=changeme;"


class Users(Resource):
    def __init__(self):
        logging.basicConfig(filename="C:\Development\GitHub\Sandbox\Python\DonutFactory3000\ServerSide\server_trace.log",
                            filemode='a',
                            format='%(asctime)s.%(msecs)d-%(name)s-%(levelname)s-%(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.INFO)

        logging.info("Running logger in Users constructor") #seems like it has to be in this order, before assigning to self.logger, weird and not sure why
        self.logger = logging.getLogger(__name__)
        #self.dbConnection = pyodbc.connect(connectionString)
        self.userData = UserData()

    def get(self, name):
        try: 
            users = self.userData.FindUser(name)
            return users, 200

        except Exception as ex:
            self.logger.error("Operation Failed:\n" + str(ex))
            return str(ex), 404


    def post(self, name):
        try:
            self.userData.AddUser(name)
            return "User {} has been added successfully".format(name), 201

        except Exception as ex:
            self.logger.error("Operation Failed:\n" + str(ex))
            return str(ex), 400


    def delete(self, name):
        try:
            result = self.userData.RemoveUser(name)
            return result, 200
        
        except Exception as ex:
            self.logger.error("Operation Failed:\n" + str(ex))
            return str(ex), 404
        

    
    def put(self, name):
        try:
            result = self.userData.UpdateUser(name)
            
            if (result == 1):
                return "User {} is successfully updated.".format(name), 200
            elif (result == 0):
                return "User {} is successfully added.".format(name), 201
            else:
                raise NameError("Unknown error occurred")
    
        except Exception as ex:
            self.logger.error("Operation Failed:\n" + str(ex))
            return str(ex), 404
        
        
            


api.add_resource(Users, '/users/<string:name>')
#api.add_resource(Users, '/users/<user_id>')


if __name__ == '__main__':
     app.run(port='5002')
     