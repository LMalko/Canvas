from model_user import User


class Mentor(User):
    role = 'Mentor'

    def __init__(
                    self,
                    uid,
                    first_name,
                    last_name,
                    password,
                    my_group):

        super().__init__(
                        uid,
                        first_name,
                        last_name,
                        password)
        self.my_group = my_group
