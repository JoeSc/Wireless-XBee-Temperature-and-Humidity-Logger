#!/usr/bin/env python
import array

DEBUG = True 
SERIAL = False

class xbee(object):
    PACKET_START= 0x7E
    MODEM_STATUS = 0x8A
    AT_COMMAND = 0X08
    AT_COMMAND_QUEUE = 0x09
    AT_COMMAND_RESPONSE = 0x88
    REMOTE_COMMAND_REQUEST = 0x97
    ZIGBEE_TRANSMIT_REQUTES = 0x10
    IO_DATA=0X92
    NODE_IDENTIFICATION_INDICATOR = 0x95
    
#-------------------------------------------------------------
    def find_packet(serial):
        test = serial.read(1)
        if test:
            if ord(test) == xbee.PACKET_START:
                lengthMSB = ord(serial.read(1))
                lengthLSB = ord(serial.read(1))
                length = lengthLSB + (lengthMSB<<8) + 1
                packet =serial.read(length)
                if DEBUG:
                    print "Packet was : ",
                    for c in packet : print "%X"%ord(c),
                    print
                return packet	
            else:
                if SERIAL:
                    serial.flushInput()
        return None
    find_packet = staticmethod(find_packet)
#-------------------------------------------------------------

    def send_cmd_local(serial,cmd):
        #writebuf=[chr(0x7e),chr(0x0),chr(0x04),chr(0x08),chr(0x01),chr(0x44),chr(0x42),chr(0x70)]
        #serial.write(writebuf)
        writebuf = chr(xbee.PACKET_START)
        writebuf += chr(0x00)
        writebuf += (chr(len(cmd)+2))
        writebuf += (chr(xbee.AT_COMMAND))
        writebuf += (chr(0x99))
        for i in cmd:
            writebuf += i
        checksum = 0x0
        for i in range(3,len(writebuf)):
            checksum += ord(writebuf[i])
        checksum &= 0xFF
        checksum = 0xFF - checksum
        writebuf += chr(checksum)
        serial.write(writebuf)

    send_cmd_local = staticmethod(send_cmd_local)
#-------------------------------------------------------------

    def __init__(self, arg):
        self.analog = [0 for x in range(8)]
        self.rssi = 9999
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


        elif self.packet_id == xbee.AT_COMMAND_RESPONSE:
            print "Got Command response"
            self.rssi = -p[5]
            print "RSSI = " + str(self.rssi)
            print ""

        else:
            print 'GOT BAD PACKET'
            print p
            print ""







