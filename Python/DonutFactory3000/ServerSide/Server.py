from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from sqlalchemy import create_engine
from flask_jsonpify import jsonify
import json
import sys
import traceback
import logging
import pyodbc


app = Flask(__name__)
api = Api(app)
connectionString = "Driver={SQL Server};Server=SINWS0127;Database=EscrowService;UID=sa;PWD=changeme;"

users = [{"name" : "Nicholas", "age" : 42, "occupation" : "Network Engineer"},
         {"name" : "Elvin", "age" : 32, "occupation" : "Doctor"},
         {"name" : "Jass", "age" : 22, "occupation" : "Web Developer"}]
         
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

    def get(self, name):
        try: 
            #self.logger.info("Inside Users get function")
            
            # cursor = self.dbConnection.cursor()
            # cursor.execute("SELECT * FROM Users")
      
            # columns = [column[0] for column in cursor.description]
            # results = []
            # for row in cursor.fetchall():
            #     results.append(dict(zip(columns, row)))
            
            # #print(results)
            # self.logger.info(results)
            
            # cursor.close()
            # return jsonify(results)
            
            if not name.strip():
                return users, 200

            for user in users:
                if (user["name"] == name):
                    return user, 200
            
            return "User not found", 404

        except Exception as ex:
            self.logger.error("Operation Failed:\n" + str(ex))

    
    # def get(self, user_id):
    #     try:
    #         self.logger.info("Inside Find User By Id get function")
                
    #         cursor = self.dbConnection.cursor()
    #         cursor.execute("SELECT * FROM Users WHERE UserId = %d" %int(user_id))
        
    #         columns = [column[0] for column in cursor.description]
    #         results = []
    #         for row in cursor.fetchall():
    #             results.append(dict(zip(columns, row)))
            
    #         #print(results)
    #         self.logger.info(results)
            
    #         cursor.close()
    #         return jsonify(results)
        
    #     except Exception as ex:
    #         self.logger.error("Operation Failed:\n" + str(ex))

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if (name == user["name"]):
                return "User with name {} already exists.".format(name), 400

        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]            
        }

        users.append(user)
        return user, 201
    

    def delete(self, name):
        for user in users:
            if (user["name"] == name):
                users.remove(user)
                return "{} is deleted.".format(name), 200

        return "User not found", 404

    
    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if (name == user["name"]):
                user["age"] = args["age"]
                user["occupation"] = args["occupation"]
                return user, 200

        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]            
        }

        users.append(user)
        return user, 201

            


api.add_resource(Users, '/users/<string:name>')
#api.add_resource(Users, '/users/<user_id>')


if __name__ == '__main__':
     app.run(port='5002')
     