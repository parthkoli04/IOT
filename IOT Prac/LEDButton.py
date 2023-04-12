import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

blinkCount = 10
count =  0
LEDPin = 13
buttonPin = 26

GPIO.setup(LEDPin, GPIO.OUT)
GPIO.setup(buttonPin,GPIO.IN,pull_up_down = GPIO.PUD_UP)

buttonPress=True
ledState=False
try:
    while count<blinkCount:
        buttonPress=GPIO.input(buttonPin)
        if buttonPress==False and ledState==False:
            GPIO.output(LEDPin,True)
            ledState=True
            sleep(3)
        elif buttonPress==False and ledState==True:
            GPIO.output(LEDPin,False)
            ledState=False
            count += 1
            sleep(0.5)
        sleep(0.1)
finally:
    GPIO.output(LEDPin,False)
    GPIO.cleanup()

