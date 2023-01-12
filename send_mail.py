import smtplib
def send_mail(reciver, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('testamail8006@gmail.com', 'ckepsgtppztlzpid')
    msg = f"{message}"
    qabul_qiluvchi = reciver
    server.sendmail('testamail8006@gmail.com', qabul_qiluvchi, msg)
    print("message send")
send_mail("xushnudbekxushnudbek59@gmail.com", 'Hello teacher! This message is sent by Begzod')