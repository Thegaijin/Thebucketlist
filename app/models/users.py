
from .lists import Lists
from .items import Items


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

    def create_list(self, list_name, details):
        '''
        This method is used to create lists
        :params list_name
        :params details
        :params username
        '''

        if list_name is not None and details is not None:
            new_bucketlist = Lists(list_name, details)
            for lists in self.user_bucketlists:
                if list_name != lists:
                    self.user_bucketlists[list_name] = new_bucketlist
                return True
        return "A list by that name already exists"

    def update_list(self, list_name, details):
        '''
        Updates the properties of a list
        :param list_name;
        :param details;
        '''
        for key in self.user_bucketlists:
            if key == list_name:
                self.user_bucketlists[list_name].details = details
        # TODO: Implement the rest of the update functionality
            else:
                return "The list does not exist"

    def display_list(self):
        '''
        Displays the lists
        :return
        '''
        return self.user_bucketlists

    def delete_list(self, list_name):
        '''
        Deletes a list
        :param list_name
        '''

        for key in self.user_bucketlists:
            if key == list_name:
                del self.user_bucketlists[list_name]
            else:
                return "The list does not exist"

    def add_item(self, list_name, item, details):
        '''
        Adds items to list
        :param listname
        :param details
        '''

        if item is not None and details is not None:

            for key in self.user_bucketlists:
                if key == list_name:
                    item_name = Items(item, details)
                    self.user_bucketlists[list_name].create_item(
                        item, item_name)
                else:
                    return "The list does not exist"

        else:
            return "Please make sure you enter values for item and details"

    def update_item(self, list_name, item_name, details):
        '''
        Updates item properties
        :param list_name
        :param item_name
        :param details
        '''

        for key in self.user_bucketlists:
            if key == list_name:
                self.user_bucketlists[list_name].update_item(
                    item_name, details)
        # TODO: Implement the rest of the update functionality
            else:
                return "The list does not exist"

    def view_items(self, list_name):

        for key in self.user_bucketlists:
            if key == list_name:
                self.user_bucketlists[list_name].display_items()
            else:
                return "The list {} does not exist".format(list_name)

    def delete_item(self, list_name, item):

        for key in self.user_bucketlists:
            if key == list_name:
                self.user_bucketlists[list_name].delete()
            else:
                return "The list {} does not exist".format(list_name)
