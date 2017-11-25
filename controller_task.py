from model_task import*


class ControllerTask():

    def create_task_from_imported_data(self, *args):
        return ModelTask(*args)

    def get_task_data_to_export(self, task):
        return task.get_data_to_export()