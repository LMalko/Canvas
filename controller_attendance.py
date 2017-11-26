from model_attendance import ModelAttendance


class ControllerAttendance():

    def create_user_attendance(self):
        return ModelAttendance()

    def set_presence_status(self, ModelAttendance, date, status):
        ModelAttendance.set_presence_status(date, status)

    def get_attendance_percentage(self, ModelAttendance):
        return ModelAttendance.count_attendance_percentage()

    def get_attendance(self, ModelAttendance):
        return ModelAttendance.get_attendance()

    def get_max_attendance(self):
        pass  # co to ma robic??
