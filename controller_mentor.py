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
        self.view.clear_screen()
        choices = ["1: View student list",
                   "2: Edit student",
                   "3: Add student",
                   "4: View task list"
                   "5: Grade task",
                   "6: Add task",
                   "7: Edit task",
                   "8: Check attendance",
                   "9: Get random groups of two",
                   "10: Get random groups of four",
                   "11: Log out"]
        correct_choices = [str(x+1) for x in range(1, len(choices))]
        message = "\nPlease, type Your choice: "
        to_continue = True
        while to_continue:
            user_input = ''
            while user_input not in correct_choices:
                self.view.clear_screen()
                self.view.display_collection(choices)
                user_input = self.view.get_user_input(message)
                if user_input == "1":
                    self.get_members_display(ControllerMemberContainer.get_members_by_role('student'))
                elif user_input == "2":

                elif user_input == "3":

                elif user_input == "4":

                elif user_input == "5":

                elif user_input == "6":

                elif user_input == "7":

                elif user_input == "8":

                elif user_input == "9":
                    self.view.display_collection(self.get_random_student_group())  
                elif user_input == "10":
                    self.view.display_collection(self.get_random_student_group(4)) 
                elif user_input == "11":
                    to_continue = False

    def create_mentor(self, first_name, last_name, password, my_group):
        '''Return ModelMentor object.'''
        uid = self.controller_member_container.get_new_ID()
        return ModelMentor(uid, first_name, last_name, password, my_group)

    def view_grades(self):
        pass
        # self.view.display()  # temp!!!
        # self.self.controller_task_container.change_delivery_status()  # którego zadania??
        # self.view.display()  # temp!!!

    def get_members_display(self, members):
        for person in members:
            self.view.display_message(self.controller_user.get_member_display(person))

    def grade_task(self):
        pass

    def add_student(self):
        pass

    def check_attendance(self):
        pass

    def remove_student(self):
        self.view.display_message("\n\nLet's get rid of student! It's always fun !! :D\n\n")
        self.get_members_display(self.controller_member_container.get_members_by_role('student'))
        student_to_release = self.controller_user.get_user()
        self.controller_member_container.remove(student_to_release)
        self.view.display_message("\n\nDone !!!\n\n")

    @classmethod
    def get_controller_model_pair(cls):
        return {cls: ModelMentor}

    @classmethod
    def create_user_from_imported_data(cls, *args):
        return ModelMentor(*args)

    def get_random_student_group(self, size=2):
        students = [x for x in self.controller_member_container if x.role == 'student']
        shuffle(students)
        groups_of_two = list(zip_longest([member.name for member in students
                             if students.index(member) % 2 == 0],
                             [member.name for member in students
                             if students.index(member) % 2 != 0],
                             fillvalue="Should join other group(s)"))
        if size == 2:
            return groups_of_two
        if size == 4:
            return [list(chain.from_iterable(group_of_four)) for group_of_four in
                    list(zip([group for group in groups_of_two if groups_of_two.index(group) % 2 == 0],
                         [group for group in groups_of_two if groups_of_two.index(group) % 2 != 0]))]
        return "No such option"
