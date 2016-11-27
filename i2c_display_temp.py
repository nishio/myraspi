import smbus
from time import sleep
bus = smbus.SMBus(1)
addr = 0x3e

# initialization
data = [0x38, 0x39, 0x14, 0x70, 0x56, 0x6c, 0x38, 0x0c, 0x01]
wait = [1, 1, 1, 1, 1, 400, 1, 1, 2]  # ms
for d, w in zip(data, wait):
  print 'write', hex(d), 'wait', w, 'ms'
  bus.write_byte_data(addr, 0b00000000, d)
  sleep(w / 1000.0)

def cls():
  bus.write_byte_data(addr, 0b00000000, 0b00000001)

char_table = {}
for i, c in enumerate('0123456789'):
  char_table[c] = 0b00110000 + i

char_table['.'] = 0b00101110

def write(s):
  for c in s:
    bus.write_byte_data(addr, 0b01000000, char_table[c])

def write_deg_mark():
  bus.write_byte_data(addr, 0b01000000, 0b11011111)
  bus.write_byte_data(addr, 0b01000000, 0b01000011)

def get_temp():
  addr = 0x48
  v0, v1 = bus.read_i2c_block_data(addr, 1, 2)
  temp = ((v0 << 8) + v1 >> 3) / 16.0
  return "%2.1f" % temp

if __name__ == '__main__':
  # test pattern
  while True:
    cls()
    write(get_temp())
    write_deg_mark()  
    sleep(0.5)
