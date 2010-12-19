#!/usr/bin/env python

import serial
import array
from xbee import xbee
from temp_logger_parse import temp_logger_parse
import sys
TEMPLOGGER1_ADDR_16 = 1

SERIALPORT = "/dev/ttyUSB0"
BAUDRATE = 9600

FILENAME = "test.csv"







ser = serial.Serial(SERIALPORT, BAUDRATE, timeout=1)
ser.open()
f = open(FILENAME, 'a')

def do_stuff(nothing):
	packet = xbee.find_packet(ser)
	if not packet:
		return
	xb = xbee(packet)
	if xb.packet_id == xbee.IO_DATA:
		print xb.addr_16
		if xb.addr_16 == TEMPLOGGER1_ADDR_16:
			temp =temp_logger_parse(xb,f)
			#xbee.send_cmd_remote(ser,"db")	
			#packet = xbee.find_packet(ser)







try:
	while True:
		do_stuff(None)
except KeyboardInterrupt:
	print 'Interrupted'
	exit()
		

print 'done'


