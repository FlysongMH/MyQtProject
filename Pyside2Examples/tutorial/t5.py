# PySide2 tutorial 5
# QLCDNumber, QSlider, QVBoxLayout


import sys
from PySide2 import QtCore, QtGui, QtWidgets


class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent) # 继承父类__init__方法

        quit = QtWidgets.QPushButton("Quit")
        quit.setFont(QtGui.QFont("Times", 18, QtGui.QFont.Bold))

        lcd = QtWidgets.QLCDNumber()  # QLCDNumber显示数字

        # slider = QtWidgets.QSlider(QtCore.Qt.Vertical)  # 垂直滑动条，默认
        slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)  # 水平滑动条
        slider.setRange(0, 99)
        slider.setValue(0)
        # connect signal and slot
        quit.clicked.connect(QtWidgets.QApplication.quit)
        slider.valueChanged.connect(lcd.display)
        # set layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(quit)
        layout.addWidget(lcd)
        layout.addWidget(slider)
        self.setLayout(layout)


if __name__ == '__main__':


    app = QtWidgets.QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())
