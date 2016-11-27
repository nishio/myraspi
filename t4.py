import RPi.GPIO as GPIO

P = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(P, GPIO.OUT)

from time import sleep
from math import sin
t = 0
while True:
	GPIO.output(P, True)
        sleep(0.01 * (sin(t) + 1))
	GPIO.output(P, False)
        sleep(0.01 * (1 - sin(t)))
	t += 0.05
