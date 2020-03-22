# PySide2 tutorial 7
# 自定义信号的处理
# 每个LCDRange类自定义了一个valueChanged信号函数，用于表示值变更的信号，当成员slider的值改变时触发信号
# MyWidget将9个LCDRange做了联动处理，当一个LCDRange变更会设置前面LCDRange的值，从而达成联动修改的效果。
# PyQt5中对应@QtCore.Slot(int)的是@QtCore.pyqtSignal(int)
import sys
from PySide2 import QtCore, QtGui, QtWidgets


class LCDRange(QtWidgets.QWidget):
    # 自定义信号,信号类型为int,其中类型与python的类型相对应,比如list传递一个列表，注意与def是一个级别的
    # 信号实际就做了一件事，出发slot，并将入参(若有)传递给slot
    # 此处信号并没有执行emit(), 是否可行?
    valueChanged = QtCore.Signal(int)  # 可以用其他名字与slider的valueChanged区分开

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        lcd = QtWidgets.QLCDNumber(2)

        self.slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider.setRange(0, 99)
        self.slider.setValue(0)

        self.slider.valueChanged.connect(lcd.display)
        self.slider.valueChanged.connect(self.valueChanged)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(lcd)
        layout.addWidget(self.slider)
        self.setLayout(layout)

    def value(self):
        return self.slider.value()

    # @QtCore.Slot(int)
    def setValue(self, value):
        self.slider.setValue(value)


class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        quit = QtWidgets.QPushButton("Quit")
        quit.setFont(QtGui.QFont("Times", 18, QtGui.QFont.Bold))

        quit.clicked.connect(QtWidgets.QApplication.quit)

        grid = QtWidgets.QGridLayout()
        previousRange = None

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(quit)
        layout.addLayout(grid)
        self.setLayout(layout)

        for row in range(3):
            for column in range(3):
                lcdRange = LCDRange()
                grid.addWidget(lcdRange, row, column)

                if previousRange:
                    # self.connect(lcdRange, QtCore.SIGNAL("valueChanged(int)"), previousRange.setValue)
                    lcdRange.valueChanged.connect(previousRange.setValue)

                previousRange = lcdRange



app = QtWidgets.QApplication(sys.argv)
widget = MyWidget()
widget.show()
sys.exit(app.exec_())
