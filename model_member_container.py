from controller_member_container import ControllerMemberContainer


class ModelMemberContainer():

    def __init__(self):
        self.members = ControllerMemberContainer().member_container

    def add_member(self, User):
        ControllerMemberContainer().member_container.append(User)

    def delete_member(self, User):
        ControllerMemberContainer().delete_member(User.uid)

    def get_member(self, uid):
        ControllerMemberContainer().get_member(uid)