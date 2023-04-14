import pyttsx3
import speech_recognition as sr
import datetime
import random
import wikipedia
import webbrowser
import pyjokes
import time 
import wolframalpha
from time import ctime
import requests
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("My name is Elara. How can I help you today?")

def get_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}\n")
        except sr.UnknownValueError:
            command = ""
            print("Sorry, I didn't catch that.")
    return command

def open_website(url):
    webbrowser.open(url)

def get_wikipedia_summary(topic):
    summary = wikipedia.summary(topic, sentences=3)
    print(summary)
    speak(summary)

def tell_joke():
    joke = pyjokes.get_joke()
    print(joke)
    speak(joke)

def wolf():
    speak("Ask any question")
    question=get_command()

    #question = input('Question: ')
    app_id = "5AKJW8-WRERQJRA54"
    client = wolframalpha.Client(app_id)
    res = client.query(question)
    answer = next(res.results).text
    speak(answer)

def flip_coin():
    return random.choice(["You got Heads","You got Tails"])
'''''''''
def send_email(to, subject, body):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('your_email@gmail.com', 'your_password')
    message = f"Subject: {subject}\n\n{body}"
    server.sendmail('your_email@gmail.com', to, message)
    server.quit()
'''''''''
def write_note():
    speak("What should I write down?")
    note_text = get_command()
    now = datetime.datetime.now()
    with open("notes.txt", "a") as file:
        file.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] {note_text}\n")
    speak("Note saved.")

def show_note():
    speak("Showing Notes")
    file = open("notes.txt", "r")
    print(file.read())
    speak(file.read(1))

def weather():
    api_key="d789fa866167225e96612704efeeeeed"
    base_url="https://api.openweathermap.org/data/2.5/weather?"
    speak("what is the city name")
    city_name=get_command()
    complete_url=base_url+"appid="+api_key+"&q="+city_name
    response = requests.get(complete_url)
    x=response.json()
    if x["cod"]!="404":
        y=x["main"]
        current_temperature = y["temp"]
        fahrenheit=((current_temperature-273.15)*9/5)+32
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        speak(" Temperature in fahrenheit unit is " +
            str(fahrenheit) +
            "\n humidity in percentage is " +
            str(current_humidiy) +
            "\n description  " +
            str(weather_description))
        print(" Temperature in fahrenheit = " +
            str(fahrenheit) +
                "\n humidity (in percentage) = " +
                str(current_humidiy) +
                "\n description = " +
                str(weather_description))

def main():
    greet()
    while True:
        command = get_command()
        if "open youtube" in command:
            open_website("https://www.youtube.com/")
            speak("Opening YouTube")
        elif "open google" in command:
            open_website("https://www.google.com/")
            speak("Opening Google")
        elif "news" in command:
            open_website("https://news.google.com/home?hl=en-US&gl=US&ceid=US:en")
            speak("Here are some headlines form Google News")
        elif "open stack overflow" in command:
            open_website("https://stackoverflow.com/")
            speak("Opening Stack Overflow")
        elif "open wikipedia" in command:
            open_website("https://www.wikipedia.org/")
            speak("Opening Wikipedia")
        elif 'search'  in command:
            command = command.replace("search", "")
            webbrowser.open_new_tab(command)
        	
        elif "open facebook" in command:
            open_website("https://www.facebook.com/")
            speak("Opening Facebook")
        elif "open twitter" in command:
            open_website("https://twitter.com/home")
            speak("Opening Twitter")
        elif "open yahoo" in command:
            open_website("https://www.yahoo.com/")
            speak("Opening Yahoo")
        elif "open amazon" in command:
            open_website("https://www.amazon.com/")
            speak("Opening Amazon")
        elif "wikipedia" in command:
            topic = command.replace("wikipedia", "")
            get_wikipedia_summary(topic)
        elif "joke" in command:
            tell_joke()
        elif "write a note" in command:
            write_note()
        elif "show the note" in command:
            show_note()
        elif "how are you" in command:
            speak("I am well")
        elif "what is your name" in command:
            speak("My name is Elera")
        
        elif "music" in command:
            open_website("https://www.youtube.com/live/jfKfPfyJRdk?feature=share")
        elif "i love you" in command:
            speak("Ok, dont care")
        elif 'wikipedia' in command:
            speak('Searching Wikipedia...')
            command = command.replace("wikipedia", "")
            results = wikipedia.summary(command, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif "who created you" in command:
            speak("Its a mystery lol")
        elif "weather" in command:
            weather()
        elif "time" in command:
            speak(ctime())
        elif "exit" in command:
            speak("Goodbye.")
            break
        elif "wolf" in command:
            wolf()
        elif "flip a coin" in command:
            speak(flip_coin())

    
        
if __name__ == "__main__":
    main()

'''''''''''
        elif "send email" in command:
            speak("Who is the recipient?")
            recipient = get_command()
            speak("What is the subject?")
            subject = get_command()
            speak("What would you like to say?")
            body = get_command()
            send_email(recipient, subject, body)
            speak("Email sent.")
        '''''''''''