# Author: Chris Chau
# Prototyping in Python

class User:
    def __init__(self, firstName, lastName, phoneNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumber = phoneNumber
        #super().__init__()


class USUser(User):
    def __init__(self, firstName, lastName, phoneNumber, socialSecurity):
        super().__init__(firstName, lastName, phoneNumber)
        self.socialSecurity = socialSecurity

    def __init__(self, user, socialSecurity):
        super().__init__(user.firstName, user.lastName, user.phoneNumber)
        self.socialSecurity = socialSecurity

    

user = User("Chris", "Chau", 123456789)

print(user.firstName)
print(user.lastName)
print(user.phoneNumber)

usUser = USUser(user, 987654321)

print(usUser.socialSecurity)

for x in str(usUser.socialSecurity):
    print(x)