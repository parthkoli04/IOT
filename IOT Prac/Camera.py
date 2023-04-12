import picamera
import time

camera = picamera.PiCamera()
camera.start_preview()
time.sleep(5)
camera.capture("snapshot.jpg")
time.sleep(5)
camera.stop_preview()
camera.close()
print("Picture Taken")
