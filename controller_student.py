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
        pass

    def view_grades(self):
        pass
        # self.view.display()  # temp!!!
        # self.self.controller_task_container.change_delivery_status()  # którego zadania??
        # self.view.display()  # temp!!!

    def get_my_group(self, student):
        return student.get_my_group()

    @classmethod
    def get_controller_model_pair(cls):
        return {cls: ModelStudent}

    @classmethod
    def create_user_from_imported_data(cls, *args):
        return ModelStudent(*args)
