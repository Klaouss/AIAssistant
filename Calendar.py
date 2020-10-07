def Show_Calendar():
    import calendar
    import speech_recognition as sr
    from Speak_Text import SpeakText



    r = sr.Recognizer()

    with sr.Microphone() as source:
        SpeakText('What Year\' calendar should I show you? ')
        print('Say')

        audiotext = r.listen(source)
        Year = r.recognize_google(audiotext)
        Year = int(Year)

        txttospeak = 'Here is the calendar from '+ str(Year)
    SpeakText(txttospeak)
    print(calendar.calendar(Year))


