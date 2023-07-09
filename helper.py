import speech_recognition
import pyautogui as pg
import webbrowser
import os 
import time



comnds = 'останови/играй музыку \n найди(в поиске пк)\n найди видео в youtube \n заново \n открой ютуб\nнайди в интернете/поиск в интернете\n открой undertale/spotify/steam/grounded\n останови музыку/играй музыку',
print('Ver№3')

commandors = {
    'comands' : {
    'search_in_internet':('найди в интернете', 'найти в интернете', 'поиск в интернете'),
    'search_for_video_on_youtube':('найди в ютубе', 'найди видео в youtube', 'найти видео в youtube', 'найти в youtube', 'найди в youtube'),
    'open_youtube':('открой ютуб', 'открой youtube'),
    'repit':('заново', 'поновой', 'сначала'),
    'cmnds':('команды','покажи команды'),
        
    'mic':('микрофон'),
    
    'spotify':('открой спотифай','открой spotify', 'открыть спотифай','открыть spotify'),
    'music':('играй музыку', 'останови музыку'),
    
    'ctimes':('время', 'сколько время', 'какой сейчас час'),
    'search_in_pk':('найди', 'найти'),

    'undertale':('открой undertale', 'открой андертейл', 'открыть undertale','открыть андертейл'),
    'grounded':('открой grounded', 'открой граундед', 'открыть grounded','открыть граундед'),
    'steam':('открой стим','открой steam','открыть стим','открыть steam'),
    
    'sleep':('в спящий режим','выключить пк', 'выключить компьютер')
    }
}

    
sr = speech_recognition.Recognizer()
def listen_fun():
    try:
        with speech_recognition.Microphone() as mic:
                sr.adjust_for_ambient_noise(source=mic, duration=0.5)
                audio = sr.listen(source=mic)
                query = sr.recognize_google(audio_data=audio , language='ru-RU').lower()
        return query
    except speech_recognition.UnknownValueError:
        return 'не понятно'


def sleep():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

def cmnds():
    print(comnds)

def music():
    os.system("C:/Users/skele/AppData/Roaming/Spotify/Spotify.exe")
    pg.typewrite(['space'])
def spotify():
    video_path = os.getcwd("AppData/Roaming/Spotify/Spotify.exe")
    print(video_path)
    os.system(video_path)


def grounded():
    os.system("D:/downloat/Grounded/Grounded.exe")
    
def undertale():
    os.system('D:/downloat/steam/steamapps/common/Undertale/UNDERTALE.exe')   

def steam():
    os.system("D:\downloat\steam\steam.exe")


def ctimes():
    sec = time.time()
    local = time.ctime(sec)
    print(local)

def search_in_pk():
    query = listen_fun()
    query2 = query.split()
    query2 = list(query2)
    serch = str(query)
    if serch == 'не понятно':
        print('не понятно')
    else:
        pg.press('win')
        pg.write(serch)
        pg.moveTo(200, 200)

def mic():
    pg.press(['f6']) 


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

def repit():
    pg.press(['0'])


def main():
    query = listen_fun()
    query2 = query.split()
    query2 = list(query2)
    print(query)
    print('   ')  
    for k, v in commandors['comands'].items():
        if query in v:
            globals()[k]()




query = listen_fun()


while True: 
    if  __name__ == '__main__':
        main()


