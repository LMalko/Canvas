class ViewControllerTaskContainer():

    def get_user_input(self, message='type Your choice ==> '):
        message = '\n' + message
        return input(message)

    def display_collection(self, collection):
        print('\n')
        for item in collection:
            print(item)
        print('\n')

    def display_message(self, message):
        print(message)
