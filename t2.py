import RPi.GPIO as GPIO

P = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(P, GPIO.OUT)

from time import sleep
while True:
	GPIO.output(P, True)
        sleep(0.5)
	GPIO.output(P, False)
	sleep(0.5)
