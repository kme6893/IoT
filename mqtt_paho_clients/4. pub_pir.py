import paho.mqtt.client as mqtt
import time
import RPi.GPIO as gpio

out_pin = 16

gpio.setmode(gpio.BCM)
gpio.setup(out_pin, gpio.IN)


def pir_sensor():
    isinput = 0
    if gpio.input(out_pin) == 1:
        isinput = 1
    return isinput
        
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

mqttc = mqtt.Client()
mqttc.on_connect = on_connect

mqttc.connect("localhost", 1883)
mqttc.loop_start()

try:
    while True:
        t = pir_sensor()
        print("pir sensor", t)
        
        infot = mqttc.publish("sensor/person", t)
        infot.wait_for_publish()
        
        time.sleep(1)
except KeyboardInterrupt:
    print("Finished!")
    mqttc.loop_stop()
    mqttc.disconnect()
