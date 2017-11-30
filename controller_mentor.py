from model_mentor import ModelMentor
from model_student import ModelStudent
from controller_task_container import ControllerTaskContainer
from controller_attendance_container import ControllerAttendanceContainer
from controller_member_container import ControllerMemberContainer
from controller_user import ControllerUser
from view_mentor import ViewMentor
from itertools import zip_longest, chain
from random import shuffle
import datetime


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
        self.controller_user = ControllerUser()

    def start(self):
        self.view.clear_screen()
        choices = ["1: View students list",
                   "2: Edit student",
                   "3: Add student",
                   "4: Remove student",
                   "5: Task menu",
                   "6: Grade today's attendance",
                   "7: Display attendance",
                   "8: Get random groups of two",
                   "9: Get random groups of four",
                   "10: Log out"]
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
                    self.get_students_list_to_display()
                elif user_input == "2":
                    self.edit_student_details()
                elif user_input == "3":
                    self.add_student()
                elif user_input == "4":
                    self.remove_student()
                elif user_input == "5":
                    self.tasks_menu()
                elif user_input == "6":
                    self.grade_attendance()
                elif user_input == "7":
                    self.get_attendance_to_display()
                elif user_input == "8":
                    self.get_random_groups()
                elif user_input == "9":
                    self.get_random_groups(4)
                elif user_input == "10":
                    to_continue = False

    def tasks_menu(self):
        choices = [
                    "1. View all tasks",
                    "2. View tasks by genre",
                    "3. View tasks by student",
                    "4. Add & deploy task",
                    "5. Delete task",
                    "6. Rename task",
                    "7. Grade task",
                    "0. Log out"]
        
        message = "\nPlease, type Your choice: "
        to_continue = True
        while to_continue:
            self.view.clear_screen()
            self.view.display_collection(choices)
            user_choice = self.view.get_user_input(message)
            if user_choice == '0':
                to_continue = False
            elif user_choice == '1':
                self.controller_task_container.get_all_tasks()
                self.view.freeze_until_key_pressed("Press any key to go back to tasks menu ")
            elif user_choice == '2':
                self.controller_task_container.get_tasks_by_genre()
                self.view.freeze_until_key_pressed("Press any key to go back to tasks menu ")
            elif user_choice == '3':
                all_students = self.controller_member_container.get_members_by_role('student')
                self.controller_member_container.get_members_display(all_students)
                student = self.controller_member_container.get_user()
                student_id = self.controller_member_container.get_member_id(student)
                student_tasks = self.controller_task_container.cherry_pick_tasks_by_user_id(student_id)
                self.controller_task_container.get_all_tasks(student_tasks)
                self.view.freeze_until_key_pressed("Press any key to go back to tasks menu ")
            elif user_choice == '4':
                target_group = self.controller_member_container.get_students_by_group()
                self.controller_task_container.create_and_deploy_task(target_group)
                self.view.freeze_until_key_pressed("Task added and deployed!\nPress any key to go back to tasks menu ")
            elif user_choice == '5':
                self.controller_task_container.del_task_from_container()
                self.view.freeze_until_key_pressed("Task deleted!\nPress any key to go back to tasks menu ")
            elif user_choice == '6':
                self.controller_task_container.rename_task()
                self.view.freeze_until_key_pressed("Task renamed!\nPress any key to go back to tasks menu ")
            elif user_choice == '7':
                self.grade_task_menu()

    def grade_task_menu(self):
        choices = [
                    "1. Choose from all tasks and students",
                    "2. Choose by student",
                    "3. Choose by task",
                    "0. Log out"]
        
        message = "\nPlease, type Your choice: "
        to_continue = True
        while to_continue:
            self.view.clear_screen()
            self.view.display_collection(choices)
            user_choice = self.view.get_user_input(message)
            if user_choice == '0':
                to_continue = False

            elif user_choice == '1':
                chosen_task = self.controller_task_container.take_and_validate_particular_task_choice()
                self.controller_task_container.grade_task(chosen_task)
                self.view.freeze_until_key_pressed("Task graded!\nPress any key to go back to tasks menu ")
            
            elif user_choice == '2':
                all_students = self.controller_member_container.get_members_by_role('student')
                self.controller_member_container.get_members_display(all_students)
                student = self.controller_member_container.get_user()
                student_id = self.controller_member_container.get_member_id(student)
                studen_tasks = self.controller_task_container.cherry_pick_tasks_by_user_id(student_id)
                chosen_task = self.controller_task_container.take_and_validate_task_choice_by_task_id(studen_tasks)
                self.controller_task_container.grade_task(chosen_task)
                self.view.freeze_until_key_pressed("Task graded!\nPress any key to go back to tasks menu ")
            
            elif user_choice == '3':
                task_id = self.controller_task_container.get_task_id_by_genre()
                tasks_of_chosen_genre = self.controller_task_container.cherry_pick_tasks_by_task_id(task_id)
                chosen_task = self.controller_task_container.take_and_validate_task_choice_by_user_id(tasks_of_chosen_genre)
                self.controller_task_container.grade_task(chosen_task)
                self.view.freeze_until_key_pressed("Task graded!\nPress any key to go back to tasks menu ")
                

    def grade_attendance(self):
        group_of_students = self.controller_member_container.get_students_by_group()
        self.__update_attendances(group_of_students)
        today = str(datetime.date.today())
        choices_to_display = [
                                '1: student is present',
                                '2: student is absent',
                                '3: student is late']
        user_choices_to_presence_value = {
                                            '1': 1.0,
                                            '2': 0.0,
                                            '3': 0.75}
        correct_choices = [str(x+1) for x in range(0, len(choices_to_display))]
        for student in group_of_students:
            self.view.clear_screen()
            self.view.display_message("\nPlease, type Your choice for student: {} {}\n".format(
                                                                                student.first_name,
                                                                                student.last_name))
            user_choice = ''
            while user_choice not in correct_choices:
                self.view.display_collection(choices_to_display)
                user_choice = self.view.get_user_input('\nType Your choice ==> ')
            print(user_choice)
            self.controller_attendance_container.set_student_presence_status_for_given_date(
                                                                student.uid,
                                                                today,
                                                                user_choices_to_presence_value[user_choice])

    def get_students_list_to_display(self):
        self.controller_member_container.get_members_display(
            self.controller_member_container.get_members_by_role("student"))
        self.view.freeze_until_key_pressed()

    def get_attendance_to_display(self):
        group_of_students = self.controller_member_container.get_students_by_group()
        self.__update_attendances(group_of_students)
        presence_values_to_words = {
                                        '1.0': 'present',
                                        '0.75': 'late',
                                        '0.0': 'absent'}
        self.view.clear_screen()
        for student in group_of_students:
            self.view.display_message('\n- student: {} {}\n\t\t\t attendance percentage: {}%'.format(
                                student.first_name,
                                student.last_name,
                                self.controller_attendance_container.get_student_attendance_percentage(student.uid)))
            attendence = self.controller_attendance_container.get_presences_for_given_student(student.uid)
            for presence in attendence:
                presence_value = str(attendence[presence])
                self.view.display_message('\t\t\t in day: {} student was {}'.format(
                                                presence, presence_values_to_words[presence_value]))
        self.view.freeze_until_key_pressed()

    def __update_attendances(self, students):
        '''Check if all students in collection have own attendances, if not, add attendance for student.'''
        attendances = self.controller_attendance_container.get_all_students_attendance()
        students_uid = [student.uid for student in students]
        attendances_uid = [attendance.student_uid for attendance in attendances]
        for uid in students_uid:
            if uid not in attendances_uid:
                self.controller_attendance_container.create_student_attendance_and_add_to_container(uid)

    def get_members_display(self, members):
        for person in members:
            self.view.display_message(self.controller_user.get_member_display(person))

    def create_mentor(self, first_name, last_name, password, my_group):
        uid = self.controller_member_container.get_new_ID()
        return ModelMentor(uid, first_name, last_name, password, my_group)

    def create_student(self, first_name, last_name, password, my_group):
        uid = self.controller_member_container.get_new_ID()
        return ModelStudent(uid, first_name, last_name, password, my_group)

    def edit_student_details(self):
        students = self.controller_member_container.get_members_by_role('student')
        if not students:
            self.view.freeze_until_key_pressed("There is no one to edit. Press any key.. ")
        else:
            if len(students) == 1:
                student_to_change = students[0]
            else:
                self.view.clear_screen()
                self.view.display_message("\n\nCongratulations, You have privilages to change student's details.\n")
                student_to_change_is_chosen = False
                while not student_to_change_is_chosen:
                    self.get_members_display(students)
                    student_to_change = self.controller_member_container.get_user()
                    if student_to_change in [
                            user for user in self.controller_member_container.get_members_by_role('student')]:
                        student_to_change_is_chosen = True
                        break
                    self.view.display_message("\n\nThis user is not a student!\n")
            student_detail_to_change_is_chosen = False
            while not student_detail_to_change_is_chosen:
                self.view.clear_screen()
                self.view.display_message("\n\nLet's change data of {}:".format(student_to_change.get_member_fullname()))
                student_detail_to_change = self.view.get_user_input(
                                "\n\nChange: first name (1) last name (2) or password (3)? ")
                if student_detail_to_change == "1":
                    return self.controller_user.change_first_name(student_to_change)
                elif student_detail_to_change == "2":
                    return self.controller_user.change_last_name(student_to_change)
                elif student_detail_to_change == "3":
                    return self.controller_user.change_password(student_to_change)
                self.view.display_message("\n\nRead instructions properly and try again.\n\n")

    def add_student(self):
        self.view.display_message("\n\nLet's recruit student..\n\n")
        user_inputs = []
        messages = ["Enter first name: ", "Enter last name: ", "Specify password: ", "Specify group: "]
        for statement in messages:
            user_input = self.validate_input(statement)
            user_inputs.append(user_input)
        user = self.create_student(user_inputs[0],
                                   user_inputs[1],
                                   user_inputs[2],
                                   user_inputs[3])
        self.view.display_message("\n\nStudent recruited..\n\n")
        self.controller_member_container.add_member(user)
        self.view.get_user_input("\nPress <enter> to continue.. ")

    def remove_student(self):
        students = self.controller_member_container.get_members_by_role("student")
        if not students:
            self.view.freeze_until_key_pressed("There is no one to release. Press any key.. ")
        else:
            self.view.display_message("\n\nLet's get rid of student! It's always fun!! :D\n\n")
            self.controller_member_container.get_members_display(students)
            if len(students) == 1:
                student_to_release = students[0]
            else:
                student_to_release = self.controller_member_container.get_user('student')
            self.controller_member_container.delete_member(student_to_release)
            self.view.freeze_until_key_pressed("Done! Press anything to continue. ")

    def get_random_groups(self, size=2):
        self.view.display_nested_collection(self.get_random_student_group(size))
        self.view.freeze_until_key_pressed("Groups selected")

    def get_random_student_group(self, size=2):
        students = [x for x in self.controller_member_container.get_all_members() if x.role == 'student']
        if students:
            shuffle(students)
            groups_of_two = list(zip_longest(["{} {} {}".format(member.uid, member.first_name, member.last_name)
                                 for member in students
                                 if students.index(member) % 2 == 0],
                                 ["{} {} {}".format(member.uid, member.first_name, member.last_name)
                                 for member in students
                                 if students.index(member) % 2 != 0],
                                 fillvalue="Should join other group"))
            if size == 2:
                return groups_of_two
            if size == 4:
                return [list(chain.from_iterable(group_of_four)) for group_of_four in
                        list(zip_longest([group for group in groups_of_two if groups_of_two.index(group) % 2 == 0],
                                         [group for group in groups_of_two if groups_of_two.index(group) % 2 != 0],
                                         fillvalue=["Should join other groups"]))]
        return "No such option"

    def tasks_menu(self):
            choices = [
                        '1. View all tasks',
                        '2. View tasks by genre'
                        '3. View tasks by student',
                        '4. Add & deploy task',
                        '5. Del task',
                        '6. Rename task',
                        '7. Grade task',
                        '0. Exit']
            message = "\nPlease, type Your choice: "
            to_continue = True
            while to_continue:
                self.view.clear_screen()
                self.view.display_collection(choices)
                user_choice = self.view.get_user_input(message)
                if user_choice == '0':
                    to_continue = False
                elif user_choice == '1':
                    self.controller_task_container.get_all_tasks()
                    self.view.freeze_until_key_pressed("Press any key to go back to tasks menu ")
                elif user_choice == '2':
                    self.controller_task_container.get_tasks_by_genre()
                    self.view.freeze_until_key_pressed("Press any key to go back to tasks menu ")
                elif user_choice == '3':
                    all_students = self.controller_member_container.get_members_by_role('student')
                    self.controller_member_container.get_members_display(all_students)
                    student = self.controller_member_container.get_user()
                    student_id = self.controller_member_container.get_member_id(student)
                    self.controller_task_container.get_student_tasks(student_id)
                    self.view.freeze_until_key_pressed("Press any key to go back to tasks menu ")
                elif user_choice == '4':
                    target_group = self.controller_member_container.get_students_by_group()
                    self.controller_task_container.create_and_deploy_task(target_group)
                    self.view.freeze_until_key_pressed("Task added and deployed!\nPress any key to go back to tasks menu ")
                elif user_choice == '5':
                    self.controller_task_container.del_task_from_container()
                    self.view.freeze_until_key_pressed("Task deleted!\nPress any key to go back to tasks menu ")
                elif user_choice == '6':
                    self.controller_task_container.rename_task()
                    self.view.freeze_until_key_pressed("Task renamed!\nPress any key to go back to tasks menu ")
                elif user_choice == '7':
                    self.controller_task_container.grade_task()
                    self.view.freeze_until_key_pressed("Task graded!\nPress any key to go back to tasks menu ")
