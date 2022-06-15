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

    # 判断字符串是否为空
    def is_null(self, str):
        if str == None or str == "":
            return True
        else:
            return False

    # 分割字符串取下标第三位和第四位
    def get_index(self, str):
        str_list = str.split('.')
        return str_list[2], str_list[3]

    # 16进制转10进制
    def hex_to_dec(self, hex_str):
        return int(hex_str, 16)

    # 16进制转2进制并打印出来
    def hex_to_bin(self, hex_str):
        return bin(int(hex_str, 16))[2:]

    # 截取字符串
    def sub_str(self, str, start, end):
        return str[start:end]

    # 定义一个字符串
    def str_test(self):
        str = "hello world"
        return str

    # 将接受到的数据存成字符串
    def str_to_list(self, str):
        str_list = str.split('.')
        return str_list



aa = bytearray.fromhex("a55a0501030280")
bb = bytearray.fromhex("a55a0501030200")
aaa = "a55a0501030280"

aav = Test_aa().sub_str(aaa, 7, 9)
print(aav)
