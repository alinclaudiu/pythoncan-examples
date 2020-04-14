#Code Generated by TestGenx v.1.0
#ANCIT CONSULTING
#Date : Tue Apr 14 12:08:09 IST 2020
#Author : arpit

from __future__ import print_function
import can
import time
import cantools
from pynput import keyboard
import threading

db = cantools.database.load_file('D:/ancit/climate_ecu.dbc')
can_bus = can.interface.Bus(bustype='socketcan',channel='vcan0',bitrate=1000000)

def on_Message():
	while True:
		response = can_bus.recv()
def on_press(key):
print("Key Event Identified")

def on_Key():
	keyboard.Listener(on_press=on_press).start()

def sendMessage():
			# Message ID : 0x07
			message = can.Message(arbitration_id=0x07, data=[8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], is_extended_id=False)
			try:
				can_bus.send(message)
				print(" 0x07 Message sent on {}".format(can_bus.channel_info))
			except can.CanError:
				print("Message NOT sent")

			# Message ID : 0x07
			message = can.Message(arbitration_id=0x07, data=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], is_extended_id=False)
			try:
				can_bus.send(message)
				print(" 0x07 Message sent on {}".format(can_bus.channel_info))
			except can.CanError:
				print("Message NOT sent")

if __name__ == '__main__':

	sendMessage()
	on_Key()
	threading.Thread(on_Message()).start()