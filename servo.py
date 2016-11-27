import RPi.GPIO as GPIO
try:
    from time import clock
    GPIO.setmode(GPIO.BOARD)
except:
    pass

GPIO.setup(12, GPIO.OUT)

def foo(x, count=-1):
    rate = 0.015 + 0.004 * x / 100
    WAVE_WIDTH = int(1000000 / 1.22 / 2.66 / 100)
    PULSE_WIDTH = WAVE_WIDTH * rate
    while count:
        count -= 1
        t = clock()
        for j in range(100):
            for i in xrange(WAVE_WIDTH * 2):
                GPIO.output(12, 1 if i < PULSE_WIDTH else 0)
    
        print clock() - t    

def bar(x):
    t = clock()
    rate = 0.015 + 0.004 * x / 100.0
    WAVE_WIDTH = int(10000000 / 24.5)
    PULSE_WIDTH = int(WAVE_WIDTH * rate)
    GPIO.output(12, 0)

    for i in xrange(PULSE_WIDTH):
        GPIO.output(12, 1)
    
    GPIO.output(12, 0)
    print (clock() - t) / rate, rate
    
def baz(x):
    from time import sleep 
    rate = 0.015 + 0.004 * x / 100.0
    rate *= 0.1
    for i in range(10):
        GPIO.output(12, 1)
        sleep(rate)
        GPIO.output(12, 0)
        sleep(0.01)

for i in range(40):
    baz(0)
for i in range(40):
    baz(100)
for i in range(40):
    baz(0)
for i in range(40):
    baz(100)
