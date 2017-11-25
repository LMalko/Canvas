from model_root import ModelRoot
from controller_task_container import *
from controller_task import *


class DAOMember():

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

    def export_data(self):
        with open(self.filename, "w", encoding="utf-8") as myfile:
            for i in self.data_for_export:
                myfile.write(i)

    def __pass_data_for_export(self):
        return self.data_for_export = ControllerMemberContainer().member_container
