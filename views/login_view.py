from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QCheckBox

class LoginView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
      
        # Create widgets
        self.token_label = QLabel("API Token:")
        self.token_input = QLineEdit()
        self.remember_me = QCheckBox("Remember me")
        self.login_button = QPushButton("Log in")
        
        # Add widgets to layout
        layout = QVBoxLayout()
        button_box = QHBoxLayout()

        # Create and add stretch box to layout
        button_box.addWidget(self.login_button)
        button_box.setAlignment(Qt.AlignRight)

        # Token label and input field
        layout.addWidget(self.token_label)
        layout.addWidget(self.token_input)
        layout.addLayout(button_box)

        # Make input field smaller
        self.token_input.setMaximumWidth(200)
        
        # Make button smaller
        self.login_button.setMaximumWidth(150)

        # Go to main_view when login button is clicked
        self.login_button.clicked.connect(self.log_in)

        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(50, 50, 50, 50)
        self.setLayout(layout)

    def log_in(self):
        # token = self.token_input.text()
        # self.token_signal.emit(token)
        # print(self.parent)
        self.parent.show_main_view()