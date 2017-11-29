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
                    "1: Add mentor",
                    "2: View mentors list",
                    "3: Release Mentor",
                    "4: Edit mentor's details",
                    "5: View student list",
                    "6: Log out"]
        correct_choices = [str(x+1) for x in range(1, len(choices))]
        message = "\nPlease, type Your choice: "
        to_continue = True
        while to_continue:
            user_input = ''
            while user_input not in correct_choices:
                self.view.clear_screen()
                self.view.display_collection(choices)
                user_input = self.view.get_user_input(message)
                if user_input == "1":
                    self.add_mentor()
                elif user_input == "2":
                    self.get_mentors_list_to_display()
                elif user_input == "3":
                    self.remove_mentor()
                elif user_input == "4":
                    self.edit_mentor()
                elif user_input == "5":
                    self.get_students_list_to_display()
                elif user_input == "6":
                    self.view.clear_screen()
                    to_continue = False

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
        self.view.freeze_until_key_pressed("Press anything to continue.")

    def get_mentors_list_to_display(self):
        self.controller_member_container.get_members_display(
             self.controller_member_container.get_members_by_role("mentor"))
        self.view.freeze_until_key_pressed()

    def get_students_list_to_display(self):
        self.controller_member_container.get_members_display(
            self.controller_member_container.get_members_by_role("student"))
        self.view.freeze_until_key_pressed()

    def remove_mentor(self):
        mentors = self.controller_member_container.get_members_by_role("mentor")
        if not mentors:
            self.view.freeze_until_key_pressed("There is no one to release. Press any key.. ")
        else:
            self.controller_member_container.get_members_display(mentors)
            mentor_to_release = self.controller_member_container.get_user('mentor')
            if mentor_to_release:
                self.controller_member_container.delete_member(mentor_to_release)
                self.view.freeze_until_key_pressed("Done! Press anything to continue. ")

    def edit_mentor(self):
        mentors = self.controller_member_container.get_members_by_role("mentor")
        if not mentors:
            self.view.freeze_until_key_pressed("There is no one to edit. Press any key.. ")
        else:
            self.controller_member_container.get_members_display(mentors)
            mentor_is_chosen = False
            while not mentor_is_chosen:
                mentor_to_change = self.controller_member_container.get_user()
                if mentor_to_change in [
                        user for user in self.controller_member_container.get_members_by_role('mentor')]:
                    mentor_is_chosen = True
                self.view.display_message("\n\nThis user is not a mentor!\n")
            detail_to_change_is_chosen = False
            while not detail_to_change_is_chosen:
                mentor_detail_to_change = self.view.get_user_input("Change: first name (1) last name (2) or password (3)? ")
                if mentor_detail_to_change == "1":
                    return self.change_first_name(mentor_to_change)
                elif mentor_detail_to_change == "2":
                    return self.change_last_name(mentor_to_change)
                elif mentor_detail_to_change == "3":
                    return self.change_password(mentor_to_change)
                self.view.freeze_until_key_pressed("Read instructions properly and try again. Press any key.. ")

    def create_first_admin(self):
        return ModelAdmin(0, "admin", "admin", "qwerty")
