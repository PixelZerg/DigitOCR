import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class TestDialog(QMainWindow):
    def __init__(self):
        super().__init__(flags=Qt.WindowStaysOnTopHint)
        self.__init_ui()
        self.setWindowModality(Qt.ApplicationModal)

    def showEvent(self, event):
        # on startup, resize
        self.resizeEvent(None)

    def resizeEvent(self, event):
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

        self.area = DrawArea(core)
        layout.addWidget(self.area,100)

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

class DrawArea(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        self.pixmap = QPixmap(28,28)
        self.pixmap.fill((QColor('white')))

    def paintEvent(self, event:QPaintEvent):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(),self.pixmap)

    def mouseMoveEvent(self, event:QMouseEvent):
        print(event.x())
        painter = QPainter(self.pixmap)

        pos = event.pos()
        painter.drawPoint(int(float(pos.x())/self.size().width()*self.pixmap.width()),
                          int(float(pos.y()) / self.size().height() * self.pixmap.height()))
        # painter.drawPoint(self.mapFromGlobal(QCursor.pos()))
        # painter.drawRect(event.x(),event.y(),5,5)
        # painter.save()
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = TestDialog()
    ui.resize(320, 320)
    ui.show()

    sys.exit(app.exec())

