from model_student import ModelStudent
from controller_task_container import ControllerTaskContainer
from view_student import ViewStudent
from controller_user import*


class ControllerStudent(ControllerUser):

    def __init__(self, user, task_container):
        self.associated_user = user
        self.controller_task_container = ControllerTaskContainer(task_container)
        self.view = ViewStudent()

    def start(self):
        pass

    def submit_task(self):
        pass
        # widoki
        # self.view.display()  # temp!!!
        # self.self.controller_task_container.change_delivery_status()  # którego zadania??
        # self.view.display()  # temp!!!

    def view_grades(self):
        pass
        # self.view.display()  # temp!!!
        # self.self.controller_task_container.change_delivery_status()  # którego zadania??
        # self.view.display()  # temp!!!

    @classmethod
    def get_controller_model_pair(cls):
        return {cls:ModelStudent}

