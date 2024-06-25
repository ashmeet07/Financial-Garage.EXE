import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, Qt


class WelcomeScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Financial Garage")
        # Set the initial size and position
        self.setGeometry(100, 100, 600, 400)

        # Create a label for welcome message
        self.welcome_label = QLabel("Welcome to Financial Garage!", self)
        self.welcome_label.setStyleSheet(
            "font-size: 20pt; font-weight: bold; color: black;")
        self.welcome_label.setAlignment(Qt.AlignCenter)

        # Create a vertical layout and add the welcome label
        layout = QVBoxLayout()
        layout.addWidget(self.welcome_label)
        self.setLayout(layout)

        # Schedule removal of welcome message after 3 seconds
        QTimer.singleShot(3000, self.remove_welcome_message)

    def remove_welcome_message(self):
        # Clear the welcome label text
        self.welcome_label.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    welcome_screen = WelcomeScreen()
    welcome_screen.show()
    sys.exit(app.exec_())
