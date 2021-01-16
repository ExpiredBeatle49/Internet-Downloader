import PySimpleGUI as sg
import wget
import os

sg.theme('dark grey 9')

paste = 'https://pastebin.com/raw/Xa2Ea4rD'
CURR_DIR = os.path.dirname(os.path.realpath(__file__))

layout = [[sg.Text(size=(30,1), key='-Download-')],
          [sg.Button('Start Download')]]

window = sg.Window('Setup', layout)

event, values = window.read()

window['-Download-'].update("Downloading files...")
os.mkdir(CURR_DIR + "/Downloads")
wget.download(paste, str(CURR_DIR) + "/Main.py")
window['-Download-'].update("Done, you may now close the window.")
