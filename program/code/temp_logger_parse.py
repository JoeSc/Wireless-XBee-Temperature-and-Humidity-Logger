#!/usr/bin/env python
import time
#import rrdtool
import os
DEBUG = True 


class temp_logger_parse(object):	

    def __init__(self, arg, f):
        self.temp_c = ((((arg.analog[0] * 1200) / 1023) - 424) / 6.25)
        self.temp_f = ((self.temp_c * 9) / 5) + 32
        if DEBUG: print "Temperature = " +str(self.temp_f) + "F"
        if DEBUG: print "RAW TEMP = " + str(arg.analog[0])

        self.rel_humidity = (((((arg.analog[2] * 1200) / 1023) / 431.19) / 3.326) - .16) / .0062
        self.act_humidity = self.rel_humidity / (1.0546 - .00216 * self.temp_c)
        if DEBUG: print "humidity Voltage = %.2f" % (arg.analog[2] * 1.2 / 1023)
        if DEBUG: print "rel Humidity = %.2f" % self.rel_humidity
        if DEBUG: print "act Humidity = %.2f" % self.act_humidity

        self.supply_voltage = ((arg.supply_voltage * 1.2) /1023)
        if DEBUG: print "Supply Voltage = %.2f" % self.supply_voltage

        self.rssi = 0

        rightnow = time.strftime("%m/%d/%Y %H:%M:%S")
        f.write("%s , %.2f , %.2f\n" %(rightnow,self.temp_f,self.act_humidity))
        f.flush()

        #print "NOT LOGGING TO RRD"
        #rrdtool.update('/home/joe/templogger/Wireless-XBee-Temperature-and-Humidity-Logger/program/database/crawlspace.rrd',"N:%.2f:%.2f:%.2f:NaN" %(self.temp_f,self.act_humidity,self.supply_voltage));

        #print "HELLASDLASDLASDLASDLADSLADAS"
        os.system("rrdtool update ../database/crawlspace.rrd N:%.2f:%.2f:%.2f:NaN" %(self.temp_f,self.act_humidity,self.supply_voltage))


        return 






