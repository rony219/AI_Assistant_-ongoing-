# import speech_recognition as sr
# import webbrowser
# import pyttsx3

# recognizer = sr.Recognizer()
# engine = pyttsx3.init()

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# def processComand(c):
#     if "open google" in c.lower():
#         webbrowser.open("https://google.com")
#     elif "open facebook" in c.lower():
#         webbrowser.open("https://facebook.com")
#     elif "open you tube" in c.lower():
#         webbrowser.open("https://you tube.com")
#     elif "open instagram" in c.lower():
#         webbrowser.open("https://instagram.com")
    #   elif command.lower().startswith("play"):
    #         song = command.lower().split(" ")[1]
    #         link = musicLibrary.music[song]
    #         webbrowser.open(link)


# if __name__=="__main__":
#     speak("Initializing...")
#     while True:
#         # Listen for the wake word "Pyrocks"

#         # obtain audio from the microphone
#         r = sr.Recognizer()
        
#         print("Recognizing...")

#         # recognize speech using google 
#         try:
#             with sr.Microphone() as source:
#                 print("Listening...")
#                 audio = r.listen(source, timeout=2, phrase_time_limit=1)
#             w = r.recognize_google(audio)
#             if(w.lower() == "Jarvis"):
#                 speak("Yes boss !")
#                 #listen for command
#                 with sr.Microphone() as source:
#                     print("Listening...")
#                     audio = r.listen(source)
#                     command = r.recognize_google(audio)

#                     processComand(command)

#         except Exception as e:
#             print("error; {0}".format(e))


import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Converts text to speech"""
    engine.say(text)
    engine.runAndWait()

def processCommand(command):
    """Processes the recognized command"""
    
    if "open google" in command.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in command.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in command.lower():
        webbrowser.open("https://youtube.com")
    elif "open instagram" in command.lower():
        webbrowser.open("https://instagram.com")
    elif command.lower().startswith("play"):
        song = command.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)


if __name__ == "__main__":
    speak("Initializing...")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                recognizer.adjust_for_ambient_noise(source)  
                audio = recognizer.listen(source)

            try:
                wake_word = recognizer.recognize_google(audio).lower()
                print(f"You said: {wake_word}")

                if (wake_word.lower()=="jarvis"):
                    speak("Yes boss!")
        
                    with sr.Microphone() as source:
                        print("Listening for command...")
                        recognizer.adjust_for_ambient_noise(source)
                        audio = recognizer.listen(source)

                    try:
                        command = recognizer.recognize_google(audio)
                        processCommand(command)
                    except sr.UnknownValueError:
                        print("Sorry, I couldn't understand the command.")
                        speak("Sorry, I couldn't understand the command.")
                    except sr.RequestError as e:
                        print(f"Google Speech API error: {e}")
                        speak("There is a problem with the speech recognition service.")

            except sr.UnknownValueError:
                print("Wake word not recognized. Try again.")
            except sr.RequestError as e:
                print(f"Google Speech API error: {e}")

        except KeyboardInterrupt:
            print("\nExiting...")
            speak("Goodbye!")
            break
