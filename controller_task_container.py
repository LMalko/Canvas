from model_task import*
from model_attendance_container import*
from view_controller_task_container import*
from controller_user import*


class ControllerTaskContainer():

    def __init__(self, container_task):
        self.container_task = container_task
        self.view_task_container = ViewControllerTaskContainer()
        self.ctrl_user = ControllerUser()

    def is_collection_empty(self, collection):
        if not collection:
            self.view_task_container.display_message("Task list is empty. Nothing to display.")
            return True
        else:
            return False

    def add_task_to_container(self, task):
        self.container_task.add_task(task)

    def del_task_from_container(self):
        all_tasks = self.container_task.get_all_tasks()
        if self.is_collection_empty(all_tasks):
            return
        task_id = self.get_task_id_by_genre()

        for index in range(len(all_tasks)-1, -1, -1):
            if all_tasks[index].get_task_id() == task_id:
                self.container_task.del_task(all_tasks[index])

    def get_student_tasks(self, student_id):
        all_tasks = self.container_task.get_all_tasks()
        if self.is_collection_empty(all_tasks):
            return
        all_users_tasks = self.cherry_pick_tasks_by_user_id(all_tasks, student_id)
        if self.is_collection_empty(all_users_tasks):
            return

        for task in all_users_tasks:
            self.view_task_container.display_message(task.get_student_task_display())

    def get_tasks_by_genre(self):
        all_tasks = self.container_task.get_all_tasks()
        if self.is_collection_empty(all_tasks):
            return
        chosen_task_id = self.get_task_id_by_genre()

        for task in all_tasks:
            if task.get_task_id() == chosen_task_id:
                self.view_task_container.display_message(task.get_mentor_task_display())

    def get_all_tasks(self):
        all_tasks = self.container_task.get_all_tasks()
        if self.is_collection_empty(all_tasks):
            return
        for task in all_tasks:
            self.view_task_container.display_message(task.get_mentor_task_display())

    def change_task_delivery_status(self, student_id=None):
        if student_id:
            all_tasks = self.container_task.get_all_tasks()
            if self.is_collection_empty(all_tasks):
                return
            all_student_tasks = self.cherry_pick_tasks_by_user_id(all_tasks, student_id)
            if self.is_collection_empty(all_student_tasks):
                return
            task = self.take_and_validate_task_choice(all_student_tasks)
            task.change_delivery_status()
        else:
            task = self.take_and_validate_particular_task_choice()
            if self.is_collection_empty(task):
                return
            task.change_delivery_status()

    def grade_task(self):
        task = self.take_and_validate_particular_task_choice()
        if self.is_collection_empty(task):
            return
        if not task.get_delivery_status():
            self.view_task_container.display_message("Task has not been submitted. Grading aborted")
            return False
        possible_grades = ['-3', '0', '4', '7', '10', '12']

        invalid_input = True
        while invalid_input:
            self.view_task_container.display_message("{}:\n {}".format('Possible choices', ",".join(possible_grades)))
            grade = self.get_valid_input("Pass tasks grade: ")
            if grade in possible_grades:
                task.mark_as_graded()
                task.set_grade(grade)
                invalid_input = False
                return True
            else:
                self.view_task_container.display_message('\nChoice not in possible choices')

    def rename_task(self):
        chosen_task_id = self.get_task_id_by_genre()
        new_task_name = self.get_valid_input("Pass new task name: ")

        all_tasks = self.container_task.get_all_tasks()
        for task in all_tasks:
            if task.get_task_id() == chosen_task_id:
                task.rename_task(new_task_name)

    def create_and_deploy_task(self, target_group):
        task_id = self.get_max_task_id()
        task_name = self.get_valid_input("Pass tasks name: ")
        target_group = target_group

        for student in target_group:
            student_id = self.ctrl_user.get_member_id(student) # Pobrać liste id zamiast listy obiektów, bo to jedyne odwolanie do CtrlUser
            self.add_task_to_container(ModelTask(task_name, task_id, student_id))

    def get_valid_input(self, message):
        invalid_input = True
        while invalid_input:
            user_input = self.view_task_container.get_user_input(message)
            if len(user_input.strip()) != 0:
                invalid_input = False

        return user_input

    def get_max_task_id(self):
        all_tasks = self.container_task.get_all_tasks()
        if self.is_collection_empty(all_tasks):
                return "0000"
        all_id = []
        for task in all_tasks:
            all_id.append(int(task.get_task_id()))
        return "{:0>4}".format(max(all_id)+1)

    def get_task_id_by_genre(self):
        all_tasks = self.container_task.get_all_tasks()
        if self.is_collection_empty(all_tasks):
            return

        tasks_by_id = []
        for task in all_tasks:
            tasks_by_id.append(task.get_short_task_display())

        invalid_choice = True
        while invalid_choice:
            self.view_task_container.display_collection(sorted(list(set(tasks_by_id))))
            user_choice = self.get_valid_input("Choose task by id: ")
            for task in all_tasks:
                if task.get_task_id() == user_choice:
                    invalid_choice = False
                    break

        return user_choice

    def take_and_validate_task_choice(self, all_tasks):

        invalid_choice = True
        chosen_task = None
        while invalid_choice:
            for task in all_tasks:
                self.view_task_container.display_message(task.get_student_task_display())
            user_choice = self.get_valid_input("Choose task by id: ")
            for task in all_tasks:
                if task.get_task_id() == user_choice:
                    chosen_task = task
                    invalid_choice = False
                    break
        return chosen_task

    def take_and_validate_particular_task_choice(self):
        all_tasks = self.container_task.get_all_tasks()
        if self.is_collection_empty(all_tasks):
            return

        chosen_task = None
        invalid_choice = True
        while invalid_choice:
            for task in all_tasks:
                self.view_task_container.display_message(task.get_mentor_task_display())

            task_id_choice = self.view_task_container.get_user_input("Choose task by task id: ")
            user_id_choice = self.view_task_container.get_user_input("Choose task by user id: ")
            for task in all_tasks:
                if (task.get_task_id() == task_id_choice) & (task.get_user_id() == user_id_choice):
                    chosen_task = task
                    invalid_choice = False
                    break
        return chosen_task

    def cherry_pick_tasks_by_user_id(self, task_collection, user_id):
        user_tasks = []
        for task in task_collection:
            if task.get_user_id() == user_id:
                user_tasks.append(task)

        return user_tasks

# from dao_task import *
# from model_task_container import*
# from dao_member import*
# from model_member_container import*
# from controller_member_container import*

# dao_task = DAOTask()
# dao_members = DAOMember()
# mtc = ModelTaskContainer()
# mtc.task_container = dao_task.import_data()
# mmc = ModelMemberContainer()
# mmc.members = dao_members.import_data()
# ctrl_mc = ControllerMemberContainer(mmc)
# ctrl_task_cont = ControllerTaskContainer(mmc, mtc)

# # target_group = ctrl_mc.get_students_by_group() # póki nie działa
# # ctrl_task_cont.create_and_deploy_task(target_group)

# # student = ctrl_mc.get_member('0014')
# # ctrl_task_cont.get_student_tasks('0014')

# ctrl_task_cont.get_tasks_by_genre()
# print('\n\n')
# ctrl_task_cont.get_student_tasks('0014')
# print('\n\n')
# ctrl_task_cont.get_all_tasks()

# dao_task.export_data(ctrl_task_cont.container_task.get_all_tasks())

# # print('\n')
# # all_tasks = ctrl_task_cont.container_task.get_all_tasks()
# # for task in all_tasks:
# #     print("{}".format(task.get_mentor_task_display()))
# # print('\n')
