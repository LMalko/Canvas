from model_attendance import ModelAttendance


class ControllerAttendanceContainer():

    def __init__(self, ModelAttendanceContainer):
        self.attendance_container = ModelAttendanceContainer

    def create_student_attendance(self, student_uid):
        return ModelAttendance(student_uid)

    def set_new_attendance(self, new_collection):
        self.attendance_container.set_new_attendance(new_collection)

    def add_student_attendance(self, ModelAttendance):
        self.attendance_container.add_student_attendance(ModelAttendance)

    def create_student_attendance_and_add_to_container(self, student_uid):
        self.attendance_container.add_student_attendance(
                                        self.create_student_attendance(student_uid))

    def del_student_attendance(self, ModelAttendance):
        self.attendance_container.del_student_attendance(ModelAttendance)

    def set_student_presence_status_for_given_date(self, student_uid, given_date, status):
        self.attendance_container.get_student_attendance(student_uid).set_presence_status(given_date, status)

    def get_all_students_attendance(self):
        return self.attendance_container.get_all_attendance()

    def get_student_attendance(self, student_uid):
        '''Return model attendance.'''
        return self.attendance_container.get_student_attendance(student_uid)

    def get_student_attendance_percentage(self, student_uid):
        return self.attendance_container.get_student_attendance(student_uid).count_attendance_percentage()

    def get_presences_for_given_student(self, student_uid):
        '''Return dict with presences.'''
        __model = self.get_student_attendance(student_uid)
        if __model:
            return self.get_student_attendance(student_uid).get_student_presence()
