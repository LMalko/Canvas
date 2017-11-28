from model_attendance_container import ModelAttendanceContainer
from model_attendance import ModelAttendance


class DAOAttendance():

    def __init__(self, filename='attendance_data.csv'):
        self.filename = filename

    def import_data(self):
        with open(self.filename, "r") as myfile:
            imported_data = myfile.read()
        print('import data')
        print(imported_data)
        return self.__extract_imported_data(imported_data.strip().split("\n"))

    def __extract_imported_data(self, imported_data):
        attendance_collection = []
        for line in imported_data:
            data = line.split('|')
            attendance = ModelAttendance(data[0])
            if len(data) > 1:
                attendance.set_new_student_presence({data[x]: float(data[x+1]) for x in range(1, len(data)-1, 2)})
            attendance_collection.append(attendance)
        return attendance_collection

    def export_data(self, attendance_collection):
        pass
        data_to_export = self.__pack_data_for_export(attendance_collection)
        with open(self.filename, "w") as myfile:
            for line in data_to_export:
                myfile.write(line)

    def __pack_data_for_export(self, attendance_collection):
        data_to_export = []
        print(attendance_collection)
        for attendance in attendance_collection:
            data = "|".join(attendance.get_data_to_export()) + '\n'
            data_to_export.append(data)
        return data_to_export
