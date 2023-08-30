import paho.mqtt.publish as publish
import time 
import serial 
import string 

#reading and writing data from and to audrino serial 
#rdcomm0 -> this could be different 

ser = serial.Serial("/dev/rfcomm1",9600)
ser.write(str.encode("Start\r\n"))

while True :	
	if ser.in_waiting > 0 :
		rawserial = ser.readline()
		cookedserial= rawserial.decode('utf-8').strip("\r\n")
		print (cookedserial)
		publish.single("ifn649", cookedserial, hostname="54.206.111.80")
		print("Done")
