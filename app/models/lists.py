class Lists(object):

    def __init__(self, list_name, details, checkbox='False'):
        self.items = {}
        self.list_name = list_name
        self.details = details
        self.checkbox = checkbox

    def create_item(self, item, item_name):
        self.items[item] = item_name
        print(self.items)

    def update_details(self, item, details):
        if item in self.items:
            self.items[item].details = details
        else:
            return "The item {} does not exist in your list".format(item)

    def display_items(self):
        return self.items

    def delete(self, item):
        del self.items[item]
