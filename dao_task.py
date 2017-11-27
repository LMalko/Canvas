from model_task import *


class DAOTask():

    def __init__(self, filename='task_data.csv'):
        self.filename = filename

    def import_data(self):
        with open(self.filename, "r", encoding="utf-8") as myfile:
            imported_data = myfile.read()

        return self.__extract_imported_data(imported_data.strip().split("\n"))

    def __extract_imported_data(self, imported_data):
        tasks_collection = []
        for line in imported_data:
            data = line.split('|')
            tasks_collection.append(ModelTask(*data))
        return tasks_collection

    def export_data(self, tasks_collection):
        data_to_export = self.__pack_data_for_export(tasks_collection)
        with open(self.filename, "w", encoding="utf-8") as myfile:
            for line in data_to_export:
                myfile.write(line)

    def __pack_data_for_export(self, tasks_collection):
        data_to_export = []
        for task in tasks_collection:
            data = "|".join(task.get_data_to_export()) + '\n'
            data_to_export.append(data)

        return data_to_export

