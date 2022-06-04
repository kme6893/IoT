import paho.mqtt.client as mqtt
import RPi.GPIO as gpio

led_pin = 26
gpio.setmode(gpio.BCM)
gpio.setup(led_pin, gpio.OUT)

def on_connect(client, userdata, flags, rc):
    print("connected with result code " + str(rc))
    client.subscribe("control/led")
        
def on_message(client, userdata, msg):
    print("Topic: " + msg.topic + " Message: " + msg.payload.decode("utf-8"))

    light = str(msg.payload.decode("utf-8"))
    
    if light == "on" :
        gpio.output(led_pin, True)
    else :
        gpio.output(led_pin, False)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost", 1883)

try:
    client.loop_forever()
except KeyboardInterrupt:
    print("Finished!")
    client.unsubscribe("control/led")
    client.disconnect()
    gpio.cleanup()