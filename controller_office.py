from model_office import ModelOffice
from controller_user import *


class ControllerOffice(ControllerUser):

    def __init__(self, user, attendance_container, member_container, task_container):
        self.associated_user = user
        self.view = ViewOffice()
        self.controller_task_container = ControllerTaskContainer(task_container)

    def start(self):
        pass

    def view_student_list(self):
        pass

    @classmethod
    def get_controller_model_pair(cls):
        return {cls:ModelOffice}

    @classmethod
    def create_user_from_imported_data(cls, *args):
        return ModelOffice(*args)

