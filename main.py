# main.py
import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageTk
import os
from speechtotext import get_speech_text
import threading

SIGN_PATH = "assets/signs/"

def show_signs(text, frame):
    for widget in frame.winfo_children():
        widget.destroy()

    words = text.split()

    for word in words:
        gif_path = os.path.join(SIGN_PATH, f"{word}.gif")
        if not os.path.exists(gif_path):
            # fallback: letter by letter
            for char in word:
                char_path = os.path.join(SIGN_PATH, f"{char}.gif")
                if os.path.exists(char_path):
                    display_gif(char_path, frame)
        else:
            display_gif(gif_path, frame)

def display_gif(path, frame):
    try:
        # Load the entire animated gif
        frames = []
        img = Image.open(path)

        # Resize each frame and store it
        try:
            while True:
                frame_image = img.copy()
                frame_image = frame_image.resize((180, 180))  # Adjust size here
                frames.append(ImageTk.PhotoImage(frame_image))
                img.seek(len(frames))  # Go to next frame
        except EOFError:
            pass  # End of frames

        # Create a label and animate it
        gif_label = Label(frame)
        gif_label.pack(pady=5)

        def update(index):
            gif_label.config(image=frames[index])
            gif_label.image = frames[index]
            frame.after(100, update, (index + 1) % len(frames))  # 100ms per frame

        update(0)

    except Exception as e:
        print(f"Error displaying gif: {e}")

def recognize_and_translate(frame, label):
    label.config(text="Listening...")
    label.update()

    text = get_speech_text()

    label.config(text="Processing...")
    label.update()

    if text:
        label.config(text=f"You said: {text}")
        show_signs(text, frame)
    else:
        label.config(text="Could not understand. Try again.")

# GUI Setup
root = tk.Tk()
root.title("Speech to Sign Language")
root.geometry("700x400")
root.configure(bg="white")

label = Label(root, text="Speech to Sign Language", font=("Helvetica", 16), bg="white")
label.pack(pady=10)

sign_frame = tk.Frame(root, bg="white")
sign_frame.pack(pady=10)

btn = Button(root, text="🎤 Speak", font=("Helvetica", 14),
             command=lambda: threading.Thread(target=recognize_and_translate, args=(sign_frame, label)).start())

btn.pack(pady=10)

root.mainloop()
