import RPi.GPIO as GPIO
import time
import smtplib

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
GMAIL_USERNAME = 'harshalsharma414@gmail.com'
GMAIL_PASSWORD = 'HarshalSharma10#'

class Emailer:
    def sendmail(self, recipient, subject, content):
        headers = ["FROM: " + GMAIL_USERNAME, "Subject: " + subject, "To: " + recipient, "MIME-Version: 1.0", "Content-Type: text/html"]
        headers = "\r\n".join(headers)

        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        session.ehlo()
        session.starttls()
        session.ehlo()

        session.login(GMAIL_USERNAME, GMAIL_PASSWORD)

        session.sendmail(GMAIL_USERNAME, recipient, headers + "\r\n\r\n" + content)
        session.quit

sender = Emailer()

channel = 3
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
    if GPIO.input(channel):
        print("Sound Detected!")
        sendTo = 'sharma.harshal55@gmail.com'
        emailSubject = "Sound Detected"
        emailContent = "Someone is Present"
        sender.sendmail(sendTo, emailSubject, emailContent)
        print("Email sent")
    else:
        print("Sound Not Detected!")

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel, callback)

while True:
    time.sleep(1)