# PySide2 tutorial 3
# Widget使用

import sys
from PySide2.QtCore import Qt
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QApplication, QWidget, QPushButton


app = QApplication(sys.argv)

window = QWidget()
window.resize(400, 300)

quit = QPushButton("Quit", window)  # 设置Button附着于window上
quit.setFont(QFont("Times", 18, QFont.Bold))
quit.setGeometry(10, 20, 150, 40)
quit.resize(300,40)
# QtCore.QObject.connect(quit, QtCore.SIGNAL("clicked()"), app, QtCore.SLOT("quit()"))
quit.clicked.connect(app.quit)
window.show()
sys.exit(app.exec_())
