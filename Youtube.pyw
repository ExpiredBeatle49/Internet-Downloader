from pytube import YouTube
import PySimpleGUI as sg
import os.path
import pytube
import Main
import os

def run():
    youtube = [[sg.Text("What's the url?")],
            [sg.Input(key='-INPUT-0')],
            [sg.Text("What's the File's name?")],
            [sg.Input(key='-INPUT-1')],
            [sg.Text(size=(40,1), key='-OUTPUT-')],
            [sg.Button('Start Download'), sg.Button('Regular Mode'), sg.Button('Exit')]]

    window = sg.Window('Youtube downloader', youtube)
    CURR_DIR = os.path.dirname(os.path.realpath(__file__))
    PARENT = os.path.dirname(CURR_DIR)

    while True:
        event, values = window.read()
        SAVE_PATH = str(PARENT) + "/Downloads"
        link = values['-INPUT-0']

        if event == 'Exit' or event == sg.WINDOW_CLOSED:
            window.close()
            break
        
        if event == 'Regular Mode':
            window.close()
            Main.run()
            break
        
        if event == 'Start Download':
            youtube = pytube.YouTube(link)
            videot = YouTube(link)
            videoti = '/' + str(videot.title)
            ftype = '.mp4'
            video = youtube.streams.first()
            video.download('Downloads')
            os.rename(str(CURR_DIR) + '/Downloads' + str(videoti) + str(ftype), str(CURR_DIR) + '/Downloads/' + values['-INPUT-1'] + '.mp4')
            window.close()
            break
