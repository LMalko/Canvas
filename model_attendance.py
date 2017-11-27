class ModelAttendance():

    def __init__(self):
        self.user_presence = {}

    def set_presence_status(self, actuall_date, status):
        self.user_presence.update({actuall_date: status})

    def count_attendance_percentage(self):
        percentage_multiplier = 100
        return (sum(self.user_presence.values()) / len(self.user_presence)) * percentage_multiplier

    def get_user_presence(self):
        return self.user_presence

    def get_data_to_export(self):
        pass  # dla Ani :)
