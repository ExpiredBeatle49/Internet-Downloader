def run():
    
    import PySimpleGUI as sg
    import Youtube as Yt
    import wget

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

    while True:

        if event == 'Exit' or event == sg.WINDOW_CLOSED:
            window.close()
            break
        
        if event == 'Youtube Mode':
            window.close()
            Yt.run()
            break
            
        if event == 'Start Download':
            window['-OUTPUT-'].update('Starting download...')
            wget.download(values['-INPUT-0'], str(CURR_DIR) + '/Downloads/' + values['-INPUT-1'] + "." + values['-INPUT-2'])
            window['-OUTPUT-'].update('Done downloading')
