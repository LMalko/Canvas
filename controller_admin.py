from controller_member_container import ControllerMemberContainer
from view_admin import ViewAdmin
from model_admin import ModelAdmin


class ControllerAdmin(ControllerMemberContainer):

    def __init__(self, user, member_container):
        self.associated_user = user
        self.controller_member_container = ControllerMemberContainer(member_container)
        self.view = ViewAdmin()

    def start(self):
        __choices = ['1: Add mentor', '2: View mentors list', '3: Log out']
        __correct_choices = [str(x+1) for x in range(1, len(__choices))]
        __user_input = ''
        __message = '\nPlease, type Your choice: '
        while True:
            while __user_input not in __correct_choices:
                self.view.display_collection(__choices)
                __user_input = self.get_user_input(__message)
            if __user_input == '1':
                self.add_mentor()
            elif __user_input == '2':
                self.view_mentor_list()
            elif __user_input == '3':
                break

    def add_mentor():
        print('adding mentor ;)')

    def remove_mentor():
        pass

    def edit_mentor():
        pass

    def view_mentor_list():
        print('displaying mentor list ;)')

    def view_student_list():
        pass
