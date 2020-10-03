rm -rf ds18b20.log dht11.log ardiuno2pi.log
python3.7 dht11.py >dht11.log 2>&1 &
python3.7 ds18b20.py >ds18b20.log 2>&1 &
python3.7 ardiuno2pi.py >ardiuno2pi.log 2>&1 &