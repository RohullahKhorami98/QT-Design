from PyQt5 import QtWidgets, uic, QtCore
import sys


class Graphy(QtWidgets.QWidget):
    def __init__(self):
        super(Graphy, self).__init__()
        uic.loadUi('watcher.ui', self)
        self.setupUI()

    def setupUI(self):
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Graphy()
    window.show()
    sys.exit(app.exec_())
