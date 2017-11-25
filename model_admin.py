from model_user import ModelUser


class ModelAdmin(ModelUser):

    role = "admin"

    def __init__(self, uid, first_name, last_name, password):
        self.uid = uid
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.set_email()
        self.set_login()

    def get_data_for_export(self):
        return [self.role, self.uid, self.first_name, self.last_name, self.password]