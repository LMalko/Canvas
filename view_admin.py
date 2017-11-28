from view_user import ViewUser


class ViewAdmin(ViewUser):

    def __init__(self):
        pass

    def take_user_input(self, message):
        return input(message)

    
