import os


class ViewUser():

    def get_user_input(self, message):
        return input(message)

    def freeze_until_key_pressed(self, message='Press any key to continue.. '):
        message = '\n' + message
        freeze_message = input(message)
        return None

    def display_collection(self, collection):
        for item in collection:
            print(item)

    def display_message(self, message):
        print(message)

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_nested_collection(self, collection):
        for element in collection:
            print(", ".join(element))
