import RPi.GPIO as GPIO
import time

def blink(pin):

    GPIO.output(pin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(1)
    return

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

for i in range(0,50):
        blink(11)
        print(i)
GPIO.cleanup()