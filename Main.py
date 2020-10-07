def Debiria_Virtual_Assistant():
    if(10>=1):

        import time
        import speech_recognition as sr
        import os
        import numpy
        import pandas

        #My Libraries
        from Speak_Text import SpeakText

        import Reminder
        from GoogleSearch import Search
        from Image_Capture.Take_Picture import Take_Picture
        from OpenApp import OpenApp
        import send_emails
        import Calendar
        from Video_Capture.Take_Video import Take_Video
        from Create_A_Folder import CreateAFolder
        from Hacker import Setup_hacking_environment
        import Printing
        from Movie_Stats import movie_search
        from AI import AI1 as AI
        from Covid_19 import Covid
        from Wikipedia import Wikipedia


    r = sr.Recognizer()
    face_rec_object = AI.Face_Recognition



    class Command():
        def __init__(self,activation,action):
            self.activation = activation
            self.action = action



    SpeakText('How can I help you?')
    while(1):

        try:
            with sr.Microphone() as source:

                print('How can I help you?')


                audiotext = r.listen(source)
                Text = r.recognize_google(audiotext)
                Text = str(Text)

                print('You said: ',Text)

                name = Command(activation='your name',
                               action='My name is Debiria and I am a Virtual Assistant created by Stavros Klaoudatos!')
                sex = Command(activation='male or a female', action='I don\'t know')
                age = Command(activation='old are you',
                              action='I was born on 21st of June during the corona virus outbreak in 2020!')
                origin = Command(activation='where are you from',
                                 action='I was created in Greece, but right now I live in your computer!')





                if (name.activation in Text):
                    SpeakText(name.action)

                if(sex.activation in Text):
                    SpeakText(sex.action)

                if(age.activation in Text):
                    SpeakText(age.action)

                if (origin.activation in Text):
                    SpeakText(origin.action)

                if ('search' in Text):
                    Search(Text)

                if('remind' in Text):
                    Reminder.Set_a_Reminder()

                if ('picture' in Text):
                    Take_Picture()

                if ('open' in Text):
                    OpenApp(Text)

                if('mail' in Text):
                    send_emails.Send_email()

                if('calendar' in Text):
                    Calendar.Show_Calendar()

                if('video' in Text):
                    Take_Video()

                if('create a folder' in Text):
                    CreateAFolder()

                if ('hack' in Text):
                    Setup_hacking_environment()

                if ('print' in Text):
                    Printing._3D_Printing()

                if ('movie' in Text):
                    movie_search()

                if ('recogni' in Text):
                    face_rec_object.Face_Recognition()

                if ('covid' in Text):
                    Covid()

                if 'iki'in Text:
                    Wikipedia(Text)


                elif('end'in Text):
                    SpeakText('Program Ended successfully')
                    exit(100)


        except TypeError:
            continue





Debiria_Virtual_Assistant()