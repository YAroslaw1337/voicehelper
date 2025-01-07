import requests , lxml
from bs4 import BeautifulSoup as BS
import webbrowser
import pyautogui as pg

def search_for_video_on_youtube(req):
    url = "https://www.youtube.com/results?search_query=" + req
    webbrowser.get().open(url)
    
def repit(req):
    pg.press(['0'])

def f_screen(req):
    pg.press(['f'])

def pars_anime(req):
    r = requests.get('https://animego.org')
    ht = BS(r.content, 'lxml')
    ongoing = ht.find_all('div', class_= "h5 font-weight-normal mb-2 card-title carousel-item-title text-truncate")
    new_series = ht.find_all('div', class_= "list-group-item list-group-item-action border-left-0 border-right-0 border-bottom-0")


def find_anime(req):
    url = "https://animego.org/search/all?q=" + req
    webbrowser.get().open(url)

def search_in_internet(req):
    if req == 'youtube' or req == 'ютуюб':
        webbrowser.open('https://www.youtube.com/')
    else:
        url = "https://www.google.com/search?q=" + req
        webbrowser.get().open(url)

