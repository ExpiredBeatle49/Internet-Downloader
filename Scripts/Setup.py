import PySimpleGUI as sg
import wget
import os

sg.theme('dark grey 9')

Examples = 'https://pastebin.com/raw/TrhGpS3E'
Uninstall = 'https://pastebin.com/raw/RV7hBhm7'
Main = 'https://pastebin.com/raw/Xa2Ea4rD'
Youtube = 'https://pastebin.com/raw/2xT4g1ac'
Hub = 'https://pastebin.com/raw/Q4Zy0uEa'

CURR_DIR = os.path.dirname(os.path.realpath(__file__))

layout = [[sg.Text(size=(40,1), key='-OUTPUT-')],
              [sg.Button('Start Installation'), sg.Button('Close')]]
     
window = sg.Window('Setup', layout)
event, values = window.read()

while True:

    if event == 'Start Installation':
        window['-OUTPUT-'].update('Starting Installation...')
        os.mkdir(str(CURR_DIR) + "/Downloads")
        os.mkdir(str(CURR_DIR) + "/Scripts")
        wget.download(Examples, str(CURR_DIR) + "/Downloads/Link Examples.txt")
        wget.download(Main, str(CURR_DIR) + "/Scripts/Main.py")
        wget.download(Uninstall, str(CURR_DIR) + "/Scripts/Uninstall.py")
        wget.download(Youtube, str(CURR_DIR) + "/Scripts/youtube.py")
        wget.download(Hub, str(CURR_DIR) + "/Hub.py")
        window['-OUTPUT-'].update('Done with the Installation')

    if event == sg.WINDOW_CLOSED or event == 'Close':
        window.close()
        break
