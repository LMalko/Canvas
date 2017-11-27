from controller_member_container import ControllerMemberContainer
from view_admin import ViewAdmin
from model_admin import ModelAdmin
from controller_mentor import ControllerMentor
from controller_user import ControllerUser


class ControllerAdmin(ControllerUser):

    def __init__(self, user, member_container):
        self.associated_user = user
        self.controller_member_container = ControllerMemberContainer(member_container)
        self.view = ViewAdmin()
        self.controller_mentor = ControllerMentor(None, None, member_container, None)

    def start(self):
        self.view.clear_screen()
        __choices = ['1: Add mentor', '2: View mentors list', '3: Release Mentor', '4: Log out']
        __correct_choices = [str(x+1) for x in range(1, len(__choices))]
        __message = '\nPlease, type Your choice: '
        __to_continue = True
        while __to_continue:
            __user_input = ''
            while __user_input not in __correct_choices:
                self.view.clear_screen()
                self.view.display_collection(__choices)
                __user_input = self.view.get_user_input(__message)
                if __user_input == '1':
                    self.add_mentor()
                elif __user_input == '2':
                    self.view_mentor_list()
                elif __user_input == '3':
                    self.remove_mentor()
                elif __user_input == '4':
                    __to_continue = False

    def add_mentor(self):
        self.view.display_message("\n\nLet's hire Mentor..\n\n")
        __user_inputs = []
        __messages = ['Enter first name: ', 'Enter last name: ', 'Specify password: ', 'Specify group: ']
        for statement in __messages:
            __user_input = self.validate_input(statement)
            __user_inputs.append(__user_input)
        __user = self.controller_mentor.create_mentor(
                                                    __user_inputs[0],
                                                    __user_inputs[1],
                                                    __user_inputs[2],
                                                    __user_inputs[3])
        self.view.display_message("\n\nMentor hired..\n\n")
        self.controller_member_container.add_member(__user)
        self.view.get_user_input('\nPress <enter> to continue.. ')

    def remove_mentor(self):
        self.view.display_message("\n\nLet's release Mentor..\n\n")
        self.view_mentor_list()
        self.view.get_user_input('\nChoose Mentor by UID.. ')
        self.view.display_message("\n\nWell abort, abort process! They're great!\n\n")
        self.view.get_user_input('\nPress <enter> to continue.. ')

    def edit_mentor(self):
        self.view.display_message("\n\nCongratulations, You have privilages to change mentor's details.\n")
        self.view.display_message("Choose mentor by ID.\n\n")
        self.view_mentor_list()
        while True:
            _mentor_ID = input("Mentor's ID is: ")
            _mentor_detail_to_change = input("You need to change: first name (1), last name (2) or password (3) ?")
            if _mentor_detail_to_change == "1":
                return ControllerUser().change_first_name(_mentor_ID)
            elif _mentor_detail_to_change == "2":
                return ControllerUser().change_last_name(_mentor_ID)
            elif _mentor_detail_to_change == "3":
                return ControllerUser().change_password(_mentor_ID)
            continue

    def view_mentor_list(self):
        self.view.display_message('\n\nMentors list:\n')
        __collection = self.controller_member_container.get_members_by_role('mentor')
        self.view.display_collection(__collection)
        self.view.get_user_input('\n\nPress <enter> to continue.. ')

    def view_student_list(self):
        pass

    def create_first_admin(self):
        return ModelAdmin(0, "admin", "admin", "qwerty")

    @classmethod
    def get_controller_model_pair(cls):
        return {cls: ModelAdmin}

    @classmethod
    def create_user_from_imported_data(cls, *args):
        return ModelAdmin(*args)