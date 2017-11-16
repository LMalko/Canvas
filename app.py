from controller_root import ControllerRoot


class App():

    def __init__(self):
        root = ControllerRoot()
        root.initialize_model()
        root.login()


if __name__ == "__main__":
    initialize_program = App()
