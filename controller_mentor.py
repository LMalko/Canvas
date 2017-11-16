from model_mentor import ModelMentor
from controller_task_container import ControllerTaskContainer
from view_mentor import ViewMentor


class ControllerMentor():

    def __init__(
                    self,
                    User,
                    ModelTaskContainer,
                    ModelAttendanceContainer,
                    ModelMemberContainer):
        self.associated_user = User
        self.view = ViewMentor()
        # self.controller_task_container = ControllerTaskContainer()  # tmp!
        self.model_task_container = ModelTaskContainer
        self.model_attendance_container = ModelAttendanceContainer
        self.model_member_container = ModelMemberContainer

    def view_grades(self):
        pass
        # self.view.display()  # temp!!!
        # self.self.controller_task_container.change_delivery_status()  # którego zadania??
        # self.view.display()  # temp!!!

    def view_student_list(self):
        pass

    def grade_task(self):
        pass

    def add_student(self):
        pass

    def check_attendance(self):
        pass

    def remove_student(self):
        pass
