from controller_root import ControllerRoot


class App():

    def __init__(self):
        self.root = ControllerRoot()


def main():
    initialize_program = App()
    initialize_program.root.start()


if __name__ == "__main__":
    main()
