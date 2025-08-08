import speech_recognition as sr#I also import PyAudio and SpeechRecognition libraries.

r = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as source:
            print("Say something cool! (or say 'exit' to quit)") 
            audio = r.listen(source)
            text = r.recognize_google(audio)
            text = text.lower()
            
            if text == "exit":  # Break condition
                print("Exiting...")
                break
            
            print("Recognized Text:", text)
            
    except:
        print("you are fool!")
        r = sr.Recognizer()
        continue