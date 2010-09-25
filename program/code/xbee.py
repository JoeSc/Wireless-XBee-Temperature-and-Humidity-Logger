#!/usr/bin/env python
import array

DEBUG = False 

class xbee(object):
	PACKET_START 	= 0x7E
	MODEM_STATUS 	= 0x8A
	AT_COMMAND 		= 0X08
	IO_DATA			= 0X92

	def find_packet(serial):
		test = serial.read()
		if test:
			if ord(test) == xbee.PACKET_START:
				lengthMSB = ord(serial.read())
				lengthLSB = ord(serial.read())
				length = lengthLSB + (lengthMSB<<8) + 1
				packet =serial.read(length)
				if DEBUG:
					print "Packet was : ",
					for c in packet : print "%X"%ord(c),
					print
				return packet	
			else:
				serial.flushInput()
				return None
		else:
			return None

	find_packet = staticmethod(find_packet)

	def send_cmd_remote(serial,cmd):
		#print "DOESNT WORK YET"	
		writebuf=[chr(0x7e),chr(0x0),chr(0x04),chr(0x08),chr(0x01),chr(0x44),chr(0x42),chr(0x70)]
		serial.write(writebuf)




	send_cmd_remote = staticmethod(send_cmd_remote)

	def __init__(self, arg):
		self.analog = [0 for x in range(8)]
		self.init_with_packet(arg)

	def init_with_packet(self,p):
		p = [ord(c) for c in p]
		checksum = 0
		for c in p: checksum += c
		if (checksum & 0xFF) != 0xFF:
			return None
		self.packet_id = p[0]

		if self.packet_id == xbee.IO_DATA:
			self.addr_16 = (p[9] << 8) + p[10]
			print "addr_16 = " + str(self.addr_16)
			self.receive_opt = p[11]
			self.num_samples = p[12]
			self.digital_channel_mask = (p[13]<<8) + p[14]
			self.analog_channel_mask = p[15]
			cnt = 16
			if self.digital_channel_mask != 0:
				self.digital_sample = (p[cnt]<<8) + p[cnt+1]
				cnt += 2

			print "length of array",
			print len(p)
			if self.analog_channel_mask & 0x01:
				self.analog[0] = (p[cnt]<<8) + p[cnt+1]
				cnt += 2
				if DEBUG: print "AD0 = " + hex(self.analog[0])

			if self.analog_channel_mask & 0x02:
				self.analog[1] = (p[cnt]<<8) + p[cnt+1]
				cnt += 2
				if DEBUG: print "AD1 = " + hex(self.analog[1])
				
			if self.analog_channel_mask & 0x04:
				self.analog[2] = (p[cnt]<<8) + p[cnt+1]
				cnt += 2
				if DEBUG: print "AD2 = " + hex(self.analog[2])
				
			if self.analog_channel_mask & 0x08:
				self.analog[3] = (p[cnt]<<8) + p[cnt+1]
				cnt += 2
				if DEBUG: print "AD3 = " + hex(self.analog[3])
				
			if self.analog_channel_mask & 0x80:
				self.supply_voltage =  (p[cnt]<<8) + p[cnt+1]
				cnt += 2
				if DEBUG: print "Vcc = " + hex(self.supply_voltage)
			


		else:
			print 'GOT BAD PACKET'







