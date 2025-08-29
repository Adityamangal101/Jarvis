import speech_recognition as sr     #Jarvis.....
import webbrowser
import pyttsx3
import musicLibrary 
import requests
from client import Ai_response

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

newsapi="9eda9622fdaa433a8eeacf4c7f39b4e4"

def process_command(c):
    if "open google" in c.lower():
        webbrowser.open("https://search.brave.com/search?q=google")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/watch?v=UrsmFxEIp5k&t=36421s")
    elif "open whatsapp" in c.lower():
        webbrowser.open("https://web.whatsapp.com/")
    elif "open facebook" in c.lower():
        webbrowser.open("www.facebook.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
       
        # Your existing GET request
        r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=9eda9622fdaa433a8eeacf4c7f39b4e4")

        # Convert the response to JSON
        data = r.json()

        # Extract and print the headlines
        if data["status"] == "ok":
            articles = data["articles"]
            print("\n📰 Top Headlines:\n")
            for i, article in enumerate(articles[:5], start=1):  # Limit to top 5
                speak(f"{i}. {article['title']}")
        else:
            print("❌ Failed to fetch news:", data.get("message", "Unknown error"))
    
    else:  #Let Ai handle the request
        output=Ai_response(c)
        speak(output)

       
       
if __name__ =="__main__":
    speak("Initializing Jarvis....")
    while True:
        # Initialize recognizer,We Firstly listen for wake word "Jarvis"
        recognizer = sr.Recognizer()
        print("recognizing....")
        try:
            # Use the default microphone as the audio source
            with sr.Microphone() as source:
                print("Listening..")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source,phrase_time_limit=2,timeout=2.5)
            # Recognize speech using Google Web Speech API
            wake_word = recognizer.recognize_google(audio)
            
            if("Jarvis" in wake_word):
                speak("Hello sir how can i help you")
                #Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active")
                    recognizer.adjust_for_ambient_noise(source)
                    audio = recognizer.listen(source,phrase_time_limit=2,timeout=2)
                # Recognize speech using Google Web Speech API
                command = recognizer.recognize_google(audio, language="en-IN")

                process_command(command)
           
        except Exception as e:
            print(f" error: {e}")

        