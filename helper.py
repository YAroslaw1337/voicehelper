import speech_recognition
import webbrowser
import os 
import subprocess as sp

sr = speech_recognition.Recognizer()
# commands = {
#     ("привет", "зраствуй", "зрайствуй", "hello"): hello,
#     ("'добавить делa", "добавь задачу", "новое дело",): create_task,
#     ("открой youtube", "youtube", "открыт youtube",): search_for_video_on_youtube,
#     ("открой спотифай", "открыть спотифай", "открой spotfiy", "открыть spotfiy"): open_spotify,
#     ("открой стим", "открыть steam"): open_steam,
# }

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


def search_for_video_on_youtube():
    webbrowser.open('https://www.youtube.com/')

def main():
    query = listen_fun()
    print(query.split())
    if query == 'привет':
         print(hello())
    elif query == 'добавить делa' or query == 'добавь задачу':
         print(create_task())
    elif query == 'открой youtube':
        search_for_video_on_youtube()
    elif query == 'открой андертейл' or query == 'открой undertale':
        os.system('D:/downloat/steam/steamapps/common/Undertale/UNDERTALE.exe')
    elif query == 'открой спотифай' or query == 'открой spotify':
        os.system("C:/Users/skele/AppData/Roaming/Spotify/Spotify.exe")
    elif query == 'открой стим' :
        os.system("D:\downloat\steam\steam.exe")
        

while True:

    if __name__ == '__main__':
        main()
