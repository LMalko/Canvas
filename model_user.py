class ModelUser():

    def set_email(self):
        self.email = "{}.{}{}@canvas.com".format(self.first_name, self.last_name, self.uid)

    def set_login(self):
        self.login = "{}-{}-{}".format(self.first_name, self.last_name, self.uid)

    def set_password(self, new_password):
        self.set_password = new_password

    def set_first_name(self, new_first_name):
        self.first_name = new_first_name
        self.set_email()
        self.set_login()

    def set_last_name(self, new_last_name):
        self.first_name = new_last_name
        self.set_email()
        self.set_login()