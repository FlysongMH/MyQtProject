# PySide2 tutorial 11
# 这是个高射炮打蚊子游戏，当前新增定时器以及射击角度和射击原力

import sys
import math
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
    forceChanged = QtCore.Signal(int)
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.currentAngle = 45
        self.currentForce = 0
        self.timerCount = 0
        self.autoShootTimer = QtCore.QTimer(self)  # 射击定时器
        self.connect(self.autoShootTimer, QtCore.SIGNAL("timeout()"),
                     self.moveShot)  # 射击定时器超时动作
        self.shootAngle = 0
        self.shootForce = 0
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
        self.emit(QtCore.SIGNAL("forceChanged(int)"), self.currentForce)

    @QtCore.Slot()
    def shoot(self):
        '''射击开始'''
        if self.autoShootTimer.isActive():
            return  # 定时器保护，无法连续射击
        self.timerCount = 0
        self.shootAngle = self.currentAngle
        self.shootForce = self.currentForce
        self.autoShootTimer.start(4)  # 定时间隔是5ms？

    @QtCore.Slot()
    def moveShot(self):
        # 移动子弹，
        region = QtGui.QRegion(self.shotRect())  # 子弹当前位置
        self.timerCount += 1

        shotR = self.shotRect() # 子弹下一个位置

        if shotR.x() > self.width() or shotR.y() > self.height():
            self.autoShootTimer.stop()  # 超出边界就停止
        else:
            region = region.united(QtGui.QRegion(shotR))

        self.update(region)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)

        self.paintCannon(painter)
        if self.autoShootTimer.isActive():
            self.paintShot(painter)

    def paintShot(self, painter):
        painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(QtCore.Qt.black)
        painter.drawRect(self.shotRect())

    barrelRect = QtCore.QRect(33, -4, 15, 8)

    def paintCannon(self, painter):
        painter.setPen(QtCore.Qt.NoPen)
        painter.setBrush(QtCore.Qt.blue)

        painter.save()
        painter.translate(0, self.height())
        painter.drawPie(QtCore.QRect(-35, -35, 70, 70), 0, 90 * 16)
        painter.rotate(-self.currentAngle)
        painter.drawRect(CannonField.barrelRect)
        painter.restore()

    def cannonRect(self):
        result = QtCore.QRect(0, 0, 50, 50)
        result.moveBottomLeft(self.rect().bottomLect())
        return result

    def shotRect(self):
        # 根据timerCount计算当前移动位置
        gravity = 10  # 重力加速度

        time = self.timerCount / 40.0
        velocity = self.shootForce  # 移动速度
        radians = self.shootAngle * 3.14159265 / 180  # 弧度，移动方向

        velx = velocity * math.cos(radians)
        vely = velocity * math.sin(radians)
        x0 = (CannonField.barrelRect.right() + 5) * math.cos(radians)
        y0 = (CannonField.barrelRect.right() + 5) * math.sin(radians)
        x = x0 + velx * time    # 水平位移
        y = y0 + vely * time - 0.5 * gravity * time * time  # 垂直位移

        result = QtCore.QRect(0, 0, 6, 6)
        result.moveCenter(QtCore.QPoint(round(x), self.height() - 1 - round(y)))
        return result


class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        quit = QtWidgets.QPushButton("&Quit")
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

        shoot = QtWidgets.QPushButton("&Shoot")
        shoot.setFont(QtGui.QFont("Times", 18, QtGui.QFont.Bold))

        self.connect(shoot, QtCore.SIGNAL("clicked()"), cannonField.shoot)

        topLayout = QtWidgets.QHBoxLayout()
        topLayout.addWidget(shoot)
        topLayout.addStretch(1)

        leftLayout = QtWidgets.QVBoxLayout()
        leftLayout.addWidget(angle)
        leftLayout.addWidget(force)

        gridLayout = QtWidgets.QGridLayout()
        gridLayout.addWidget(quit, 0, 0)
        gridLayout.addLayout(topLayout, 0, 1)
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
