import os


class ViewRoot():


    def display_login_screen(self, txt1='', txt2=''):
#        self.clear_screen()
        _new_lines = '\n\n'*2
        if not txt1 and not txt2:
            txt1 = _new_lines + 'Enter login --> '
            txt2 = _new_lines + 'Enter password --> '
        return self.take_user_input(txt1, txt2)

    @staticmethod
    def take_user_input(txt1, txt2):
        '''Return login, password in tuple.'''
        _login, _password = '', ''
        while not _login:
            _login = input(txt1)
        if _login == 'X':
            return ()
        while not _password:
            _password = input(txt2)
        return _login, _password

    @staticmethod
    def display_message(message):
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


# a = ViewRoot()
#
# tmp = a.display_login_screen()
# print(tmp)
# print(tmp[0], tmp[1])
# a.display_start_screen()
# a.display_exit_screen()
