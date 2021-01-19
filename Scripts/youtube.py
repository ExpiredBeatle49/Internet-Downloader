def run():

    from pytube import YouTube
    import PySimpleGUI as sg
    import Main
    import os

    main = [[sg.Text("What's the url?")],
            [sg.Input(key='-INPUT-0')],
            [sg.Text("What's the File's name?")],
            [sg.Input(key='-INPUT-1')],
            [sg.Text(size=(40,1), key='-OUTPUT-')],
            [sg.Button('Start Download'), sg.Button('Regular Mode', sg.Button('Exit'))]]

    window = sg.Window('Internet downloader (Youtube mode)', main)

    while True:
        event, values = window.read()
        SAVE_PATH = str(os.path.abspath(os.curdir)) + "/Downloads"
        link = values['-INPUT-0']

        if event == 'Exit' or event == sg.WINDOW_CLOSED:
            window.close()
            break
        
        if event == 'Regular Mode':
            window.close()
            Main.run()
            break
        
        if event == 'Start Download':
            window['-OUTPUT-'].update('Starting download...')
            yt = YouTube(link)
            mp4files = yt.filter('mp4') 
            yt.set_filename(values['-INPUT-1']) 
            d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution) 
            d_video.download(SAVE_PATH)
            window['-OUTPUT-'].update('Done downloading')
