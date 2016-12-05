"""
pomodoro timer with HT16K33 Adafruit LED
"""

import smbus
from time import sleep
bus = smbus.SMBus(1)

addr = 0x70

# initialization
data = [0x21, 0x81, 0xE0]
wait = [10, 10, 10]  # ms

for d, w in zip(data, wait):
  print 'write', hex(d), 'wait', w, 'ms'
  bus.write_byte(addr, d)
  sleep(w / 1000.0)
sleep(0.1)

numeric = [
  0x3F, 0x06, 0x5B, 0x4F, 0x66,
  0x6D, 0x7D, 0x07, 0x7F, 0x6F,
]

buf = [0] * 16
def draw(v):
  buf[0] = numeric[v[0]]
  buf[2] = numeric[v[1]]
  buf[4] = 0xff
  buf[6] = numeric[v[2]]
  buf[8] = numeric[v[3]]

  for i, v in enumerate(buf):
    bus.write_byte_data(addr, i, v)

import RPi.GPIO as GPIO
P1 = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(P1, GPIO.IN)
def button(e):
  global value, dvalue
  print 'pushed'
  dvalue = -1
  value = 25 * 60
GPIO.add_event_detect(P1, GPIO.FALLING, callback=button, bouncetime=300)

value = 25 * 60
dvalue = 0
def start():
  global value, dvalue
  while True:
    minute = value / 60
    second = value % 60
    draw([minute / 10, minute % 10, second / 10, second % 10])
    value += dvalue
    sleep(1)
    if not value:  # pomodoro finished
      dvalue = 1  # count up
    if value == 25 * 60 and dvalue == 1:
      dvalue = 0  # stop counting up
try:
  start()
except KeyboardInterrupt:
  GPIO.cleanup()
except:
  GPIO.cleanup()
  raise


