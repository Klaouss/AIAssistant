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



    Contact_1 = Contact(name='Name',first_part='first part of email',last_part='part after the @')
    .
    .
    .
    .
    .
      # Enter your contacts

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

            if (Before=='Name 1'or 'alias'):
                Before = Contact_1.first_part
                After = Contact_1.last_part

           

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
    sender_email = 'ypur email'
    receiver_email = Before + '@'+After
    print(receiver_email)
    password = 'Your Email Password'



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
