# *Real* simple first-cut at building a cloud detector using an MLX90614 #

Read ambient and sky temperature from MLX90614; push to HomeAssistant MQTT broker

## Initial library setup on RPi0 ##

    $ sudo apt-get install python-smbus
    $ git clone https://github.com/CRImier/python-MLX90614.git

Next, copy the cloned mlx90614.py source file to directory with skytemp.py

Download and install the Python Paho mqtt implementation:
    $ sudo pip install paho-mqtt

Download/install Adafruit BMP180 Python library

    $ sudo apt-get install python-dev
    $ git clone https://github.com/adafruit/Adafruit_Python_BMP.git
    $ cd Adafruit_Python_BMP
    $ sudo python setup.py install

