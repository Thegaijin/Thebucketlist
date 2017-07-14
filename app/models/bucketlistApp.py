from .items import Items
from .lists import Lists
from .users import User


class BucketlistApp(object):
    '''
    The BucketlistApp class is the main implementation class.
    It has 3 functions, create_user, login and logout.
    It has 2 global variables Users and Users_List both dictionaries.
    Users holds the username and passwords of each user.
    Users_Lists holds all the users and their lists
    '''

    def __init__(self):
        self.usercredentials = {}
        self.users = {}
        self.user_names = []

    def create_user(self, username, password, confirm_password):
        if username != None or password != None or confirm_password != None:
            if username not in self.user_names:
                if password == confirm_password:
                    new_user = User(username)
                    self.user_names.append(username)
                    self.usercredentials[username] = password
                    self.users[username] = new_user
                    return 'Welcome to the Bucketlist app, please login'
                else:
                    return "The password combination was wrong"
            else:
                return "Your username already exists"
        return "Please make sure all the fields are filled in"

    def check_for_user(self, username):
        if username in self.users:
            return self.users[username]
        return None

    def login(self, username, password):
        if username in self.user_names:
            if password == self.usercredentials[username]:
                return "Successfully logged in"
            else:
                return "Your username and password combination is wrong, please try again"
                # TODO: Implement open Lists page
        else:
            return 'Your username does not exist'
        # return "Please make sure all the fields are filled in"

    def logout(self):
        pass
        # TODO: Implement logout functionality
