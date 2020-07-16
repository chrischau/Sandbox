from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from flask_jsonpify import jsonify
import json
import sys
import traceback
import logging
import pyodbc


app = Flask(__name__)
api = Api(app)
connectionString = "Driver={SQL Server};Server=SINWS0127;Database=Company;UID=sa;PWD=changeme;"

class Employees(Resource):
    def __init__(self):
        logging.basicConfig(filename="C:\Development\GitHub\Sandbox\Python\DonutFactory3000\ServerSide\server_trace.log",
                            filemode='a',
                            format='%(asctime)s.%(msecs)d-%(name)s-%(levelname)s-%(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.INFO)

        logging.info("Running logger in Employees constructor") #seems like it has to be in this order, before assigning to self.logger, weird and not sure why
        self.logger = logging.getLogger(__name__)
        
        self.dbConnection = pyodbc.connect(connectionString)

    def get(self):
        try: 
            self.logger.info("Inside Employees get function")
            
            cursor = self.dbConnection.cursor()
            cursor.execute("SELECT * FROM Employees")
      
            columns = [column[0] for column in cursor.description]
            results = []
            for row in cursor.fetchall():
                results.append(dict(zip(columns, row)))
            
            #print(results)
            self.logger.info(results)
            
            cursor.close()
            return jsonify(results)
            

        except Exception as ex:
            self.logger.error("Operation Failed:\n" + str(ex))
            
class Employees_Name(Resource):
    def __init__(self):
        logging.basicConfig(filename="C:\Development\GitHub\Sandbox\Python\DonutFactory3000\ServerSide\server_trace.log",
                            filemode='a',
                            format='%(asctime)s.%(msecs)d-%(name)s-%(levelname)s-%(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.INFO)

        logging.info("Running logger in Employees Name constructor")
        self.logger = logging.getLogger(__name__)
        
        self.dbConnection = pyodbc.connect(connectionString)

    def get(self, employee_id):
        try:
            self.logger.info("Inside Employees Name get function")
                
            cursor = self.dbConnection.cursor()
            cursor.execute("SELECT * FROM Employees WHERE EmployeeId = %d" %int(employee_id))
        
            columns = [column[0] for column in cursor.description]
            results = []
            for row in cursor.fetchall():
                results.append(dict(zip(columns, row)))
            
            #print(results)
            self.logger.info(results)
            
            cursor.close()
            return jsonify(results)
        
        except Exception as ex:
            self.logger.error("Operation Failed:\n" + str(ex))

api.add_resource(Employees, '/employees')
api.add_resource(Employees_Name, '/employees/<employee_id>')


if __name__ == '__main__':
     app.run(port='5002')
     