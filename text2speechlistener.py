from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import logging
import time
import argparse
import json
from text2speech import text2speech

# Custom MQTT message callback
def customCallback(client, userdata, message):
    print("Received a new message: ")
    print(message.payload)
    text2speech(message.payload.decode("utf-8"))
    print("from topic: ")
    print(message.topic)
    print("--------------\n\n")

def subscribe_mqtt():
    host = "agvi1nwfqezoa-ats.iot.us-east-1.amazonaws.com"
    clientId = ""
    topic = "suspectAlert"

    # Init AWSIoTMQTTClient
    myAWSIoTMQTTClient = None
    myAWSIoTMQTTClient = AWSIoTMQTTClient(clientId)
    myAWSIoTMQTTClient.configureEndpoint(host, 8883)
    myAWSIoTMQTTClient.configureCredentials("smslambdapackage/AmazonRootCA1.pem", "smslambdapackage/fe36c1fbb0-private.pem.key", "smslambdapackage/fe36c1fbb0-certificate.pem.crt")

    # AWSIoTMQTTClient connection configuration
    myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
    myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
    myAWSIoTMQTTClient.configureDrainingFrequency(1)  # Draining: 2 Hz
    myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
    myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec
    
    myAWSIoTMQTTClient.connect()

    # Subscribe to the topic
    myAWSIoTMQTTClient.subscribe(topic, 1, customCallback)
    myAWSIoTMQTTClient.onMessage
    #time.sleep(2)

if __name__ == "__main__":
    while True:
        #subscribe_mqtt()
        time.sleep(1)
    
