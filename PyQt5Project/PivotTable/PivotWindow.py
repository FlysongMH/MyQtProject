import pandas as pd
import numpy as np
import os
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QFileDialog
from PyQt5 import QtChart
from ui_PivotWindow import Ui_Pivot
from table_model import PandasModel


class PivotWindow(QMainWindow):
    # 自动初始化PivotWindow对象
    def __init__(self):
        super().__init__()  # 执行父类QMainWindow的初始化方法
        # 其他初始化
        self.init_ui()
        self.init_var()
        self.init_slot()

    def init_ui(self):
        # ui初始化, 新建一个成员ui
        self.ui = Ui_Pivot()
        self.ui.setupUi(self)
        self.ui_moveCenter(self)

    def init_var(self):
        self.cwd = os.getcwd()
        self.data_isValid = False
        self.dataList = []

    def init_slot(self):
        # signal and slot
        self.ui.actiontool_label.triggered.connect(self.slot_show_label)
        self.ui.actiontool_import.triggered.connect(self.slot_import_data)

    def ui_moveCenter(self, window):
        # 窗口居中
        qr = window.frameGeometry()  # 获得主窗口所在的框架。
        cp = QDesktopWidget().availableGeometry().center()  # 获取显示器的分辨率，然后得到屏幕中间点的位置。
        qr.moveCenter(cp)  # 把主窗口框架的中心点放置到屏幕的中心位置。
        window.move(qr.topLeft())  # 通过move函数把主窗口的左上角移动到其框架的左上角，这样就把窗口居中了。

    def slot_show_label(self):
        self.label = QLabel("This is QLabel")
        self.label.show()

    def slot_import_data(self):
        # 打开多个文件，返回两个参数：文件路径列表和文件筛选器结果
        files, filetype = QFileDialog.getOpenFileNames(self, "多文件选择", self.cwd,
                                                       "All Files (*);;csv Files (*.csv);;Text Files (*.txt)")
        if len(files) == 0:
            print("\n您已取消选择.")
            return
        print("\n你选择的文件为:")
        for file in files:
            print(file)
        print("文件筛选器类型：", filetype)
        # files=[r"F:\Qt5Project\MyQtProject\PyQt5Project\PivotTable\TestData.csv"]
        # 导入数据
        for file in files:
            if (file.endswith(".csv")):
                temp = pd.read_csv(file)
                print('data.shape:', temp.shape)
                print('data.index:', temp.index)
                print('data.columns:', temp.columns)
                self.dataList.append(temp)
                self.data_isValid = True
                break
        self.reset_model()

    def reset_model(self):
        self.model = PandasModel(self.dataList[0])
        self.ui.tableView.setModel(self.model)
        print('reset model success!')
        self.show_chart(col='depth')

    def show_chart(self, col):
        '''
        1.QChartView : 是一个可以显示图表（chart）的独立部件。
        2.QChart : 用于创建图表。
        3.series : 被词典翻译为 串联;级数;系列，连续; 这里我理解为存储的一系列坐标；
        4.QValueAxis : 继承自QAbstractAxis,用于对坐标轴进行操作。
        流程: 坐标附加到series然后使用addSeries方法把series载入ChartView。
        '''
        if not self.data_isValid:
            return

        # creating LineSeries
        data = self.dataList[0]
        len = data.shape[0]
        series = QtChart.QLineSeries()
        series.setName(col)
        for idx in data.index:
            series.append(idx, data.loc[idx,col])
        print(data.index.min(), data.index.max())

        # define x/y axis
        x_axis = QtChart.QValueAxis()
        x_axis.setRange(data.index.min(), data.index.max())
        x_axis.setLabelFormat("%0.1f")  # 设置坐标轴的显示方式，精确到小数点后1位
        x_axis.setTickCount(len)
        x_axis.setMinorTickCount(1)  # 设置每个单元格有几个小的分级

        y_axis = QtChart.QValueAxis()
        y_axis.setRange(data[col].min(), data[col].max())
        y_axis.setLabelFormat("%0.2f")  # 设置坐标轴的显示方式，精确到小数点后2位
        y_axis.setTickCount(10)
        y_axis.setMinorTickCount(0)  # 设置每个单元格有几个小的分级

        # Creating QChartQview
        self.chartView = QtChart.QChartView()
        self.chartView.resize(800,600)
        self.ui_moveCenter(self.chartView)
        chart = QtChart.QChart()
        chart.addSeries(series)
        chart.setAxisX(x_axis)  # 设置x轴属性
        chart.setAxisY(y_axis)  # 设置y轴属性
        # chart.createDefaultAxes() # 使用默认坐标系
        chart.setTitle("数据列显示：%s" % col)  # 设置标题
        self.chartView.setChart(chart)
        self.chartView.show()




