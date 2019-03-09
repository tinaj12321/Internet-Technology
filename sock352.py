import binascii
import socket as syssock
import threading
import struct
import sys

# Flags
SOCK352_SYN = 0x01          # initiate connection
SOCK352_FIN = 0x02          # end connection
SOCK352_ACK = 0x04          # ack number
SOCK352_RESET = 0x08        # reset the connection
SOECK352_HAS_OPT = 0xA0     # option field is valid

sock352PktHdrData = '!BBBBHHLLQQLL'
# these functions are global to the class and
# define the UDP ports all messages are sent
# and received from

def init(UDPportTx,UDPportRx):   # initialize your UDP socket here
	if UDPportRx == 0:
		UDPportRx = 42069
	if UDPportTx == 0:
		UDPportTx = 42069
	pass 
    
class socket:
	def __init__(self):  # fill in your code here 
		self.socket = syssock.socket(syssock.AF_INET, syssock.SOCK_DGRAM)
		self.udpPkt_hdr_data = struct.Struct(sock352PktHdrData)  # returns struct obj, R/W binary data according to the given format

        return

def bind(self,address):


        return

def connect(self,address):  # fill in your code here
	
	
	
	
        version = 0x1       # Part 1
        flags = 0           # Part 1
        opt_ptr = 0
        protocol = 0
        header_len = 0
        checksum = 0
        source_port = 0
        dest_port = 0
        seq_no = 0          # Part 1
        ack_no = 0          # Part 1
        window = 0
        payload_len = 0     # Part 1
        header_len = struct.calcsize(sock352PktHdrData)
        header = self.udpPkt_hdr_data.pack(version, flags, opt_ptr, protocol, header_len, checksum,
                                         source_port, dest_port, seq_no, ack_no, window, payload_len)

	self.bind(self, int(UDPportRx))	
	self.socket.connect(address, int(UDPportRx))
	return

def listen(self,backlog):
	return

def accept(self):
	(clientsocket, address) = (1,1)  # change this to your code
	self.socket.bind(self, int(UDPportTx))
	return (clientsocket,address)

def close(self):   # fill in your code here
	return

def send(self,buffer):
	bytessent = 0     # fill in your code here
	return bytessent

def recv(self,nbytes):
	bytesreceived = 0     # fill in your code here
	return bytesreceived 


