import smtplib
import ssl


def send_email():
    # host = "smtp.gmail.com"
    # port = 465
    # username = 'devopsesi2022@gmail.com'
    # password = 'unkj vlla dtat dxkd'
    # receiver = 'michelgm276@gmail.com'
    # context = ssl.create_default_context()
    # message = """\
Subject: Hi!

 How are you?
 Bye!
"""
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


send_email()
