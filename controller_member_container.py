class ControllerMemberContainer():

    def __init__(self, ModelMemberContainer):
        member_container = ModelMemberContainer()

    def get_member(self, UID):
        for i in member_container:
            if i.uid = uid:
                return i.uid + i.first_name + i.last_name

    def get_members_by_role(self, Role):
        return [(x.uid + x.first_name + x.last_name) for x in member_container if x.role == Role]

    def get_members_by_group(self, Group):
        return [(x.uid + x.first_name + x.last_name) for x in member_container if x.my.group == Group]

    def add_member(self, User):
        member_container.append(User)

    def delete_member(self, UID):
        member_container = [x for x in member_container if x.uid != UID]
