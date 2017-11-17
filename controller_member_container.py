class ControllerMemberContainer():

    def __init__(self, member_container):
        self.member_container = member_container

    def get_new_ID(self):
        return max([user.uid for user in self.member_container]) + 1

    def get_member(self, UID):
        for user in self.member_container:
            if user.uid == UID:
                return "{} {} {} {}.".format("{:04d}".format(user.uid), user.first_name, user.last_name, user.role)

    def get_members_by_role(self, Role):
        return ["{} {} {} {}.".format("{:04d}".format(user.uid), user.first_name, user.last_name, user.my_group)
                for user in self.member_container if user.role == Role]

    def get_members_by_group(self, Group):
        return ["{} {} {} {}.".format("{:04d}".format(user.uid), user.first_name, user.last_name, user.my_group)
                for user in self.member_container if user.my_group == Group]

    def add_member(self, User):
        self.member_container.append(User)

    def delete_member(self, UID):
        self.member_container = [user for user in self.member_container if user.uid != UID]
