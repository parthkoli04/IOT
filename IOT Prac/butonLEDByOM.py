import RPi.GPIO as GPIO
from time import sleep
buttonPin = 19
ledPin = 21
blinkCount = 3


GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(ledPin,GPIO.OUT)
blinkcount=3
bt = True
ledState=False
c=0
try:
    while c<blinkcount:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(buttonPin,GPIO.IN,pull_up_down = GPIO.PUD_UP)
        GPIO.setup(ledPin,GPIO.OUT)
        btp=GPIO.input(buttonPin)
        if (btp==False and ledState==False):
            GPIO.ouput(ledPin,True)
            ledState=True
            sleep(0.2)
        elif (btp==False and ledState==True):
            GPIO.output(ledPin,False)
            ledState=False
            c+=1
            sleep(0.5)
        sleep(0.5)
finally:
    GPIO.output(ledPin,False)
    GPIO.cleanup()