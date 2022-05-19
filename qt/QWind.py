import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QHBoxLayout, QWidget
from PyQt5.QtGui import QIcon
import conn_com
from configparser import ConfigParser


class MainWind(QMainWindow):
    def __init__(self,parent=None):
        super(MainWind,self).__init__(parent)
        self.setWindowTitle("Test")
        self.resize(714, 443)
        self.button1=QPushButton("Test")
        self.button1.clicked.connect(self.on_Click)
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
    #     conf.read('settings/port_date.ini')
    #     opd = conf['date']['openLED']
    #     print(opd)
    #     return opd
    #     # conn_com.Communication.Send_data(opd)

    def on_Click(self,conf):
        self.sender()
        if __name__ == '__main__':
            conf
        print("sss")
        ss=Tools().Open_led()
        print("2")
        print(ss)
        #MainWind.instance()



if __name__=='__main__':
    app=QApplication(sys.argv)
    main=MainWind()
    main.show()
    sys.exit(app.exec_())


class Tools():

    def Open_led(self):
        conf = ConfigParser()
        conf.read('settings/port_date.ini')
        opd = conf['date']['openLED']
        print(opd)
        return opd
        # conn_com.Communication.Send_data(opd)