from model_user import *
from view_user import *


class ControllerUser():

    def __init__(self, ModelMemberContainer):
        self.model_member_container = model_member_container
        self.view = ViewUser
        
    def __get_user(self):
        # print list of students
        # get student id from input
        # get user object from container
        # return object

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