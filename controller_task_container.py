from model_task import*
from model_attendance_container import*
from view_controller_task_container import*
from controller_user import*


class ControllerTaskContainer():

    def __init__(self, container_task):
        self.container_task = container_task
        self.view_task_container = ViewControllerTaskContainer()
        self.ctrl_user = ControllerUser()

    def is_collection_empty(self, collection):
        if not collection:
            self.view_task_container.display_message("\nTask list is empty. Nothing to display.")
            return True
        else:
            return False

    def add_task_to_container(self, task):
        self.container_task.add_task(task)

    def del_task_from_container(self):
        all_tasks = self.container_task.get_all_tasks()
        if self.is_collection_empty(all_tasks):
            return
        task_id = self.get_task_id_by_genre()

        for index in range(len(all_tasks)-1, -1, -1):
            if all_tasks[index].get_task_id() == task_id:
                self.container_task.del_task(all_tasks[index])

    def get_tasks_by_genre(self):
        all_tasks = self.container_task.get_all_tasks()
        if self.is_collection_empty(all_tasks):
            return
        chosen_task_id = self.get_task_id_by_genre()

        for task in all_tasks:
            if task.get_task_id() == chosen_task_id:
                self.view_task_container.display_message(task.get_detailed_task_display())

    def get_all_tasks(self, all_tasks=None):
        if not all_tasks:
            all_tasks = self.container_task.get_all_tasks()

        if self.is_collection_empty(all_tasks):
            return

        for task in all_tasks:
            self.view_task_container.display_message(task.get_detailed_task_display())

    def sumbit_task_link(self, task):
        link = self.get_valid_input("\nPass tasks link: ")
        task.set_task_link(link)

    def get_task_link(self, task):
        return task.get_task_link()

    def change_task_delivery_status(self, student_id=None):
        all_tasks = self.container_task.get_all_tasks()
        if self.is_collection_empty(all_tasks):
            return
        all_student_tasks = self.cherry_pick_tasks_by_user_id(student_id)
        if self.is_collection_empty(all_student_tasks):
            return
        task = self.take_and_validate_task_choice_by_task_id(all_student_tasks)
        self.sumbit_task_link(task)
        task.change_delivery_status()

    def grade_task(self, task):
        if not task.get_delivery_status():
            self.view_task_container.display_message("\nTask has not been submitted. Grading aborted\n")
            return False
        self.view_task_container.display_message(self.get_task_link(task))

        possible_grades = ['-3', '0', '4', '7', '10', '12']

        invalid_input = True
        while invalid_input:
            self.view_task_container.display_message("{}:\n {}".format('\nPossible choices', ",".join(possible_grades)))
            grade = self.get_valid_input("\nPass tasks grade: ")
            if grade in possible_grades:
                task.set_grade(grade)
                invalid_input = False
                self.view_task_container.display_message('\nTask graded!')
            else:
                self.view_task_container.display_message('\nChoice not in possible choices\n')

    def rename_task(self):
        chosen_task_id = self.get_task_id_by_genre()
        new_task_name = self.get_valid_input("\nPass new task name: ")

        all_tasks = self.container_task.get_all_tasks()
        for task in all_tasks:
            if task.get_task_id() == chosen_task_id:
                task.rename_task(new_task_name)

    def create_and_deploy_task(self, target_group):
        task_id = self.get_max_task_id()

        max_task_name_length = 15
        invalid_input = True
        while invalid_input:
            task_name = self.get_valid_input("\nPass tasks name(max {} char): ".format(max_task_name_length))
            if len(task_name) <= max_task_name_length:
                invalid_input = False

        for student in target_group:
            student_id = self.ctrl_user.get_member_id(student)
            self.add_task_to_container(ModelTask(task_name, task_id, student_id))

    def get_valid_input(self, message):
        invalid_input = True
        while invalid_input:
            user_input = self.view_task_container.get_user_input(message)
            if (len(user_input.strip()) != 0) and ('\\' not in user_input):
                invalid_input = False

        return user_input

    def get_max_task_id(self):
        all_tasks = self.container_task.get_all_tasks()
        if self.is_collection_empty(all_tasks):
                return "0000"  # First tasks id
        all_id = []
        for task in all_tasks:
            all_id.append(int(task.get_task_id()))
        return "{:0>4}".format(max(all_id)+1)

    def get_task_id_by_genre(self):
        all_tasks = self.container_task.get_all_tasks()
        if self.is_collection_empty(all_tasks):
            return

        tasks_by_id = []
        for task in all_tasks:
            tasks_by_id.append(task.get_short_task_display())

        invalid_choice = True
        while invalid_choice:
            self.view_task_container.display_collection(sorted(list(set(tasks_by_id))))
            user_choice = self.get_valid_input("\nChoose task by id: ")
            for task in all_tasks:
                if task.get_task_id() == user_choice:
                    invalid_choice = False
                    break

        return user_choice

    def take_and_validate_task_choice_by_task_id(self, all_tasks):
        invalid_choice = True
        chosen_task = None
        while invalid_choice:
            self.view_task_container.display_message('\n')
            for task in all_tasks:
                self.view_task_container.display_message(task.get_generic_task_display())
            user_choice = self.get_valid_input("\nChoose task by task id: ")
            for task in all_tasks:
                if task.get_task_id() == user_choice:
                    chosen_task = task
                    invalid_choice = False
                    break
        return chosen_task

    def take_and_validate_task_choice_by_user_id(self, all_tasks):
        invalid_choice = True
        chosen_task = None
        while invalid_choice:
            self.view_task_container.display_message('\n')
            for task in all_tasks:
                self.view_task_container.display_message(task.get_detailed_task_display())
            
            user_choice = self.get_valid_input("\nChoose task by user id: ")

            for task in all_tasks:
                if task.get_user_id() == user_choice:
                    chosen_task = task
                    invalid_choice = False
                    break
        return chosen_task

    def take_and_validate_particular_task_choice(self):
        all_tasks = self.container_task.get_all_tasks()
        if self.is_collection_empty(all_tasks):
            return

        chosen_task = None
        invalid_choice = True
        while invalid_choice:
            self.view_task_container.display_message('\n')
            for task in all_tasks:
                self.view_task_container.display_message(task.get_detailed_task_display())

            task_id_choice = self.view_task_container.get_user_input("\nChoose task by task id: ")
            user_id_choice = self.view_task_container.get_user_input("\nChoose task by user id: ")
            for task in all_tasks:
                if (task.get_task_id() == task_id_choice) & (task.get_user_id() == user_id_choice):
                    chosen_task = task
                    invalid_choice = False
                    break
        return chosen_task

    def cherry_pick_tasks_by_user_id(self, user_id):
        all_tasks = self.container_task.get_all_tasks()
        user_tasks = []
        for task in all_tasks:
            if task.get_user_id() == user_id:
                user_tasks.append(task)

        return user_tasks

    def cherry_pick_tasks_by_task_id(self, task_id):
        all_tasks = self.container_task.get_all_tasks()
        tasks = []
        for task in all_tasks:
            if task.get_task_id() == task_id:
                tasks.append(task)
        return tasks

