import RPi.GPIO as GPIO

P1 = 21
P2 = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(P1, GPIO.IN)
GPIO.setup(P2, GPIO.IN)

from time import time
t = time()

prev1 = 0
prev2 = 0

WIDTH = 80
buf1 = ['_'] * WIDTH
buf2 = ['_'] * WIDTH

print 'ready'
c = 0
while True:
    v1 = GPIO.input(P1)
    v2 = GPIO.input(P2)
    #count += 1
    if v1 != prev1 or v2 != prev2:
        buf1[c] = 'H' if v1 else '_'
        buf2[c] = 'H' if v2 else '_'
        c += 1
        if c == WIDTH:
            c = 0
            print ''.join(buf1)
            print ''.join(buf2)
            print
        prev1 = v1
        prev2 = v2
        t = time()
    if time() > t + 1:
        if not c:
            c = 0
            print ''.join(buf1[:c])
            print ''.join(buf2[:c])
            print
        t = time()
    #if count == 100000: break

print time() - t
