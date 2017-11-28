class ModelMemberContainer():

    def __init__(self):
        self.members = []

    def add_member(self, user):
        self.members.append(user)

    def delete_member(self, user):
        self.members.remove(user)

