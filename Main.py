import PySimpleGUI as sg
import youtube
import os.path
import wget
import os

def run():
    sg.theme('dark grey 9')

    main = [[sg.Text("What's the url?")],
            [sg.Input(key='-INPUT-0')],
            [sg.Text("What's the File's name?")],
            [sg.Input(key='-INPUT-1')],
            [sg.Text("What's the File's extension?")],
            [sg.Input(key='-INPUT-2')],
            [sg.Text(size=(40,1), key='-OUTPUT-')],
            [sg.Button('Start Download'), sg.Button('Youtube Mode'), sg.Button('Exit')]]

    window = sg.Window('Internet Downloader', main)
    event, values = window.read()

    CURR_DIR = os.path.dirname(os.path.realpath(__file__))
    PARENT = os.path.dirname(CURR_DIR)

    while True:

        if event == 'Exit' or event == sg.WINDOW_CLOSED:
            window.close()
            break
        
        if event == 'Youtube Mode':
            window.close()
            youtube.run()
            break
            
        if event == 'Start Download':
            window['-OUTPUT-'].update('Starting download...')
            wget.download(values['-INPUT-0'], str(PARENT) + '/Downloads/' + values['-INPUT-1'] + "." + values['-INPUT-2'])
            window['-OUTPUT-'].update('Done downloading')
            window.close()
            break
