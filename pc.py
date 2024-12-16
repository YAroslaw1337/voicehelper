import pyautogui as pg
import time
import os 
import pygetwindow as gw
import subprocess
import psutil

def sleep(req):
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

def find_file(req, search_dir):
    for root, dirs, files in os.walk(search_dir):
        for file in files:
            if file.lower() == req:
                return os.path.join(root, file)
    return None

def open(req):
    search_dir = r'C:\Users\skele\AppData\Roaming\.tlauncher\legacy\Minecraft'
    big_leter = req.capitalize()
    file_path = find_file(f'{big_leter}.exe', search_dir)
    if file_path:
        try:
            subprocess.run([file_path], check=True)
        except subprocess.CalledProcessError as sub:
            print(f"Ошибка при запуске файла: {sub}")
    else:
        print(f"Файл {big_leter} не найден")

def big_min(req):
    big_leter = req.strip().title()  
    try:
        window = gw.getWindowsWithTitle(big_leter)[0]
        if querys == 'сверни':
            try:
                if window.isMinimized == False:
                    window.minimize()
                else:
                    print(f"Окно с названием '{req}' уже свернуто.")
            except Exception :
                pass
        else:
            try:
                if window.isMinimized == True:
                    window.restore() 
                else:
                    print(f"Окно с названием '{req}' уже развернуто.")
            except Exception :
                pass
    except:
        print(f"Произошла ошибка")

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
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if req in proc.info['name'].lower():
                proc.terminate()
                run = True
                break
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    if not run:
        print(f'{req} не запущен')