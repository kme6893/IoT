# #
# import RPi.GPIO as gpio
# import time
# 
# trig_pin = 13
# echo_pin = 19
# 
# gpio.setmode(gpio.BCM)
# gpio.setup(trig_pin, gpio.OUT)
# gpio.setup(echo_pin, gpio.IN)
#  
# try:
#     while True:
#         gpio.output(trig_pin, False)
#         time.sleep(0.5)
# 
#         gpio.output(trig_pin, True)
#         time.sleep(0.00001)
#         gpio.output(trig_pin, False)
# 
#         while gpio.input(echo_pin) == 0:
#             pulse_start = time.time()
# 
#         while gpio.input(echo_pin) == 1:
#             pulse_end = time.time()
# 
#         pulse_duration = pulse_end - pulse_start
# 
#         distance = pulse_duration * 34000 / 2 
#         distance = round(distance, 2)
#         print("Distance : ", distance, "cm")
# 
# except KeyboardInterrupt:
#     gpio.cleanup()



# [try] sensor & light
import RPi.GPIO as gpio
import time

trig_pin = 13
echo_pin = 19

led_pin = 16
yellow_pin = 12
green_pin = 25

gpio.setmode(gpio.BCM)
gpio.setup(trig_pin, gpio.OUT)
gpio.setup(echo_pin, gpio.IN)
gpio.setup(led_pin,gpio.OUT)
gpio.setup(yellow_pin,gpio.OUT)
gpio.setup(green_pin,gpio.OUT)

try:
    while True:
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

        print("Distance : ", distance, "cm")
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
            
except KeyboardInterrupt:
    gpio.cleanup()
