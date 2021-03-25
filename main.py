import speech_recognition as sr
import pyttsx3
import pywhatkit
listener = sr.Recognizer()
speech = pyttsx3.init()
siri_tone =speech.getProperty('voices')
speech.setProperty('voice', siri_tone[1].id)
def say(text):
    speech.say(text)
    speech.runAndWait()
def Command():
    try:
        with sr.Microphone() as source:
            print("Hey boss")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
            return command.lower()
    except:
        pass
def WhatsApp(name, receiver):
    pywhatkit.sendwhatmsg(str(receiver), name, 20, 52)
contact_list = {
    "noble": "+919360492626",
    "singh": "+916369580556",
    "subash": "+918489295091",
    "harish": "+919445155405"
}
def get_msg():
    say("Hello boss Siri Here")
    say("How come I can help you")
    task = Command()
    say("To whom you need to send the message")
    name = Command()
    receiver = contact_list[name]
    print(receiver)
    say("What's the matter")
    subject = Command()
    WhatsApp(name, receiver)
get_msg()

# while True:
#      get_msg()