import RPi.GPIO as GPIO
P = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(P, GPIO.OUT)
GPIO.output(P, True)
raw_input('>')
GPIO.output(P, False)
raw_input('>')
from time import sleep
while True:
	GPIO.output(P, True)
	raw_input('>')
	GPIO.output(P, False)
	raw_input('>')
