import sys
import threading
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QHBoxLayout, QWidget

import Demo
import auto_operation
import conn_com
from configparser import ConfigParser

class MainWind(QMainWindow):
    def __init__(self,parent=None):
        super(MainWind,self).__init__(parent)
        self.setWindowTitle("Test")
        self.resize(714, 443)
        self.button1=QPushButton("Test")
        self.button1.clicked.connect(self.on_Click1)
        layout = QHBoxLayout()
        layout.addWidget(self.button1)
        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

    def con_port(self):
        conn_com.Communication.__name__("/dev/ttys0", 115200, timeout=0.5)
        conn_com.Communication.Open_Port()
        conn_com.Communication.Print_Port()

    # def Open_led(self):
    #     conf = ConfigParser()
    #     conf.read('E:\AutoTest_Tools\settings\port_date.ini')
    #     opd = conf['date']['openLED']
    #     print(opd)
    #     return opd
    #     # conn_com.Communication.Send_data(opd)

    def on_Click1(self,conf):
        self.sender()
        # if __name__ == '__main__':
        #     conf
        #print("sss")
        #线程操作
        # t3 = threading.Thread(target=self.Open_led, args=('t3',))
        # t3.start()

        #self.Open_led()
        auto_operation.Auto_opert.Open_led(self)
        app = QApplication.instance()
        #app.quit()


if __name__=='__main__':
    app=QApplication(sys.argv)
    main=MainWind()
    main.show()
    sys.exit(app.exec_())




