#

import RPi.GPIO as gpio
import time

led_pin = 5

gpio.setmode(gpio.BCM)
gpio.setup(led_pin, gpio.OUT)

gpio.output(led_pin, True)
time.sleep(0.5)
gpio.output(led_pin, False)
time.sleep(0.5)
gpio.output(led_pin, True)
time.sleep(0.5)
gpio.output(led_pin, False)
time.sleep(0.5)

print("Blink Finished")
gpio.cleanup()




# # 10times

# import RPi.GPIO as gpio
# import time
# 
# led_pin = 5
# 
# gpio.setmode(gpio.BCM)
# gpio.setup(led_pin, gpio.OUT)
# 
# i=0
# while True:
#     i=i+1
#     print(i,"time")
#     gpio.output(led_pin, True)
#     time.sleep(0.5)
#     gpio.output(led_pin, False)
#     time.sleep(0.5)
#     if i > 9 :
#         break
# 
# print("Blink Finished")
# gpio.cleanup()



# # forever
#  
# import RPi.GPIO as gpio
# import time
# 
# led_pin = 5
# 
# gpio.setmode(gpio.BCM)
# gpio.setup(led_pin, gpio.OUT)
# 
# try :
#     while True :
#         gpio.output(led_pin, True)
#         time.sleep(0.5)
#         gpio.output(led_pin, False)
#         time.sleep(0.5)
# 
# 
# except KeyboardInterrupt:
#     gpio.cleanup()

