class ControllerMemberContainer():

    def __init__(self, member_container):
        self.member_container = member_container

    def get_new_ID(self):
        return str(max([int(user.uid) for user in self.member_container]) + 1)

    def get_member(self, UID):
        for user in self.member_container:
            if user.uid == UID:
                return user

    def get_members_by_role(self, Role):
        return [user for user in self.member_container if user.role == Role]
# get students by group z petlą walidacją czy ta grupa istnieje z metod get_my.group
    def get_students_by_group(self, Group):
        students = get_members_by_role(self, 'student')
        return [student for student in students if ]

    def add_member(self, User):
        self.member_container.append(User)

    def delete_member(self, UID):
        self.member_container = [user for user in self.member_container if user.uid != UID]
