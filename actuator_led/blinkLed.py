#
# import RPi.GPIO as gpio
# import time
# 
# led_pin = 5
# 
# gpio.setmode(gpio.BCM)
# gpio.setup(led_pin, gpio.OUT)
# 
# def blinkLED(numTimes, speed):
# 	for i in range(0, numTimes): # 0~n-1 times
# 		print("Iteration " + str(i+1))
# 		gpio.output(led_pin, True)
# 		time.sleep(speed)
# 		gpio.output(led_pin, False)
# 		time.sleep(speed)
# 	print("Blink Finished")
# 	gpio.cleanup()
# 
# try:
#     iterations = input("Enter total number of times to blink: ")
#     speed = input("Enter length of each blink(seconds): ")
# 
#     blinkLED(int(iterations), float(speed))
# 
# except KeyboardInterrupt:
#     gpio.cleanup()


# # [try1]
# import RPi.GPIO as gpio
# import time
# 
# led_pin = 5
# pin_color = int(input("what is color?"))
# if pin_color == 2 :
#     led_pin = 6
# elif pin_color == 3 :
#     led_pin = 19
# else :
#     pass
# 
# gpio.setmode(gpio.BCM)
# gpio.setup(led_pin, gpio.OUT)
# 
# def blinkLED(numTimes, speed):
#     for i in range(0, numTimes):
#         print("Iteration " + str(i+1))
#         gpio.output(led_pin, True)
#         time.sleep(speed)
#         gpio.output(led_pin, False)
#         time.sleep(speed)
#     print("Blink Finished")
#     gpio.cleanup()
# 
# try:
#     iterations = input("Enter total number of times to blink: ")
#     speed = input("Enter length of each blink(seconds): ")
# 
#     blinkLED(int(iterations), float(speed))
# 
# except KeyboardInterrupt:
#     gpio.cleanup()
    

# # [tyr1] answer
# import RPi.GPIO as gpio
# import time
# 
# red_pin = 5
# yello_pin = 6
# green_pin = 19
# 
# gpio.setmode(gpio.BCM)
# gpio.setup(led_pin, gpio.OUT)
# gpio.setup(yello_pin, gpio.OUT)
# gpio.setup(green_pin, gpio.OUT)
# 
# gpio.output(led_pin, False)
# gpio.output(yello_pin, False)
# gpio.output(green_pin, False)
# 
# try :
#     while True:
#         i = eval(input("red(1) yellow(2) green(3) :"))
#         if i == 1:
#             gpio.output(red_pin, True)
#             gpio.output(yellow_pin, False)
#             gpio.output(green_pin, False)
#         elif i == 2:
#             gpio.output(red_pin, False)
#             gpio.output(yellow_pin, True)
#             gpio.output(green_pin, False)
#         elif i == 3:
#             gpio.output(red_pin, False)
#             gpio.output(yellow_pin, False)
#             gpio.output(green_pin, True)
#             
# except KeyboardInterrupt:
#     gpio.cleanup()
    
