from model_user import ModelUser


class ModelStudent(ModelUser):
    role = 'student'

    def __init__(self, uid, first_name, last_name, password, my_group):
        self.uid = uid
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.set_email()
        self.set_login()
        self.my_group = my_group


