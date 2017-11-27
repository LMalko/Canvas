from model_task import*
from model_attendance_container import*
from view_controller_task_container import*
from controller_student import *

class ControllerTaskContainer():

    def __init__(self, container_member, container_task):
        self.container_task = container_task
        self.view_task_container = ViewControllerTaskContainer()
        self.ctrl_student = ControllerStudent()

    def add_task_to_container(self, task):
        self.container_task.add_task(task)

    def del_task_from_container(self):
        self.container_task.del_task()  ## dokończyć

    def change_task_delivery_status(self):
        pass

    def grade_task(self):
        pass

    def change_task_grade(self):
        all_tasks = self.container_task.get_all_tasks()
        for count, task in enumerate(all_tasks, 1):
            self.view_task_container.display_message("{}. {}".format(coune, task.task_display()))
        self.view_task_container.display_message("Choose Task by it's number: ")

        invalid_input = True
        while invalid_input
############################
            if (len(chosen_task_name) == 1) & (chosen_task_name.isdigit()) & (int(chosen_task_name) in range(1, len(set(tasks_names)+1))):
                invalid_input = False

        
        invalid_input = True
        while invalid_input:


    def rename_task(self):
        # get by task id, nie po numerze, bo mniej sprawdzania
        tasks_names = []
        for task in self.container_task():
            tasks_names.append(task.get_task_name())

        # self.view_task_container.display_message("Choose number of task to change:")
        for count, name in enumerate({set(tasks_names)}, 1):
            self.view_task_container.display_message("\t{}. {}".format(count, name))
        invalid_input = True
        while invalid_input:
            chosen_task_name = self.get_valid_input("Choose number of task to change: ")
            if (len(chosen_task_name) == 1) & (chosen_task_name.isdigit()) & (int(chosen_task_name) in range(1, len(set(tasks_names)+1))):
                invalid_input = False
        new_task_name = self.get_valid_input("Pass new task name: ")
        for task in self.container_task:
            if task.get_task_name() == chosen_task_name:
                task.rename_task(new_task_name)
        self.view_task_container.display_message("Task {} renamed to {}".format(chosen_task_name, new_task_name))
##################################
        chosen_task_id = self.take_and_validate_task_id_choice()
        new_task_name = self.get_valid_input()



    def __get_task(self):
        pass

    def get_taks_id(self):
        pass

    def create_and_deploy_task(self):
        task_id = self.get_max_task_id
        task_name = self.get_valid_input()
        target_group = self.get_target_group_for_task_deployment()  #zt listę obiektów studentów DOKOŃCZYĆ!!!
        
        for student in target_group:
            student_id = self.ctrl_student.get_member_id(student)
            self.add_task_to_container(ModelTask(task_name, task_id, student_id))

    def get_target_group_for_task_deployment(self):
        #### z members container gest students group, wybieranie grupy już tam, zt listę obiektów studentów danej grupy
        pass
    
    def get_valid_input(self, message):
        invalid_input = True
        while invalid_input:
            user_input = self.view_task_container.get_user_input(message)
            if len(user_input.strip()) != 0:
                invalid_input = False

        return user_input

    def get_max_task_id(self):
        all_tasks = self.container_task.get_all_tasks()
        all_id = []
        for task in all_tasks:
            all_id.append(int(task.get_task_id()))
        return "{:0>4}".format(max(all_id)+1)

    def get_task_by_id(self):
        all_tasks = self.container_task.get_all_tasks()
        tasks_by_id = []
        
        for task in all_tasks:
            tasks_by_id.append(task.get_task_by_id())

        return sorted(list(set(tasks_by_id)))

    def take_and_validate_task_id_choice(self):
        all_tasks = self.container_task.get_all_tasks()

        invalid_choice = True
        while invalid_choice:
            self.view_task_container.display_collection(self.get_task_by_id)
            user_choice = self.view_task_container.get_user_input("Choose task by id: ")
            for task in all_tasks:
                if task.get_task_id() == user_choice:
                    invalid_choice = False
                    break
        return user_choice  ##task id          



