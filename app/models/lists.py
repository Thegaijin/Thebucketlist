class Lists(object):

    def __init__(self, list_name, details, username, checkbox='False'):
        self.items = []
        self.username = username
        self.list_name = list_name
        self.details = details
        self.checkbox = checkbox

    def output(self):
        return self.list_name, self.details


'''new = Lists('Mikr', 'Blah blah')
print(new.list_name)'''
