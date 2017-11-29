class ModelTask():

    def __init__(self, name, task_ID, user_ID, grade=None, is_done=0, is_graded=0):

        self.name = name
        self.task_ID = task_ID
        self.user_ID = user_ID
        self.grade = grade
        self.is_done = is_done
        self.is_graded = is_graded

    def change_delivery_status(self):
        
        self.is_done = True
        # self.is_done = 1 if not self.is_done else 0
        # if self.is_done == 0:
        #     self.grade = None
        #     self.is_graded = 0

    def mark_as_graded(self):
        self.is_graded = 1

    def rename_task(self, new_name):
        self.name = new_name

    def set_grade(self, grade):
        self.grade = grade

    def get_task_id(self):
        return self.task_ID

    def get_user_id(self):
        return self.user_ID

    def get_task_name(self):
        return self.name

    def get_delivery_status(self):
        return self.is_done

    def get_mentor_task_display(self):
        done = 'DELIVERED' if self.is_done else 'NOT DELIVERED'
        return "Task: '{:>30}', ID: {:>4}, student: {:>4}, grade {:>4}, status: {}".format(self.name, self.task_ID, self.user_ID, self.grade, done)
    
    def get_student_task_display(self):
        done = 'DELIVERED' if self.is_done else 'NOT DELIVERED'
        return "Task: '{:>30}', ID: {:>4}, grade {:>4}, status: {}".format(self.name, self.task_ID, self.grade, done)
    
    def get_short_task_display(self):
        return "{:>4}: {}".format(self.task_ID, self.name)
    
    def get_data_to_export(self):
        return [self.name,
                self.task_ID,
                self.user_ID,
                str(self.grade),
                str(self.is_done),
                str(self.is_graded)]

