import RPi.GPIO as GPIO

P1 = 20  # SDA
P2 = 21  # SCL
GPIO.setmode(GPIO.BCM)
GPIO.setup(P1, GPIO.IN)
GPIO.setup(P2, GPIO.IN)

prev1 = 1
prev2 = 1

WIDTH = 10 * 1024
buf1 = [0] * WIDTH
buf2 = [0] * WIDTH

def to_str(buf):
    return ''.join('H' if v else '_' for v in buf)
    
print 'ready'
c = 0
recording = False
while True:
    v1 = GPIO.input(P1)
    v2 = GPIO.input(P2)
    if recording or v1 != prev1 or v2 != prev2:
        recording = True
        buf1[c] = v1
        buf2[c] = v2
        c += 1
        prev1 = v1
        prev2 = v2
        if c == WIDTH: break

for i in range(WIDTH / 80):
    print to_str(buf1[i * 80:i * 80 + 80])
    print to_str(buf2[i * 80:i * 80 + 80])
