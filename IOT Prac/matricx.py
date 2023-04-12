#ground=gnd
#din=spimosi
##vcc=5v
##cs=ce0
##clk=sclk

from machine import Pin,SPI
from max7219 import Matrix8x8

spi= SPI(0,baudrate=10000000,polarity=1,phase=0,sck=Pin(2),mosi=Pin(3))
ss=Pin(5,Pin.OUT)

display=Matrix8x8(spi,ss,4)

display.brightness(5)

display.zero()
display.show()

display.text('CODE')
display.show()

