from model_user import *
from view_user import *
from controller_member_container import *


class ControllerUser():

    def __init__(self):
        self.controller_member_container = ControllerMemberContainer()
        self.view = ViewUser()

    def _get_user(self):

        while True:
            user = self.view.get_user_input("Choose user by id: ")
            user = self.controller_member_container.get_member(UID)
            if user is not None:
                return user
            self.view.display_message("No such user. Try again.")

    def change_first_name(self, UID):
        new_first_name = self.validate_input("Pass new first name: ")
        user.set_first_name(new_name)
        self.view.display_message("Name has been changed!")

    def change_last_name(self, UID):
        new_last_name = self.validate_input("Pass new last name: ")
        user.set_last_name(new_last_name)
        self.view.display_message("Last name has been changed!")

    def change_password(self, UID):
        new_password = self.validate_input("Pass new password (not shorter than 6 chars): ")
        user.set_first_name(new_password)
        self.view.display_message("Password has been changed!")

    def validate_input(self, message):
        not_valid_input = True
        while not_valid_input:
            user_input = self.view.get_user_input(message)
            if (len(user_input.strip()) != 0):
                not_valid_input = False
            else:
                self.view.display_message("Invalid input. Try again. ")
        return user_input

    @classmethod
    def get_user_role(cls, user_class):
        return user_class.get_role_attribute()

    @classmethod
    def get_user_data_to_export(cls, user):
        return user.get_data_for_export()

