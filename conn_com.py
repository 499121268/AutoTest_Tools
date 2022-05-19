import serial
import serial.tools.list_ports
from configparser import ConfigParser

class Communication():
    #初始化
    def __name__(self,com,bps,timeout):
        self.port = com
        self.bps = bps
        self.timeout = timeout
        global Ret
        try:
            self.ser = serial.Serial(self.port,self.bps,timeout=self.timeout)
            if  (self.ser.is_open):
                Ret = True
        except  Exception as e:
            print("------串口打开异常------",e)

# ser=serial.Serial("/dev/ttys0",115200,timeout=0.5) #Linux系统
# ser=serial.Serial("COM1",115200,timeout=0.5)    #Windows系统

    #打印设备基本信息
    def Print_Port(self):
        print("串口连接成功")
        print(self.ser.name)

    #打开串口
    def Open_Port(self):
        self.ser.open()

    #关闭串口
    def Close_Port(self):
        self.ser.close()
        print(self.ser.is_open)

    #发送数据
    def Send_data(self,data):
        self.ser.write(data)