# PySide2 tutorial 4
# 自定义Widget继承

import sys
from PySide2 import QtCore, QtGui, QtWidgets


class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)  # 继承父类的初始化方法

        self.setFixedSize(400, 120)

        self.quit = QtWidgets.QPushButton("Quit", self)
        self.quit.setGeometry(100, 40, 75, 30)
        self.quit.setFont(QtGui.QFont("Times", 18, QtGui.QFont.Bold))

        self.quit.clicked.connect(QtWidgets.QApplication.quit)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    widget = MyWidget()
    widget.show()

    sys.exit(app.exec_())
