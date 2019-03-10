import binascii
import socket as syssock
import threading
import struct
import sys

# Flags
SOCK352_SYN = bytearray(0x01)          # initiate connection
SOCK352_FIN = 0x02          # end connection
SOCK352_ACK = bytearray(0x04)          # ack number
SOCK352_RESET = 0x08        # reset the connection
SOECK352_HAS_OPT = 0xA0     # option field is valid
portTx = 0
portRx = 0

sock352PktHdrData = '!BBBBHHLLQQLL'
max_packsize = bin(64000)        # in bytes
segments = 0
# these functions are global to the class and
# define the UDP ports all messages are sent
# and received from

def init(UDPportTx,UDPportRx):   # initialize your UDP socket here
	if UDPportRx == 0:
		UDPportRx = 42069
	if UDPportTx == 0:
		UDPportTx = 42069
	portTx = UDPportTx
	portRx = UDPportRx
	pass 

def parse_flag(flags):    # process header flags
    while flags > 0:
        if flags > 160:     # SOCK352_HAS_OPT
            opt = 1
            flags -= 160
        elif flags > 8:     # SOCK352_RESET = 0x08
            reset = 1
            flags -= 8
        elif flags > 4:     # SOCK352_ACK = 0x04
            ack = 1
            flags -= 4
        elif flags > 2:     # SOCK352_FIN = 0x02
            fin = 1
            flags -= 2
        elif flags > 1:     # SOCK352_SYN = 0x01
            syn = 1
            flags -= 1
    f = (opt, reset, ack, fin, syn)
    return f

class socket:
	def __init__(self):  # fill in your code here 
		self.clientsocket = syssock.socket(syssock.AF_INET, syssock.SOCK_DGRAM)
		self.serversocket = syssock.socket(syssock.AF_INET, syssock.SOCK_DGRAM)
		self.udpPkt_hdr_data = struct.Struct(sock352PktHdrData)  # returns struct obj, R/W binary data according to the given format
		return

	def bind(self,address):
		self.sock.bind(address)
		return

	def connect(self,address):  # fill in your code here
		
		#flags for header set here
        	version = 0x1       # Part 1
        	flags = SOCK352_SYN          # Part 1
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
        	header = self.udpPkt_hdr_data.pack(version, flags, opt_ptr, protocol, header_len, checksum, source_port, dest_port, seq_no, ack_no, window, payload_len)
		clientsocket = self
		self.bind(self, int(UDPportRx))
		
		clientsocket.recv(SOCK352_SYN)
 		clientsocket.send(SOCK352_ACK)
		self.socket.connect(address, int(UDPportRx))
		return

	def listen(self,backlog):
		return

	def accept(self):
		(clientsocket, address) = (1,1)  # change this to your code
		serversocket = self
		serversocket.bind(serversocket, portTx)
		#3-way handshake occurs here
		serversocket.send(SOCK352_SYN)
#		clientsocket.recv(SOCK352_SYN)
#		clientsocket.send(SOCK352_ACK)
		serversocket.recv(SOCK352_ACK)
		socket.bind(self, portTx)
		return self

	def close(self):   # fill in your code here
		return

	def send(self,buffer):
		load = struct.unpack(sock352PktHdrData, buffer, 0)
		
		version = int(load[0])  # Part 1
        	flags = int(load[1])  # Part 1
        	opt_ptr = int(load[2])
        	protocol = int(load[3])
        	headerlen = int(load[4])
        	checksum = int(load[5])
        	source_port = int(load[6])
        	dest_port = int(load[7])
        	seq_no = int(load[8])  # Part 1
        	ack_no = int(load[9])  # Part 1
        	window = int(load[10])
        	payload_len = int(load[11])  # Part 1
		
		f = parse_flag(flags)
        	# returns f = (opt, reset, ack, fin, syn)
		
		
        	bytes_to_send = payload_len
        	segments = math.ceil(payload_len/max_packsize)        # total number of segments (use for seq number)
        	seg_ack = 0         # last ack sent (turn this into a list and pop/append)
		# 64000 - '!BBBBHHLLQQLL' = amt to send (must account for header in package size)
        	# load[0:64000]
        	# load[64000:2 x 64000]
		
		
	        # send the size of the file as a 4 byte integer
        	# to the server, so it knows how much to read
        	FRAGMENTSIZE = 8192
        	while (bytes_to_send > 0):
            		fragment = fd.read(FRAGMENTSIZE)
            		bytessent = 0
            	# make sure we sent the whole fragment
            	while (bytessent < len(fragment)):
                	sent = s.send(fragment[bytessent:])
                	if (sent == 0):
                    		raise RuntimeError("socket broken")
                	bytessent = bytessent + sent
            	bytes_to_send = bytes_to_send - len(fragment)	
		
		return bytessent

	def recv(self,nbytes):

		bytesreceived = 0     # fill in your code here
		 chunks = []
        	bytes_recd = 0
        	while bytes_recd < MSGLEN:
            	chunk = self.sock.recv(min(MSGLEN - bytes_recd, 2048))
            	if chunk == b'':
                raise RuntimeError("socket connection broken")
            	chunks.append(chunk)
            	bytes_recd = bytes_recd + len(chunk)
        	return b''.join(chunks)
	#	return bytesreceived 


