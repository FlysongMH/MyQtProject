import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_PivotWindow import Ui_Pivot


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QMainWindow()
    ui = Ui_Pivot()
    ui.setupUi(win)
    win.show()

    sys.exit(app.exec_())
