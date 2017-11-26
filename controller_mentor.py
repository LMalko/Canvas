from model_mentor import ModelMentor
from controller_task_container import ControllerTaskContainer
from controller_attendance_container import ControllerAttendanceContainer
from controller_member_container import ControllerMemberContainer
from view_mentor import ViewMentor
from controller_user import*
from itertools import zip_longest, chain
from random import shuffle


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

    @classmethod
    def get_controller_model_pair(cls):
        return {cls: ModelMentor}

    @classmethod
    def create_user_from_imported_data(cls, *args):
        return ModelMentor(*args)

    def get_random_student_group(self, size=2):
        shuffle(self.controller_member_container)
        groups_of_two = list(zip_longest([member for member in self.controller_member_container
                             if self.controller_member_container.index(member) % 2 == 0],
                             [member for member in self.controller_member_container
                             if self.controller_member_container.index(member) % 2 != 0],
                             fillvalue="Should join other group(s)"))
        if size == 2:
            return groups_of_two
        if size == 4:
            return [list(chain.from_iterable(group_of_four)) for group_of_four in
                    list(zip([group for group in groups_of_two if groups_of_two.index(group) % 2 == 0],
                         [group for group in groups_of_two if groups_of_two.index(group) % 2 != 0]))]
        return "No such option"
