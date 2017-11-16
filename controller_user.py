from model_user import *
from view_user import *


class ControllerUser():

    def __init__(self, ModelMemberContainer):
        self.model_member_container = model_member_container
        self.view = ViewUser

    def __get_user(self):

        while True:
            # print list of students - metoda z membera
            user_id = view.get_user_input("Choose user by id: ")
            # user = get user object from container, input
            if user != None:
                return user
            self.view.display_message("No such user. Try again.")

    def change_first_name(self):
        # using getter get user obj
        # get new name from input
        # call model_member_container on user, pas new name

    def change_lats_name(self):
        pass

    def change_password(self):
        pass

    def display_list(self):
        pass

    def display_message(self):
        pass

    def get_user_input(self):
        pass