from PyQt5.QtWidgets import QApplication, QMainWindow
from views.log_view import LogView
from views.login_view import LoginView
from views.main_view import MainView

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Set up login view
        self.login_view = LoginView(self)
        self.setCentralWidget(self.login_view)
        
    def show_main_view(self):
        self.setCentralWidget(MainView(self))
        
    def show_login_view(self):
        self.setCentralWidget(LoginView(self))

    def show_log_view(self):
        self.setCentralWidget(LogView(self))

if __name__ == '__main__':
    app = QApplication([])
    # Load stylesheet
    stylesheet = "views/styles.qss"
    with open(stylesheet, "r") as fh:
        app.setStyleSheet(fh.read())
    window = MainWindow()
    window.resize(800, 600)
    window.setWindowTitle("MinoTime")
    window.show()
    app.exec_()
