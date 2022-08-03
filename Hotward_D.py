import os
import speech_recognition as sr

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
        print(f"Your Command :  {query}\n")

    except:   
        return "None"
        
    return query.lower()

while True:

    wake_Up = takecommand()

    if 'on' in wake_Up:
        os.startfile('F:\\voice Assistent\\panther.py')

    else:
        print(".........")
