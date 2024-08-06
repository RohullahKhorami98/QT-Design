import sys
from PyQt5 import QtWidgets, uic, QtCore
class MyButtons(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyButtons, self).__init__()
        uic.loadUi('buttons.ui', self)
        self.setupUI()

    def setupUI(self):
        self.pushButton.clicked.connect(self.on_click)
        self.clearButton.clicked.connect(self.on_clear)
        self.exitButton.clicked.connect(self.on_close)

    def on_click(self):
        self.label.setText("Button was clicked!")

    def on_clear(self):
        self.label.setText("")
    
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