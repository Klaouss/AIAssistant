

def CreateAFolder():
    import os
    from Speak_Text import SpeakText
    import speech_recognition as sr
    r = sr.Recognizer()
    SpeakText('What do you want to name your desktop folder?')
    folder_name = ''
    while (folder_name == ''):
        with sr.Microphone() as source:
            audiotxt = r.listen(source)
            folder_name = str(r.recognize_google(audiotxt))

            SpeakText('Successfully created folder')
    dir = folder_name + '\\'

    path = os.path.join("C:\\Users\stavr\OneDrive\Υπολογιστής\\",dir)

    os.mkdir(path)


