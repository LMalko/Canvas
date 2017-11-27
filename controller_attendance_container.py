from model_attendance import ModelAttendance


class ControllerAttendanceContainer():

    def __init__(self, ControllerAttendanceContainer):
        self.attendance_container = ControllerAttendanceContainer

    def create_user_attendance(self):
        return ModelAttendance()

    def add_user(self, user_id):
        self.attendance_container.add_user(user_id, self.create_user_attendance())

    def del_user(self, user_id):
        self.attendance_container.del_user(user_id)

    def set_user_presence_status(self, user_id, actuall_date, status):
        self.attendance_container.get_user_attendance(user_id).set_presence_status(actuall_date, status)

    def get_all_students_attendance(self):
        return self.attendance_container.get_all_attendance()

    def get_user_attendance(self, user_id):
        return self.attendance_container.get_user_attendance(user_id)

    def get_user_attendance_percentage(self, user_id):
        return self.attendance_container.get_user_attendance(user_id).count_attendance_percentage()
