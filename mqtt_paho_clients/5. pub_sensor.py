import paho.mqtt.client as mqtt
import time
import RPi.GPIO as gpio

out_pin = 16
trig_pin = 13
echo_pin = 19

gpio.setmode(gpio.BCM)
gpio.setup(out_pin, gpio.IN)
gpio.setup(trig_pin, gpio.OUT)
gpio.setup(echo_pin, gpio.IN)


def pir_sensor():
    isinput = False
    if gpio.input(out_pin) == 1:
        isinput = True
    return isinput
        
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

mqttc = mqtt.Client()
mqttc.on_connect = on_connect

mqttc.connect("192.168.0.93", 8883)
mqttc.loop_start()

try:
    while True:
        if pir_sensor() == True:
            gpio.output(trig_pin, False)
            time.sleep(0.5)

            gpio.output(trig_pin, True)
            time.sleep(0.00001)
            gpio.output(trig_pin, False)

            while gpio.input(echo_pin) == 0:
                pulse_start = time.time()

            while gpio.input(echo_pin) == 1:
                pulse_end = time.time()

            pulse_duration = pulse_end - pulse_start

            distance = pulse_duration * 34000 / 2 
            distance = round(distance, 2)
            
            print("[pir_sensor ON] Distance : ", distance, "cm")        
            infot = mqttc.publish("sensor/distance", distance)
            infot.wait_for_publish()
        
            time.sleep(1)
        else :
            print("[pir_sensor OFF] Distance :", 10000, "over")
            infot = mqttc.publish("sensor/distance", 10000)
            infot.wait_for_publish()
            
            time.sleep(0.5)
        
        
except KeyboardInterrupt:
    print("Finished!")
    mqttc.loop_stop()
    mqttc.disconnect()