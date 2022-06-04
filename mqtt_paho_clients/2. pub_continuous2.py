import paho.mqtt.client as mqtt
import random
import time

def getMsg():
    d = random.randrange(0, 2)
    msg = d                
    return msg                

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

mqttc = mqtt.Client()
mqttc.on_connect = on_connect

mqttc.connect("localhost", 1883)
mqttc.loop_start()

try:
    while True:
        t = getMsg()
        print("person", t)
        
        infot = mqttc.publish("building/person", t)  # difference
        infot.wait_for_publish()
        
        time.sleep(1)
except KeyboardInterrupt:
    print("Finished!")
    mqttc.loop_stop()
    mqttc.disconnect()