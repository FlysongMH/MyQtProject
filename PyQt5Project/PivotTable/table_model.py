import pandas as pd
import numpy as np
from PyQt5.QtCore import Qt, QAbstractTableModel, QModelIndex, QVariant
from PyQt5.QtGui import QColor


class PandasModel(QAbstractTableModel):
    def __init__(self, df=pd.DataFrame()):
        QAbstractTableModel.__init__(self)
        self._df = df

    def rowCount(self, parent=QModelIndex()):
        return self._df.shape[0]

    def columnCount(self, parent=QModelIndex()):
        return self._df.shape[1]

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:  # 仅支持显示
            return QVariant()
        if orientation == Qt.Horizontal:  # show columns
            try:
                return self._df.columns[section]
            except (IndexError,):
                return QVariant()
        elif orientation == Qt.Vertical:  # show index
            try:
                return self._df.index[section]
            except (IndexError,):
                return QVariant()

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return QVariant()

        if role == Qt.DisplayRole:
            return str(self._df.iloc[index.row(), index.column()])
        # elif role == Qt.BackgroundRole:
        #     return QColor(Qt.white)
        # elif role == Qt.TextAlignmentRole:
        #     return Qt.AlignRight

        return None
