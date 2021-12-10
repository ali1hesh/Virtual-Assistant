import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("BONJOUR!")

    elif hour>=12 and hour<18:
        speak("bonne après-midi!")   

    else:
        speak("Bonsoir!")  

    speak("Hi i am Alaadin. What do you need me to do sir")       

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        
        print("I was not able to understand that. Could you please repeat yourself")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('abcd@gmail.com', 'password of account')
    server.sendmail('efgh@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    
        query = takeCommand().lower()

        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open lenovo' in query:
            webbrowser.open("lenovo.com")

        elif 'open google' in query:
            webbrowser.open("google.in")  
        
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")     

        elif 'play music' in query:
            music_dir = 'D:\music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open vscode' in query:
            codePath = "C:\\Users\\ali\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to abc' in query:
            try:
                speak("Speak! what you want to say?")
                content = takeCommand()
                to = "abcd@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Human! i was not able to send this email")  
        elif 'quit' in query:
               os._exit(0)
        
                
                
                  
