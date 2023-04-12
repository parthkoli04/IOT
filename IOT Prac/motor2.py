import RPi.GPIO as GPIO
from time import sleep
import sys

motor_channel = (29,31,33,35)  
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(motor_channel, GPIO.OUT)

def runClockwise(n):
    for i in range(0,n):
        print('motor running clockwise\n')
        GPIO.output(motor_channel, (GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.HIGH))
        sleep(0.005)
        GPIO.output(motor_channel, (GPIO.HIGH,GPIO.HIGH,GPIO.LOW,GPIO.LOW))
        sleep(0.005)
##        GPIO.output(motor_channel, (GPIO.LOW,GPIO.HIGH,GPIO.HIGH,GPIO.LOW))
        sleep(0.005)
        GPIO.output(motor_channel, (GPIO.LOW,GPIO.LOW,GPIO.HIGH,GPIO.HIGH))
        sleep(0.005)
        
def runAnticlockwise(n):
    for i in range(0,n):
        print('motor running anti-clockwise\n')
        GPIO.output(motor_channel, (GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.HIGH))
        sleep(0.005)
        GPIO.output(motor_channel, (GPIO.LOW,GPIO.LOW,GPIO.HIGH,GPIO.HIGH))
        sleep(0.005)
        GPIO.output(motor_channel, (GPIO.LOW,GPIO.HIGH,GPIO.HIGH,GPIO.LOW))
        sleep(0.005)
        GPIO.output(motor_channel, (GPIO.HIGH,GPIO.HIGH,GPIO.LOW,GPIO.LOW))
        sleep(0.00)
    
n=int(input('Enter the number of rotations: '))

while True:
    runClockwise(n)
    runAnticlockwise(n)
    
    