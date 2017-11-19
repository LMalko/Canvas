from model_root import ModelRoot
from controller_admin import *
from controller_mentor import *
from controller_office import *
from controller_student import *
from controller_member_container import *
'''
Model danych:
role|uid|first_name|last|name|password|my_group
'''

class DAOMember():

    def __init__(self, filename):
        self.filename = filename
        self.role_class_pairs = {}
        self.role_class_pairs.update(ControllerAdmin.get_role_class_pair())
        self.role_class_pairs.update(ControllerMentor.get_role_class_pair())
        self.role_class_pairs.update(ControllerStudent.get_role_class_pair())
        self.role_class_pairs.update(ControllerOffice.get_role_class_pair())

    def import_data(self):
        with open(self.filename, "r", encoding="utf-8") as myfile:
            file_content = myfile.readlines()
        return self.__extract_imported_data(file_content)

    def __extract_imported_data(self, file_content):
        imported_data = []
        for line in file_content:
            user_role, *args = line.split('|')
            imported_data.append(self.role_class_pairs[user_role](*args))
        
        return imported_data

    def export_data(self):
        with open(self.filename, "w", encoding="utf-8") as myfile:
            for i in self.data_for_export:
                myfile.write(i)

    def __pass_data_for_export(self):
        return self.data_for_export = ControllerMemberContainer().member_container
