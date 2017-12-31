#!/usr/bin/python
import paho.mqtt.client as mqtt
from mlx90614 import MLX90614

thermometer_address = 0x5a
topic = "pod/sky"

thermometer = MLX90614(thermometer_address)

client = mqtt.Client("P1") 
client.connect("hassio.local") 
print "Connected to broker"

amb_temp = thermometer.get_amb_temp()
obj_temp = thermometer.get_obj_temp()

json = "{\"ambient_temp\": %d, \"sky_temp\": %d }" % (amb_temp, obj_temp) 
client.publish(topic, json )

