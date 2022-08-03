import webbrowser as web
import time
import keyboard

def whatsapp(number,massage):
    numb = '+91' + number
    mess = message
    open_chat = "https://web.whatsapp.com/send?photo=" + numb + "&text=" + message
    web.open(open_chat)
    time.sleep(15)
    keyboard.press(message)
    time.sleep(10)
    keyboard.press('enter')

def whatsapp_Grp(group_id,message):
    open_chat = "https://web.whatsapp.com/accept?code=" + group_id
    web.open(open_chat)
    time.sleep(15)
    keyboard.write(message)
    time.sleep(10)
    keyboard.press('enter')

