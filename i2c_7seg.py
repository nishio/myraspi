"""
count down timer with HT16K33 Adafruit LED
"""

import smbus
from time import sleep
bus = smbus.SMBus(1)

addr = 0x70

# initialization
data = [0x21, 0x81, 0xEF]
wait = [10, 10, 10]  # ms

for d, w in zip(data, wait):
  print 'write', hex(d), 'wait', w, 'ms'
  #bus.write_byte_data(addr, 0b00000000, d)
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
  buf[6] = numeric[v[2]]
  buf[8] = numeric[v[3]]

  for i, v in enumerate(buf):
    bus.write_byte_data(addr, i, v)

def start():
  left = 25 * 60
  while left:
    minute = left / 60
    second = left % 60
    draw([minute / 10, minute % 10, second / 10, second % 10])
    left -= 1
    sleep(1)

start()
print 'ok'

