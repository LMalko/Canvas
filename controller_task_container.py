from model_task import*
from model_attendance_container import*

class ControllerTaskContainer():

    def __init__(self, container_task):
        self.container_task = container_task

    def add_task_to_container(self, task):
        self.container_task.add_task()

    def del_task_from_container(self):
        pass

    def change_task_delivery_status(self):
        pass

    def change_task_graded_status(self):
        pass

    def change_task_grade(self):
        pass

    def rename_task(self):
        pass

    def get_max_task_id(self):
        pass

    def __get_task(self):
        pass

    def get_taks_id(self):
        pass

    def create_task(self, name, user_id, task_id):
        pass
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