#!/usr/bin/env python
import time

DEBUG = True 


class temp_logger_parse(object):	








	 def __init__(self, arg, f):
		self.temp_c = ((((arg.analog[0] * 1200) / 1023) - 424) / 6.25)
		self.temp_f = ((self.temp_c * 9) / 5) + 32
		if DEBUG: print "Temperature = " +str(self.temp_f) + "F"

		self.rel_humidity = (((((arg.analog[2] * 1200) / 1023) / 431.19) / 3.326) - .16) / .0062
		self.act_humidity = self.rel_humidity / (1.0546 - .00216 * self.temp_c)
		if DEBUG: print "Humidity = %.2f" % self.act_humidity


		rightnow = time.strftime("%m/%d/%Y %H:%M:%S")
		f.write("%s , %.2f , %.2f\n" %(rightnow,self.temp_f,self.act_humidity))
		f.flush()


		return 






