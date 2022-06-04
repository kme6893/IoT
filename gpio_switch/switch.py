#
import RPi.GPIO as gpio
import time

switch_pin = 18

gpio.setmode(gpio.BCM)
gpio.setup(switch_pin, gpio.IN, gpio.PUD_UP)

def button():
    isClicked = False
    if gpio.input(switch_pin) == 0:
        isClicked = True
    return isClicked

try:
    while True:
        if button() == True:
            print("Switch On")
            time.sleep(0.5)
        else :
            print("Switch OFF")
            time.sleep(0.5)
            
except KeyboardInterrupt:
    gpio.cleanup()



# # [try] switch & light
# import RPi.GPIO as gpio
# import time
# 
# switch_pin = 18
# led_pin = 5
# yellow_pin = 6
# 
# gpio.setmode(gpio.BCM)
# gpio.setup(switch_pin, gpio.IN, gpio.PUD_UP)
# gpio.setup(led_pin,gpio.OUT)
# gpio.setup(yellow_pin,gpio.OUT)
# 
# def button():
#     isClicked = False
#     if gpio.input(switch_pin) == 0:
#         isClicked = True
#     return isClicked
# 
# try:
#     while True:
#         if button() == True:
#             print("Switch On")
#             time.sleep(0.2)
#             gpio.output(led_pin, True)
#             gpio.output(yellow_pin,False)
#             
#         else:
#             print("Switch Off")
#             time.sleep(0.2)
#             gpio.output(yellow_pin, True)
#             gpio.output(led_pin, False)
#             
# except KeyboardInterrupt:
#     gpio.cleanup()
    

