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
                    attendance_container,
                    member_container,
                    task_container):
        self.associated_user = user
        self.view = ViewMentor()
        self.controller_task_container = ControllerTaskContainer(task_container)
        self.controller_attendance_container = ControllerAttendanceContainer(attendance_container)
        self.controller_member_container = ControllerMemberContainer(member_container)

    def start(self):
        pass

    def create_mentor(self, first_name, last_name, password, my_group):
        '''Return ModelMentor object.'''
        __uid = self.controller_member_container.get_new_ID()
        return ModelMentor(__uid, first_name, last_name, password, my_group)

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

    def get_role_class_pair(self):
        return {ModelMentor.role:ModelMentor}

