class ControllerMemberContainer():

    def __init__(self, member_container):
        self.member_container = member_container

    def get_new_ID(self):
        return "{:04d}".format(max([x.uid for x in self.member_container]) + 1)

    def get_member(self, UID):
        for i in self.member_container:
            if i.uid == UID:
                return str(i.uid) + i.first_name + i.last_name

    def get_members_by_role(self, Role):
        return [(str(x.uid) + " " + x.first_name + " " + x.last_name) for x in self.member_container if x.role == Role]

    def get_members_by_group(self, Group):
        return [(str(x.uid) + " " + x.first_name + " " + x.last_name + " " + x.my_group)
                 for x in self.member_container if x.my.group == Group]

    def add_member(self, User):
        self.member_container.append(User)

    def delete_member(self, UID):
        self.member_container = [x for x in self.member_container if x.uid != UID]
