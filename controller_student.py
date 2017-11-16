from model_student import ModelStudent
from controller_task_container import ControllerTaskContainer
from view_student import ViewStudent


class ControllerStudent():

    def __init__(self, User):
        self.associated_user = User
        self.controller_task_container = ControllerTaskContainer()
        self.view = ViewStudent()

    def submit_task(self):
        # widoki
        self.view.display()  # temp!!!
        self.self.controller_task_container.change_delivery_status()  # którego zadania??
        self.view.display()  # temp!!!

    def view_grades(self):
        pass
