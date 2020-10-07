
def OpenApp(Text):
    import os
    if('Opera' in Text):
        os.startfile("C:Users\stavr\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Opera GX Browser .lnk")     #Opera

    if ('Word'in Text):
        os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk") #Word

    if('Music'in Text):
        os.startfile('"C:Users\stavr\OneDrive\Υπολογιστής\Music"')     #Music

    if ('Test'in Text):
        os.startfile('"C:Users\stavr\OneDrive\Υπολογιστής\Speedtest.lnk"')        #SpeedTest

    if('Instagram' in Text):
        os.startfile("C:Users\stavr\OneDrive\Υπολογιστής\Instagram.lnk")            #Instagram

    if('Twitter'in Text):
        os.startfile("C:Users\stavr\OneDrive\Υπολογιστής\Twitter.lnk")              #Twitter

    if('Skype'in Text):
        os.startfile("C:Users\stavr\OneDrive\Υπολογιστής\Skype.lnk")            #Skype

    if ('Netflix' in Text):
        os.startfile("C:Users\stavr\OneDrive\Υπολογιστής\eNetflix.lnk")      #Netflix

    if ('Skype' in Text):
        os.startfile("C:Users\stavr\OneDrive\Υπολογιστής\Skype.lnk")

    if('amera' in   Text):
        import subprocess

        subprocess.run('start microsoft.windows.camera:', shell=True)

    if ('usion' in Text):
        os.startfile("C:\\Users\stavr\OneDrive\Υπολογιστής\Autodesk Fusion 360.lnk")

    if ('meshmicer' in Text):
        os.startfile("C:\\Users\stavr\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Autodesk\Meshmixer.lnk")

    if('Flash'in Text):
        os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\FlashForge\FlashPrint (x64)\FlashPrint.lnk")

