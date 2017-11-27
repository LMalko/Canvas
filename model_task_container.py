class ModelTaskContainer():

    def __init__(self):
        self.task_container = []

    def add_task(self, task):
        self.task_container.append(task)

    def del_task(self, task):
        self.task_container.remove(task)

    def get_task(self, task_id):
        pass

    def get_max_id(self):
        pass

