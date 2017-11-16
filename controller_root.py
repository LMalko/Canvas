from controller_attendance_container import *
from controller_member_container import *
from controller_task_container import *

from model_attendance_container import *
from model_member_container import *
from model_task_container import *

from model_root import *

class ControllerRoot:

    def __init__(self):
        self.initialize_model()

    def initialize_model(self):
        self.associated_model = ModelRoot()

    def login(user_login, input_password):
        '''
        Checks whether user password matches the input_password.
        '''
        pass

    def engage_user_controller(user_obj):
        '''
        Launches a user controller based on class of user_obj.
        '''
        pass

    def initialize_containers(self):
        pass

    def initial_admin_creation(self):
        pass
