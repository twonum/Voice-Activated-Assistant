from neuralintents import BasicAssistant
import speech_recognition as sr
import pyttsx3 as tts
import sys

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
speaker = tts.init()
speaker.setProperty('rate', 150)

# Sample todo list
todo_list = ['Go Shopping', 'Clean Room', 'Record Video']

def create_note():
    global recognizer

    speaker.say("What do you want to write in your note?")
    speaker.runAndWait()
    done = False
    while not done:
        try:
            with sr.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                note = recognizer.recognize_google(audio)
                
                speaker.say("Choose a filename")
                speaker.runAndWait()
                
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                filename = recognizer.recognize_google(audio).lower()
                
                with open(f"{filename}.txt", 'w') as f:
                    f.write(note)
                    done = True
                    speaker.say(f"Note saved as {filename}")
                    speaker.runAndWait()
        except sr.UnknownValueError:
            recognizer = sr.Recognizer()
            speaker.say("I did not understand you! Please try again!")
            speaker.runAndWait()

def add_todo():
    global recognizer
    speaker.say("What do you want to add?")
    speaker.runAndWait()
    done = False
    while not done:
        try:
            with sr.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                item = recognizer.recognize_google(audio).lower()
                todo_list.append(item)
                done = True
                speaker.say(f"{item} added to the list!")
                speaker.runAndWait()
        except sr.UnknownValueError:
            recognizer = sr.Recognizer()
            speaker.say("I did not understand you! Please try again!")
            speaker.runAndWait()

def show_todo():
    speaker.say("The items on your todo list are the following:")
    for item in todo_list:
        speaker.say(item)
    speaker.runAndWait()

def greetings():
    speaker.say("Hello there! How can I help you today?")
    speaker.runAndWait()

def exit_program():
    speaker.say("Goodbye!")
    speaker.runAndWait()
    sys.exit()

# Start the assistant
assistant = BasicAssistant('VoiceRec.json')

# Start the assistant
while True:
    try:
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)
            message = recognizer.recognize_google(audio).lower()
            assistant.request(message)
    except sr.UnknownValueError:
        recognizer = sr.Recognizer()
        speaker.say("I did not understand you! Please try again!")
        speaker.runAndWait()
