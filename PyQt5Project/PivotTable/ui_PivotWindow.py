# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_PivotWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Pivot(object):
    def setupUi(self, Pivot):
        Pivot.setObjectName("Pivot")
        Pivot.resize(1026, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Pivot.sizePolicy().hasHeightForWidth())
        Pivot.setSizePolicy(sizePolicy)
        Pivot.setMinimumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        Pivot.setFont(font)
        Pivot.setAcceptDrops(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ico/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Pivot.setWindowIcon(icon)
        self.centralWidget = QtWidgets.QWidget(Pivot)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setMinimumSize(QtCore.QSize(800, 500))
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget_5 = QtWidgets.QListWidget(self.centralWidget)
        self.listWidget_5.setObjectName("listWidget_5")
        self.verticalLayout.addWidget(self.listWidget_5)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidget = QtWidgets.QListWidget(self.centralWidget)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 0, 0, 1, 1)
        self.listWidget_3 = QtWidgets.QListWidget(self.centralWidget)
        self.listWidget_3.setObjectName("listWidget_3")
        self.gridLayout.addWidget(self.listWidget_3, 0, 1, 1, 1)
        self.listWidget_2 = QtWidgets.QListWidget(self.centralWidget)
        self.listWidget_2.setObjectName("listWidget_2")
        self.gridLayout.addWidget(self.listWidget_2, 1, 0, 1, 1)
        self.listWidget_4 = QtWidgets.QListWidget(self.centralWidget)
        self.listWidget_4.setObjectName("listWidget_4")
        self.gridLayout.addWidget(self.listWidget_4, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.tableWidget = QtWidgets.QTableWidget(self.centralWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.horizontalLayout.addWidget(self.tableWidget)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 5)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        Pivot.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(Pivot)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1026, 23))
        self.menuBar.setMinimumSize(QtCore.QSize(0, 23))
        self.menuBar.setAutoFillBackground(False)
        self.menuBar.setStyleSheet("background-color: rgb(239, 239, 239);\n"
"font: 75 9pt \"Microsoft YaHei UI\";")
        self.menuBar.setObjectName("menuBar")
        self.menumenu_A = QtWidgets.QMenu(self.menuBar)
        self.menumenu_A.setObjectName("menumenu_A")
        self.menumenu_B = QtWidgets.QMenu(self.menuBar)
        self.menumenu_B.setObjectName("menumenu_B")
        self.menumenu_C = QtWidgets.QMenu(self.menuBar)
        self.menumenu_C.setObjectName("menumenu_C")
        self.menumenu_D = QtWidgets.QMenu(self.menuBar)
        self.menumenu_D.setObjectName("menumenu_D")
        Pivot.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(Pivot)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainToolBar.sizePolicy().hasHeightForWidth())
        self.mainToolBar.setSizePolicy(sizePolicy)
        self.mainToolBar.setMinimumSize(QtCore.QSize(0, 23))
        self.mainToolBar.setObjectName("mainToolBar")
        Pivot.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(Pivot)
        self.statusBar.setObjectName("statusBar")
        Pivot.setStatusBar(self.statusBar)
        self.actiontool_A = QtWidgets.QAction(Pivot)
        self.actiontool_A.setObjectName("actiontool_A")
        self.actiontool_B = QtWidgets.QAction(Pivot)
        self.actiontool_B.setObjectName("actiontool_B")
        self.actiontool_C = QtWidgets.QAction(Pivot)
        self.actiontool_C.setObjectName("actiontool_C")
        self.actiontool_D = QtWidgets.QAction(Pivot)
        self.actiontool_D.setObjectName("actiontool_D")
        self.actiontool_A_2 = QtWidgets.QAction(Pivot)
        self.actiontool_A_2.setObjectName("actiontool_A_2")
        self.actiontool_B_2 = QtWidgets.QAction(Pivot)
        self.actiontool_B_2.setObjectName("actiontool_B_2")
        self.actiontool_import = QtWidgets.QAction(Pivot)
        self.actiontool_import.setObjectName("actiontool_import")
        self.actiontool_label = QtWidgets.QAction(Pivot)
        self.actiontool_label.setObjectName("actiontool_label")
        self.actionmenu_A1 = QtWidgets.QAction(Pivot)
        self.actionmenu_A1.setObjectName("actionmenu_A1")
        self.actionmenu_A2 = QtWidgets.QAction(Pivot)
        self.actionmenu_A2.setObjectName("actionmenu_A2")
        self.actionmenu_A3 = QtWidgets.QAction(Pivot)
        self.actionmenu_A3.setObjectName("actionmenu_A3")
        self.menumenu_A.addAction(self.actionmenu_A1)
        self.menumenu_A.addAction(self.actionmenu_A2)
        self.menumenu_A.addAction(self.actionmenu_A3)
        self.menuBar.addAction(self.menumenu_A.menuAction())
        self.menuBar.addAction(self.menumenu_B.menuAction())
        self.menuBar.addAction(self.menumenu_C.menuAction())
        self.menuBar.addAction(self.menumenu_D.menuAction())
        self.mainToolBar.addAction(self.actiontool_A)
        self.mainToolBar.addAction(self.actiontool_B)
        self.mainToolBar.addAction(self.actiontool_C)
        self.mainToolBar.addAction(self.actiontool_D)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actiontool_A_2)
        self.mainToolBar.addAction(self.actiontool_B_2)
        self.mainToolBar.addAction(self.actiontool_import)
        self.mainToolBar.addAction(self.actiontool_label)

        self.retranslateUi(Pivot)
        QtCore.QMetaObject.connectSlotsByName(Pivot)

    def retranslateUi(self, Pivot):
        _translate = QtCore.QCoreApplication.translate
        Pivot.setWindowTitle(_translate("Pivot", "Pivot Window"))
        self.menumenu_A.setTitle(_translate("Pivot", "menu_A"))
        self.menumenu_B.setTitle(_translate("Pivot", "menu_B"))
        self.menumenu_C.setTitle(_translate("Pivot", "menu_C"))
        self.menumenu_D.setTitle(_translate("Pivot", "menu_D"))
        self.actiontool_A.setText(_translate("Pivot", "tool_A"))
        self.actiontool_A.setToolTip(_translate("Pivot", "tool_A"))
        self.actiontool_B.setText(_translate("Pivot", "tool_B"))
        self.actiontool_B.setToolTip(_translate("Pivot", "tool_B"))
        self.actiontool_C.setText(_translate("Pivot", "tool_C"))
        self.actiontool_C.setToolTip(_translate("Pivot", "tool_C"))
        self.actiontool_D.setText(_translate("Pivot", "tool_D"))
        self.actiontool_D.setToolTip(_translate("Pivot", "tool_D"))
        self.actiontool_A_2.setText(_translate("Pivot", "tool_A"))
        self.actiontool_A_2.setToolTip(_translate("Pivot", "tool_A"))
        self.actiontool_B_2.setText(_translate("Pivot", "tool_B"))
        self.actiontool_B_2.setToolTip(_translate("Pivot", "tool_B"))
        self.actiontool_import.setText(_translate("Pivot", "import"))
        self.actiontool_import.setToolTip(_translate("Pivot", "import"))
        self.actiontool_label.setText(_translate("Pivot", "actiontool_label"))
        self.actiontool_label.setToolTip(_translate("Pivot", "actiontool_label"))
        self.actionmenu_A1.setText(_translate("Pivot", "menu_A1"))
        self.actionmenu_A2.setText(_translate("Pivot", "menu_A2"))
        self.actionmenu_A3.setText(_translate("Pivot", "menu_A3"))
