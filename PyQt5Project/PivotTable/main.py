import sys
from PyQt5.QtWidgets import QApplication, QStyleFactory
from PivotWindow import PivotWindow

if __name__ == '__main__':
    # APP settings
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))  # <- Choose the style

    win = PivotWindow()  # create mainWindow
    win.show()  # show the main window

    # system settings
    sys.exit(app.exec_())


    pass
