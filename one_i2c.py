import smbus
from time import sleep
bus = smbus.SMBus(1)
addr = 0x48
v0, v1 = bus.read_i2c_block_data(addr, 1, 2)
print bin(v0), bin(v1)


