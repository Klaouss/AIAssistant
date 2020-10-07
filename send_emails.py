def Send_email():

    def SpeakText(command):
        import pyttsx3
        # Initialize the engine
        engine = pyttsx3.init()
        engine.say(command)
        engine.runAndWait()

    import speech_recognition as sr

    import smtplib, ssl



    class Contact:
        def __init__(self,name, first_part, last_part):
            self.name = name
            self.first_part = first_part
            self.last_part = last_part



    Panos = Contact(name='panos',first_part='pyannakopoulos',last_part='uniwa.gr')
    Dad = Contact(name='Dad',first_part='cklaouda',last_part='otenet.gr')
    Mom = Contact(name='Mom',first_part='christinaklaoudatou',last_part='yahoo.de')
    Stavros = Contact(name='Stavros',first_part='stavrosklaoudatos1',last_part='gmail.com')
    Leo = Contact(name='Leo',first_part='leo.vournas',last_part='gmail.com')
    Elias = Contact(name='Elias',first_part='elias.bourlas', last_part='gmail.com')

    AntonisMag = Contact(name='AntonisMag',first_part='antonismagriotis',last_part='gmail.com')
      # Enter your address

    r = sr.Recognizer()

    Before = ''
    text = ''
    After = ''

    while (Before=='') :
        with sr.Microphone() as source:
            SpeakText('Tell me the first part of the receivers email, from the start just until the @, or the name of the person')
            print('Start')

            audiotext = r.listen(source)
            Before = r.recognize_google(audiotext)
            Before = str(Before)
            print('You said: ', Before)
            SpeakText(Before)

            if ('pano'in Before):
                Before = Panos.first_part
                After = Panos.last_part

            if ('om'in Before):
                Before = Mom.first_part
                After = Mom.last_part

            if ('ad'in Before):
                Before = Dad.first_part
                After = Dad.last_part

            if ('tavros'in Before):
                Before = Stavros.first_part
                After = Stavros.last_part

            if ('eo'in Before):
                Before = Leo.first_part
                After = Leo.last_part

            if ('lias'in Before):
                Before = Elias.first_part
                After = Elias.last_part



            if 'anton' in Before:
                Before = AntonisMag.first_part
                After = AntonisMag.last_part

        with sr.Microphone() as source:
            SpeakText('Is this correct?')
            print('Yes or No')

            audiotext = r.listen(source)
            YorN = r.recognize_google(audiotext)
            YorN = str(YorN)

            if('ye'in YorN):
                Before=Before
            else:
                SpeakText('Please Enter it manually! Remember to only put the information of the receiver up until the @!')
                Before=input('First Part')

    while(After==''):
        with sr.Microphone() as source:
            SpeakText('Now tell me the second part of the receivers email, from the @ until the end')
            print('Start')

            audiotext = r.listen(source)
            After = r.recognize_google(audiotext)
            After = str(After.lower())
            print('You said: ', After)
            SpeakText(After)

        with sr.Microphone() as source:
            SpeakText('Is this correct?')
            print('Yes or No')

            audiotext = r.listen(source)
            YorN2 = r.recognize_google(audiotext)
            YorN2 = str(YorN2)

            if ('yes' in YorN2):
                After = After.lower()
            else:
                SpeakText('Please Enter it manually! Remember to only put the information of the receiver after the @')
                After = input('Second Part')



    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = input('Your Email:  ')
    receiver_email = Before + '@'+After
    print(receiver_email)
    password = print("Your password:  ")



    while(text==''):
        with sr.Microphone() as source:
            SpeakText('Now tell me  what you want the message to be')
            print('Start')

            audiotext = r.listen(source)
            text  = r.recognize_google(audiotext)
            text = str(text)
            print('You said: ', text)

    message ='Subject:  \n' + text+'\n\n\n\n This message was sent using the Debiria Virtual Assistant created by Stavros Klaoudatos using the Python Language!'

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
