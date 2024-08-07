import sys
from PyQt5 import QtWidgets, uic, QtCore
from datetime import datetime

class MyButtons(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyButtons, self).__init__()
        uic.loadUi('clock.ui', self)
        self.setupUI()

    def setupUI(self):
        self.pushButton.clicked.connect(self.start_timer)
        self.exitButton.clicked.connect(self.on_close)
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_time)

    def start_timer(self):
        self.timer.start(1000)  

    def update_time(self):
        times = datetime.now()
        convertedTime = times.strftime("%d-%m-%Y %H:%M:%S")
        self.label.setText(str(convertedTime))

    def on_close(self):
        reply = QtWidgets.QMessageBox.question(self, 'Message',
                                               "Are you sure to quit?",
                                               QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            self.close()
        else:
            pass

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyButtons()
    window.show()
    sys.exit(app.exec_())
