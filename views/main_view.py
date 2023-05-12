from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

class MainView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Create widgets
        self.message_label = QLabel("Welcome!")
        self.logout_button = QPushButton("Generate Log")

        # Go to login_view when logout button is clicked
        self.logout_button.clicked.connect(parent.show_log_view)
        
        # Add widgets to layout
        layout = QVBoxLayout()
        layout.addWidget(self.message_label)
        layout.addWidget(self.logout_button)
        layout.setAlignment(Qt.AlignCenter)
        self.setLayout(layout)