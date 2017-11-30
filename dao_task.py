from model_task import *


class DAOTask():

    def __init__(self, filename='task_data.csv'):
        self.filename = filename

    def import_data(self):
        with open(self.filename, "r", encoding="utf-8") as myfile:
            imported_data = myfile.readlines()

        return self.__extract_imported_data(imported_data)

    def __extract_imported_data(self, imported_data):
        if not imported_data:
            return []

        grade_attribute_index = 3
        is_done_attribute_index = 4
        task_link_attribute = 5

        tasks_collection = []
        for line in imported_data:
            data = line.strip().split('|')
            data[grade_attribute_index] = None if data[grade_attribute_index] == 'None' else data[grade_attribute_index]
            data[is_done_attribute_index] = int(data[is_done_attribute_index])
            data[task_link_attribute] = None if data[task_link_attribute] == 'None' else data[task_link_attribute]
            tasks_collection.append(ModelTask(*data))
        return tasks_collection

    def export_data(self, tasks_collection):
        if not tasks_collection:
            return

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

