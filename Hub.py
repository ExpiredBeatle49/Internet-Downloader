import PySimpleGUI as sg
from Scripts import Uninstall
from Scripts import Youtube
from Scripts import Main

layout = [[sg.Text(size=(40, 0), key="Text")],
          [sg.Button('Downloader'), sg.Button('Uninstaller')]]

window = sg.Window("Hub", layout)

while True:
    
    event, value = window.read()

    if event == 'Exit' or event == sg.WINDOW_CLOSED:
        window.close()
        break
        
    if event == "Downloader":
        window.close()
        Main.run()
        break

    if event == "Uninstaller":
        window.close()
        Uninstall.run()
        break
