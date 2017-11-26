class ModelAttendanceContainer():

    def __init__(self):
        self.attendance = {}

    def add_user(self, user_id, ModelAttendance):
        self.attendance.update({user_id: ModelAttendance})

    def del_user(self, user_id):
        if user_id in self.attendance:
            del self.attendance[user_id]

    def get_user_attendance(self, user_id):
        if user_id in self.attendance:
            return self.attendance[user_id]
