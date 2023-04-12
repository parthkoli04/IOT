##import RPi.GPIO as GPIO
##import time
##
##
##GPIO.setwarnings(False)
##GPIO.setmode(GPIO.BOARD)
##
##buzzer_pin=22
##GPIO.setup(buzzer_pin,GPIO.OUT)
##
##
##
##
##for i in range(2):
##    print(i)
##    GPIO.output(buzzer_pin,GPIO.HIGH)
##    time.sleep(3)
##    GPIO.output(buzzer_pin,GPIO.LOW)
##    time.sleep(3)
##
##
##GPIO.cleanup()
##




import RPi.GPIO as GPIO
import time


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

buzzer_pin=16
GPIO.setup(buzzer_pin,GPIO.OUT)



GPIO.output(buzzer_pin,GPIO.HIGH)
time.sleep(1)
print("On")
##GPIO.output(buzzer_pin,GPIO.LOW)
##time.sleep(1)
print("Off")
GPIO.cleanup()
