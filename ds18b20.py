import time
from w1thermsensor import W1ThermSensor
import paho.mqtt.publish as publish
import simplejson as json


sensor = W1ThermSensor()


while True:
  temp = sensor.get_temperature()
  time.sleep(0.1)
  payload = {
    "state": {
        "reported": {
            "bodytemptreture": "",
            "patientno": "20",
            "patientname" : "kamal",
            "bedno" : "501"
        }
     }
  }
  payload["state"]["reported"]["bodytemptreture"]=temp



  if temp is not None:
       print("Temperature = %0.1f celcius" % temp)
       print(json.dumps(payload))
       publish.single("/sensors/ds18b20/temp", payload=json.dumps(payload), hostname="192.168.1.2",qos=0)
       time.sleep(10)
  else:
       print('Failed to get reading. Try again!')
       sys.exit(1)

