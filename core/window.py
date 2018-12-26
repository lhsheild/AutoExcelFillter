

from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.center_widget = QWidget(self)
        self.setCentralWidget(self.center_widget)

        self.do_button = self.do_button_init()

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.do_button)

        self.center_widget.setLayout(main_layout)

    def do_button_init(self):
        do_button = QPushButton(self)
        do_button.setFixedSize(128, 128)
        return do_button

    def exit_button_init(self):
        exit_button = QPushButton(self)
        exit_button.setFixedSize(128, 128)
        return exit_button
