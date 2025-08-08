import speech_recognition as sr
import tkinter as tk
import threading

def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something cool! (or say 'exit' to quit)")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        text = text.lower()
        print("Recognized Text:", text)
        text_box.insert(tk.END, text + "\n") 
        if text == "exit":
            root.destroy() 
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def start_recognition_thread():
    recognition_thread = threading.Thread(target=recognize_speech)
    recognition_thread.start()

root = tk.Tk()
root.title("Speech Recognition")

text_box = tk.Text(root, wrap=tk.WORD)
text_box.pack(expand=True, fill="both")

start_button = tk.Button(root, text="Start", command=start_recognition_thread)
start_button.pack()

root.mainloop()