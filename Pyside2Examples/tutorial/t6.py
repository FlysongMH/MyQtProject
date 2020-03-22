# PySide2 tutorial 6
# 快速添加9个相同的LCD+滑动条

import sys
from PySide2 import QtCore, QtGui, QtWidgets


class LCDRange(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        lcd = QtWidgets.QLCDNumber(2)
        # slider = QtWidgets.QSlider(QtCore.Qt.Vertical)  # 垂直滑动条，默认
        slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)  # 水平滑动条
        slider.setRange(0, 99)
        slider.setValue(0)
        slider.valueChanged.connect(lcd.display)
        # set layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(lcd)
        layout.addWidget(slider)
        self.setLayout(layout)


class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        quit = QtWidgets.QPushButton("Quit")
        quit.setFont(QtGui.QFont("Times", 18, QtGui.QFont.Bold))
        quit.clicked.connect(QtWidgets.QApplication.quit)

        grid = QtWidgets.QGridLayout()
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(quit)
        layout.addLayout(grid)
        self.setLayout(layout)
        for row in range(3):
            for column in range(3):
                grid.addWidget(LCDRange(), row, column)




app = QtWidgets.QApplication(sys.argv)
widget = MyWidget()
widget.show()
sys.exit(app.exec_())
