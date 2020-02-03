from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget
from ui_PivotWindow import Ui_Pivot
import sys


class PivotWindow(QMainWindow):
    def __init__(self):
        super().__init__()   # 执行父类的初始化方法
        self.init()  # 执行初始化
        # show the main window
        self.show()

    def init(self):
        # 调用UI工具初始化窗口
        ui = Ui_Pivot()
        ui.setupUi(self)

        # 窗口居中
        qr = self.frameGeometry()  # 获得主窗口所在的框架。
        cp = QDesktopWidget().availableGeometry().center()  # 获取显示器的分辨率，然后得到屏幕中间点的位置。
        qr.moveCenter(cp)  # 把主窗口框架的中心点放置到屏幕的中心位置。
        self.move(qr.topLeft())  # 通过move函数把主窗口的左上角移动到其框架的左上角，这样就把窗口居中了。


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pivotWindow = PivotWindow()
    sys.exit(app.exec_())
