import sys
from random import randint
from PyQt6 import QtWidgets, QtCore, QtGui, uic

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.add_circle)
        self.circles = []

    def add_circle(self):
        diameter = randint(10, 100)
        x = randint(0, self.centralwidget.width() - diameter)
        y = randint(0, self.centralwidget.height() - diameter)
        self.circles.append((x, y, diameter))
        self.update()

    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        qp.setBrush(QtGui.QColor('yellow'))
        for x, y, diameter in self.circles:
            qp.drawEllipse(x, y, diameter, diameter)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
