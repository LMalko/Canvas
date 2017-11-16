from model_mentor import ModelMentor
from controller_task_container import ControllerTaskContainer
from controller_attendance_container import ControllerAttendanceContainer
from controller_member_container import ControllerMemberContainer
from view_mentor import ViewMentor
from controller_user import*



class ControllerMentor(ControllerUser):

    def __init__(
                    self,
                    user,
                    task_container,
                    attendance_container,
                    member_container):
        self.associated_user = user
        self.view = ViewMentor()
        self.controller_task_container = ControllerTaskContainer(task_container)
        self.controller_attendance_container = ControllerAttendanceContainer(attendance_container)
        self.controller_member_container = ControllerMemberContainer(member_container)

    def start(self):
        pass

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
