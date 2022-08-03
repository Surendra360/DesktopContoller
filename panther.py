import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit 
import wikipedia
import os
import pyautogui
import requests
import PyPDF2
from gtts import gTTS
from pytube import YouTube
import datetime   
from playsound import playsound  
import keyboard
from googletrans import Translator


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',170)

def Speak(Audio):
    print("   ")
    print(f": {Audio}")
    engine.say(Audio)
    print("    ")
    engine.runAndWait()

def Wishme():
    hour =int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        Speak("Good morning Sir !")

    elif hour >= 12 and hour<18:
        Speak("Good Afternoon Sir !")

    else:
        Speak("Good Evening sir !")

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
   

def TaskExe():
    Wishme()
    Speak("please tell me  your name")
    name = takecommand()
    Speak(f"hello {name}")
    Speak(f"How Can I Help You{name}")

    def Music():
        Speak("Tell Me The Name oF The Song!")
        musicName = takecommand()

        if 'Hanuman Chalisa' in musicName:
            os.startfile('C:\\Users\\suren\\Music\\Hanuman Chalisa.mp3')

        else:
            pywhatkit.playonyt(musicName)

        Speak("Your Song Has Been Started! , Enjoy Sir!")

    def OpenApps():
        Speak("Ok Sir , Wait A Second!")
        
        if 'vs code' in query:
            os.startfile("C:\\Users\\suren\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

        elif 'telegram' in query:
            os.startfile("E:\\Telegram Desktop\\Telegram.exe")

        elif 'notepad' in query:
            os.startfile("%windir%\\system32\\notepad.exe")
            if 'new' in query:
                keyboard.press_and_release("ctrl+n")    

        elif 'chrome' in query:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        
        elif 'facebook' in query:
            webbrowser.open('https://www.facebook.com/')

        elif 'notepa' in query:
            os.startfile("%windir%\\system32\\notepad.exe")

        elif 'maps' in query:
            webbrowser.open('https://www.google.com/maps/@28.7091225,77.2749958,15z')

        elif 'youtube' in query:
            webbrowser.open('https://www.youtube.com')

        Speak("Your Command Has Been Completed Sir!")
         
    def Whatsapp(): 
        Speak("Tell Me The Name Of The Person!")
        name = takecommand()

        if 'uttam' in name:
            Speak(f"Tell Me The Message for{name} !")
            msg = takecommand()  
            Speak("Tell Me The Time Sir!")
            Speak("Time In Hour")
            hour = int(takecommand())
            Speak("Time In Minutes!")
            min = int(takecommand())
            pywhatkit.sendwhatmsg("+917617209817",msg,hour,min,20)
            Speak("Ok Sir , Sending Whatsapp Message !")
        elif 'surendra' in name:
            Speak("Tell Me The Message !")
            msg = takecommand()
            Speak("Tell Me The Time Sir!")
            Speak("Time In Hour")
            hour = int(takecommand())
            Speak("Time In Minutes!")
            min = int(takecommand())
            pywhatkit.sendwhatmsg("+916266996231",msg,hour,min,20)
            Speak("Ok Sir , Sending Whatsapp Massage !")
        else:
            Speak("Tell Me The Phone Number:")
            phone = int(takecommand())
            ph = '+91' + phone
            Speak("Tell Me The Message !")
            msg = takecommand()
            Speak("Tell Me The Time Sir!")
            Speak("Time In Hour")
            hour = int(takecommand())
            Speak("Time In Minutes!")
            min = int(takecommand())
            pywhatkit.sendwhatmsg(ph,msg,hour,min,20)
            Speak("Ok Sir , Sending Whatsapp Massage !")    


    def Reader():
        Speak("Tell me the name of the book!")
        name = takecommand()
        
        if 'operating system' in name:
            os.startfile('F:\\book\\unit 1.pdf')
            book = open('F:\\book\\unit 1.pdf','rb')
            pdfreader = PyPDF2.PdfFileReader(book)
            pages = pdfreader.getNumPages()
            Speak(f"Number of page in this books are {pages}")
            Speak("Frome which page i have to start reading ?") 
            numPage = int(input("Enter page no: "))
            page = pdfreader.getpage(numPage)
            text = page.extractText()
            Speak("In which language , I have to read ?")
            lang = takecommand()

            if 'hindi' in lang:
                transl = Translator()
                textHin = transl.translate(text,'hi')
                textm = textHin.text
                speech = gTTS(text = textm)  
                try:
                    speech.save('book.mp3')
                    playsound('book.mp3')
                
                except:
                    playsound('book.mp3')

            else:
                Speak(text)
               
    def CloseAPPS():
        Speak("Ok Sir , Wait A second!")

        if 'youtube' in query:
            os.system("TASKKILL /F /im Chrome.exe")

        elif 'chrome' in query:
            os.system("TASKKILL /f /im Chrome.exe")

        elif 'telegram' in query:
            os.system("TASKKILL /F /im Telegram.exe")

        elif 'vs code' in query:
            os.system("TASKKILL /F /im code.exe")

        elif 'notepad' in query:
            os.system("TASKKILL /F /im notepad.exe")

        elif 'instagram' in query:
            os.system("TASKKILL /F /im chrome.exe")
            
        Speak("Your Command Has Been Succesfully Completed!")

    def YoutubeAuto():
        Speak("Whats Your Command ?")
        comm = takecommand()

        if 'pause' in comm:
            keyboard.press_and_release('space bar')

        elif 'next' in comm:
            keyboard.press_and_release('shift+n')

        elif 'mute' in comm:
            keyboard.press_and_release('m')

        elif 'skip' in comm:
            keyboard.press_and_release('l')

        elif 'back' in comm:
            keyboard.press_and_release('j')

        elif 'full screen' in comm:
            keyboard.press_and_release('f')

        elif 'film mode' in comm:
            keyboard.press_and_release('t')

        Speak("Done Sir")
     
    def TakeHindi():
        command = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening..........")
            command.pause_threshold = 1
            audio = command.listen(source)

            try:
                print("Recognizing............")    
                query = command.recognize_google(audio, language='hi')
                print(f"Your said : {query}")

        
            except Exception as Error:   
                return "none"
        
            return query.lower()

    def Tran():
        Speak("Tell Me The line !")
        line = TakeHindi()
        translate = Translator()
        result = translate.translate(line)
        Taxt = result.text
        Speak("The Translation For this line is : "+Text)

    def ChromeAuto():
        Speak("Chrome Automation started!")

        command = takecommand()

        if 'close this tab' in command:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in command:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in command:
            keyboard.press_and_release('ctrl + n')

    def screenshot():
        Speak("Ok Boss , What Should I Name That File ?")
        path = takecommand()
        path1name = path + ".png"
        path1 = "E:\\Kaushik Shresth\\Screenshots\\"+ path1name
        kk = pyautogui.screenshot()
        kk.save(path1)
        os.startfile("E:\\Kaushik Shresth\\Screenshots")
        Speak("Here Is Your ScreenShot") 

    while True:

        query = takecommand()

        if 'hello' in query:
            Speak("Hello Sir , I Am Your Personal AI Assistant!")
            Speak("How May I Help You?")

        elif 'whatsapp' in query:
            os.startfile('F:\\voice Assistent\\message.py')
            break

        elif 'how are you' in query:
            Speak("I Am Fine Sir!")
            Speak("Whats About YOU?")

        elif 'stop' in query:
            Speak("Ok Sir , You Can Call Me Anytime !")
            Speak(" Just Say  Wacke Up panther")
            break

        elif 'youtube search' in query:
            Speak("OK sIR , This Is What I found For Your Search!")
            query = query.replace("panther","")
            query = query.replace("youtube search","")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            Speak("Done Sir!")

        elif 'website' in query:
            Speak("Ok Sir , Launching.....")
            query = query.replace("panther","")
            query = query.replace("website","")
            query = query.replace(" ","")
            web1 = query.replace("open","")
            web2 = 'https://www.' + web1 + '.com'
            webbrowser.open(web2)
            Speak("Launched!")

        elif 'launch' in query:
            Speak("Tell Me The Name Of The Website!")
            name = takecommand()
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            Speak("Done Sir!")

        elif 'wikipedia' in query:
            Speak("Searching Wikipedia.....")
            query = query.replace("panther","")
            query = query.replace("wikipedia","")
            wiki = wikipedia.summary(query,2)
            Speak(f"According To Wikipedia : {wiki}")

        elif 'screenshot' in query:
            screenshot()

        elif 'open facebook' in query:
            OpenApps()

        elif 'open instagram' in query:
            OpenApps()

        elif 'open maps' in query:
            OpenApps()

        elif 'open vs code' in query:
            OpenApps()

        elif 'open notepad'in query:
            OpenApps()

        elif 'open youtube' in query:
            OpenApps()
            
        elif 'open telegram' in query:
            OpenApps()

        elif 'open chrome' in query:
            OpenApps()

        elif 'close chrome' in query:
            CloseAPPS()

        elif 'music' in query:
            Music()

        elif 'close telegram' in query:
            CloseAPPS()

        elif 'close instagram' in query:
            CloseAPPS()

        elif 'close vs code' in query:
            CloseAPPS()

        elif 'close notepad' in query:
            CloseAPPS()

        elif 'pause' in query:
            keyboard.press_and_release('k')

        elif 'next' in query:
            keyboard.press_and_release('shift+n')

        elif 'mute' in query:
            keyboard.press_and_release('m')

        elif 'skip' in query:
            keyboard.press_and_release('l')

        elif 'back' in query:
            keyboard.press_and_release('j')

        elif 'full screen' in query:
            keyboard.press_and_release('f')

        elif 'film mode' in query:
            keyboard.press_and_release('t')

        elif 'youtube tool' in query:
            YoutubeAuto()

        elif 'close the tab' in query:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')

        elif 'chrome automation' in query:
            ChromeAuto()

        elif 'repeat my word' in query:
            Speak("Speak Sir!")
            jj = takecommand()
            Speak(f"You Said : {jj}")

        elif 'my location' in query:
            Speak("Ok Sir , Wait A Second!")
            webbrowser.open('https://www.google.com/maps/place/A-Sector,+Gopal+Nagar,+Bhopal,+Madhya+Pradesh+462022/@23.2458573,77.4907322,17z/data=!3m1!4b1!4m5!3m4!1s0x397c41e828fb430d:0xa54fc1eccd8662f2!8m2!3d23.2459388!4d77.4927793')

        elif 'alarm' in query:
            Speak("Enter The Time !")
            time = input(": Enter The Time :")

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")

                if now == time:
                    Speak("Time To Wake Up Sir!")
                    playsound('')
                    Speak("Alarm Closed!")

                elif now>time:
                    break

        elif 'google search' in query:
            import wikipedia as googleScrap
            query = query.replace("panther","")
            query = query.replace("google search","")
            query = query.replace("google","")
            Speak("This Is What I Found On The Web!")
            pywhatkit.search(query)

            try:
                result = googleScrap.summary(query,2)
                Speak(result)

            except:
                Speak("No Speakable Data Available!")
        
        elif 'translator' in query:
            Tran()

        elif 'book read' in query:
            Reader()

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            Speak(f"sir , the time is {strTime}")

        elif 'chat' in query:
            Whatsapp()
TaskExe()