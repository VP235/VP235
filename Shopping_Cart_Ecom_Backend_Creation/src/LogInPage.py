import uuid
from src.Dashboard import Dashboard

"""After receiving the userName and userPass from the init page, it validates the login credentials of 
customer/admin. Once validated successfully it triggers dashboard process, if validation fails than it will dissplay 
Invalid login error msg. . Else, if it’s a new user than a row is added in the database."""


# generate a sessionId
def generate_sessionId():
    return str(uuid.uuid4())  # generated sessionId using random uuid


class LogInPage(Dashboard):
    # customer login credential dict
    customer_login = {
        'cust1': 'cust123',
        'cust2': 'cust234'
    }

    # admin login credential dict
    admin_login = {
        'admin1': 'admin123',
        'admin2': 'admin234'
    }

    # Dictionary to store session information (session_id: username)
    sessions = {}

    def __init__(self, userType, userName, userPass):
        super().__init__()
        self.userType = userType
        self.userName = userName
        self.userPass = userPass

    def check_login_cred(self, loginDict):

        # check if user already present
        if self.userName in loginDict.keys():

            # check the password matches the userName
            if loginDict[self.userName] == self.userPass:

                # create a sessionId for the user and store it in the sessions dict
                sessionId = generate_sessionId()
                self.sessions[sessionId] = self.userName

                # if credentials matches show catalog
                return True

            else:
                # if it does not match print invalid error
                print('Invalid Password...!\n')
                return False
        else:
            # if it's a new user, add its details in loginDict
            loginDict[self.userName] = self.userPass
            print(loginDict)

            return True

    # check the login credential if user already exist else create new
    def login(self):

        # check who is trying to log in Admin or Customer
        global validity
        if self.userType == 'admin':

            # if the user is Admin check his credentials from admin dict
            validity = self.check_login_cred(self.admin_login)

        elif self.userType == 'customer':
            # if the user is Customer check his credentials from customer dict
            validity = self.check_login_cred(self.customer_login)

        if validity:

            # show Dashboard
            self.showDashboard()

        else:
            print(f'*--$--* Try Re-logIn *--$--*'.center(60))
            self.userPass = input("Enter password : ")
            self.login()
