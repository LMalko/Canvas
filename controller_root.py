from controller_attendance_container import ControllerAttendanceContainer
from controller_member_container import ControllerMemberContainer
from controller_task_container import ControllerTaskContainer

from model_attendance_container import ModelAttendanceContainer
from model_member_container import ModelMemberContainer
from model_task_container import ModelTaskContainer

import dao_attendance
import dao_member
import dao_task

from controller_admin import ControllerAdmin
from controller_mentor import ControllerMentor
from controller_office import ControllerOffice
from controller_student import ControllerStudent

import view_root
from model_root import ModelRoot


class ControllerRoot:

    def __init__(self):
        self.initialize_model()
        self.view = view_root.ViewRoot()

    def initialize_model(self):
        self.associated_model = ModelRoot()
        self.initialize_containers()
        if not self.associated_model.container_member:
            # the user db is empty, instantiate memb. contain. control. to add first admin
            member_ctrl = ControllerMemberContainer(self.associated_model.container_member)

            # create first admin
            first_admin = self.initial_admin_creation()

            # add it to the container via member container controller
            member_ctrl.add_member(first_admin)

    def login(self, user_login, input_password):
        '''
        Checks whether user password matches the input_password.
        '''
        for user_obj in self.associated_model.container_member.get_all_members():
            if user_obj.login == user_login and user_obj.password == input_password:
                return user_obj

        return None

    def engage_user_controller(self, user_obj):
        if user_obj.role == "admin":
            user_ctrl = ControllerAdmin(user_obj, self.associated_model.container_member)
            user_ctrl.start()
        elif user_obj.role == "mentor":
            attnd = self.associated_model.container_attendance
            mmbr = self.associated_model.container_member
            tsk = self.associated_model.container_task
            user_ctrl = ControllerMentor(user_obj, attnd, mmbr, tsk)
            user_ctrl.start()
        elif user_obj.role == "office":
            user_ctrl = ControllerOffice(user_obj, self.associated_model.container_member)
            user_ctrl.start()

        elif user_obj.role == "student":
            user_ctrl = ControllerStudent(user_obj, self.associated_model.container_task)
            user_ctrl.start()
        else:
            raise ValueError("not implemented role")
        '''
        Launches a user controller based on class of user_obj.
        '''

    def initialize_containers(self):
        # load members
        member_dao = dao_member.DAOMember()
        member_object_collection = member_dao.import_data()
        # initialize member container object
        member_container = ModelMemberContainer()
        for member in member_object_collection:
            member_container.add_member(member)

        self.associated_model.container_member = member_container

        # load tasks
        task_dao = dao_task.DAOTask()
        task_object_collection = task_dao.import_data()
        # initialize task container object
        task_container = ModelTaskContainer()
        for task in task_object_collection:
            task_container.add_task(task)
        self.associated_model.container_task = task_container

        # load attendance
        attendance_dao = dao_attendance.DAOAttendance()
        attendance_object_collection = attendance_dao.import_data()
        # initialize attendance container object
        attendance_container = ModelAttendanceContainer()
        for attendance in attendance_object_collection:
            attendance_container.add_student_attendance(attendance)
        self.associated_model.container_attendance = attendance_container

    def save_containers(self):
        # grab collections
        member_collection = self.associated_model.container_member.get_all_members()
        task_collection = self.associated_model.container_task.get_all_tasks()
        attendance_collection = self.associated_model.container_attendance.get_all_attendance()

        # instantiate DAOs
        member_dao = dao_member.DAOMember()
        task_dao = dao_task.DAOTask()
        attendance_dao = dao_attendance.DAOAttendance()

        # perform the export
        member_dao.export_data(member_collection)
        task_dao.export_data(task_collection)
        attendance_dao.export_data(attendance_collection)

    def initial_admin_creation(self):
        ctrl_admin = ControllerAdmin(None, None)
        return ctrl_admin.create_first_admin()

    def start(self):
        self.view.display_start_screen()
        self.view.clear_screen()
        login_credentials = self.view.get_login_credentials()
        # login_credentials is a tuple with (login, password)
        while login_credentials:
            user_login = login_credentials[0]
            user_password = login_credentials[1]
            user_obj = self.login(user_login, user_password)
            if user_obj is not None:
                self.engage_user_controller(user_obj)
            else:
                self.view.freeze_until_key_pressed("Invalid credentials or account does not exist")
            login_credentials = self.view.get_login_credentials()

        # we are about to exit - save the containers
        self.save_containers()
        self.view.display_exit_screen()
