import RPi.GPIO as GPIO

P = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(P, GPIO.IN)
