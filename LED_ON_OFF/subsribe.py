import paho.mqtt.client as mqtt
import time 
import serial 
import string 

#reading and writing data from and to audrino serial 
#rdcomm0 -> this could be different 

ser = serial.Serial("/dev/rfcomm0",9600)
ser.write(str.encode("Start\r\n"))


def on_connect(client, userdata, flags, rc): # func for making connection
	print("Connected to MQTT")
	print("Connection returned result: " + str(rc) )
	client.subscribe("ifn649")
def on_message(client, userdata, msg): # Func for Sending msg
	print(msg.topic+" "+str(msg.payload))
	ser.write(str.encode(str(msg.payload)))
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("13.236.118.0", 1883, 60)
client.loop_forever()
