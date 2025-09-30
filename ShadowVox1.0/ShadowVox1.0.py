
#Powered by T4Qi Core
#Developed by ShadowByte

import pyttsx3

print("STARTING ShadowVox...\n")
print("-" * 30)
print("Version   : 1.0")
print("Developer : ShadowByte")
print("Engine    : T4Qi Core")
print("-" * 30 + "\n")

# Function to speak
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Intro voice
speak("Hello, welcome to ShadowVox version 1 point 0, powered by T4Qi Core")

print("PRESS !,QUIT,EXIT TO EXIT ShadowVox")

while True:
    sentence = input("ENTER ANYTHING:\n")
    if sentence == "!" or sentence.upper()=="EXIT" or sentence.upper()=="QUIT":
        speak("bye bye")
        break
    if sentence.lower() == "about":
        speak("I am ShadowVox, developed by ShadowByte, powered by T4Qi Core")
        continue
    speak(sentence)


print("USER ENDED ShadowVox!!")
print("EXITING...")
