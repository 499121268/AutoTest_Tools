import conn_com
from configparser import ConfigParser

class Auto_opert():

    def con_port(self):
        conn_com.Communication.__name__("/dev/ttys0", 115200, timeout=0.5)
        conn_com.Communication.Open_Port()
        conn_com.Communication.Print_Port()

    def Open_led(self):
        conf=ConfigParser()
        conf.read('E:\AutoTest_Tools\settings\port_date.ini')
        opd=conf['date']['openLED']
        #print(opd)
        #conn_com.Communication.Send_data(opd)


Auto_opert().Open_led()
