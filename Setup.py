import PySimpleGUI as sg
import wget
import os

sg.theme('dark grey 9')

Examples = 'https://pastebin.com/raw/TrhGpS3E'
Uninstall = 'https://pastebin.com/raw/RV7hBhm7'
Main = 'https://pastebin.com/raw/Xa2Ea4rD'
CURR_DIR = os.path.dirname(os.path.realpath(__file__))

layout = [[sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Start Installation'), sg.Button('Close')]]
 
window = sg.Window('Uninstaller', layout)
event, values = window.read()

while True:

    if event == 'Start Installation':
        window['-OUTPUT-'].update('Starting Installation...')
        os.mkdir(str(CURR_DIR) + "/Downloads")
        wget.download(Examples, str(CURR_DIR) + "\Downloads\Link Examples.txt")
        wget.download(Main, str(CURR_DIR) + "\Main.py")
        wget.download(Uninstall, str(CURR_DIR) + "/Uninstall.py")
        window['-OUTPUT-'].update('Done with the Installation')

    if event == sg.WINDOW_CLOSED or event == 'Close':
        window.close()
        break
