import sys
import time
import Adafruit_DHT
import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe



#Humidity and Temperature Sensor Reading
humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 17)


while True:
   if humidity is not None and temperature is not None:
       print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
    #    client.connect("mqtt.eclipse.org", 1883, 60)
       publish.single("/sensors/dht11/temperature", temperature, hostname="192.168.1.2",qos=2)
       publish.single("/sensors/dht11/humidity", humidity, hostname="192.168.1.2",qos=2)
       time.sleep(1)
   else:
       print('Failed to get reading. Try again!')
       sys.exit(1)

