import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

P = 21
GPIO.setup(P, GPIO.OUT)
GPIO.output(P, True)

P = 17
GPIO.setup(P, GPIO.OUT)
GPIO.output(P, True)

