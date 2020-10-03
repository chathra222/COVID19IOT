import serial
import time
import paho.mqtt.publish as publish


ser = serial.Serial('/dev/ttyACM0',9600)
ser.baudrate=9600
ser.timeout=1000
def receiving(ser):
    global last_received

    buffer_string = ''
    while True:
      try:
        buffer_string = buffer_string + ser.read(ser.inWaiting()).decode("utf-8")
        if '\n' in buffer_string:
            lines = buffer_string.split('\n') # Guaranteed to have at least 2 entries
            if lines[-2] != "":
             last_received = lines[-2]
            #If the Arduino sends lots of empty lines, you'll lose the
            #last filled line, so you could make the above statement conditional
            #like so: if lines[-2]: last_received = lines[-2]
            buffer_string = lines[-1]
            print(last_received)
            
            publish.single("/sensors/ardiuno", last_received, hostname="192.168.1.2",qos=2)
      except serial.SerialException:
            time.sleep(0.01)  # Maybe don't do this, or mess around with the interval
            continue   

while True:
        #read_serial=ser.readline()
        receiving(ser)
        
        #s[0] = str(int (ser.readline(),16))
#       sound = s[0]
#       print(s[0])
#       publish.single("/sensors/sound/audio", sound, hostname="192.168.1.2",qos=2)
#       #print(read_serial)
#       time.sleep(1)


# ser = serial.Serial('/dev/ttyACM0', 9600)
# ser.baudrate=9600
# while 1: 
#     if(ser.in_waiting >0):
#         line = ser.readline()
#         if line != '':
#                 print(line.decode("utf-8"))