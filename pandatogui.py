import sqlite3
import sys
from PyQt5 import QtCore, QtGui
import pandas as pd

import sys
from PyQt5.QtWidgets import QTableView, QMainWindow, QLabel, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtCore import *
from PyQt5.QtGui import *


Qt = QtCore.Qt

class PandasModel(QtCore.QAbstractTableModel):
    def __init__(self, data, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data.values)

    def columnCount(self, parent=None):
        return self._data.columns.size

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return QtCore.QVariant(str(
                    self._data.values[index.row()][index.column()]))
        return QtCore.QVariant()

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self._data.columns[col]
        return None


if __name__ == '__main__':

    conn = sqlite3.connect('database/database.db')
    print("opened database successfully")
    cursor = conn.execute("SELECT sessionid, date, query, positive, negative from MiningReport;")

    data = []
        
    for row in cursor:
        datarow = [row[0],row[1],row[2],row[3],row[4]]
        data.append(datarow)
        df = pd.DataFrame(data,columns=['Session ID','Date','Keyword/Query','Positive%','Negative%'])

    application = QApplication(sys.argv)
    
    view = QTableView()
    model = PandasModel(df)
    view.setModel(model)
        
    view.setGeometry(30,60,520,300)

    view.show()

    conn.close()
    sys.exit(application.exec_())
