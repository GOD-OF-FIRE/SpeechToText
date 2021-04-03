import pyttsx3
import speech_recognition as sr
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices',voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning....")
        #r.pause_threshold = 1
        r.energy_threshold = 3000
        audio = r.listen(source)
        
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        #speak(f"You said: {query}\n")
        print(f"You said: {query}\n")
    except Exception as e:
        #print(e)
        print("I can't hear that sir, please say it again.")
        return "None"
    return query
if __name__ =="__main__":
    while True:
        query = takecommand()