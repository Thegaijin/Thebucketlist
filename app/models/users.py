from .lists import Lists


class User(object):
    '''
    User is an object which is used to create, edit, update and delete bucketlists.
    It is also used to add, view, update, and delete items from the lists
    '''

    def __init__(self, username):
        # Dictionary to store lists, list_name is key, List object is value
        self.user_bucketlists = {}
        # username holds the username parameter passed to the class
        self.username = username

    def create_list(self, list_name, details, username, checkbox='False'):
        '''
        This method is used to create lists
        :params list_name; Data type > string
        :params details; Data type > string
        :params user_name; Data type >string
        :params checkbox; Data type > Boolean. This is an optional paramater...
        '''
        '''new_list_name = self.username + '-' + list_name'''
        if list_name != None and details != None:
            if isinstance(list_name, str) and isinstance(details, str):
                new_bucketlist = Lists(list_name, details, username)
                self.user_bucketlists[list_name] = new_bucketlist
                print(self.user_bucketlists[list_name])

    def update_list(self, list_name, details):

        if isinstance(list_name, str):
            for key in self.user_bucketlists:
                if key == list_name:
                    self.user_bucketlists[list_name].details = details
            # TODO: Implement the rest of the update functionality

    def view_list(self, list_name):
        if isinstance(list_name, str):
            for key in self.user_bucketlists:
                if key == list_name:
                    return list_name

    def delete_list(self, name_of_list):
        if isinstance(name_of_list, str):
            for key in self.user_bucketlists:
                if key == list_name:
                    del.self.user_bucketlists[listname]


new = User('Thegaijin')
new.create_list("Travel", "East west and all that", 'Thegaijin')
'''new.create_list("Fly", " west and all that", 'Thegaijin')


new.create_list("Level", "East west all that", 'Thegaijin')
new.create_list("Jump", "East west and that", 'Thegaijin')
new.create_list("Skip", "East west all", 'Thegaijin')
new.create_list("Read", "all that", 'Thegaijin')
new.create_list("Scoop", "East", 'Thegaijin')
new.create_list("Mate", "that", 'Thegaijin')'''
