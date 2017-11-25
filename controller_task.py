from model_task import*


class ControllerTask():

    def create_task_from_imported_data(self, *args):
        return ModelTask(*args)

    def get_user_data_to_export(self, task):
        return task.get_user_data_to_export()