import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

reader = SimpleMFRC522()
try:
    id, data = reader.read()
    a = str(id)
    print(a)
    print(data)

finally:
    GPIO.cleanup()





