from model_user import ModelUser
from view_user import ViewUser


class ControllerUser():

    def __init__(self):
        self.view = ViewUser()

    def change_first_name(self, member):
        new_first_name = self.validate_input("Pass new first name: ")
        member.set_first_name(new_first_name)
        self.view.freeze_until_key_pressed("First name has been changed!")

    def change_last_name(self, member):
        new_last_name = self.validate_input("Pass new last name: ")
        member.set_last_name(new_last_name)
        self.view.freeze_until_key_pressed("Last name has been changed!")

    def change_password(self, member):
        new_password = self.validate_input("Pass new password (not shorter than 6 chars): ")
        member.set_password(new_password)
        self.view.freeze_until_key_pressed("Password has been changed!")

    def validate_input(self, message):
        not_valid_input = True
        while not_valid_input:
            user_input = self.view.get_user_input(message)
            if (len(user_input.strip()) != 0):
                not_valid_input = False
            else:
                self.view.display_message("Invalid input. Try again. ")
        return user_input

    def get_member_id(self, member):
        return member.get_id()

    def get_member_display(self, member):
        return member.get_member_display()

    def execute_member_display(self, member):
        self.view.clear_screen()
        self.view.display_message('\n' + member.get_full_data())
        self.view.freeze_until_key_pressed()
