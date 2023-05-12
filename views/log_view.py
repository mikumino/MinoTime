from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from controllers.log_controller import LogController
from views.login_view import LoginView
import pyperclip

class LogView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.login_view = LoginView(self)
        # self.login_view.token_signal.connect(self.get_token)
        self.token = ""

        # Create widgets
        self.select_label = QLabel("Select a date to view time entries for:")

        # Create a date picker
        self.date_picker = QDateEdit(calendarPopup=True)
        self.date_picker.setDisplayFormat("yyyy-MM-dd")
        self.date_picker.setDateTime(QtCore.QDateTime.currentDateTime())

        # Create submit button
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit_button_clicked)

        # Create copy to clipboard button
        self.copy_button = QPushButton("Copy to clipboard")
        self.copy_button.clicked.connect(self.copy_to_clipboard)

        # Entry field for time entries to be copied to
        self.time_entries = QTextEdit()
        self.time_entries.setMaximumWidth(500)
        self.time_entries.setMaximumHeight(100)

        # Add widgets to layout
        layout = QVBoxLayout()
        # layout.addWidget(self.select_label)
        layout.addWidget(self.date_picker)
        layout.addWidget(self.time_entries)
        layout.addWidget(self.submit_button)
        layout.addWidget(self.copy_button)
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(50, 50, 50, 50)
        self.setLayout(layout)

    def submit_button_clicked(self):
        date = self.date_picker.dateTime().toString("yyyy-MM-dd")
        entries= LogController(self).get_time_entries(date)
        self.time_entries.setText(entries)

    def copy_to_clipboard(self):
        pyperclip.copy(self.time_entries.toPlainText())

    def get_token(self, token):
        self.token = token
        print(self.token)