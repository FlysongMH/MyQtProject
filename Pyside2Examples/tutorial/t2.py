# PySide2 tutorial 2
# 信号和槽的使用

import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QApplication


app = QApplication(sys.argv)

quit = QtWidgets.QPushButton("Quit")
quit.resize(400, 50)
quit.setFont(QtGui.QFont("微软雅黑", 22, QtGui.QFont.Bold))  # 设置字体
# QtCore.QObject.connect(quit, QtCore.SIGNAL("clicked()"), app, QtCore.SLOT("quit()"))
quit.clicked.connect(app.quit)  # 新式写法，注意无参数的函数不要带括号
quit.show()
sys.exit(app.exec_())