
MQTT Topics


වාට්ටු සංවේදක ඒකකය
/sensors/dht11/temperature
/sensors/dht11/humidity

රෝගියාගේ සංවේදක ඒකකය
/sensors/ds18b20/temp
/sensors/ardiuno
/sensors/heartpulse/bpm
/sensors/ky038/sound


Message format to AWS IOT

1)bodytempreture

{
    "state": {
        "reported": {
            "bodytemptreture": 37
            "patientno": "1"
            "patientname" : "kamal"

        }
    }
}

