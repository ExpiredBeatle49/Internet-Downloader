import PySimpleGUI as sg
import os
import wget

sg.theme('dark grey 9')

CURR_DIR = os.path.dirname(os.path.realpath(__file__))

layout = [[sg.Text("What's the url?")],
          [sg.Input(key='-INPUT-0')],
          [sg.Text("What's the File's name?")],
          [sg.Input(key='-INPUT-1')],
          [sg.Text("What's the File's extension?")],
          [sg.Input(key='-INPUT-2')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Start Download'), sg.Button('Quit')]]

window = sg.Window('Internet Downloader', layout)

while True:
    
    event, values = window.read()

    if event == 'Quit' or event == sg.WINDOW_CLOSED:
        window.close()
        break
    
    if event == 'Start Download':
        window['-OUTPUT-'].update("Downloading File...")
        wget.download(values['-INPUT-0'], str(CURR_DIR) + '/Downloads/' + values['-INPUT-1'] + "." + values['-INPUT-2'])
        window['-OUTPUT-'].update("Done Downloading File")
