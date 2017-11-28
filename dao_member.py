from model_admin import*
from model_mentor import*
from model_office import*
from model_student import*
from controller_user import*


class DAOMember():

    def __init__(self, filename='data.csv'):
        self.filename = filename
        self.ctrl_user = ControllerUser()

    def import_data(self):
        with open(self.filename, "r", encoding="utf-8") as myfile:
            file_content = myfile.readlines()
        return self.__extract_imported_data(file_content)

    def __extract_imported_data(self, file_content):
        imported_data = []
        for line in file_content:
            user_role, *args = line.strip().split('|')
            if user_role == 'admin':
                imported_data.append(ModelAdmin(*args))
            elif user_role == 'mentor':
                imported_data.append(ModelMentor(*args))
            elif user_role == 'office':
                imported_data.append(ModelOffice(*args))
            elif user_role == 'student':
                imported_data.append(ModelStudent(*args))
        
        return imported_data

    def export_data(self, users_collection):
        data_to_export = self.__pack_data_for_export(users_collection)
        with open(self.filename, "w", encoding="utf-8") as myfile:
            for i in data_to_export:
                myfile.write(i)

    def __pack_data_for_export(self, users_collection):
        data_to_export = []
        for user in users_collection:
            user_data = self.ctrl_user.get_user_data_to_export(user)
            data_to_export.append("|".join(user_data) + '\n')

        return data_to_export

# tt = DAOMember()
# data = tt.import_data()
# print(data)
# data.append(ModelStudent('0014', 'Super', 'Student', 'piwo', 'A'))
# tt.export_data(data)