import RPi.GPIO as GPIO
import os
import time
import smtplib
from twilio.rest import Client
from mfrc522 import SimpleMFRC522
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from sendms import send_email, send_sms


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

reader = SimpleMFRC522()

MAX_RETRIES = 3
retry_count = 0

##########################################################_CONST_for_MAIL_##########################################################
sender_email = "<your mail>"
sender_password = "<passwd from 3rd party g.app>"

receiver_email = "<receiver mail>"

subject = "<text>"
message = "<text>"

##########################################################_CONST_for_SMS_###########################################################
account_sid = '<your sid>'
auth_token = '<your token>'

body='<text>'

send_num='<twilio number>'
receive_num='<receiver number>'

try:
    while retry_count < MAX_RETRIES:
        try:
            os.system(f"clear")
            os.system(f"figlet -c -w 160 -f ANSI\ Shadow LINUX CLUB | lolcat")
            id, text = reader.read()
            a = str(id)
            #print(id)
            #print(text)
            os.system(f"cat <filename>")
            #time.sleep(1)
            os.system(f"figlet -c -w 160 -f univers.flf ACCESS GRANTED | lolcat ")
            #os.system(f"figlet -c -w 160 -f Georgia11.flf ACCESS GRANTED | lolcat ")
            os.system(f"mpv --no-terminal access.mp3")
            os.system(f"figlet -c -w 160 -f standard WELCOME TO PASSWORD | lolcat")
            os.system(f"figlet -c -w 160 -f ANSI\ Shadow ACCESS GRANTED | lolcat")
            os.system(f"figlet -c -w 160 -f ANSI\ Shadow HACKER ID: {a} | lolcat")
            os.system(f"figlet -c -w 160 -f ANSI\ Shadow HACKER NAME: {text} | lolcat")
            send_email(sender_email, sender_password, receiver_email, subject, message)
            send_sms(body,send_num,receive_num)
            time.sleep(10)
            os.system(f"clear")
            break
        except Exception as e:
            if str(e) == "Error while reading!":
                retry_count += 1
                print(f"Retry {retry_count}/{MAX_RETRIES}")
            elif str(e) == "AUTH ERROR" or "AUTH ERROR!!":
                print("Authentication error. Please check authentication keys.")
                break
            else:
                print(f"Error: {e}")
                break
finally:
    GPIO.cleanup()
