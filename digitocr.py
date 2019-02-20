import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

class TestDialog(QMainWindow):
    def __init__(self):
        super().__init__(flags=Qt.WindowStaysOnTopHint)
        self.__init_ui()

    def __init_ui(self):
        # core = QWidget()
        # layout = QVBoxLayout()
        #
        # layout.addWidget(self.__init_info_bar())
        # layout.addWidget(self.__init_button_bar())
        #
        # core.setLayout(layout)
        # self.setCentralWidget(core)

        self.setCentralWidget(QTextEdit())
        self.addDockWidget(Qt.TopDockWidgetArea,self.__make_bar(
            QLabel("wow")
        ))

    def __make_bar(self, *widgets):
        bar = QWidget()
        layout = QHBoxLayout()
        # layout.setContentsMargins(5,10,5,5)

        for widget in widgets:
            widget.setAlignment(Qt.AlignVCenter)
            layout.addWidget(widget)

        bar.setLayout(layout)

        ret = QDockWidget()
        ret.setTitleBarWidget(QWidget()) # remove QDockWidget title
        ret.setWidget(bar)
        ret.setContentsMargins(0,0,0,0)

        return ret

    def __init_info_bar(self):
        top_bar = QWidget()
        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)

        layout.addWidget(QLabel("asdasdsadadsasd"))
        layout.addWidget(QLabel("asdasd"))

        top_bar.setLayout(layout)

        ret = QDockWidget()
        ret.setTitleBarWidget(QWidget()) # remove QDockWidget title
        ret.setWidget(top_bar)
        ret.setContentsMargins(0,0,0,0)
        return ret

    def __init_button_bar(self):
        top_bar = QDockWidget()
        layout = QHBoxLayout()

        layout.addWidget(QPushButton("wow"))
        layout.addWidget(QPushButton("asdasd"))

        top_bar.setLayout(layout)
        return top_bar

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = TestDialog()
    ui.show()

    sys.exit(app.exec())

