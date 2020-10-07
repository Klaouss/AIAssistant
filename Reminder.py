def Set_a_Reminder():
    import speech_recognition as sr
    from Speak_Text import SpeakText
    from time import sleep

    r = sr.Recognizer()

    with sr.Microphone() as source:
        SpeakText('What should I remind you?')

        audiotext = r.listen(source)
        txt_to_remind = r.recognize_google(audiotext)
        txt_to_remind = str(txt_to_remind)
        print(txt_to_remind)
        SpeakText(txt_to_remind)






    with sr.Microphone() as source:
        SpeakText('In How Many Hours?')
        try:
            audiotext = r.listen(source)
            TXT = r.recognize_google(audiotext)
        except TypeError:
            SpeakText('I didn\' understand you!')
            TXT = r.recognize_google(audiotext)

        TXT = str(TXT)
        print(TXT)
        SpeakText(TXT)
        if(TypeError==True):
            SpeakText('I didn`t understnd you')

        InHours = (TXT)
        if ('none' in TXT):
            InHours = 0
        else:
            InHours = float(TXT)

    with sr.Microphone() as source:
        SpeakText('In How Many Minutes?')

        audiotext = r.listen(source)
        TXT2 = r.recognize_google(audiotext)
        TXT2 = str(TXT2)
        print(TXT2)
        SpeakText(TXT2)

        InMinutes = (TXT2)

        if ('none' in TXT2):
            InMinutes = 0
        else:
            InMinutes = float(TXT2)

    Reminder_Time = (InHours * 3600) + (InMinutes * 60)

    Reminder_Speak_Time = 'I set a reminder due in: ' + str(Reminder_Time) + ' seconds'
    SpeakText(Reminder_Speak_Time)
    print(Reminder_Speak_Time)

    sleep(Reminder_Time)
    SpeakText(txt_to_remind)
    print(txt_to_remind)



