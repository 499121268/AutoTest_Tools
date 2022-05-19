from configparser import ConfigParser

class Test_aa():

    def te(self):
        conf = ConfigParser()
        conf.read('settings/port_date.ini')
        #opd = conf['date']['openLED']
        print(conf['date']['openLED'])


    def a(date):
        c=1
        a = 1+c
        return a

    def b(self):
        s=Test_aa().a()
        print(s)

    def Open_led(self):
        conf = ConfigParser()
        conf.read('settings/port_date.ini')
        opd = conf['date']['openLED']
        print(opd)
        return opd
        # conn_com.Communication.Send_data(opd)
    def sss(self):
        tt=Test_aa().Open_led()
        print(tt)

Test_aa().sss()