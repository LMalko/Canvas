from model_user import ModelUser


class ModelMentor(ModelUser):
    role = 'mentor'

    def __init__(self, uid, first_name, last_name, password, my_group):
        self.uid = uid
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.set_email()
        self.set_login()
        self.my_group = my_group

    def get_my_group(self):
        return self.my_group

    def get_full_data(self):
        return '{}\ngroup: {}'.format(super().get_full_data(), self.my_group)

    def get_data_for_export(self):
        return [self.role, self.uid, self.first_name, self.last_name, self.password, self.my_group]
