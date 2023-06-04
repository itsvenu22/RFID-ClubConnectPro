import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

max_tries = 3
try_count = 0

reader = SimpleMFRC522()
try:
    while try_count < max_tries:
        try:
            id, data = reader.read()
            a = str(id)
            print(a)
            print(data)
            break
        except Exception as e:
            if str(e) == "Error while reading!":
                try_count += 1
                print(f"Retry {try_count}/{max_tries}")
            elif str(e) == "AUTH ERROR" or "AUTH ERROR!!":
                print("Authentication error. Please check authentication keys.")
                break
            else:
                print(f"Error: {e}")
                break
finally:
    GPIO.cleanup()





