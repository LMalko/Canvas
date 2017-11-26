class ModelAttendance():

    def __init__(self):
        self.user_presence = {}

    def set_presence_status(self, actuall_date, status):
        self.user_presence.update({actuall_date: status})

    def count_attendance_percentage(self):
        return (sum(self.user_presence.values()) / len(self.user_presence)) * 100

    def get_attendance(self):
        return self.user_presence
