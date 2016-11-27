import smbus
from time import sleep
bus = smbus.SMBus(1)
addr = 0x48
while True:
  v0, v1 = bus.read_i2c_block_data(addr, 1, 2)
  print bin(v0), bin(v1)
  print ((v0 << 8) + v1 >> 3) / 16.0
  sleep(0.5)
  sleep(1)
  #break


