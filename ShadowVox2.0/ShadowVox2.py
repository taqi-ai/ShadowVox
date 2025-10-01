# Powered by T4Qi Core
# Developed by ShadowByte

import pyttsx3
import tkinter as tk
import webbrowser


def switch_to_chat():
    frame_1.pack_forget()
    frame_2.pack(expand=True)
    speak("Welcome to ShadowVox chat mode. I am ready to listen.")
    entry.focus_set()


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def on_speak():
    sentence = entry.get()
    entry.delete(0, tk.END)

    if sentence.upper() in ["QUIT", "EXIT"]:
        speak("bye bye")
        root.after(1000, root.destroy)
        return
    elif sentence.lower() == "about":
        speak("I am ShadowVox, developed by ShadowByte, powered by T4Qi Core")
    elif "open google" in sentence.lower():
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "open youtube" in sentence.lower():
        speak("Opening Youtube")
        webbrowser.open("https://www.youtube.com")
    elif sentence.lower() == "hello":
        speak("Hello Master ShadowByte!")
    elif sentence.lower() == "who are you":
        speak("I am ShadowVox, your personal voice assistant")
    elif sentence.lower() == "joke":
        speak("Why don’t programmers like nature? Too many bugs.")
    else:
        speak(sentence)


root = tk.Tk()
root.title("ShadowVox 2.0")
root.geometry("800x900")
root.configure(bg="#f0f0f0")
# root.iconbitmap("shadowvox.ico")  # add your custom icon here

frame_1 = tk.Frame(root, bg="#f0f0f0")
frame_2 = tk.Frame(root, bg="#f0f0f0")

title_label = tk.Label(frame_1, text="ShadowVox 2.0", font=("Segoe UI", 18, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

welcome_label = tk.Label(frame_1, text="WELCOME TO ShadowVox — Powered by T4Qi Core", font=("Segoe UI", 12),
                         bg="#f0f0f0")
welcome_label.pack(pady=5)

instructions_label = tk.Label(frame_1, text="""INSTRUCTIONS:\n
• Type any text in the input box and press the 'Speak' button — ShadowVox will speak what you typed.
• Use special easter egg commands like:
    - 'about' → Learn more about ShadowVox.
    - 'quit' or 'exit' → Close the program instantly.
• You can also launch programs using commands like:
    - 'open google' → Opens Google in your default browser.
    - 'open youtube' → Opens YouTube in your default browser.
• More features and commands will be added soon — ShadowVox is evolving!
""",
                               font=("Segoe UI", 11), justify="left", bg="#f0f0f0")
instructions_label.pack(pady=20)

start = tk.Button(frame_1, text="START", font=("Segoe UI", 12, "bold"), bg="black", fg="white",
                  command=switch_to_chat)
start.pack(pady=20)

version_label = tk.Label(frame_1, text="ShadowVox v2.0", font=("Segoe UI", 9), fg="gray", bg="#f0f0f0")
version_label.pack(side="bottom", pady=5)

frame_1.pack(fill="both", expand=True)

writehere_label = tk.Label(frame_2, text="TYPE HERE-", font=("Segoe UI", 11), bg="#f0f0f0")
writehere_label.grid(row=0, column=0, padx=10, pady=10)

entry = tk.Entry(frame_2, width=40, font=("Segoe UI", 11))
entry.grid(row=0, column=1, padx=10, pady=10)

speak_btn = tk.Button(frame_2, text="Speak", font=("Segoe UI", 11, "bold"), bg="black", fg="white", command=on_speak)
speak_btn.grid(row=0, column=2, padx=10, pady=10)

frame_2.grid_columnconfigure(0, weight=1)
frame_2.grid_columnconfigure(1, weight=1)
frame_2.grid_columnconfigure(2, weight=1)

entry.bind("<Return>", lambda event: on_speak())

root.mainloop()
