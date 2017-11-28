class ViewMemberContainer():

    def __init__(self):
        pass

    def display_message(self, message):
        print("\n\n" + message + "\n\n")

    def take_user_input(self, message):
        return input(message)

    def display_collection(self, collection):
        for item in collection:
            print(item)
