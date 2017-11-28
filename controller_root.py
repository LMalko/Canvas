'''
import controller_attendance_container
'''
import controller_member_container
'''
import controller_task_container

import model_attendance_container
'''
import model_member_container
'''
import model_task_container

import dao_attendance
'''
import dao_member
'''
import dao_task
'''
from controller_admin import *

from controller_mentor import *
from controller_office import *
from controller_student import *

import view_root
from model_root import *

import controller_admin

class ControllerRoot:

    def __init__(self):
        self.initialize_model()
        self.view = view_root.ViewRoot()

    def initialize_model(self):
        self.associated_model = ModelRoot()
        self.initialize_containers()
        if not self.associated_model.container_member:
            # the user db is empty, instantiate memb. contain. control. to add first admin
            member_ctrl = controller_member_container.ControllerMemberContainer(\
                self.associated_model.container_member)

            # create first admin
            first_admin = self.initial_admin_creation()

            # add it to the container via member container controller
            member_ctrl.add_member(first_admin)

    def login(self, user_login, input_password):
        '''
        Checks whether user password matches the input_password.
        '''
        for user_obj in self.associated_model.container_member:
            if user_obj.login == user_login and user_obj.password == input_password:
                return user_obj

        return None

    def engage_user_controller(self, user_obj):
        if user_obj.role == "admin":
            user_ctrl = ControllerAdmin(user_obj, self.associated_model.container_member)
            user_ctrl.start()
        else:
            raise ValueError("not implemented role")
        '''
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
        '''
        '''
        Launches a user controller based on class of user_obj.
        '''
        pass

    def initialize_containers(self):
        # load members
        member_dao = dao_member.DAOMember("data.csv")
        member_object_collection = member_dao.import_data()
        # initialize member container object
        member_container = ModelMemberContainer()
        for member in member_object_collection:
            member_container.add_member(member)

        self.associated_model.container_member = member_container
        # uncomment below when appropriate DAOs are implemented
        '''
        # load attendance
        attendance_dao = dao_attendance.DAOAttendance("attendance.csv")
        attendance = dao_attendance.import_data()
        self.associated_model.container_attendance = attendance
        # load tasks
        task_dao = dao_task.DAOTask("tasks.csv")
        tasks = dao_task.import_data()
        self.associated_model.container_task = tasks
        '''
        # self.associated_model.container_member = [] # we assume emptiness for now
        self.associated_model.container_task = []
        self.associated_model.container_attendance = []

    def initial_admin_creation(self):
        ctrl_admin = controller_admin.ControllerAdmin(None, None)
        return ctrl_admin.create_first_admin()

    def start(self):
        self.view.display_start_screen()
        login_credentials = self.view.get_login_credentials()
        # login_credentials is a tuple with (login, password)
        while login_credentials:
            user_login = login_credentials[0]
            user_password = login_credentials[1]
            user_obj = self.login(user_login, user_password)
            if user_obj is not None:
                self.engage_user_controller(user_obj)
            else:
                self.view.display_message("Invalid credentials or account does not exist")
            login_credentials = self.view.get_login_credentials()

        self.view.display_exit_screen()
