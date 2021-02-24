import sys, random

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QPen, QColor
from UI import Ui_Form


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Git и случайные окружности')
        self.circles = []
        self.pushButton.clicked.connect(self.circle)

    def circle(self):
        d = random.randint(1, min([self.width(), self.height()]))
        x = random.randint(0, self.width() - d - 1)
        y = random.randint(0, self.height() - d - 1)
        c = [random.randint(0, 255) for i in range(3)]
        self.circles += [(c, (x, y, d, d))]
        self.update()

    def paintEvent(self, *args, **kwargs):
        b = QPainter()
        b.begin(self)
        self.draw(b)
        b.end()

    def draw(self, a):
        a.setBrush(QColor(0, 0, 0, 0))
        for color, data in self.circles:
            pen = QPen(QColor(*color), 5)
            a.setPen(pen)
            a.drawEllipse(*data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
