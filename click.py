from PyQt5.QtCore import QBasicTimer
from PyQt5.QtWidgets import QMainWindow

from MainWindow import Ui_MainWindow
from conn_com import Engine1


class Click(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.on_led)
        self.pushButton_2.clicked.connect(self.off_led)
        self.pushButton_3.clicked.connect(self.Door_open)
        self.pushButton_4.clicked.connect(self.Door_close)
        self.pushButton_5.clicked.connect(self.Z_motor_up)
        self.pushButton_6.clicked.connect(self.Z_motor_down)
        self.pushButton_7.clicked.connect(self.P_motor_up)
        self.pushButton_8.clicked.connect(self.P_motor_down)
        self.pushButton_9.clicked.connect(self.heat_on)
        self.pushButton_10.clicked.connect(self.heat_off)

        self.pv = 0
        self.pv_timer = QBasicTimer()
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(self.pv)
        self.pushButton_13.clicked.connect(self.auto_check)

        # Door_up
        # self.label.setVisible(True)
        # self.label_13.setVisible(False)

        # Door_down
        # self.label_8.setVisible(True)
        # self.label_14.setVisible(True)

        # Z_up
        # self.label_9.setVisible(True)
        # self.label_15.setVisible(False)

        # Z_down
        # self.label_10.setVisible(True)
        # self.label_16.setVisible(True)

        # P_up
        # self.label_11.setVisible(True)
        # self.label_17.setVisible(False)

        # P_down
        # self.label_12.setVisible(True)
        # self.label_18.setVisible(True)

    def on_led(self):
        self.sender()
        print("灯被打开了！")
        self.textBrowser.append("灯被打开了！")
        data = bytearray.fromhex("a55a050103028067b1")
        Engine1.Send_data(data)
        # self.pushButton_3.setVisible(False)

    def off_led(self):
        self.sender()
        print("灯被关闭了！")
        self.textBrowser.append("灯被关闭了！")
        data = bytearray.fromhex("a55a050103028067b0")
        Engine1.Send_data(data)
        # self.pushButton_3.setVisible(False)

    def Door_open(self):
        self.sender()
        print("门被打开了！")
        self.textBrowser.append("门被打开了！")
        data = bytearray.fromhex("a55a050103028067b2")
        Engine1.Send_data(data)
        self.label.setVisible(True)
        self.label_13.setVisible(True)
        # self.pushButton_3.setVisible(False)

    def Door_close(self):
        self.sender()
        print("门被关闭了！")
        self.textBrowser.append("门被关闭了！")
        data = bytearray.fromhex("a55a050103028067b3")
        Engine1.Send_data(data)
        # self.label_13.setVisible(True)
        self.label_8.setVisible(True)
        self.label_14.setVisible(True)
        # self.pushButton_3.setVisible(False)

    def Z_motor_up(self):
        self.sender()
        print("Z轴向上转动！")
        self.textBrowser.append("Z轴向上转动！")
        data = bytearray.fromhex("a55a050103028067b4")
        Engine1.Send_data(data)
        self.label_9.setVisible(True)
        self.label_15.setVisible(True)
        # self.pushButton_3.setVisible(False)

    def Z_motor_down(self):
        self.sender()
        print("Z轴向下转动！")
        self.textBrowser.append("Z轴向下转动！")
        data = bytearray.fromhex("a55a050103028067b5")
        Engine1.Send_data(data)
        self.label_10.setVisible(True)
        self.label_16.setVisible(True)
        # self.pushButton_3.setVisible(False)

    def P_motor_up(self):
        self.sender()
        print("P轴向上转动！")
        self.textBrowser.append("P轴向上转动！")
        data = bytearray.fromhex("a55a050103028067b6")
        Engine1.Send_data(data)
        self.label_11.setVisible(True)
        self.label_17.setVisible(True)
        # self.pushButton_3.setVisible(False)

    def P_motor_down(self):
        self.sender()
        print("P轴向下转动！")
        self.textBrowser.append("P轴向下转动！")
        data = bytearray.fromhex("a55a050103028067b7")
        Engine1.Send_data(data)
        self.label_12.setVisible(True)
        self.label_18.setVisible(True)
        # self.pushButton_3.setVisible(False)

    def heat_on(self):
        self.sender()
        print("加热被打开了！")
        self.textBrowser.append("加热被打开了！")
        data = bytearray.fromhex("a55a050103028067b8")
        Engine1.Send_data(data)
        # self.pushButton_3.setVisible(False)

    def heat_off(self):
        self.sender()
        print("加热被关闭了！")
        self.textBrowser.append("加热被关闭了！")
        data = bytearray.fromhex("a55a050103028067b9")
        Engine1.Send_data(data)
        # self.pushButton_3.setVisible(False)

    def auto_check(self):
        self.sender()
        self.textBrowser.append("自动检测开始！")
        self.textBrowser.append("请等待...")
        self.pv = 0
        if self.pv_timer.isActive():
            self.pv_timer.stop()
            print("开始自动检测！")
            data = bytearray.fromhex("a55a050103028067ba")
            Engine1.Send_data(data)
            # self.pushButton_3.setVisible(False)
        else:
            self.pv_timer.start(100, self)

    def timerEvent(self, e):
        if self.pv == 100:
            self.pv_timer.stop()
        else:
            self.pv += 1
            self.progressBar.setValue(self.pv)
