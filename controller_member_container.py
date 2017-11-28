from view_member_container import ViewMemberContainer


class ControllerMemberContainer():

    def __init__(self, member_container):
        self.member_container = member_container
        self.view_member_container = ViewMemberContainer()

    def get_new_ID(self):
        return str(max([int(user.uid) for user in self.member_container]) + 1)

    def get_member(self, UID):
        for user in self.member_container:
            if user.uid == UID:
                return user

    def get_members_by_role(self, Role):
        all_members = self.member_container.get_all_members()
        return [user for user in all_members if user.role == Role]

    def get_students_by_group(self):
        students = self.get_members_by_role('student')
        while True:
            student_group = self.view_member_container.take_user_input("Choose group: ")
            students_from_student_group = [student for student in students if student.get_my_group() == student_group]
            if students_from_student_group:
                return students_from_student_group
            self.view_member_container.display_message("No such group !!!")

    def add_member(self, User):
        self.member_container.append(User)

    def delete_member(self, UID):
        self.member_container = [user for user in self.member_container if user.uid != UID]
