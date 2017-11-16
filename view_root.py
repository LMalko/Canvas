
class ViewRoot():

    def display_login_screen(self, txt1='', txt2=''):
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
        while not _password:
            _password = input(txt2)
        return _login, _password

    def display_message(message):
        pass

    def display_text(text):
        pass

    @staticmethod
    def display_start_screen(text=''):
        if not text:
            text = '\n\nWelcome in Kanwas by ***ABS***\n\n\t\tsupported by ship picker...\n\n'
        print(text)
        input('\n\nPress <enter> to continue.. ')

    def display_exit_screen(text=''):
        pass

#
# a = ViewRoot()
#
# tmp = a.display_login_screen()
# print(tmp)
# print(tmp[0], tmp[1])
# a.display_start_screen()
  #
  #
  # + __init__(): None
  # + display_login_screen(text): None
  # + take_user_input(text, valid_condition): string
  # + check_if_input_is_valid(valid_condition): bool
  # + display_message(message): None
  # + display_text(text): None
  # + display_start_screen(text=''): None
  # + display_exit_screen(text=''): None
