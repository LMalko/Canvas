class ModelTaskContainer():

    def __init__(self):
        self.task_container = []

    def add_task(self, task):
        self.task_container.append(task)

    def del_task(self, task):
        self.task_container.remove(task)

    def get_all_tasks(self):
        return self.task_container

