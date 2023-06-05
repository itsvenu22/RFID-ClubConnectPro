import RPi.GPIO as GPIO
import os
import time
import smtplib
from twilio.rest import Client
from mfrc522 import SimpleMFRC522
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, receiver_email, subject, message):

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully!")

    except Exception as e:
        print("An error occurred while sending the email:", str(e))

    finally:
        server.quit()

def send_lug_message(mess,send_num,receive_num):
    client = Client(account_sid, auth_token)
    message = client.messages.create(from_=send_num,body=mess,to=receive_num)
    print(message.sid)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

reader = SimpleMFRC522()

MAX_RETRIES = 3
retry_count = 0

#CONST for email
sender_email = "<your mail>"
sender_password = "<passwd from 3rd party g.app>"

receiver_email = "<receiver mail>"

subject = "<text>"
message = "<text>"

#CONST for mess
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
            send_lug_message(body,send_num,receive_num)
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
