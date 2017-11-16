from model_user import *
from view_user import *
import string


class ControllerUser():

    def __init__(self, ModelMemberContainer):
        self.model_member_container = model_member_container
        self.view = ViewUser

    def __get_user(self):

        while True:
            # print list of students - metoda z membera
            user_id = view.get_user_input("Choose user by id: ")
            # user = get user object from container, input
            if user is not None:
                return user
            self.view.display_message("No such user. Try again.")

    def change_first_name(self):
        not_valid_input = True
        while not_valid_input:
            new_name = self.view.get_user_input("Pass new first name: ")
            if (len(new_name.strip()) != 0) and (new_name not in string.punctuation):
                not_valid_input = False
            else:
                self.view.display_message("Invalid input. Try again. ")
        user = self.__get_user()
        user.set_first_name(new_name)
        self.view.display_message("Name has been changed!")

    def change_last_name(self):
        not_valid_input = True
        while not_valid_input:
            new_name = self.view.get_user_input("Pass new last name: ")
            if (len(new_name.strip()) != 0) and (new_name not in string.punctuation):
                not_valid_input = False
            else:
                self.view.display_message("Invalid input. Try again. ")
        user = self.__get_user()
        user.set_last_name(new_name)
        self.view.display_message("Name has been changed!")


    def change_password(self):
        not_valid_input = True
        while not_valid_input:
            new_password = self.view.get_user_input("Pass new password (not shorter than 6 chars): ")
            if (len(new_password.strip()) >= 6):
                not_valid_input = False
            else:
                self.view.display_message("Invalid input. Try again. ")
        user = self.__get_user()
        user.set_first_name(new_password)
        self.view.display_message("Name has been changed!")


    def display_list(self):
        pass

    def display_message(self):
        pass

    def get_user_input(self):
        pass