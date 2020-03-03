from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QFileDialog
from ui_PivotWindow import Ui_Pivot
import os

class PivotWindow(QMainWindow):
    # 自动初始化PivotWindow对象
    def __init__(self):
        super().__init__()   # 执行父类QMainWindow的初始化方法
        # ui初始化, 新建一个成员ui
        self.ui = Ui_Pivot()
        self.ui.setupUi(self)

        # 窗口居中
        qr = self.frameGeometry()  # 获得主窗口所在的框架。
        cp = QDesktopWidget().availableGeometry().center()  # 获取显示器的分辨率，然后得到屏幕中间点的位置。
        qr.moveCenter(cp)  # 把主窗口框架的中心点放置到屏幕的中心位置。
        self.move(qr.topLeft())  # 通过move函数把主窗口的左上角移动到其框架的左上角，这样就把窗口居中了。

        # 其他初始化
        self.init()

    def init(self):
        self.cwd = os.getcwd()
        # signal and slot
        self.ui.actiontool_label.triggered.connect(self.show_label)
        self.ui.actiontool_import.triggered.connect(self.import_data)


    def show_label(self):
        self.label = QLabel("This is QLabel")
        self.label.show()

    def import_data(self):
        self.import_dialog = QFileDialog()
        files, filetype = QFileDialog.getOpenFileNames(self, "多文件选择", self.cwd,
                                                       "All Files (*);;csv Files (*.csv);;Text Files (*.txt)")
        if len(files)==0:
            print("\n您已取消选择")
            return
        print("\n你选择的文件为:")
        for file in files:
            print(file)
        print("文件筛选器类型：", filetype)
