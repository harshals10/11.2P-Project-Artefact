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

GPIO.setmode(GPIO.BCM)
PIR_PIN = 2
GPIO.setup(PIR_PIN, GPIO.IN)

    while True:
        if GPIO.input(PIR_PIN):
            print("Motion Detected!")
            sendTo = 'sharma.harshal55@gmail.com'
            emailSubject = "Motion Detected"
            emailContent = "Someone is there"
            sender.sendmail(sendTo, emailSubject, emailContent)
            print("Email sent")
        time.sleep(1)
    print("Quit")
    GPIO.cleanup()