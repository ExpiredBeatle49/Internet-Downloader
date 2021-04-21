import PySimpleGUI as sg
import Youtube
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

    while True:

        if event == 'Exit' or event == sg.WINDOW_CLOSED:
            window.close()
            break
        
        if event == 'Youtube Mode':
            window.close()
            Youtube.run()
            break
            
        if event == 'Start Download':
            window.close()
            sg.SystemTray.notify('Internet Donwloader', 'Starting download...')
            wget.download(values['-INPUT-0'], str(CURR_DIR) + '/Downloads/' + values['-INPUT-1'] + "." + values['-INPUT-2'])
            x = os.listdir(str(CURR_DIR) + "/Downloads")
            for i in x:
                if i.endswith("." + values['-INPUT-2']):
                    if i == values['-INPUT-1'] + "." + values['-INPUT-2']:
                        try:
                            sg.SystemTray.notify('Internet Donwloader', 'Done downloading')
                        except:
                            sg.SystemTray.notify('Internet Donwloader', 'Downloading ERROR')
                        break
