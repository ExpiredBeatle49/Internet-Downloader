import PySimpleGUI as sg
import os
import wget

CURR_DIR = os.path.dirname(os.path.realpath(__file__))

sg.theme('dark grey 9')

layout = [[sg.Text("What's the url?")],
          [sg.Input(key='-INPUT-0')],
          [sg.Text("What's the File's name?")],
          [sg.Input(key='-INPUT-1')],
          [sg.Text("What's the File's extension?")],
          [sg.Input(key='-INPUT-2')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Ok')]]

window = sg.Window('Internet Downloader', layout)

event, values = window.read()

window['-OUTPUT-'].update("Downloading file...")
wget.download(values['-INPUT-0'], str(CURR_DIR) + '/Downloads/' + values['-INPUT-1'] + "." + values['-INPUT-2'])
window['-OUTPUT-'].update("Done")
window.close()
