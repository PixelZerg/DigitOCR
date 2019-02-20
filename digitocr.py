import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QResizeEvent
from PyQt5.QtWidgets import *

class TestDialog(QMainWindow):
    def __init__(self):
        super().__init__(flags=Qt.WindowStaysOnTopHint)
        self.__init_ui()
        self.setWindowModality(Qt.ApplicationModal)

    def showEvent(self, event):
        # on startup, resize
        self.resizeEvent(None)

    def resizeEvent(self, event:QResizeEvent):
        print("resize")

        area_size = self.area.size()
        dh = area_size.width()-area_size.height()

        cur_size = self.size()
        self.resize(cur_size.width(),cur_size.height()+dh)

        if event is not None:
            QMainWindow.resizeEvent(self, event)

    def __init_ui(self):
        core = QWidget()
        layout = QVBoxLayout()

        bar = QWidget()
        bar.layout = QHBoxLayout()

        self.label = QLabel("Draw a digit:")
        layout.addWidget(self.__make_bar(self.label))

        self.area = QTextEdit()
        layout.addWidget(self.area)

        self.btn_clear = QPushButton("Clear")
        self.btn_run = QPushButton("Run")

        layout.addWidget(self.__make_bar(self.btn_clear, self.btn_run))

        core.setLayout(layout)
        self.setCentralWidget(core)

    def __make_bar(self, *widgets):
        bar = QWidget()
        bar.layout = QHBoxLayout()

        for widget in widgets:
            bar.layout.addWidget(widget)

        bar.layout.setContentsMargins(2, 0, 2, 3)
        bar.setLayout(bar.layout)
        return bar

if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = TestDialog()
    ui.resize(320, 320)
    ui.show()

    sys.exit(app.exec())

