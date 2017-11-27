class ViewControllerTaskContainer():

    def get_user_input(self, message):
        return input(message)

    def display_collection(self, collection):
        for item in collection:
            print(item)

    def display_message(self, message):
        print(message)