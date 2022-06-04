import RPi.GPIO as gpio
import time

pin = 18 # PWM pin

gpio.setmode(gpio.BCM)
gpio.setup(pin, gpio.OUT)

p = gpio.PWM(pin, 50)
p.start(0)

try:
    while True:
        p.ChangeDutyCycle(2.5)
        time.sleep(1)
        print("DutyCycle 2.5 over")
        p.ChangeDutyCycle(5)
        time.sleep(1)
        print("DutyCycle 5 over")
        p.ChangeDutyCycle(7.5)
        time.sleep(1)
        print("DutyCycle 7.5 over")
        p.ChangeDutyCycle(10)
        time.sleep(1)
        print("DutyCycle 10 over")
        p.ChangeDutyCycle(12.5)
        time.sleep(1)
        print("DutyCycle 12.5 over")
       
except KeyboardInterrupt:
    p.stop()
    gpio.cleanup()
