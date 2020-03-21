#############################################################################
##
## Copyright (C) 2019 The Qt Company Ltd.
## Contact: http://www.qt.io/licensing/
##
## This file is part of the Qt for Python examples of the Qt Toolkit.
##
## $QT_BEGIN_LICENSE:BSD$
## You may use this file under the terms of the BSD license as follows:
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are
## met:
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above copyright
##     notice, this list of conditions and the following disclaimer in
##     the documentation and/or other materials provided with the
##     distribution.
##   * Neither the name of The Qt Company Ltd nor the names of its
##     contributors may be used to endorse or promote products derived
##     from this software without specific prior written permission.
##
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
##
## $QT_END_LICENSE$
##
#############################################################################
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import *
from PyQt5.QtChart import *

class Widget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.items = 0

        # Examples data
        self._data = {"Water": 24.5,
                      "Electricity": 55.1,
                      "Rent": 850.0,
                      "Supermarket": 230.4,
                      "Internet": 29.99,
                      "Bars": 21.85,
                      "Public transportation": 60.0,
                      "Coffee": 22.45,
                      "Restaurants": 120}

        # Left
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Description", "Price"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Right
        self.description = QLineEdit()
        self.price = QLineEdit()
        self.add = QPushButton("Add")
        self.plot = QPushButton("Plot")
        self.clear = QPushButton("Clear")
        self.quit = QPushButton("Quit")
        self.chart_view = QChartView()
        self.chart_view.setRenderHint(QPainter.Antialiasing)  ##
        self.add.setEnabled(False)

        # 右侧采用纵向布局
        self.right = QVBoxLayout()
        # self.right.setMargin(10)  # PyQt5: 'QVBoxLayout' object has no attribute 'setMargin'
        self.right.addWidget(QLabel("Description"))
        self.right.addWidget(self.description)
        self.right.addWidget(QLabel("Price"))
        self.right.addWidget(self.price)
        self.right.addWidget(self.add)
        self.right.addWidget(self.plot)
        self.right.addWidget(self.chart_view)
        self.right.addWidget(self.clear)
        self.right.addWidget(self.quit)

        # QWidget整体横向布局
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.table)
        self.layout.addLayout(self.right)

        self.setLayout(self.layout)

        # Signals and Slots
        self.description.textChanged[str].connect(self.check_disable)
        self.price.textChanged[str].connect(self.check_disable)
        self.add.clicked.connect(self.add_element)
        self.plot.clicked.connect(self.plot_data)
        self.clear.clicked.connect(self.clear_table)
        self.quit.clicked.connect(self.quit_application)
        # fill example data
        self.fill_table()

    def check_disable(self):
        # "Add"按钮有效性检查
        if not self.description.text() or not self.price.text():
            self.add.setEnabled(False)
        else:
            self.add.setEnabled(True)

    def add_element(self):
        # 插入一行
        des = self.description.text()
        price = self.price.text()

        self.table.insertRow(self.items)
        des_item = QTableWidgetItem(des)   # text
        price_item = QTableWidgetItem("{:.2f}".format(float(price)))  # number
        price_item.setTextAlignment(Qt.AlignRight)
        self.table.setItem(self.items, 0, des_item)
        self.table.setItem(self.items, 1, price_item)
        self.items += 1

        self.description.setText("")
        self.price.setText("")



    def plot_data(self):
        series = QPieSeries()
        for i in range(self.table.rowCount()):
            text = self.table.item(i, 0).text()
            number = float(self.table.item(i, 1).text())
            series.append(text, number)
        self.chart = QChart()
        self.chart.addSeries(series)
        self.chart.legend().setAlignment(Qt.AlignLeft)
        self.chart_view.setChart(self.chart)

    def clear_table(self):
        self.table.setRowCount(0)
        self.items = 0

    def quit_application(self):
        QApplication.quit()

    def fill_table(self):
        data = self._data
        for des, price in data.items():
            self.table.insertRow(self.items)
            des_item = QTableWidgetItem(des)  # text
            price_item = QTableWidgetItem("{:.2f}".format(float(price)))  # number
            price_item.setTextAlignment(Qt.AlignRight)
            self.table.setItem(self.items, 0, des_item)
            self.table.setItem(self.items, 1, price_item)
            self.items += 1

class MainWindow(QMainWindow):
    def __init__(self, widget=None):
        QMainWindow.__init__(self)
        self.setWindowTitle("Tutorial")

        # Menu
        self.menu = self.menuBar()
        self.file_menu = self.menuBar().addMenu("File")

        # Exit QAction
        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.exit_app)

        self.file_menu.addAction(exit_action)
        self.setCentralWidget(widget)

    def exit_app(self, checked):
        QApplication.quit()


if __name__ == '__main__':
    # Qt Application
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))  # <- Choose the style

    widget = Widget()
    window = MainWindow(widget)
    window.resize(800, 600)
    window.show()

    # Execute application
    sys.exit(app.exec())
