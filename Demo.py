import threading
from configparser import ConfigParser


class Test_aa():

    def te(self):
        conf = ConfigParser()
        conf.read('settings/port_date.ini')
        # opd = conf['date']['openLED']
        print(conf['date']['openLED'])

    def a(date):
        c = 1
        a = 1 + c
        return a

    def b(self):
        s = Test_aa().a()
        print(s)

    def Open_led(self):
        conf = ConfigParser()
        conf.read('E:\AutoTest_Tools\settings\port_date.ini')
        opd = conf['date']['openLED']
        print(opd)
        return opd
        # conn_com.Communication.Send_data(opd)

    # if __name__=='__main__':
    #     t1 = threading.Thread(target=Open_led,args=('t1',))
    #     t2 = threading.Thread(target=Open_led, args=('t2',))
    #     t1.start()

    # Xmodem CRC 计算
    def crc16(self, data):
        crc = 0x0000
        for i in range(len(data)):
            crc = crc ^ (data[i] << 8)
            for j in range(8):
                if (crc & 0x8000) != 0:
                    crc = (crc << 1) ^ 0x1021
                else:
                    crc = crc << 1
        print(crc)
        return crc & 0xffff

    # 九九乘法表



aa = bytearray.fromhex("a55a0501030280")
bb = bytearray.fromhex("a55a0501030200")

Test_aa().crc16(bb)
