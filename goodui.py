import tkinter as tk
from tkinter import Label, Button
import speech_recognition as sr
from PIL import Image, ImageTk

# Initialize Tkinter window
root = tk.Tk()
root.title("Speech Recognition")
root.geometry("600x400")
root.configure(bg="black")  # Background color

# Load and display neon image
image_path = "ChatGPT Image Apr 4, 2025, 10_29_39 AM (1).png"  #  the  actual file path
img = Image.open(image_path)
img = img.resize((200, 200))  # Resize image
photo = ImageTk.PhotoImage(img)

image_label = Label(root, image=photo, bg="black")
image_label.pack(pady=10)

# Label to display recognized text
output_label = Label(root, text="Press 'Start' to Speak", fg="cyan", bg="black", font=("Arial", 14, "bold"))
output_label.pack(pady=20)

# Speech recognition function
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        output_label.config(text="Listening...", fg="orange")
        root.update_idletasks()

        output_label.config(text="Processing...", fg="green")
            
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            output_label.config(text=f"Recognized: {text}", fg="lime")
        except sr.UnknownValueError:
            output_label.config(text="Could not understand audio", fg="red")
        except sr.RequestError:
            output_label.config(text="API request error", fg="red")

# Button to start speech recognition
start_button = Button(root, text="Let's Start", command=recognize_speech, bg="orange", fg="white", font=("Arial", 12, "bold"))
start_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
