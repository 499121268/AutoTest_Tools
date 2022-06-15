import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from MainWindow import Ui_MainWindow
from click import Click

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Click()
    # ui.setupUi(mainWindow)
    # mainWindow.show()
    ui.show()
    sys.exit(app.exec_())
