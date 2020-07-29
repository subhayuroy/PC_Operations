import keyboard as kb
import webbrowser
import os

browserExe = "chrome.exe"

rk = kb.record(until="shift")

kb.add_hotkey('ctrl+shift+s+r', lambda: webbrowser.open_new('http://google.com'))  #For opening a chrome tab
kb.add_hotkey('ctrl+shift+r+s', lambda: os.system("taskkill /f /im " + browserExe))  #For closing a chrome tab
kb.wait('Esc')

kb.play(rk, speed_factor=10)