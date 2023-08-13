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

def send_sms(mess,send_num,receive_num):
    client = Client(account_sid, auth_token)
    message = client.messages.create(from_=send_num,body=mess,to=receive_num)
    print(message.sid)
