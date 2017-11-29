from view_member_container import ViewMemberContainer
from model_member_container import ModelMemberContainer


class ControllerMemberContainer():

    def __init__(self, member_container_object):
        self.member_container = member_container_object
        self.view_member_container = ViewMemberContainer()
        self.model_member_container = ModelMemberContainer()

    def get_user(self, role=None):
        user_is_chosen = False
        while not user_is_chosen:
            user_id = self.view_member_container.get_user_input("\nChoose by id: ")
            user = self.get_member(user_id)
            if not user:
                self.view_member_container.freeze_until_key_pressed("\nNo such user. Try again.\n")
            elif role and user and user not in self.get_members_by_role(role):
                self.view_member_container.freeze_until_key_pressed("\nThis user exists but has a different role.\n")
            else:
                user_is_chosen = True
                return user

    def get_new_ID(self):
        return str(max([int(user.uid) for user in self.member_container.get_all_members()]) + 1)

    def get_member(self, uid):
        for user in self.member_container.get_all_members():
            if user.uid == uid:
                return user

    def get_member_id(self, member):
        return member.uid

    def get_members_by_role(self, role):
        all_members = self.member_container.get_all_members()
        all_members_by_role = [member for member in all_members if member.role == role]
        return all_members_by_role

    def get_members_display(self, members):
        self.view_member_container.clear_screen()
        self.view_member_container.display_collection([self.model_member_container.get_member_display(member)
                                                       for member in members])

    def get_students_by_group(self):
        students = self.get_members_by_role('student')
        while True:
            student_group = self.view_member_container.take_user_input("\nChoose group: ")
            students_from_student_group = [student for student in students if student.get_my_group() == student_group]
            if students_from_student_group:
                return students_from_student_group
            self.view_member_container.display_message("\nNo such group !!!")

    def add_member(self, user):
        self.member_container.add_member(user)

    def delete_member(self, member):
        self.member_container.delete_member(member)

    def get_all_members(self):
        return self.member_container.get_all_members()
