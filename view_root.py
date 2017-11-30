import os
import getpass


class ViewRoot():

    def get_login_credentials(self, login_prompt='', password_prompt=''):
        '''Return login, password in tuple.'''
        _new_lines = '\n' * 4
        self.clear_screen()
        self.display_message("Type X as login to quit the program.")

        if not login_prompt and not password_prompt:
            login_prompt = _new_lines + 'Enter login --> '
            password_prompt = _new_lines + 'Enter password --> '
        _login, _password = '', ''
        while not _login:
            _login = input(login_prompt)
        if _login == 'X':
            return ()
        while not _password:
            _password = getpass.getpass(password_prompt)
        return _login, _password

    def display_message(self, message):
        print('\n\n' + message + '\n\n')

    def display_start_screen(self, text=''):
        self.clear_screen()
        if not text:
            text = '\n\nWelcome in Kanwas by ***ABS***\n\n\t\tsupported by ship picker...\n\n'
        print(text)
        input('\n\nPress <enter> to continue.. ')

    def display_exit_screen(self, text=''):
        self.clear_screen()
        if not text:
            text = '\n\n..logged out, exit program.\n\n'
        print(text)

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
