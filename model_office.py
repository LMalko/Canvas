from model_user import ModelUser


class ModelOffice(ModelUser):
    role = 'office'

    def __init__(self, uid, first_name, last_name, password):
        self.uid = uid
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.set_email()
        self.set_login()