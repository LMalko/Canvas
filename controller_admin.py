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
        choices = [
                    " 1: View my data",
                    " 2: Add mentor",
                    " 3: View mentors list",
                    " 4: Release Mentor",
                    " 5: Edit mentor's details",
                    " 6: View student list",
                    " 0: Log out"]
        correct_choices = [str(x) for x in range(0, len(choices))]
        message = "\nPlease, type Your choice: "
        to_continue = True
        while to_continue:
            user_input = ''
            while user_input not in correct_choices:
                self.view.clear_screen()
                self.view.display_collection(choices)
                user_input = self.view.get_user_input(message)
                if user_input == "1":
                    self.execute_member_display(self.associated_user)
                if user_input == "2":
                    self.add_mentor()
                elif user_input == "3":
                    self.get_mentors_list_to_display()
                elif user_input == "4":
                    self.remove_mentor()
                elif user_input == "5":
                    self.edit_mentor()
                elif user_input == "6":
                    self.get_students_list_to_display()
                elif user_input == "0":
                    self.view.clear_screen()
                    to_continue = False

    def add_mentor(self):
        self.view.clear_screen()
        self.view.display_message("\n\nLet's hire Mentor..\n\n")
        user_inputs = []
        messages = ["Enter first name: ", "Enter last name: ", "Specify password: ", "Specify group: "]
        for num, statement in enumerate(messages):
            if num in (0, 1):
                user_input = self.validate_input_name(statement)
            else:
                user_input = self.validate_input(statement)
            user_inputs.append(user_input)
        user = self.controller_mentor.create_mentor(user_inputs[0],
                                                    user_inputs[1],
                                                    user_inputs[2],
                                                    user_inputs[3])
        self.view.clear_screen()
        self.view.display_message("\n\nMentor hired..")
        self.controller_member_container.add_member(user)
        self.view.freeze_until_key_pressed()

    def get_mentors_list_to_display(self):
        self.get_members_list_to_display(self.controller_member_container.get_members_by_role("mentor"))

    def get_students_list_to_display(self):
        self.get_members_list_to_display(self.controller_member_container.get_members_by_role("student"))

    def remove_mentor(self):
        mentors = self.controller_member_container.get_members_by_role("mentor")
        if not mentors:
            self.view.freeze_until_key_pressed("There is no one to release. Press any key.. ")
        else:
            self.controller_member_container.get_members_display(mentors)
            if len(mentors) == 1:
                mentor_to_release = mentors[0]
            else:
                mentor_to_release = self.controller_member_container.get_user('mentor')
            self.controller_member_container.delete_member(mentor_to_release)
            self.view.freeze_until_key_pressed("Done! Press anything to continue. ")

    def edit_mentor(self):
        mentors = self.controller_member_container.get_members_by_role("mentor")
        if not mentors:
            self.view.freeze_until_key_pressed("There is no one to edit. Press any key.. ")
        else:
            self.controller_member_container.get_members_display(mentors)
            if len(mentors) == 1:
                mentor_to_change = mentors[0]
            else:
                mentor_is_chosen = False
                while not mentor_is_chosen:
                    mentor_to_change = self.controller_member_container.get_user()
                    if mentor_to_change in [
                            user for user in self.controller_member_container.get_members_by_role('mentor')]:
                        mentor_is_chosen = True
                        break
                    self.view.display_message("This user is not a mentor!")
            detail_to_change_is_chosen = False
            while not detail_to_change_is_chosen:
                self.view.display_message("Let's change data of {}:".format(mentor_to_change.get_fullname()))
                mentor_detail_to_change = self.view.get_user_input(
                                        "Change: first name (1) last name (2) or password (3)? ")
                if mentor_detail_to_change == "1":
                    return self.change_first_name(mentor_to_change)
                elif mentor_detail_to_change == "2":
                    return self.change_last_name(mentor_to_change)
                elif mentor_detail_to_change == "3":
                    return self.change_password(mentor_to_change)
                self.view.freeze_until_key_pressed("Read instructions properly and try again. Press any key.. ")

    def create_first_admin(self):
        return ModelAdmin(0, "admin", "admin", "qwerty")
