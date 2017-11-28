from model_attendance_container import ModelAttendanceContainer
from controller_attendance_container import ControllerAttendanceContainer


class DAOAttendance():

    def __init__(self, filename='attendance_data.csv'):
        self.filename = filename

    def import_data(self):
        with open(self.filename, "r", encoding="utf-8") as myfile:
            imported_data = myfile.read()
        print('import data')
        print(imported_data)
        # return self.__extract_imported_data(imported_data.strip().split("\n"))

    def __extract_imported_data(self, imported_data):
        pass
        # tasks_collection = []
        # for line in imported_data:
        #     data = line.split('|')
        #     tasks_collection.append(ModelTask(*data))
        # return tasks_collection

    def export_data(self, tasks_collection):
        pass
        # data_to_export = self.__pack_data_for_export(tasks_collection)
        # with open(self.filename, "w", encoding="utf-8") as myfile:
        #     for line in data_to_export:
        #         myfile.write(line)

    def __pack_data_for_export(self, tasks_collection):
        pass
        # data_to_export = []
        # for task in tasks_collection:
        #     data = "|".join(task.get_data_to_export()) + '\n'
        #     data_to_export.append(data)
        #
        # return data_to_export


#
# class DAOMember():
#
#     def __init__(self, filename):
#         self.filename = filename
#
#     def import_data(self):
#         return __extract_imported_data()
#
#     def __extract_imported_data(self):
#         self.imported_data = []
#         with open(self.filename, "r", encoding="utf-8") as myfile:
#             for item in myfile.split("\n"):
#                 self.imported_data.append(line)
#         return self.imported_data
#
#     def export_data(self):
#         with open(self.filename, "w", encoding="utf-8") as myfile:
#             for i in self.data_for_export:
#                 myfile.write(i)
#
#     def __pass_data_for_export(self):
#         return self.data_for_export = ControllerMemberContainer().member_container
