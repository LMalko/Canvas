class ModelTask():

    def __init__(self, name, task_ID, user_ID, grade=None, is_done=False, is_graded=False):

        self.name = name
        self.task_ID = task_ID
        self.user_ID = user_ID
        self.grade = grade
        self.is_done = is_done
        self.is_graded = is_graded

    def mark_as_done(self):

        self.is_done = True

    def mark_as_graded(self):

        self.is_graded = True

    def rename_task(self, new_name):

        self.name = new_name

    def set_grade(self, grade):

        self.grade = grade

    def task_display(self):

        return "Task: '{}' of ID number: {} assignet to user: {} has earned a grade of {}.".format(self.name,
                                                                                                   self.task_ID,
                                                                                                   self.user_ID,
                                                                                                   self.grade)
    def get_data_to_export(self):
        return [self.name = name,
                self.task_ID = task_ID,
                self.user_ID = user_ID,
                self.grade = grade,
                self.is_done = is_done,
                self.is_graded = is_graded]