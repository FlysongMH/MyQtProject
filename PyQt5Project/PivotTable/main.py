import sys
from PyQt5.QtWidgets import QApplication
from PivotTable import PivotWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = PivotWindow()
    sys.exit(app.exec_())
