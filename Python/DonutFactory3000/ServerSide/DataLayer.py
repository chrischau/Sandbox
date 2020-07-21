# Data Layer class to return reults from database interaction
# This is for code separation and ease of change
from flask_restful import Resource, Api, reqparse

class UserData:
    users = [{"name" : "Nicholas", "age" : 42, "occupation" : "Network Engineer"},
            {"name" : "Elvin", "age" : 32, "occupation" : "Doctor"},
            {"name" : "Jass", "age" : 22, "occupation" : "Web Developer"}]

    def FindUser(self, name):
        if (name.strip().lower() == "all"):
            return self.users
        
        if not name.strip():
            return self.users

        for user in self.users:
            if (user["name"] == name):
                return user
        
        raise NameError("User {} does not exist.".format(name))

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


    def AddUser(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in self.users:
            if (name == user["name"]):
                raise NameError("User with name {} already exists.".format(name))

        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]            
        }

        self.users.append(user)

    
    def RemoveUser(self, name):
        for user in self.users:
            if (user["name"] == name):
                self.users.remove(user)
                return "User {} is deleted.".format(name)

        raise NameError("User not found")
    
        
    def UpdateUser(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in self.users:
            if (name == user["name"]):
                user["age"] = args["age"]
                user["occupation"] = args["occupation"]
                return 1

        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]            
        }

        self.users.append(user)
        return 0


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