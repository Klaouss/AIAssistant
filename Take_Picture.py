def Take_Picture():
    import cv2
    import time
    from Speak_Text import SpeakText
    camera = cv2.VideoCapture(0)
    for i in range(1):
        time.sleep(0.01)
        return_value, image = camera.read()
        cv2.imwrite('Day '+str(time.localtime().tm_mday)+', Hour '+str(time.localtime().tm_hour)+', Minute '+str(time.localtime().tm_min)+'.jpg', image)
    del(camera)
    print('Succesful')
    SpeakText('Successful task!')



Take_Picture()