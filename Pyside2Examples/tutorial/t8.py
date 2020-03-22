# PySide2 tutorial 8
# Widget的绘图功能示例。更方便的绘图可以考虑使用QtChart
# 调色板 https://doc.qt.io/qtforpython/PySide2/QtGui/QPalette.html

import sys
from PySide2 import QtCore, QtGui, QtWidgets


class LCDRange(QtWidgets.QWidget):
    valueChanged = QtCore.Signal(int)  # Signal

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        lcd = QtWidgets.QLCDNumber(2)

        self.slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider.setRange(0, 99)
        self.slider.setValue(0)

        # self.connect(self.slider, QtCore.SIGNAL("valueChanged(int)"), lcd, QtCore.SLOT("display(int)"))
        # self.connect(self.slider, QtCore.SIGNAL("valueChanged(int)"), self, QtCore.SIGNAL("valueChanged(int)"))
        self.slider.valueChanged.connect(lcd.display)
        self.slider.valueChanged.connect(self.valueChanged)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(lcd)
        layout.addWidget(self.slider)
        self.setLayout(layout)

        self.setFocusProxy(self.slider)  # Focus

    def value(self):
        return self.slider.value()

    @QtCore.Slot(int)
    def setValue(self, value):
        self.slider.setValue(value)

    def setRange(self, minValue, maxValue):
        if minValue < 0 or maxValue > 99 or minValue > maxValue:
            QtCore.qWarning("LCDRange.setRange(%d, %d)\n"
                    "\tRange must be 0..99\n"
                    "\tand minValue must not be greater than maxValue" % (minValue, maxValue))
            return

        self.slider.setRange(minValue, maxValue)

# Widget的绘图功能示例
class CannonField(QtWidgets.QWidget):
    angleChanged = QtCore.Signal(int)  # Signal

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.currentAngle = 45
        self.setPalette(QtGui.QPalette(QtGui.QColor(250, 250, 200)))  # 调色板
        self.setAutoFillBackground(True)

    def angle(self):
        return self.currentAngle

    @QtCore.Slot(int)
    def setAngle(self, angle):
        if angle < 5:
            angle = 5
        if angle > 70:
            angle = 70
        if self.currentAngle == angle:
            return
        self.currentAngle = angle
        self.update()
        # self.emit(QtCore.SIGNAL("angleChanged(int)"), self.currentAngle)
        self.angleChanged.emit(self.currentAngle)  # 发送信号的新式写法: 对象.信号.emit(信号入参值)

    # 这是重新实现的绘图事件, QtWidgets.QWidget.paintEvent
    def paintEvent(self, event):
        painter = QtGui.QPainter(self)  # painter 画笔
        painter.setFont(QtGui.QFont('微软雅黑',40))  # 设置画笔字体大小
        painter.drawText(200, 200, "Angle = %d" % self.currentAngle)  # 在给定位置输出文本，如何设置显示大小？

class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        quit = QtWidgets.QPushButton("Quit")
        quit.setFont(QtGui.QFont("Times", 18, QtGui.QFont.Bold))

        # self.connect(quit, QtCore.SIGNAL("clicked()"), QtWidgets.qApp, QtCore.SLOT("quit()"))
        quit.clicked.connect(QtWidgets.QApplication.quit)

        angle = LCDRange()
        angle.setRange(5, 70)

        cannonField = CannonField()

        # self.connect(angle, QtCore.SIGNAL("valueChanged(int)"), cannonField.setAngle)
        # self.connect(cannonField, QtCore.SIGNAL("angleChanged(int)"), angle.setValue)
        angle.valueChanged.connect(cannonField.setAngle)
        cannonField.angleChanged.connect(angle.setValue)

        gridLayout = QtWidgets.QGridLayout()
        gridLayout.addWidget(quit, 0, 0)
        gridLayout.addWidget(angle, 1, 0)
        gridLayout.addWidget(cannonField, 0, 1, 3, 1)  # 在网格中占了多行，表示从(0,1)->(3,1)的区域
        gridLayout.setColumnStretch(1, 10)
        self.setLayout(gridLayout)

        angle.setValue(60)
        angle.setFocus()


app = QtWidgets.QApplication(sys.argv)
widget = MyWidget()
widget.setGeometry(100, 100, 500, 355)
widget.resize(800,600)
widget.show()
sys.exit(app.exec_())
