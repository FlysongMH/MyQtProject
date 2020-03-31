# PySide2 tutorial 10
# 为CannonField新增了一个forceChanged信号，但貌似没什么作用

import sys
from PySide2 import QtCore, QtGui, QtWidgets


class LCDRange(QtWidgets.QWidget):
    valueChanged = QtCore.Signal(int)
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        lcd = QtWidgets.QLCDNumber(2)
        self.slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider.setRange(0, 99)
        self.slider.setValue(0)

        self.connect(self.slider, QtCore.SIGNAL("valueChanged(int)"),
                     lcd, QtCore.SLOT("display(int)"))
        self.connect(self.slider, QtCore.SIGNAL("valueChanged(int)"),
                     self, QtCore.SIGNAL("valueChanged(int)"))

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(lcd)
        layout.addWidget(self.slider)
        self.setLayout(layout)

        self.setFocusProxy(self.slider)

    def value(self):
        return self.slider.value()

    @QtCore.Slot(int)
    def setValue(self, value):
        self.slider.setValue(value)

    def setRange(self, minValue, maxValue):
        if minValue < 0 or maxValue > 99 or minValue > maxValue:
            QtCore.qWarning("LCDRange::setRange(%d, %d)\n"
                    "\tRange must be 0..99\n"
                    "\tand minValue must not be greater than maxValue" % (minValue, maxValue))
            return

        self.slider.setRange(minValue, maxValue)


class CannonField(QtWidgets.QWidget):
    angleChanged = QtCore.Signal(int)
    forceChanged = QtCore.Signal(int)  # 新增一个信号
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.currentAngle = 45
        self.currentForce = 0  # 配合新信号使用
        self.setPalette(QtGui.QPalette(QtGui.QColor(250, 250, 200)))
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
        self.emit(QtCore.SIGNAL("angleChanged(int)"), self.currentAngle)

    def force(self):
        return self.currentForce

    @QtCore.Slot(int)
    def setForce(self, force):
        if force < 0:
            force = 0
        if self.currentForce == force:
            return
        self.currentForce = force
        self.emit(QtCore.SIGNAL("forceChanged(int)"), self.currentForce)  # 发送forceChanged信号

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)

        painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(QtCore.Qt.blue)

        h = self.rect().height()
        painter.translate(0, self.rect().height())  # 坐标转换：中心坐标平移位置. 左为x，下为y # 此处为移到左下角
        painter.drawPie(QtCore.QRect(-h/2, -h/2, h, h), 0*16, 90*16)  # 绘制饼型和扇形 # 注意这里的角度单位是1/16度
        painter.rotate(-self.currentAngle)  # 整个画布进行了逆时针旋转
        painter.drawRect(QtCore.QRect(0, -2, h, 4))  # 绘制一个方框

    def cannonRect(self):
        result = QtCore.QRect(0, 0, 50, 50)
        result.moveBottomLeft(self.rect().bottomLect())
        return result


class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        quit = QtWidgets.QPushButton("&Quit")  # 多了个&好像是快捷键
        quit.setFont(QtGui.QFont("Times", 18, QtGui.QFont.Bold))

        self.connect(quit, QtCore.SIGNAL("clicked()"),
                     QtWidgets.qApp, QtCore.SLOT("quit()"))

        angle = LCDRange()
        angle.setRange(5, 70)

        force = LCDRange()
        force.setRange(10, 50)

        cannonField = CannonField()

        self.connect(angle, QtCore.SIGNAL("valueChanged(int)"),
                     cannonField.setAngle)
        self.connect(cannonField, QtCore.SIGNAL("angleChanged(int)"),
                     angle.setValue)

        self.connect(force, QtCore.SIGNAL("valueChanged(int)"),
                     cannonField.setForce)
        self.connect(cannonField, QtCore.SIGNAL("forceChanged(int)"),
                     force.setValue)

        leftLayout = QtWidgets.QVBoxLayout()
        leftLayout.addWidget(angle)
        leftLayout.addWidget(force)

        gridLayout = QtWidgets.QGridLayout()
        gridLayout.addWidget(quit, 0, 0)
        gridLayout.addLayout(leftLayout, 1, 0)
        gridLayout.addWidget(cannonField, 1, 1, 2, 1)
        gridLayout.setColumnStretch(1, 10)
        self.setLayout(gridLayout)

        angle.setValue(60)
        force.setValue(25)
        angle.setFocus()


app = QtWidgets.QApplication(sys.argv)
widget = MyWidget()
widget.setGeometry(100, 100, 500, 355)
widget.show()
sys.exit(app.exec_())
