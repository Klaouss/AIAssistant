def movie_search():
    import imdb
    import speech_recognition as sr
    from Speak_Text import SpeakText
    ia = imdb.IMDb()
    r = sr.Recognizer()




    class Movie_Search():
        def __init__(self,object):
            self.object = object

    Object = Movie_Search

    SpeakText('Do you want to search for a movie, an actor or a company?')
    with sr.Microphone() as source:

        print('How can I help you?')

        audiotext = r.listen(source)
        Text = r.recognize_google(audiotext)
        Text = str(Text)

        print('You said: ', Text)
        print('Do you want to search for a movie, an actor or a company?')


        if 'movie' in Text:
            Object=Movie_Search(object='movie')
        if 'actor' in Text:
            Object = Movie_Search(object='actor')
        if 'company' in Text:
            Object = Movie_Search(object='company')




        if Object.object=='movie':
            SpeakText('Which movie do you want to search, or which top rankings do you want?')
            with sr.Microphone() as sourc:
                print('Which movie do you want to search, or which top rankings do you want?')

                audiotex = r.listen(sourc)
                Tex = r.recognize_google(audiotex)
                Tex = str(Tex)

                if 'top' in Tex:
                    top = ia.get_top250_movies()['title']
                    print(top[:9])
                    SpeakText(top[:2])
                else:
                    ia.search_movie(Tex)

        if Object.object=='actor':
            SpeakText('Which actor or actress do you want to search for?')

            with sr.Microphone() as sourc:
                print('Which actor or actresses do you want to search for?')

                audiotex = r.listen(sourc)
                Tex = r.recognize_google(audiotex)
                Tex = str(Tex)

                person = ia.search_person(Tex)['name']
                print(person[:2])
                SpeakText(person[:2])

        if Object.object=='company':
            SpeakText('What is the name of the compay you want to search for?')

            with sr.Microphone() as sourc:
                print('Which actor or actresses do you want to search for?')

                audiotex = r.listen(sourc)
                Tex = r.recognize_google(audiotex)
                Tex = str(Tex)

                company = ia.search_company(Tex)['name']
                print(company[0])
                SpeakText(company[0])

