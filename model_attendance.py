class ModelAttendance():

    def __init__(self, student_uid):
        self.student_uid = student_uid
        self.student_presence = {}

    def set_student_uid(self, new_student_uid):
        self.student_uid = new_student_uid

    def set_new_student_presence(self, new_dict):
        '''Replace student presence with new dict.'''
        self.student_presence = new_dict

    def set_presence_status(self, actuall_date, status):
        self.student_presence.update({actuall_date: status})

    def count_attendance_percentage(self):
        percentage_multiplier = 100
        return (sum(self.student_presence.values()) / len(self.student_presence)) * percentage_multiplier

    def get_student_uid(self):
        return self.student_uid

    def get_student_presence(self):
        return self.student_presence

    def __str__(self):
        return 'attendance for student UID: {}'.format(self.student_uid)

    def __repr__(self):
        return 'ModelAttendance({})'.format(self.student_uid)

    def get_data_to_export(self):
        data_to_export = [self.student_uid]
        for date, presence in self.student_presence.items():
            data_to_export.append(date)
            data_to_export.append(str(presence))
        return data_to_export
