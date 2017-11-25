from model_root import ModelRoot
from controller_admin import *
from controller_mentor import *
from controller_office import *
from controller_student import *
from controller_member_container import *
'''
Model danych:
role|uid|first_name|last_name|password|my_group
'''

class DAOMember():
    '''
        controller_model_pairs dict contains:
                keys - Controller (class)
                values - ModelUser (class)
    '''
    def __init__(self, filename):
        self.filename = filename
        self.controller_model_pairs = {}
        self.controller_model_pairs.update(ControllerAdmin.get_controller_model_pair())
        self.controller_model_pairs.update(ControllerMentor.get_controller_model_pair())
        self.controller_model_pairs.update(ControllerStudent.get_controller_model_pair())
        self.controller_model_pairs.update(ControllerOffice.get_controller_model_pair())

    def import_data(self):
        with open(self.filename, "r", encoding="utf-8") as myfile:
            file_content = myfile.readlines()
        return self.__extract_imported_data(file_content)

    def __extract_imported_data(self, file_content):
        imported_data = []
        for line in file_content:
            user_role, *args = line.strip().split('|')
            print("{:>10}:{}".format(user_role, args))
            for ctrl in self.controller_model_pairs:
                if ctrl.get_user_role(self.controller_model_pairs[ctrl]) == user_role:
                    imported_data.append(ctrl.create_user_from_imported_data(*args))
                    break
        
        return imported_data

    def export_data(self, users_collection):
        data_to_export = self.__pack_data_for_export(users_collection)
        with open(self.filename, "w", encoding="utf-8") as myfile:
            for i in data_to_export:
                myfile.write(i)

    def __pack_data_for_export(self, users_collection):
        data_to_export = []
        for user in users_collection:
            for ctrl in self.controller_model_pairs:
                if isinstance(user, self.controller_model_pairs[ctrl]):
                    user_data = ctrl.get_user_data_to_export(user)
                    data_to_export.append("|".join(user_data) + '\n')
                    break
        return data_to_export

