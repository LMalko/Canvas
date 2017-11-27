from model_task import*
from model_attendance_container import*
from view_controller_task_container import*

class ControllerTaskContainer():

    def __init__(self, container_task):
        self.container_task = container_task
        self.view_task_container = ViewControllerTaskContainer()

    def add_task_to_container(self):
        task = self.create_task()
        self.container_task.add_task(task)

    def del_task_from_container(self):
        self.container_task.del_task()  ## dokończyć

    def change_task_delivery_status(self):
        pass

    def change_task_graded_status(self):
        pass

    def change_task_grade(self):
        pass

    def rename_task(self):
        pass

    def get_max_task_id(self):
        all_tasks = self.container_task.get_all_tasks()
        all_id = []
        for task in all_tasks:
            all_id.append(int(task.get_task_id()))
        return "{:0>4}".format(max(all_id)+1)



    def __get_task(self):
        pass

    def get_taks_id(self):
        pass

    def create_task(self, name, user_id, task_id):
        pass
    
    def get_valid_input(self, user_input):
        
        invalid_input = True
        while invalid_input:
            user_input = self.view_task_container.get_user_input()
            if len(user_input.strip()) != 0:
                invalid_input = False

        return user_input


        
###
# + __get_task(task_id): ModelTask  #
# + task_display(): str
# + all_tasks_display(): list
# + certain_student_tasks_display(): list
# + certain_task_students_display(): list

# ###
# +rename_task(ModelTask):None
# +get_task_id(ModelTask):str/int
# +task_display(ModelTask):str