import RPi.GPIO as gpio
import time

trig_pin = 13
echo_pin = 19
out_pin = 16
led_pin = 26
yellow_pin = 5
green_pin = 6

gpio.setmode(gpio.BCM)
gpio.setup(trig_pin, gpio.OUT)
gpio.setup(echo_pin, gpio.IN)
gpio.setup(led_pin, gpio.OUT)
gpio.setup(yellow_pin, gpio.OUT)
gpio.setup(green_pin, gpio.OUT)
gpio.setup(out_pin, gpio.IN)

def pir_sensor():
    isinput = False
    if gpio.input(out_pin) == 1:
        isinput = True
    return isinput

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
            if distance >= 40 :
                gpio.output(led_pin, False)
                gpio.output(yellow_pin,False)
                gpio.output(green_pin, True)
            elif 20 <= distance <= 40 :
                gpio.output(led_pin, False)
                gpio.output(yellow_pin,True)
                gpio.output(green_pin, False)
            elif distance <= 20 :
                gpio.output(led_pin, True)
                gpio.output(yellow_pin,False)
                gpio.output(green_pin, False)
        else :
            print("[pir_sensor OFF]")
            gpio.output(led_pin, False)
            gpio.output(yellow_pin,False)
            gpio.output(green_pin, False)
            time.sleep(0.5)

except KeyboardInterrupt:
    gpio.cleanup()