from controller_member_container import ControllerMemberContainer
from view_admin import ViewAdmin
from model_admin import ModelAdmin


class ControllerAdmin(ControllerMemberContainer):

    def __init__(self, user, member_container):
        self.associated_user = user
        self.controller_member_container = ControllerMemberContainer(member_container)
        self.view = ViewAdmin()

    def start(self):
        pass

    def add_mentor():
        pass

    def remove_mentor():
        pass

    def edit_mentor():
        pass

    def view_mentor_list():
        pass

    def view_student_list():
        pass
