from controller_member_container import ControllerMemberContainer


class ModelMemberContainer():

    def __init__(self):
        self.members = ControllerMemberContainer().member_container

    def add_member(User):
        ControllerMemberContainer().member_container.append(User)

    def delete_member(User):
        ControllerMemberContainer().delete_member(User.uid)

    def get_member(uid):
        ControllerMemberContainer().get_member(uid)