# NOT USED

from models.token_manager import TokenManager

class LoginController():
    def __init__(self, view):
        self.view = view

    def log_in(self, token):
        TokenManager.save_token(token, self.view.remember_me.isChecked())
        self.view.show_main_view()

    