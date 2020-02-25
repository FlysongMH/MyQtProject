import sys
from PyQt5.QtCore import * # PyQt5中的qDebug在此
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PivotTable import PivotWindow


if __name__ == '__main__':
    # APP settings
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))  # <- Choose the style

    # mainWindow settings
    win = PivotWindow()

    # system settings
    sys.exit(app.exec_())
