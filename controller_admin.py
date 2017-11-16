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
        __message = '\nPlease, type Your choice: '
        __to_continue = True
        while __to_continue:
            __user_input = ''
            while __user_input not in __correct_choices:
                self.view.display_collection(__choices)
                __user_input = self.view.get_user_input(__message)
                if __user_input == '1':
                    self.add_mentor()
                elif __user_input == '2':
                    self.view_mentor_list()
                elif __user_input == '3':
                    __to_continue = False

    def add_mentor(self):
        print('\n\nadding mentor ;)\n\n')

    def remove_mentor(self):
        pass

    def edit_mentor(self):
        pass

    def view_mentor_list(self):
        print('\n\ndisplaying mentor list ;)\n\n')

    def view_student_list(self):
        pass

    def create_first_admin(self):
        return ModelAdmin(0, "admin", "admin", "qwerty")
