from controller_task_container import *
from controller_task import *


class DAOTask():

    def __init__(self, filename):
        self.filename = filename
        self.ctrl_task = ControllerTask()

    def import_data(self):
        imported_data = []
        with open(self.filename, "r", encoding="utf-8") as myfile:
            for line in myfile.split("\n"):
                imported_data.append(line)

        return __extract_imported_data(imported_data)

    def __extract_imported_data(self, imported_data):
        tasks_collection = []
        for line in imported_data:
            data = line.split('|')
            tasks_collection.append(self.ctrl_task.create_task_from_imported_data(*data))
        return tasks_collection

    def export_data(self, tasks_collection):
        data_to_export = self.__pack_data_for_export(tasks_collection)
        with open(self.filename, "w", encoding="utf-8") as myfile:
            for line in data_to_export:
                myfile.write(line)

    def __pack_data_for_export(self, tasks_collection):
        data_to_export = []
        for task in tasks_collection:
            data = "|".join(self.ctrl_task.get_task_data_to_export(task)) + '\n'
            data_to_export.append(data)

        return data_to_export

