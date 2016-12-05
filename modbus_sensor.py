import minimalmodbus
import serial
from datetime import datetime

ROOM1 = '1'
TANK1 = '1'

instrument = minimalmodbus.Instrument('COM3', 1) # port name, slave address (in decimal)
instrument.serial.port     = 'COM3'        # this is the serial port name
instrument.serial.baudrate = 9600   # Baud
instrument.serial.bytesize = 8
instrument.serial.parity   = serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.serial.timeout  = 0.05   # seconds

instrument.address = 1     # this is the slave address number
instrument.mode = minimalmodbus.MODE_RTU   # rtu or ascii mode

print ('connect to port %s' %instrument.serial.port)

now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  #this will remove decimal point value
date = str(datetime.now().date().today())
print('date: %s' %now)

print('test in Room %s tank %s' %(ROOM1, TANK1))

salinity = instrument.read_register(registeraddress=0, numberOfDecimals=2, functioncode=4, signed=False)
print('Salinity value: %.2f%%' %salinity)

temp = instrument.read_register(registeraddress=1, numberOfDecimals=1, functioncode=4, signed=False)
a = '\u2103'
print('temperature value: %.1f %s' %(temp, a))

print('\nCommand process done!')

line = ROOM1 + ' ' + TANK1 + ' ' + \
       now + ' ' + str(salinity) + ' ' + str(temp)
print('data format: %s' %line)
