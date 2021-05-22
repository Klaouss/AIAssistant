def Send_email():

    from email.mime.text import MIMEText
    from Speak_Text import SpeakText
    from email.mime.multipart import MIMEMultipart
    import speech_recognition as sr

    import smtplib, ssl



    class Contact:
        def __init__(self,name, first_part, last_part):
            self.name = name
            self.first_part = first_part
            self.last_part = last_part



    Panos = Contact(name='Panos',first_part='pyannakopoulos',last_part='uniwa.gr')
    Dad = Contact(name='Dad',first_part='cklaouda',last_part='otenet.gr')
    Mom = Contact(name='Mom',first_part='christinaklaoudatou',last_part='yahoo.de')
    Stavros = Contact(name='Stavros',first_part='stavrosklaoudatos1',last_part='gmail.com')
    Leo = Contact(name='Leo',first_part='leo.vournas',last_part='gmail.com')
    Elias = Contact(name='Elias',first_part='elias.bourlas', last_part='gmail.com')
    Karolos = Contact(name='Karolos',first_part='karolos.bourlas', last_part='icloud.com')
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

            if (Before=='Panos'or 'panos'):
                Before = Panos.first_part
                After = Panos.last_part

            if (Before=='Mom'or 'mom'):
                Before = Mom.first_part
                After = Mom.last_part

            if (Before=='Dad' or 'dad'):
                Before = Dad.first_part
                After = Dad.last_part

            if (Before=='stavros'or 'Stavros' or 'Me' or 'me'):
                Before = Stavros.first_part
                After = Stavros.last_part

            if (Before == 'Leo' or 'leo'):
                Before = Leo.first_part
                After = Leo.last_part

            if (Before == 'Elias' or 'elias'):
                Before = Elias.first_part
                After = Elias.last_part

            if (Before == 'Karolos'or 'karolos'):
                Before = Karolos.first_part
                After = Karolos.last_part

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
    sender_email = 'stavrosklaoudatos@gmail.com'
    receiver_email = Before + '@'+After
    print(receiver_email)
    password = 'Miriki100'



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
