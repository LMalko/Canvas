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

    def get_data_for_export(self):
        return [self.role, self.uid, self.first_name, self.last_name, self.password, self.my_group]

    def get_menu_options(self):
        return ["1: View student list",
                "2: Edit student",
                "3: Add student",
                "4: View task list"
                "5: Grade task",
                "6: Add task",
                "7: Edit task",
                "8: Check attendance",
                "9: Get random groups of two",
                "10: Get random groups of four",
                "11: Log out"]
