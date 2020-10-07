
def SpeakText(command):
    import pyttsx3
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()



