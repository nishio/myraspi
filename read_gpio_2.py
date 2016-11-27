import RPi.GPIO as GPIO

P1 = 20  # SDA
P2 = 21  # SCL
GPIO.setmode(GPIO.BCM)
GPIO.setup(P1, GPIO.IN)
GPIO.setup(P2, GPIO.IN)

from time import time
t = time()

prev1 = 1
prev2 = 1

WIDTH = 80
buf1 = ['_'] * WIDTH
buf2 = ['_'] * WIDTH

def to_str(buf):
    return ''.join('H' if v else '_' for v in buf)

def show():
    print to_str(buf1)
    print to_str(buf2)
    print
    
print 'ready'
c = 0
recording = False
while True:
    v1 = GPIO.input(P1)
    v2 = GPIO.input(P2)
    #count += 1
    if recording or v1 != prev1 or v2 != prev2:
        recording = True
#        buf1[c] = 'H' if v1 else '_'
#        buf2[c] = 'H' if v2 else '_'
        buf1[c] = v1
        buf2[c] = v2
        c += 1
        if c == WIDTH:
            c = 0
            if all(x == 1 for x in buf1):
                break
            show()
        prev1 = v1
        prev2 = v2
        #t = time()
    if time() > t + 1:
        if c:
            print to_str(buf1[:c])
            print to_str(buf2[:c])
            print
            c = 0
        t = time()
    #if count == 100000: break

print time() - t
