class ControllerMemberContainer():

    def __init__(self, member_container):
        self.member_container = member_container

    def get_member(self, UID):
        for i in self.member_container:
            if i.uid == UID:
                return i.uid + i.first_name + i.last_name

    def get_members_by_role(self, Role):
        return [(x.uid + x.first_name + x.last_name) for x in self.member_container if x.role == Role]

    def get_members_by_group(self, Group):
        return [(x.uid + x.first_name + x.last_name) for x in self.member_container if x.my.group == Group]

    def add_member(self, User):
        self.member_container.append(User)

    def delete_member(self, UID):
        self.member_container = [x for x in self.member_container if x.uid != UID]
