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
from tkinter import scrolledtext, messagebox, simpledialog
import datetime

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
def wolf():
        speak("Ask any question")
        question=get_command()

        app_id = "5AKJW8-WRERQJRA54"
        client = wolframalpha.Client(app_id)
        res = client.query(question)
        wolf.answer = next(res.results).text
        speak(wolf.answer)
def get_wikipedia_summary(topic):
    get_wikipedia_summary.summary = wikipedia.summary(topic, sentences=3)
    print(get_wikipedia_summary.summary)
    speak(get_wikipedia_summary.summary)

def tell_joke():
    joke = pyjokes.get_joke()
    print(joke)
    speak(joke)


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

def how_are_you():
        responses = ["I'm doing well, thank you for asking!", 
                    "I'm great, how can I assist you today?", 
                    "I'm feeling awesome, thanks for asking! How can I help you?", 
                    "I'm functioning perfectly, thank you for asking. How can I be of assistance today?"]
        return random.choice(responses)


class GUI:
    def __init__(self):
        # Initialize the main window
        self.root = tk.Tk()
        self.root.title("Elara - Your Personal Voice Assistant")
        self.root.geometry("1000x1000")
        self.root.configure(bg="#28282B")

        # Create and style label widget for title
        self.title_label = tk.Label(self.root, text="Elara", font=("Roboto", 36), fg="#f8f8f2", bg="#28282B")
        self.title_label.pack(side="top", fill="both", padx=20, pady=20)

        # Create and style textbox widget
        self.textbox = scrolledtext.ScrolledText(self.root, height=30, width=80, font=("Roboto", 16), fg="#f8f8f2", bg="#343434")
        self.textbox.pack(padx=20, pady=20)

        # Create and style button widget
        self.button = tk.Button(self.root, width=50, text="Click to Speak", command=self.start_assistant, font=("Roboto", 18), fg="#f8f8f2", bg="#146C94", activebackground="#44475a", relief="ridge", bd=3)
        self.button.pack(pady=20)

        # Create the menu bar
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # Create the "Help" menu
        self.help_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.menu_bar.add_cascade(label="Options", menu=self.help_menu)

        # Add the "About" option to the "Options" menu
        self.help_menu.add_command(label="About", command=self.show_about_dialog)


        #Add the "Commands List" to the "Options" menu
        self.help_menu.add_command(label="Commands List", command=self.show_command_dialog)

    def show_about_dialog(self):
        messagebox.showinfo("About Elara", "Introducing Elara, your personal virtual assistant designed to make your life easier. Whether you're a busy parent, a business owner, or a student, Elara is here to help by providing efficient and practical support through cutting-edge AI technology. With features such as automated emailing, YouTube, Wikipedia, and Wolfram Alpha integration, Elara is your go-to assistant for quick and up-to-date information on any topic. Need help with calculations or geographic questions? Elara has you covered with Wolfram Alpha integration. Plus, with Elara's streamlined task management and productivity-enhancing features, you can focus on what's important while Elara handles the rest.")


    def show_command_dialog(self):
        # Define the list of commands with descriptions
        commands = [
            "1. open youtube - Elara will open YouTube in your browser.",
            "2. open google - Elara will open Google in your browser.",
            "3. open wikipedia - Elara will open Wikipedia in your browser.",
            "4. open facebook - Elara will open Facebook in your browser.",
            "5. open twitter - Elara will open Twitter in your browser.",
            "6. open yahoo - Elara will open Yahoo in your browser.",
            "7. open stack overflow - Elara will open Stack Overflow in your browser.",
            "8. open amazon - Elara will open Amazon in your browser.",
            "9. show me ... on wikipedia - Elara will give you a small description of the thing you ask for using Wikipedia. For example, 'show me Albert Einstein on wikipedia'.",
            "10. joke - Elara will tell you a joke.",
            "11. write a note - Elara will write a note for you and save it in a .txt file.",
            "12. show the note - Elara will show you the note that you wrote.",
            "13. play some music - Elara will play some music for you.",
            "14. how are you - Elara will tell you how it is feeling.",
            "15. i love you - Elara will respond to your affection.",
            "16. what is your name - Elara will tell you its name.",
            "17. who created you - Elara will tell you who created it.",
            "18. weather - Elara will ask you the city and give you the temperature, humidity and weather description of that city.",
            "19. time - Elara will tell you the current time.",
            "20. wolf - You can ask any computation or geographic questions to Elara using Wolfram Alpha. For example, 'what is the capital of England?' or 'what is 5 * 5'.",
            "21. flip a coin - Elara will flip a coin and give you either heads or tails.",
            "22. exit - Elara will say goodbye and exit."
        ]

        # Combine the list items into a single string with newlines between each item
        message = "\n".join(commands)
        messagebox.showinfo("List of Elara commands", message)

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
    
    def wolf(self):
        speak("Ask any question")
        question=get_command(self.textbox)

        app_id = "5AKJW8-WRERQJRA54"
        client = wolframalpha.Client(app_id)
        res = client.query(question)
        wolf.answer = next(res.results).text
        speak(wolf.answer)

    

    def weather(self):
        api_key="d789fa866167225e96612704efeeeeed"
        base_url="https://api.openweathermap.org/data/2.5/weather?"
        speak("what is the city name")
        city_name=get_command(self.textbox)
        complete_url=base_url+"appid="+api_key+"&q="+city_name
        response = requests.get(complete_url)
        x=response.json()
        if x["cod"]!="404":
            y=x["main"]
            current_temperature = y["temp"]
            fahrenheit=((current_temperature-273.15)*9/5)+32
            rounded_fahrenheit=round(fahrenheit,2)
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            speak(" Temperature in fahrenheit unit is " +
                str(rounded_fahrenheit) +
                "\n humidity in percentage is " +
                str(current_humidiy) +
                "\n description  " +
                str(weather_description))
            print(" Temperature in fahrenheit = " +
                str(rounded_fahrenheit) +
                    "\n humidity (in percentage) = " +
                    str(current_humidiy) +
                    "\n description = " +
                    str(weather_description))
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
                open_website("https://twitter.com/")
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
                self.textbox.insert(tk.END, f"Assistant:{file.read()} + \n")
            elif "what is your name" in command:
                speak("My name is Elara")
                self.textbox.insert(tk.END, "Assistant: " + "My name is Elara" + "\n")

            elif "don't listen" in command or "stop listening" in command:
                speak("I will stop listening for 5 seconds")
                self.textbox.insert(tk.END, f"Assistant: I will stop listening for 5 seconds  \n")
                time.sleep(5)
                speak("Ok Im back")
            elif "music" in command:
                open_website("https://www.youtube.com/live/jfKfPfyJRdk?feature=share")
                speak("Enjoy your music!")
                self.textbox.insert(tk.END, "Assistant: " + "Enjoy your music!"+ "\n")
            elif "coin" in command:
                speak(flip_coin())
            elif "wolf" in command:
                self.wolf()
                self.textbox.insert(tk.END, f"Assistant:{wolf.answer}  \n")
            elif "time" in command:
                speak(ctime())
                self.textbox.insert(tk.END, f"Assistant:{ctime()}  \n")
            elif "weather" in command or "temperature" in command:
                self.weather()
            elif "where is" in command:
                command = command.replace("where is", "")
                location = command
                speak("User asked to Locate")
                speak(location)
                webbrowser.open("https://www.google.nl / maps / place/" + location + "")
                self.textbox.insert(tk.END, f"Assistant:{location}\n")
            elif 'the time' in command:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")   
                speak(f"Sir, the time is {strTime}")
                self.textbox.insert(tk.END, f"Assistant:{strTime}\n")
            elif "stop" in command or "exit" in command or "quit" in command:
                speak("Goodbye!")
                self.button.config(text="Start Listening")
                self.textbox.insert(tk.END, "Assistant: " + "Goodbye" + "\n")
                break
            elif "how are you" in command:
                speak(how_are_you())   
            else:
                speak("Sorry, I didn't understand that.")
                self.textbox.insert(tk.END, "Assistant: " + "Sorry, I didn't understand that" + "\n")
                  
if __name__=='__main__':
    gui=GUI()
    gui.root.mainloop()
