import RPi.GPIO as GPIO
import time

ledpin=12
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledpin,GPIO.OUT)

try:
    for i in range(1,10)
    GPIO.output(ledpin,GPIO.HIGH)
    time.sleep(3)
    GPIO.output(ledpin,GPIO.LOW)
    
except:
    GPIO.cleanup()
