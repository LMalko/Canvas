from controller_member_container import ControllerMemberContainer
from view_office import ViewOffice
from model_office import ModelOffice
from controller_user import *


class ControllerOffice(ControllerUser):

    def __init__(self, user, member_container):
        self.associated_user = user
        self.view = ViewOffice()
        self.controller_member_container = ControllerMemberContainer(member_container)

    def start(self):
        self.view.clear_screen()
        choices = ['1: View student list', '2: Log out']
        correct_choices = [str(x+1) for x in range(1, len(choices))]
        message = '\nPlease, type Your choice: '
        to_continue = True
        while to_continue:
            user_input = ''
            while user_input not in correct_choices:
                self.view.clear_screen()
                self.view.display_collection(choices)
                user_input = self.view.get_user_input(message)
                if user_input == '1':
                    self.controller_member_container.get_members_display(
                        self.controller_member_container.get_members_by_role("student"))
                elif user_input == '2':
                    to_continue = False
