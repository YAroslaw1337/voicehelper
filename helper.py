from command_list import commandors
from pc import *
from browser import *
# from fuzzywuzzy import process
# from fuzzywuzzy import fuzz


import speech_recognition

print('Ver№4')

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
    # best_sim = 0
    string =''
    query = listen_fun()
    query2 = query.split()
    req = query2[-1]
    if len(query2) > 1:
        query2.pop(-1)
    string = ' '.join(query2) 
    print(query)
    print('  ')

    # for k, v in commandors['comands'].items():
    #     for vs in v:
    #         similarity = fuzz.ratio(string, vs)
    #         if similarity >= best_sim:
    #             best_sim = similarity
    #             best_match = (k, vs)
    
    # if best_sim >=70:
    #     print(query)
    #     print('  ')
    #     print(f'Команду распознано как: {best_match}')
    # else:
    #     print('Команду не распознано')
    
    for k, v in commandors['comands'].items():
        if string in v:
            globals()[k](req)


def cmnds(req):
    print(comnds)

query = listen_fun()

while True  : 
    if  __name__ == '__main__':
        main()


