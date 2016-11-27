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



def sda(x):
  GPIO.output(SDA, x)

def scl():
  GPIO.output(SCL, True)
  sleep(0.01)
  GPIO.output(SCL, False)
  sleep(0.01)

def bit(x):
  sda(x)
  scl()

def byte(x):
  for c in x:
    if c == '0':
      bit(0)
    elif c == '1':
      bit(1)
  
if __name__ == '__main__':
  # test pattern
  cls()

  import RPi.GPIO as GPIO
  SDA = 2
  SCL = 3
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(SDA, GPIO.OUT)
  GPIO.setup(SCL, GPIO.OUT)
  
  sda(0)
  scl()
  # 3e = 0011 1110
  byte("0011 1110")
      
  scl()  # ack
  # write
  byte("0100 0000")
  # '0' =  0x38 = 0011 1000
  byte("0011 1000")

