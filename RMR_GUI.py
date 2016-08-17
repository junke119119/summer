import sys
from PyQt4.QtCore import pyqtSlot
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 700)
        self.setWindowTitle("RMR Calculator")

        extractAction = QtGui.QAction("Quit", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Quit The App')
        extractAction.triggered.connect(self.close)

        self.statusBar()

        mainMenu = self.menuBar()

        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)

        self.home()

    def home(self):

        # Create textbox
        self.textbox = QtGui.QLineEdit(self)
        self.textbox.move(130,80)
        self.textbox.resize(300, 20)

        # Create a button in the window
        self.btn = QtGui.QPushButton("Select File", self)
        self.btn.clicked.connect(self.select_file)
        #btn.resize(btn.minimumSizeHint())
        self.btn.move(20,80)
        self.btn.resize(100,20)

        self.show()

    def select_file(self):
        fileName = QtGui.QFileDialog.getOpenFileName(self, 'Select File','*.xlsx')
        self.textbox.setText(fileName)
        print(fileName)


def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()     
