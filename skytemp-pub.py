#!/usr/bin/python
import paho.mqtt.publish as publish
import time
from mlx90614 import MLX90614
import logging
import logging.handlers


thermometer_address = 0x5a
topic = "pod/sky"
broker = "hassio.local"
delay = 60

logger = logging.getLogger( __name__ )
logger.setLevel(logging.DEBUG)

handler = logging.handlers.SysLogHandler(address = '/dev/log')
logger.addHandler(handler)
logger.setLevel(logging.INFO)


logger.info("Starting up: broker = %s, topic = %s" % (broker,topic) )


thermometer = MLX90614(thermometer_address)

while True:
    amb_temp = thermometer.get_amb_temp()
    obj_temp = thermometer.get_obj_temp()

    json = "{\"ambient_temp\": %d, \"sky_temp\": %d }" % (amb_temp, obj_temp) 

    print json + "\n"
    publish.single( topic, json, hostname=broker )
    time.sleep( delay )
