import os


class ViewMemberContainer():

    def __init__(self):
        pass

    def display_message(self, message):
        print("\n\n" + message + "\n\n")

    def take_user_input(self, message):
        return input(message)

    def freeze_until_key_pressed(self, message='Press any key to continue.. '):
        message = '\n' + message
        freeze_message = input(message)
        return None

    def display_collection(self, collection):
        for item in collection:
            print(item)

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def get_user_input(self, message):
        return input(message)
