def Search(query):
    import time
    import webbrowser
    from googlesearch import search
    from Speak_Text import SpeakText
    Query = str(query)

    Data = ''

    data = Query.split(sep=' ')
    x = len(data)
    try:
        for i in range(x):
            if ('earch' in data[i]):
                data.remove(data[i])
                x+=1
            else:
                Data += data[i] + ' '
    except IndexError:
        pass

    for i in search(Data,tld='co.in',num=5,stop=3,pause=2):

        print('You searched: ', Data)
        print(i)
        webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"))
        webbrowser.get('chrome').open_new(url=i)

