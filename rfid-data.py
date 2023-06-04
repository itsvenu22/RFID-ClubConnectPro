import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

import os
import time

#def send_mess():


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

reader = SimpleMFRC522()

max_tries = 3
try_count = 0
try:
    while try_count < max_tries:
        try:
            os.system(f"clear")
            os.system(f"figlet -c -w 160 -f ANSI\ Shadow LINUX CLUB | lolcat")
            id, data = reader.read()
            a = str(id)
            #print(id)
            #print(data)
            time.sleep(1)
            os.system(f"figlet -c -w 160 -f univers.flf ACCESS GRANTED | lolcat ")
            os.system(f"figlet -c -w 160 -f Georgia11.flf ACCESS GRANTED | lolcat ")
            os.system(f"figlet -c -w 160 -f standard WELCOME TO PASSWORD | lolcat")
            os.system(f"figlet -c -w 160 -f ANSI\ Shadow ACCESS GRANTED | lolcat")
            os.system(f"figlet -c -w 160 -f term HACKER ID: {a} | lolcat")
            os.system(f"figlet -c -w 160 -f term HACKER NAME: {data} | lolcat")
            #time.sleep(2)
            #os.system(f"clear")
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
