from controller_member_container import ControllerMemberContainer
from view_office import ViewOffice
from model_office import ModelOffice
from controller_user import ControllerUser


class ControllerOffice(ControllerUser):

    def __init__(self, user, member_container):
        self.associated_user = user
        self.view = ViewOffice()
        self.controller_member_container = ControllerMemberContainer(member_container)

    def start(self):
        self.view.clear_screen()
        choices = [
                    ' 1: View my data',
                    ' 2: View student list',
                    ' 0: Log out']
        correct_choices = [str(x) for x in range(0, len(choices))]
        message = '\nPlease, type Your choice: '
        to_continue = True
        while to_continue:
            user_input = ''
            while user_input not in correct_choices:
                self.view.clear_screen()
                self.view.display_collection(choices)
                user_input = self.view.get_user_input(message)
                if user_input == '1':
                    self.execute_member_display(self.associated_user)
                elif user_input == '2':
                    self.get_students_list_to_display()
                elif user_input == '0':
                    to_continue = False

    def get_students_list_to_display(self):
        self.controller_member_container.get_members_display(
            self.controller_member_container.get_members_by_role("student"))
        self.view.freeze_until_key_pressed()
