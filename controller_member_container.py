from view_member_container import ViewMemberContainer
from model_member_container import ModelMemberContainer


class ControllerMemberContainer():

    def __init__(self, member_container_object):
        self.member_container = member_container_object
        self.view_member_container = ViewMemberContainer()
        self.model_member_container = ModelMemberContainer()

    def get_user(self):
        while True:
            user_id = self.view_member_container.get_user_input("Choose by id: ")
            user = self.get_member(user_id)
            if user is not None:
                return user
            self.view.display_message("No such user. Try again.")

    def get_new_ID(self):
        return str(max([int(user.uid) for user in self.member_container.get_all_members()]) + 1)

    def get_member(self, uid):
        for user in self.member_container.get_all_members():
            if user.uid == uid:
                return user

    def get_members_by_role(self, role):
        self.view_member_container.clear_screen()
        all_members = self.member_container.get_all_members()
        self.view_member_container.display_collection([self.model_member_container.get_member_display(user)
                                                       for user in all_members if user.role == role])
        return self.view_member_container.take_user_input("\n\nJeśli skończyłeś juz patrzeć to wciśnij coś.\n")

    def get_students_by_group(self):
        students = self.get_members_by_role('student')
        while True:
            student_group = self.view_member_container.take_user_input("Choose group: ")
            students_from_student_group = [student for student in students if student.get_my_group() == student_group]
            if students_from_student_group:
                return students_from_student_group
            self.view_member_container.display_message("No such group !!!")

    def add_member(self, user):
        self.member_container.add_member(user)

    def delete_member(self, uid):
        member_to_be_deleted = self.get_user(uid)
        if member_to_be_deleted is not None:
            self.member_container.delete_member(member_to_be_deleted)
