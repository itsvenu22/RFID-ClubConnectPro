import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

max_tries = 3
try_count = 0

reader = SimpleMFRC522()
while try_count < max_tries:
    try:
        id, data = reader.read()
        a = str(id)
        print(a)
        print(data)
        break
    finally:
        GPIO.cleanup()
