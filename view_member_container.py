import os


class ViewMemberContainer():

    def __init__(self):
        pass

    def display_message(self, message):
        print("\n" + message + "\n")

    def get_user_input(self, message='==> '):
        message = '\n' + message
        return input(message)

    def freeze_until_key_pressed(self, message='Press any key to continue.. '):
        message = '\n' + message + '\n'
        input(message)

    def display_collection(self, collection):
        print('\n')
        for item in collection:
            print(item)
        print('\n')

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
