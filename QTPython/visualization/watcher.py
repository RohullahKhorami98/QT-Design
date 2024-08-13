from PyQt5 import QtWidgets, uic, QtCore, QtGui
import sys
import os
import pandas as pd

class PandasModel(QtCore.QAbstractTableModel):
    def __init__(self, df=pd.DataFrame(), parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._dataframe = df

    def rowCount(self, parent=None):
        counts = len(self._dataframe.index)
        return counts
    
    def columnCount(self, parent=None):
        counts = len(self._dataframe.columns)
        return counts
    
    def data(self, index, role=QtCore.Qt.DisplayRole):
        if not index.isValid():
            return None
        if role == QtCore.Qt.DisplayRole:
            return str(self._dataframe.iloc[index.row(), index.column()])
        return None
    

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return self._dataframe.columns[section]
            if orientation == QtCore.Qt.Vertical:
                return self._dataframe.index[section]
        return None

class Graphy(QtWidgets.QWidget):
    def __init__(self):
        super(Graphy, self).__init__()
        uic.loadUi('watcher.ui', self)
        self.setupUI()

    def setupUI(self):
        self.show()
        self.openButton.clicked.connect(self.openFile)

    def openFile(self):
        default_dir = ""
        if sys.platform == 'win32' or sys.platform == 'win64':
            default_dir = "C:\\"
        elif sys.platform == "darwin":
            default_dir = os.path.expanduser("~/Documents")
        else:
            default_dir = os.path.expanduser("~")
        
        self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', 
            default_dir, 'CSV files (*.csv)')
        
        if self.fileName:
            df = pd.read_csv(self.fileName)
            self.loadCsvData(df)
            

    def loadCsvData(self, df):
        model = PandasModel(df)
        self.dataFrameTable.setModel(model)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Graphy()
    window.show()
    sys.exit(app.exec_())
