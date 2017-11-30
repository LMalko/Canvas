from model_admin import ModelAdmin
from model_mentor import ModelMentor
from model_office import ModelOffice
from model_student import ModelStudent


class DAOMember():

    def __init__(self, filename='member_data.csv'):
        self.filename = filename

    def import_data(self):
        with open(self.filename, "r", encoding="utf-8") as myfile:
            file_content = myfile.readlines()
        return self.__extract_imported_data(file_content)

    def __extract_imported_data(self, file_content):
        if not file_content:
            return []

        imported_data = []
        for line in file_content:
            user_role, *args = line.strip().split('|')
            if user_role == ModelAdmin.get_role_attribute():
                imported_data.append(ModelAdmin(*args))
            elif user_role == ModelMentor.get_role_attribute():
                imported_data.append(ModelMentor(*args))
            elif user_role == ModelOffice.get_role_attribute():
                imported_data.append(ModelOffice(*args))
            elif user_role == ModelStudent.get_role_attribute():
                imported_data.append(ModelStudent(*args))

        return imported_data

    def export_data(self, users_collection):
        if users_collection:
            data_to_export = self.__pack_data_for_export(users_collection)
            with open(self.filename, "w", encoding="utf-8") as myfile:
                for i in data_to_export:
                    myfile.write(i)

    def __pack_data_for_export(self, users_collection):
        data_to_export = []
        for user in users_collection:
            user_data = user.get_data_for_export()
            data_to_export.append("|".join(user_data) + '\n')

        return data_to_export
