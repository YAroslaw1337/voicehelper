import speech_recognition
import webbrowser
import os 
print('Я могу поздороватся \n могу влючить видео , открыть ютуб \n могу запускать приложения такие как grounded, undertale, steam , spotify') 
print('Ver№1')


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

def hello():
    return 'привет аут'

def create_task():
    print('новое дело')
    query = listen_fun()
    with open('todo-list.txt', 'a') as file:
        file.write(f'{query}\n')
    return f'дело {query} добавлено'


def open_youtube():
    webbrowser.open('https://www.youtube.com/')
def search_for_video_on_youtube():
    query = listen_fun()
    query2 = query.split()
    query2 = list(query2)
    serch = query2[-1]
    url = "https://www.youtube.com/results?search_query=" + serch
    webbrowser.get().open(url)

def main():
    query = listen_fun()
    query2 = query.split()
    query2 = list(query2)
    serch = query2[-1]
    print(query) 
    print(serch)
    if query == 'привет' or query =='здраствуй':
         print(hello())
    elif query == 'добавить делa' or query == 'добавь задачу':
         print(create_task())
    elif query == 'найди видео в youtube'or query == 'найти видео в youtube':
        search_for_video_on_youtube()
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
    elif query == 'открой muse dash' or query == 'открой муздэш':
        os.system("D:/downloat/steam/steamapps/common/Muse Dash/MuseDash.exe")    

while True:

    if __name__ == '__main__':
        main()
