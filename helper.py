import speech_recognition
import pyautogui as pg
import webbrowser
import os 

print('могу влючить видео , открыть ютуб, искать в интернете\n вкл/выкл микрофон\n играть/остановить музыку \n могу запускать приложения такие как grounded, undertale, steam , spotify') 
print('Ver№2')
print('команды\n останови/играй музыку\n найди видео в youtube \n заново ,открой ютуб\nнайди в интернете/поиск в интернете\n открой undertale/spotify/steam/grounded\n останови музыку/играй музыку')

sr = speech_recognition.Recognizer()

game = True

def listen_fun():
    try:
        with speech_recognition.Microphone() as mic:
                sr.adjust_for_ambient_noise(source=mic, duration=0.5)
                audio = sr.listen(source=mic)
                query = sr.recognize_google(audio_data=audio , language='ru-RU').lower()
        return query
    except speech_recognition.UnknownValueError:
        return 'не понятно'



def open_youtube():
    webbrowser.open('https://www.youtube.com/')

def search_for_video_on_youtube():
    query = listen_fun()
    query2 = query.split()
    query2 = list(query2)
    serch = str(query)
    if serch == 'не понятно':
        print('не понятно')
    else:
        url = "https://www.youtube.com/results?search_query=" + serch
        webbrowser.get().open(url)

def search_in_internet():
    query = listen_fun()
    query2 = query.split()
    query2 = list(query2)
    serch = str(query)
    if serch == 'не понятно':
        print('не понятно')
    else:
        url = "https://www.google.com/search?q=" + serch
        webbrowser.get().open(url)

def main():
    query = listen_fun()
    query2 = query.split()
    query2 = list(query2)
    print(query) 
    if query == 'останови музыку' or query == 'играй музыку':
         os.system("C:/Users/skele/AppData/Roaming/Spotify/Spotify.exe")
         pg.typewrite(['space'])
    elif query == 'найди в интернете'or query == 'поиск в интернете':
        search_in_internet()
    elif query == 'найди видео в youtube'or query == 'найти видео в youtube':
        search_for_video_on_youtube()
    elif query == 'повтори'or query == 'заново':
        pg.press(['0'])
    elif query == 'открой youtube':
        open_youtube()
    elif query == 'открой андертейл' or query == 'открой undertale':
        os.system('D:/downloat/steam/steamapps/common/Undertale/UNDERTALE.exe')
    elif query == 'открой спотифай' or query == 'открой spotify':
        os.system("C:/Users/skele/AppData/Roaming/Spotify/Spotify.exe")
    elif query == 'открой стим' or query == 'открой steam':
        os.system("D:\downloat\steam\steam.exe")
    elif query == 'открой граундед' or query == 'открой grounded':
        os.system("D:/downloat/Grounded/Grounded.exe")
    elif query == 'микрофон':
        pg.press(['f6'])    




query = listen_fun()
while True: 
    if  __name__ == '__main__':
        main()
        