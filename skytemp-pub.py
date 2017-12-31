#!/usr/bin/python
import paho.mqtt.client as mqtt
import time
from mlx90614 import MLX90614
import logging
import logging.handlers


logger = logging.getLogger( __name__ )
logger.setLevel(logging.DEBUG)

handler = logging.handlers.SysLogHandler(address = '/dev/log')
logger.addHandler(handler)
logger.setLevel(logging.INFO)


logger.info("Starting up")

thermometer_address = 0x5a
topic = "pod/sky"
broker = "hassio.local"

thermometer = MLX90614(thermometer_address)

client = mqtt.Client("P1") 
try:
    client.connect( broker, keepalive=120 ) 
except:
    logger.error( "Error connecting to broker [%s]" % broker )
    sys.exit()

logger.info( "Successfully connected to mqtt broker [%s]" % broker )

while True:
    amb_temp = thermometer.get_amb_temp()
    obj_temp = thermometer.get_obj_temp()

    json = "{\"ambient_temp\": %d, \"sky_temp\": %d }" % (amb_temp, obj_temp) 

    print json + "\n"
    (result,mid) = client.publish(topic, json )
    time.sleep( 60 )
