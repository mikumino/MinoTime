# NOT USED
# Handles the switching and updating of views

from PyQt5.QtWidgets import QStackedWidget
from views.login_view import LoginView
from views.main_view import MainView
from views.log_view import LogView

class ViewManager:
    def __init__(self, stacked_widget):
        self.stacked_widget = stacked_widget
        self.views = {}
        self.current_view = None
        # There's probably a better way to do this
        self.add_view("login", LoginView(self))
        # self.add_view("main", MainView(self))
        # self.add_view("log", LogView(self))

        for view in self.views.values():
            self.stacked_widget.addWidget(view)

    def add_view(self, name, view):
        self.views[name] = view

    def show_view(self, name):
        if name not in self.views:
            raise Exception("View not found: " + name)
        if self.current_view is not None:
            self.current_view.hide()
        self.current_view = self.views[name]
        self.current_view.show()
