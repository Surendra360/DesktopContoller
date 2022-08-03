import pyttsx3
import speech_recognition as sr
import webbrowser as web
import time
import keyboard

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',170)

def Speak(audio):
    print("   ")
    print(f": {audio}")
    engine.say(audio)
    print("    ")
    engine.runAndWait()

def takecommand(): 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("          ")
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"Your Command : {query}")

    except:   
        return "None"
        
    return query.lower()
Speak("")
def whatsapp(number,message):
    numb = '+91' + number
    mess = message
    openChat = "https://web.whatsapp.com/send?phone=" + numb + "&text="+mess
    web.open(openChat)
    time.sleep(15)
    keyboard.write(mess)
    time.sleep(2)
    keyboard.press_and_release('.')
    time.sleep(2)
    keyboard.press_and_release('enter')

def whatsapp_Grp(group_id,message):
    openChat = "https://web.whatsapp.com/accept?code=" + group_id
    web.open(openChat)
    time.sleep(15)
    keyboard.write(message)
    time.sleep(10)
    keyboard.press('enter')


def Task():
    Speak("i am ready")

    while True:

        query = takecommand()

        if 'hello' in query: 
            Speak("hello sir ") 


        elif 'whatsapp message' in query:
            query=query.replace("penthar","")
            query=query.replace("send","")
            query=query.replace("whatsapp message","")
            query=query.replace("to","")
            
            
            if 'surendra' in query:
                numb = "9575005647"
                Speak(f"what's the message for{query}")
                mess = takecommand()
                whatsapp(numb,mess)
            
            elif 'Surendra' in query:
                numb = "6266993271"
                Speak(f"what's the message for{query}")
                mess = takecommand()
                whatsapp(numb,mess)

            elif 'umesh bhai' in query:
                numb = "9981176469"
                Speak(f"what's the message for{query}")
                mess = takecommand()
                whatsapp(numb,mess)    

            elif 'family' in query:
                gro ="EWlAjdrLV0H972ksLSIHKs"  
                Speak(f"what's the message for {query}")
                mess = takecommand()
                whatsapp_Grp(gro,mess)

            elif 'stop message' in query:
                Speak("ok sir")
                break
Task()