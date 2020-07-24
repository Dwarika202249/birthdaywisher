import pyttsx3
import speech_recognition as sr
import datetime
import os
import random
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"Dwarika said: {query}\n")

    except Exception as e:   
        speak("Say that again sir...")  
        return "None"
    return query

if __name__ == "__main__":
    speak("Hello sir!, I am jarvis.")
    speak("Happy Birthday to you sir!. on this precious day, what can i do for you, sir!")
    while True:
        query = takeCommand().lower()

        if 'music' in query:
            speak("which song sir!")

        elif 'wish' in query:
            music_dir = 'E:\\Dwarika Chand\\birthday song_jarvis'
            songs = os.listdir(music_dir)
            
            os.startfile(os.path.join(music_dir, songs[0]))
            time.sleep(4)

        elif 'romantic' in query:
            music_dir = 'E:\\Dwarika Chand\\birthday song_jarvis\\secnd'
            songs = os.listdir(music_dir)
            
            os.startfile(os.path.join(music_dir, songs[random.randint(0,len(songs))]))
            time.sleep(4)

        elif 'shayari' in query:
            with open("E:\\Jarvis_AI\\shayris.txt", "r") as reader:
                speak(reader.read())
                
        elif 'shukriya' in query:
            speak("its my pleasure sir!")
            exit()