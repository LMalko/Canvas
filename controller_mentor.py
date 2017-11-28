from model_mentor import ModelMentor
from controller_task_container import ControllerTaskContainer
from controller_attendance_container import ControllerAttendanceContainer
from controller_member_container import ControllerMemberContainer
from view_mentor import ViewMentor
from controller_user import*
from itertools import zip_longest, chain
from random import shuffle


class ControllerMentor(ControllerUser):

    def __init__(self,
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
                   "4: Remove student",
                   "5: View task list"
                   "6: Grade task",
                   "7: Add task",
                   "8: Edit task",
                   "9: Check attendance",
                   "10: Get random groups of two",
                   "11: Get random groups of four",
                   "12: Log out"]
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
                    self.edit_student_details()
                elif user_input == "3":
                    self.add_student()
                elif user_input == "4":
                    self.remove_student()
                elif user_input == "5":

                elif user_input == "6":

                elif user_input == "7":

                elif user_input == "8":
                    
                elif user_input == "9":

                elif user_input == "10":
                    self.view.display_collection(self.get_random_student_group())  
                elif user_input == "11":
                    self.view.display_collection(self.get_random_student_group(4)) 
                elif user_input == "12":
                    to_continue = False

    def create_mentor(self, first_name, last_name, password, my_group):
        uid = self.controller_member_container.get_new_ID()
        return ModelMentor(uid, first_name, last_name, password, my_group)

    def edit_student_details():
        self.view.display_message("\n\nCongratulations, You have privilages to change student's details.\n")
        while True:
            self.get_members_display(self.controller_member_container.get_members_by_role('student'))
            student_to_change = self.controller_user.get_user()
            if student_to_change in [user for user in self.controller_member_container.get_members_by_role('student')]:
                break
            self.view.display_message("\n\nThis user is not a student!\n")
        while True:
            student_detail_to_change = self.view.get_user_input("Change: first name (1) last name (2) or password (3) ?")
            if student_detail_to_change == "1":
                return self.controller_user.change_first_name(self.controller_user.get_member_id(student_to_change))
            elif student_detail_to_change == "2":
                return self.controller_user.change_last_name(self.controller_user.get_member_id(student_to_change))
            elif student_detail_to_change == "3":
                return self.controller_user.change_password(self.controller_user.get_member_id(student_to_change))
            self.view.display_message("\n\n\nRead instructions properly and try again.\n\n\n")
        continue

    def view_grades(self):
        ###################################################DO ZROBIEBNIA

    def get_members_display(self, members):
        for person in members:
            self.view.display_message(self.controller_user.get_member_display(person))

    def grade_task(self):
        ###################################################DO ZROBIEBNIA

    def add_student(self):
        self.view.display_message("\n\nLet's recruit student..\n\n")
        user_inputs = []
        messages = ["Enter first name: ", "Enter last name: ", "Specify password: ", "Specify group: "]
        for statement in messages:
            user_input = self.validate_input(statement)
            user_inputs.append(user_input)
        user = self.controller_mentor.create_student(user_inputs[0],
                                                     user_inputs[1],
                                                     user_inputs[2],
                                                     user_inputs[3])
        self.view.display_message("\n\nStudent recruited..\n\n")
        self.controller_member_container.add_member(user)
        self.view.get_user_input("\nPress <enter> to continue.. ")

    def check_attendance(self):
        pass
        ###################################################DO ZROBIEBNIA

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
