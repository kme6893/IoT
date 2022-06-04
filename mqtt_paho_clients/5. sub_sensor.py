import paho.mqtt.client as mqtt
import RPi.GPIO as gpio

led_pin = 26
yellow_pin = 5
green_pin = 6

gpio.setmode(gpio.BCM)
gpio.setup(led_pin, gpio.OUT)
gpio.setup(yellow_pin, gpio.OUT)
gpio.setup(green_pin, gpio.OUT)

def on_connect(client, userdata, flags, rc):
    print("connected with result code " + str(rc))
    client.subscribe("control/led")
        
def on_message(client, userdata, msg):
    print("Topic: " + msg.topic + " Message: " + msg.payload.decode("utf-8"))

    light = str(msg.payload.decode("utf-8"))
    
    if light == "off" :
        gpio.output(led_pin, False)
        gpio.output(yellow_pin,False)
        gpio.output(green_pin, False)
    elif light == "Red on" :
        gpio.output(led_pin, True)
        gpio.output(yellow_pin,False)
        gpio.output(green_pin, False)
    elif light == "Yellow on" :
        gpio.output(led_pin, False)
        gpio.output(yellow_pin,True)
        gpio.output(green_pin, False)
    elif light == "Green on" :
        gpio.output(led_pin, False)
        gpio.output(yellow_pin,False)
        gpio.output(green_pin, True)
        

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.0.93", 8883)

try:
    client.loop_forever()
except KeyboardInterrupt:
    print("Finished!")
    client.unsubscribe("control/led")
    client.disconnect()
    gpio.cleanup()