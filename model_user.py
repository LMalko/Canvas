class ModelUser():

    def __init__(self, uid, first_name, last_name, password):
        self.uid = uid
        self.first_name = first_name
        self.last_name = last_name
        self.set_password = password
        self.set_email()
        self.set_login()

    def set_email(self):
        self.email = "{}.{}{}@canvas.com".format(self.first_name, self.last_name, self.uid)

    def set_login(self):
        self.login = "{}-{}-{}".format(self.first_name, self.last_name, self.uid)

    def set_password(self, new_password):
        self.set_password = 

    def set_first_name(self):
        pass

    def set_last_name(self):
        pass