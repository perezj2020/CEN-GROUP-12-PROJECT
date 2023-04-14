import pyttsx3
import speech_recognition as sr
import datetime
import random
import wikipedia
import webbrowser
import pyjokes
import tkinter as tk
import threading
from tkinter import scrolledtext
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

root = tk.Tk()
root.geometry("400x400")
root.title("Elara - Your Personal Assistant")

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

def get_command(textbox):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        textbox.insert(tk.END, "Assistant: " + "Listening..." + "\n")
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
    get_wikipedia_summary.summary = wikipedia.summary(topic, sentences=3)
    print(get_wikipedia_summary.summary)
    speak(get_wikipedia_summary.summary)

def tell_joke():
    joke = pyjokes.get_joke()
    print(joke)
    speak(joke)

def wolf():
    speak("Ask any question")
    question=get_command()

    app_id = "5AKJW8-WRERQJRA54"
    client = wolframalpha.Client(app_id)
    res = client.query(question)
    wolf.answer = next(res.results).text
    speak(wolf.answer)

def flip_coin():
    return random.choice(["You got Heads","You got Tails"])

def write_note(self):
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
class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Elara Voice Assistant")
        self.root.geometry("1000x1000")
        self.textbox = scrolledtext.ScrolledText(self.root, height=20, width=80, font=("Times New Roman", 16, "bold"), fg="white", bg="gray25")
        self.textbox.pack()
        
        self.button = tk.Button(self.root, text="Click to Speak", command=self.start_assistant, font=("Helvetica", 18), fg="white", bg="DodgerBlue2", activebackground="DodgerBlue3")
        self.button.pack()

        self.root.mainloop()


    def start_assistant(self):
        self.button.config(text="Listening...")        
        threading.Thread(target=self.run_assistant).start()
    
    def write_note(self):
        speak("What should I write down?")
        note_text = get_command(self.textbox)
        now = datetime.datetime.now()
        with open("notes.txt", "a") as file:
            file.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] {note_text}\n")
        speak("Note saved.")

    def run_assistant(self):
        greet()
        self.textbox.insert(tk.END, "Assistant: " + "My name is Elara. How can I help you today?" + "\n")
        while True:
            command = get_command(self.textbox)
            self.textbox.insert(tk.END, f"You: {command}\n")
            if "open youtube" in command:
                open_website("https://www.youtube.com/")
                speak("Opening YouTube")
                self.textbox.insert(tk.END, "Assistant: " + "Opening Youtube" + "\n")
            elif "open google" in command:
                open_website("https://www.google.com/")
                speak("Opening Google")
                self.textbox.insert(tk.END, "Assistant: " + "Opening Google" + "\n")
            elif "news" in command:
                open_website("https://news.google.com/home?hl=en-US&gl=US&ceid=US:en")
                speak("Here are some headlines from Google News")
                self.textbox.insert(tk.END, "Assistant: " + "Here are some headlines from Google News" + "\n")
            elif "open stack overflow" in command:
                open_website("https://stackoverflow.com/")
                speak("Opening Stack Overflow")
                self.textbox.insert(tk.END, "Assistant: " + "Opening Stack Overflow" + "\n")
            elif "open wikipedia" in command:
                open_website("https://www.wikipedia.org/")
                speak("Opening Wikipedia")
                self.textbox.insert(tk.END, "Assistant: " + "Opening Wikipedia" + "\n")
            elif 'search' in command:
                command = command.replace("search", "")
                webbrowser.open_new_tab(command)
                self.textbox.insert(tk.END, f"Assistant: search{command}\n")

            elif "open facebook" in command:
                open_website("https://www.facebook.com/")
                speak("Opening Facebook")
                self.textbox.insert(tk.END, "Assistant: " + "Opening Facebook" + "\n")
            elif "open twitter" in command:
                open_website("https://twitter.com/home")
                speak("Opening Twitter")
                self.textbox.insert(tk.END, "Assistant: " + "Opening Twitter" + "\n")
            elif "open yahoo" in command:
                open_website("https://www.yahoo.com/")
                speak("Opening Yahoo")
                self.textbox.insert(tk.END, "Assistant: " + "Opening Yahoo" + "\n")
            elif "open amazon" in command:
                open_website("https://www.amazon.com/")
                speak("Opening Amazon")
                self.textbox.insert(tk.END, "Assistant: " + "Opening Amazon" + "\n")
            elif "wikipedia" in command:
                topic = command.replace("wikipedia", "")
                get_wikipedia_summary(topic)
                self.textbox.insert(tk.END, f"Assistant:{get_wikipedia_summary.summary} \n")
            elif "joke" in command:
                tell_joke()
            elif "write a note" in command:
                self.write_note()
            elif "show the note" in command:
                show_note()
                file = open("notes.txt", "r")
                self.textbox.insert(tk.END, f"Assistant:{file.read()} \n")
            elif "how are you" in command:
                speak("I am well")
                self.textbox.insert(tk.END, "Assistant: " + "I am well" + "\n")
            elif "what is your name" in command:
                speak("My name is Elera")
                self.textbox.insert(tk.END, "Assistant: " + "My name is Elera" + "\n")

            elif "music" in command:
                open_website("https://www.youtube.com/live/jfKfPfyJRdk?feature=share")
                speak("Enjoy your music!")
                self.textbox.insert(tk.END, "Assistant: " + "Enjoy your music!"+ "\n")
            elif "coin" in command:
                speak(flip_coin())
            elif "wolf" in command:
                wolf()
                self.textbox.insert(tk.END, f"Assistant:{wolf.answer}  \n")
            elif "time" in command:
                speak(ctime())
                self.textbox.insert(tk.END, f"Assistant:{ctime()}  \n")
            elif "weather" in command:
                weather()

            elif "stop" in command or "exit" in command or "quit" in command:
                speak("Goodbye!")
                self.button.config(text="Start Listening")
                self.textbox.insert(tk.END, "Assistant: " + "Goodbye" + "\n")
                break
            else:
                speak("Sorry, I didn't understand that.")
                self.textbox.insert(tk.END, "Assistant: " + "Sorry, I didn't understand that" + "\n")
                  
if __name__=='__main__':
    gui=GUI()
