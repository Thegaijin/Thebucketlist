from items import Items
from lists import Lists
from users import User


class BucketlistApp():
    '''
    The BucketlistApp class is the main implementation class.
    It has 3 functions, create_user, login and logout.
    It has 2 global variables Users and Users_List both dictionaries.
    Users holds the username and passwords of each user.
    Users_Lists holds all the users and their lists
    '''

    def __init__(self):
        self.UserCredentials = {}
        self.Users = []

    def create_user(self, username, password):
        if isinstance(username, str) and username not in self.Users:
            new_user = User(username)
            self.Users.append[new_user]
            self.UserCredentials[username] = password

    def login(self, username, password):
        if isinstance(username, str) and username in self.Users:
            if password == self.Users[username]:
                pass
                # TODO: Implement open Lists page

    def logout(self):
        pass
        # TODO: Implement logout functionality
