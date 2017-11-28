from controller_member_container import ControllerMemberContainer
from view_admin import ViewAdmin
from model_admin import ModelAdmin
from controller_mentor import ControllerMentor
from controller_user import ControllerUser
import sys


class ControllerAdmin(ControllerUser):

    def __init__(self, user, member_container):
        self.associated_user = user
        self.controller_member_container = ControllerMemberContainer(member_container)
        self.view = ViewAdmin()
        self.controller_mentor = ControllerMentor(None, None, member_container, None)

    def start(self):
        self.view.clear_screen()
        choices = ["1: Add mentor", "2: View mentors list", "3: Release Mentor", "4: Log out"]
        correct_choices = [str(x+1) for x in range(1, len(choices))]
        message = "\nPlease, type Your choice: "
        to_continue = True
        while True:
            user_input = ''
            while user_input not in correct_choices:
                self.view.clear_screen()
                self.view.display_collection(choices)
                user_input = self.view.get_user_input(message)
                if user_input == "1":
                    self.add_mentor()
                elif user_input == "2":
                    self.controller_member_container.get_members_by_role('mentor')
                elif user_input == "3":
                    self.remove_mentor()
                elif user_input == "4":
                    self.view.clear_screen()
                    sys.exit()

    def add_mentor(self):
        self.view.display_message("\n\nLet's hire Mentor..\n\n")
        user_inputs = []
        messages = ["Enter first name: ", "Enter last name: ", "Specify password: ", "Specify group: "]
        for statement in messages:
            user_input = self.validate_input(statement)
            user_inputs.append(user_input)
        user = self.controller_mentor.create_mentor(user_inputs[0],
                                                    user_inputs[1],
                                                    user_inputs[2],
                                                    user_inputs[3])
        self.view.clear_screen()
        self.view.display_message("\n\nMentor hired..\n\n")
        self.controller_member_container.add_member(user)
        self.view.freeze_until_key_pressed("\nPress anything to continue.")

    def remove_mentor(self):
        self.view.display_message("\n\nLet's release Mentor..\n\n")
        self.controller_member_container.get_members_by_role('mentor')
        mentor_to_release = self.controller_member_container.get_user()
        self.controller_member_container.delete_member(mentor_to_release)
        self.view.freeze_until_key_pressed("Done !! Press anything to continue.")

    def edit_mentor(self):
        self.view.display_message("\n\nCongratulations, You have privilages to change mentor's details.\n")
        while True:
            self.get_members_display(self.controller_member_container.get_members_by_role('mentor'))
            mentor_to_change = self.controller_user.get_user()
            if mentor_to_change in [user for user in self.controller_member_container.get_members_by_role('mentor')]:
                break
            self.view.display_message("\n\nThis user is not a mentor!\n")
        while True:
            mentor_detail_to_change = self.view.get_user_input("Change: first name (1) last name (2) or password (3) ?")
            if mentor_detail_to_change == "1":
                return self.controller_user.change_first_name(self.controller_user.get_member_id(mentor_to_change))
            elif mentor_detail_to_change == "2":
                return self.controller_user.change_last_name(self.controller_user.get_member_id(mentor_to_change))
            elif mentor_detail_to_change == "3":
                return self.controller_user.change_password(self.controller_user.get_member_id(mentor_to_change))
            self.view.display_message("\n\n\nRead instructions properly and try again.\n\n\n")
            continue

    def get_members_display(self, members):
        for person in members:
            self.view.display_message(self.controller_user.get_member_display(person))

    def create_first_admin(self):
        return ModelAdmin(0, "admin", "admin", "qwerty")


