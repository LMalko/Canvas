class ModelAttendanceContainer():

    def __init__(self):
        self.attendance = []

    def add_student_attendance(self, ModelAttendance):
        self.attendance.append(ModelAttendance)

    def del_student_attendance(self, ModelAttendance):
        self.attendance.remove(ModelAttendance)

    def get_student_attendance(self, student_id):
        '''Return model attendance.'''
        return [attendance for attendance in self.attendance if attendance.student_uid == student_id][0]

    def get_all_attendance(self):
        return self.attendance
