def speak(str):
    from win32com.client import Dispatch

    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


if __name__ == '__main__':
    import requests
    import json

    url = ('https://newsapi.org/v2/everything?'
           'q=INDIA&'
           'from=2021-04-27&'
           
           'sortBy=popularity&'
           'apiKey=33c0703c7e3944e69437a7b7f5107383')

    response = requests.get(url)
    print(response.text )

    text = response.text
    my_json = json.loads(text)
    for i in range(0, 2):
        speak(my_json['articles'][i]['title'])
        speak(my_json['articles'][i]['description'])



""""
def speak(str):
    from win32com.client import Dispatch

    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


if __name__ == '__main__':
    import requests
    import json

    url = ('https://newsapi.org/v2/everything?'
           'q=INDIA&'
           'from=2021-04-27&'
           'sources=bbc-news&'
           'sortBy=popularity&'
           'apiKey=33c0703c7e3944e69437a7b7f5107383')

    response = requests.get(url)
    print(response.text )

    text = response.text
    my_json = json.loads(text)
    for i in range(0, 2):
        speak(my_json['articles'][i]['title'])

"""