#!/usr/bin/python
import paho.mqtt.client as mqtt
import time
from mlx90614 import MLX90614

thermometer_address = 0x5a
topic = "pod/sky"

thermometer = MLX90614(thermometer_address)

client = mqtt.Client("P1") 
client.connect("hassio.local") 
print "Connected to broker..."

while True:
    amb_temp = thermometer.get_amb_temp()
    obj_temp = thermometer.get_obj_temp()

    json = "{\"ambient_temp\": %d, \"sky_temp\": %d }" % (amb_temp, obj_temp) 

    print json + "\n"
    client.publish(topic, json )
    time.sleep( 60 )
