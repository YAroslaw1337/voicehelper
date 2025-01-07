from command_list import commandors
from pc import *
from browser import *
# from fuzzywuzzy import process
# from fuzzywuzzy import fuzz
import speech_recognition

print('Ver№5')

sr = speech_recognition.Recognizer()
def listen_fun():
    try:
        with speech_recognition.Microphone(device_index = 2) as mic:
                sr.adjust_for_ambient_noise(source=mic, duration=0.7)
                audio = sr.listen(source=mic)
                query = sr.recognize_google(audio_data=audio , language='ru-RU').lower()
        return query
    except speech_recognition.UnknownValueError:
        return 'не понятно'

def main():
    string = ''
    query = listen_fun()
    query2 = query.split()
    print(query)
    print('  ')
    
    for k, v in commandors['comands'].items():
        for cml in v:
            cmls = cml.split()
            if all(word in query2 for word in cmls):
                query2 = [word for word in query2 if word not in cmls]                     
                string = ' '.join(query2).strip()
                req = string

                if k in commandors['required'] and not req:
                    print('нужен запрос')
                    continue
                
                globals()[k](req)
                break


# def cmnds(req):
#     print(comnds)

query = listen_fun()

while True  : 
    if  __name__ == '__main__':
        main()


