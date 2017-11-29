from model_student import ModelStudent
from controller_task_container import ControllerTaskContainer
from view_student import ViewStudent
from controller_user import*


class ControllerStudent(ControllerUser):

    def __init__(self, user, task_container):
        self.associated_user = user
        self.controller_task_container = ControllerTaskContainer(task_container)
        self.controller_user = ControllerUser()
        self.view = ViewStudent()

    def start(self):
        self.view.clear_screen()
        choices = ["1: Submit task", "2: View Your grades", "3: Log out"]
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
                    self.submit_task()
                elif user_input == "2":
                    self.view_grades()
                elif user_input == "3":
                    to_continue = False

    def submit_task(self):
        self.controller_task_container.change_task_delivery_status( \
            self.controller_user.get_member_id(self.associated_user))

    def view_grades(self):
        self.controller_task_container.get_student_tasks( \
            self.controller_user.get_member_id(self.associated_user))

    def get_my_group(self, student):
        return student.get_my_group()
