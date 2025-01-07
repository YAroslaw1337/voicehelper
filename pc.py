import pyautogui as pg
import time
import os 
import pygetwindow as gw
import subprocess
import datetime

import win32api
import win32gui
import win32file
import win32process
import win32con
import win32com.client
import psutil

from urls import files

c_list = ['все', 'всё', 'всё окна', 'все окна']

def sleep(req):
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

# def find_file(req):
#     search_path='D:\\'
#     try:
#         shell = win32com.client.Dispatch("Shell.Application")
#         folder = shell.Namespace(search_path)
        
#         search_res = []

#         def recursive_search(folder):
#             for item in folder.Items():
#                 if req.lower() in item.Name.lower():
#                     search_res.append(item.Path)

#                 if item.IsFolder:
#                     subfolder = shell.Namespace(item.Path)
#                     recursive_search(subfolder)

#         recursive_search(folder)
        
#         return search_res

#     except Exception as e:
#         print(f"Ошибка при поиске файла: {e}")
#         return []


def open_file(req):
    for k, p in files['links'].items():
        if req in k:
                os.startfile(p)
    else:
        print(f"Файл {req} не найден")

def min(req):
    def enum_win(hwnd, windows):
        if win32gui.IsWindowVisible(hwnd): 
            place = win32gui.GetWindowPlacement(hwnd)
            win_name = win32gui.GetWindowText(hwnd)

            if req == '':
                main_win = win32gui.GetForegroundWindow()
                main_place = win32gui.GetWindowPlacement(main_win)
                if main_place[1] == win32con.SW_NORMAL or main_place[1] == win32con.SW_MAXIMIZE:
                    win32gui.ShowWindow(main_win, win32con.SW_MINIMIZE)
            elif req in c_list:
                if place[1] == win32con.SW_NORMAL or place[1] == win32con.SW_MAXIMIZE:
                    win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
            else:
                if req.lower() == win_name.lower():
                    if place[1] == win32con.SW_NORMAL or place[1] == win32con.SW_MAXIMIZE:
                        win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)

    windows = []
    win32gui.EnumWindows(enum_win, windows)


def big(req):
    def enum_win(hwnd, windows):
        if win32gui.IsWindowVisible(hwnd):  
            place = win32gui.GetWindowPlacement(hwnd)
            win_name = win32gui.GetWindowText(hwnd)

            if req in c_list:
                if place[1] == win32con.SW_MINIMIZE:
                    win32gui.ShowWindow(hwnd, win32con.SW_NORMAL)
            else:
                if req.lower() == win_name.lower():
                    if place[1] == win32con.SW_MINIMIZE:
                        win32gui.ShowWindow(hwnd, win32con.SW_NORMAL)

    windows = []
    win32gui.EnumWindows(enum_win, windows)



def ctimes(req):
    sec = time.time()
    local = time.ctime(sec)
    print(local)


def search_in_pk(req):
    pg.press('win')
    time.sleep(0.5)
    pg.write(req)

#kills
def kill_progs(req):
    run = False
    for proces in psutil.process_iter(['pid', 'name']):
        try:
            if req in proces.info['name'].lower():
                proces.terminate()
                run = True
                break
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    if not run:
        print(f'{req} не запущен')